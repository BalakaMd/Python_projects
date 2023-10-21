from setuptools import setup

APP_NAME = 'Sugar Control'
APP = ['MeaseringSugarUI.py']
DATA_FILES = [('Data', '/Users/dimkabalakin/Measuring_sugar_with_BD/Data/Sugar_DB.db')]
OPTIONS = {'iconfile': 'Data/medical_icon.ico',
           'argv_emulation': True
           }

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
