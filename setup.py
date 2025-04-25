import os
from setuptools import setup

# Dynamically fetch the version from version.py
version = {}
version_file = os.path.join(os.path.dirname(__file__), "version.py")
with open(version_file) as f:
    exec(f.read(), version)

setup(
    version=version["__version__"],
    entry_points={
        "console_scripts": [
            "shopofy=shopofy.__main__:main",  # Replace 'shopofy.main:main' with the actual module and function
        ]
    },
)
