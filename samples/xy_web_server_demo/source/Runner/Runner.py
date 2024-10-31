# -*- coding: utf-8 -*-
__doc__ = "Runner.py"
__version__ = "0.0.1"
from pathlib import Path
import os, sys
import subprocess
import uuid, asyncio
from utils import local_python_path_string
from xy_web_server.WebServerWork import WebServerWork
from xy_web_server.Server.Tornado.Tornado import Tornado
from xy_web_server.Server.Django.Django import Django

admin_path = Path.cwd().joinpath("source/Runner/Admin/").resolve().as_posix()
sys.path.insert(0, admin_path)
# 若需要使用django-orm调用该函数
Django().load("xy_web_server_demo.settings")

# 加载Django要在引入Tornado的RequestHandler早, 这样才能够在Tornado的RequestHandler中调用Django的模型
from Site.Indexes import Index
from Site.Databases import Query, Add, Delete, Update
from RequestHandlerDemo.Demoes import Demo


class Runner(WebServerWork, Tornado, Django):
    @property
    def __version__(self) -> str:
        return __version__

    def get_name(self) -> str:
        return "xy_web_server_demo"

    def __init__(self, *args, **kwargs) -> None:
        description: str = (
            f""">>>>>>>>>>>> {self.get_name()} - v{self.__version__} <<<<<<<<<<<<<"""
        )
        print(description)
        print()
        print(f"{self.get_name()} Hello World!!!")
        self.default_parser()
        self.add_arguments()
        self.run_arguments()

    def add_arguments(self):
        self.add_argument(
            flag="-w",
            name="--work",
            help_text="""
                工作方式: 1. tornado [start]. 2. django [help|start|shell|makemigrations|migrate|...]
            """,
            nargs="+",
        )

    def on_arguments(
        self,
        name,
        value,
        arguments=None,
    ):
        if name == "work":
            if isinstance(value, list):
                if len(value) > 0:
                    work = value[0]
                    match work:
                        case "tornado":
                            if len(value) > 1:
                                command = value[1]
                                if command == "start":
                                    self.tornado_start()
                                else:
                                    print(f"Unsupported tornado command: {value}")
                            else:
                                print("Tornado not start...")
                        case "django":
                            if len(value) > 1:
                                command = value[1]
                                work_args = value[1:]
                                if command == "start":
                                    self.django_start()
                                else:
                                    self.django_manage(work_args)
        print(f"on_arguments {name} = {value}")
        return True

    # 运行 xy_web_server -w django help
    def django_manage(self, work_args: list):
        print(f"django_manage {work_args}")
        admin_path = (
            self.settings.settings_dir_path.joinpath("../source/Runner/Admin")
            .resolve()
            .as_posix()
        )
        os.chdir(admin_path)
        manage_path = (
            self.settings.settings_dir_path.joinpath("../source/Runner/Admin/manage.py")
            .resolve()
            .as_posix()
        )
        manage_cmd_list = self.manage_cmd_list(
            manage_path=manage_path,
            manage_cmd_list=work_args,
        )
        print(f"manage_path => {manage_cmd_list}")
        env = os.environ.copy()
        python_path = local_python_path_string()
        env.update({"PYTHONTPATH": python_path})
        admin_path = (
            self.settings.settings_dir_path.joinpath("../source/Runner/Admin")
            .resolve()
            .as_posix()
        )
        env.update(
            {
                self.settings.GLOBAL_CFG_SETTINGS_PATH_KEY: self.settings.settings_cfg_path.as_posix(),
            }
        )
        subprocess.run(manage_cmd_list, env=env)

    #   运行 xy_web_server -w django start
    def django_start(self):
        print("django_start")
        manage_path = (
            self.settings.settings_dir_path.joinpath("../source/Runner/Admin/manage.py")
            .resolve()
            .as_posix()
        )
        start_cmd_list = self.start_cmd_list(
            manage_path=manage_path,
            host="127.0.0.1",
            port=8401,
        )

        print(f"start_cmd_list {start_cmd_list}")
        print()
        print(f"访问后台: http://127.0.0.1:8401/admin")
        print()
        subprocess.run(start_cmd_list)

    urls = [
        (r"/", Index),
        (r"/query", Query),
        (r"/add", Add),
        (r"/delete", Delete),
        (r"/update", Update),
        (r"/demo", Demo),
    ]

    # 运行 xy_web_server -w tornado start
    def tornado_start(self):
        print("tornado_start")
        settings = self.default_application_settings()
        settings.update(
            {
                "debug": True,
                "autoreload": True,
                "template_path": self.settings.settings_dir_path.joinpath("../template")
                .resolve()
                .as_posix(),
                "cookie_secret": uuid.uuid4().hex,
                "login_url": "/user/login",
            }
        )
        settings.update(
            {
                "static_path": self.settings.settings_dir_path.joinpath("../static")
                .resolve()
                .as_posix(),
            }
        )
        loop = asyncio.get_event_loop()
        loop.create_task(
            self.sync_make_application(urls=self.urls, settings=settings, bind=8400)
        )
        pending = asyncio.all_tasks(loop=loop)
        group = asyncio.gather(*pending, return_exceptions=True)
        print("请访问服务: \nhttp://127.0.0.1:8400")
        results = loop.run_until_complete(group)
        print(f"服务运行结果, {results}")
        loop.close()
