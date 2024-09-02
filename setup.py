from setuptools import setup

setup(
    name="task-cli",
    version="0.1",
    py_modules=["main", "utils", "command_processor", "storage"],
    entry_points={
        'console_scripts' : [
            'task-cli = main:main'
        ]
    }
)