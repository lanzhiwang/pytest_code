# pytest 测试实战

```bash
(venv) huzhi@bogon tasks_proj % pwd
/Users/huzhi/work/code/pytest_code/tasks_proj
(venv) huzhi@bogon tasks_proj % tree -a .
.
├── CHANGELOG.rst
├── LICENSE
├── MANIFEST.in
├── setup.py
├── src
│   └── tasks
│       ├── .DS_Store
│       ├── __init__.py
│       ├── api.py
│       ├── cli.py
│       ├── config.py
│       ├── tasksdb_pymongo.py
│       └── tasksdb_tinydb.py
└── tests
    ├── conftest.py
    ├── func
    │   ├── __init__.py
    │   └── test_add.py
    ├── pytest.ini
    └── unit
        ├── __init__.py
        └── test_task.py

5 directories, 17 files
(venv) huzhi@bogon tasks_proj %

(venv) huzhi@bogon pytest_code % pip install -e ./tasks_proj
Obtaining file:///Users/huzhi/work/code/pytest_code/tasks_proj
Collecting click (from tasks==0.1.0)
  Downloading https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl (82kB)
    100% |████████████████████████████████| 92kB 26kB/s
Collecting tinydb (from tasks==0.1.0)
  Downloading https://files.pythonhosted.org/packages/b6/f6/b3e112addc8eb4a097f158124ce8b206767361a381f80c5f0c506d855e4a/tinydb-4.1.1-py3-none-any.whl
Requirement already satisfied: six in /Users/huzhi/work/code/venv/lib/python3.7/site-packages (from tasks==0.1.0) (1.14.0)
Installing collected packages: click, tinydb, tasks
  Running setup.py develop for tasks
Successfully installed click-7.1.2 tasks tinydb-4.1.1
(venv) huzhi@bogon pytest_code %

(venv) huzhi@bogon pytest_code % pip list
Package            Version Location
------------------ ------- -------------------------------------------------
aiohttp            3.6.2
asgiref            3.2.5
astroid            2.3.3
async-timeout      3.0.1
attrs              19.3.0
chardet            3.0.4
click              7.1.2
Django             1.8.2
idna               2.9
importlib-metadata 1.6.0
isort              4.3.21
lazy-object-proxy  1.4.3
mccabe             0.6.1
more-itertools     8.3.0
multidict          4.7.5
packaging          20.4
pip                19.0.3
pluggy             0.13.1
py                 1.8.1
pylint             2.4.4
pyparsing          2.4.7
pytest             5.4.2
python-slugify     4.0.0
pytz               2019.3
setuptools         40.8.0
six                1.14.0
SQLAlchemy         1.3.15
sqlparse           0.3.1
tasks              0.1.0   /Users/huzhi/work/code/pytest_code/tasks_proj/src
text-unidecode     1.3
tinydb             4.1.1
typed-ast          1.4.1
wcwidth            0.1.9
wrapt              1.11.2
yapf               0.29.0
yarl               1.4.2
zipp               3.1.0
(venv) huzhi@bogon pytest_code %

(venv) huzhi@bogon pytest_code % pip uninstall tasks
Uninstalling tasks-0.1.0:
  Would remove:
    /Users/huzhi/work/code/venv/bin/tasks
    /Users/huzhi/work/code/venv/lib/python3.7/site-packages/tasks.egg-link
Proceed (y/n)? y
  Successfully uninstalled tasks-0.1.0
(venv) huzhi@bogon pytest_code %
(venv) huzhi@bogon pytest_code % pip list
Package            Version
------------------ -------
aiohttp            3.6.2
asgiref            3.2.5
astroid            2.3.3
async-timeout      3.0.1
attrs              19.3.0
chardet            3.0.4
click              7.1.2
Django             1.8.2
idna               2.9
importlib-metadata 1.6.0
isort              4.3.21
lazy-object-proxy  1.4.3
mccabe             0.6.1
more-itertools     8.3.0
multidict          4.7.5
packaging          20.4
pip                19.0.3
pluggy             0.13.1
py                 1.8.1
pylint             2.4.4
pyparsing          2.4.7
pytest             5.4.2
python-slugify     4.0.0
pytz               2019.3
setuptools         40.8.0
six                1.14.0
SQLAlchemy         1.3.15
sqlparse           0.3.1
text-unidecode     1.3
tinydb             4.1.1
typed-ast          1.4.1
wcwidth            0.1.9
wrapt              1.11.2
yapf               0.29.0
yarl               1.4.2
zipp               3.1.0

(venv) huzhi@bogon pytest_code % ll tasks_proj/src/tasks.egg-info
total 48
drwxr-xr-x  8 huzhi  staff  256  5 20 11:08 ./
drwxr-xr-x  4 huzhi  staff  128  5 20 11:08 ../
-rw-r--r--  1 huzhi  staff  295  5 20 11:08 PKG-INFO
-rw-r--r--  1 huzhi  staff  472  5 20 11:08 SOURCES.txt
-rw-r--r--  1 huzhi  staff    1  5 20 11:08 dependency_links.txt
-rw-r--r--  1 huzhi  staff   47  5 20 11:08 entry_points.txt
-rw-r--r--  1 huzhi  staff   34  5 20 11:08 requires.txt
-rw-r--r--  1 huzhi  staff    6  5 20 11:08 top_level.txt
(venv) huzhi@bogon pytest_code %


```

参考：

* https://pragprog.com/book/bopytest/python-testing-with-pytest

