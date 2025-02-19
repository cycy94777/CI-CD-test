import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from my_app import add  # 這裡應該要成功找到 my_app.py


def test_add():
    assert add(2, 3) == 5 #預期 2 + 3 = 5
    assert add(-1, 1) == 0 #預期 -1 + 1 = 0