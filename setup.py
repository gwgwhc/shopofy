from setuptools import setup, find_packages

setup(
    name="shopofy",
    packages=find_packages(),  # Automatically finds 'shopofy' package
    install_requires=[],  # Add dependencies here if needed
    entry_points={
        "console_scripts": [
            "shopofy = shopofy.__main__:main",  # Enables `shopofy` as a CLI command
        ],
    },
)
