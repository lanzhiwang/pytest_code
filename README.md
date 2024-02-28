# 本地运行方法

```bash
$ docker run -ti --rm -v ~/work/code/py_code/pytest_code/pytest_code:/pytest_code -w /pytest_code python:3.10.13-bullseye bash

$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

$ find . -name "*.py" -exec yapf -i {} \;

$ find . -name .gitignore -exec mv {} {}-bak \;

```

```bash
pytest \
-n 2 \
--dist=loadscope \
-s \
-o junit_logging=all \
--html=./report/pytest.html \
--junitxml=./report/report.xml \
--self-contained-html \
--alluredir=./report/allure-result \
new_case/middleware/rabbitmq

# pytest-xdist==3.5.0
-n numprocesses, --numprocesses=numprocesses
Shortcut for '--dist=load --tx=NUM*popen'.
With 'auto', attempt to detect physical CPU count.
With 'logical', detect logical CPU count.
If physical CPU count cannot be found, falls back to logical count.
This will be 0 when used with --pdb.

--dist=distmode
set mode for distributing tests to exec environments.
each: send each test to all available environments.
load: load balance by sending any pending test to any available environment.
loadscope: load balance by sending pending groups of tests in the same scope to any available environment.
loadfile: load balance by sending test grouped by file to any available environment.
loadgroup: like load, but sends tests marked with 'xdist_group' to the same worker.
worksteal: split the test suite between available environments, then rebalance when any worker runs out of tests.
(default) no: run tests inprocess, don't distribute.

--tx=xspec
add a test execution environment.
some examples: --tx popen//python=python2.5 --tx socket=192.168.1.102:8888 --tx ssh=user@codespeak.net//chdir=testcache

-s
Shortcut for --capture=no

--capture=method
Per-test capturing method: one of fd|sys|no|tee-sys

-o OVERRIDE_INI, --override-ini=OVERRIDE_INI
Override ini option with "option=value" style, e.g. `-o xfail_strict=True -o cache_dir=cache`.

```
