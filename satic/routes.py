from typing import Callable
from fastapi import APIRouter

def dummy_view():  # 示例视图函数
    return {"message": "Hello World"}

def another_view():  # 另一个示例视图函数
    return {"message": "Another View"}

# 定义一个列表，其中每个元素都是一个包含路径、视图函数引用和方法的字典
route_list = [
    {
        "path": "/",
        "view": dummy_view,
        "method": ["GET"]
    },
    {
        "path": "/another",
        "view": another_view,
        "method": ["GET"]
    }
]