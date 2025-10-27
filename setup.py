from setuptools import find_packages, setup

setup(
    name="cli-password-manager",
    version="0.1.0",
    description="CLI Password Manager",
    python_requires=">=3.11",
    packages=find_packages(),
    install_requires=[
        "cryptography>=46.0.3",
        "python-dotenv>=1.2.1",
        "tabulate>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "password-manager=cli_password_manager.main:main",
        ],
    },
)
