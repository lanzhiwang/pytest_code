import os
import json

"""
os.path.expanduser(path)
把 path 中包含的 "~" 和 "~user" 转换成用户目录

>>> import os
>>> full_path = os.path.expanduser('~/.cheese.json')
>>> full_path
'/Users/huzhi/.cheese.json'
>>>
"""

def read_cheese_preferences():
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'r') as f:
        prefs = json.load(f)
    return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)


def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)


_default_prefs = {
    'slicing': ['manchego', 'sharp cheddar'],
    'spreadable': ['Saint Andre', 'camembert',
                   'bucheron', 'goat', 'humbolt fog', 'cambozola'],
    'salads': ['crumbled feta']
}

if __name__ == '__main__':
    write_default_cheese_preferences()

"""
(venv) huzhi@bogon monkey % python cheese.py
(venv) huzhi@bogon monkey % ll /Users/huzhi/.cheese.json
-rw-r--r--  1 huzhi  staff  267  5 20 19:00 /Users/huzhi/.cheese.json
(venv) huzhi@bogon monkey % cat /Users/huzhi/.cheese.json
{
    "slicing": [
        "manchego",
        "sharp cheddar"
    ],
    "spreadable": [
        "Saint Andre",
        "camembert",
        "bucheron",
        "goat",
        "humbolt fog",
        "cambozola"
    ],
    "salads": [
        "crumbled feta"
    ]
}                                                                                                                                                                                                     (venv) huzhi@bogon monkey % rm -rf /Users/huzhi/.cheese.json
(venv) huzhi@bogon monkey %
"""
