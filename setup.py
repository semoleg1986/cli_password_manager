from setuptools import find_packages, setup

setup(
    name="cli-password-manager",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "password-manager=cli_password_manager.main:main",
        ],
    },
)
