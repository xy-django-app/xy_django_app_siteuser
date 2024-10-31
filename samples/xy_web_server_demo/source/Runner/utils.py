# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "utils"
"""
  * @File    :   utils.py
  * @Time    :   2024/10/30 11:30:55
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

import os, sys
from xy_string.utils import is_empty_string


def local_python_path_list() -> list | None:
    env = os.environ.copy()
    python_path = env.get("PYTHONPATH")
    if not is_empty_string(python_path):
        sys_python_path = ":".join(sys.path)
        if not is_empty_string(python_path):
            python_path = f"{sys_python_path}:{python_path}"
    else:
        python_path = ":".join(sys.path)
    source_python_path_list = (
        python_path.split(":") if not is_empty_string(python_path) else []
    )
    python_path_list = []
    for path in source_python_path_list:
        if path not in python_path_list:
            python_path_list.append(path)

    return python_path_list


def local_python_path_string() -> str | None:
    python_path_list = local_python_path_list()
    python_path = None
    if isinstance(python_path_list, list) and len(python_path_list) > 0:
        python_path = ":".join(python_path_list)
    return python_path
