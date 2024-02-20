# 本地运行方法

```bash
$ docker run -ti --rm -v /Users/huzhi/work/code/py_code/pytest_code/pytest_code:/pytest_code -w /pytest_code python:3.10.13-bullseye bash

$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

$ find . -name "*.py" -exec yapf -i {} \;

$ find . -name .gitignore -exec mv {} {}-bak \;

```
