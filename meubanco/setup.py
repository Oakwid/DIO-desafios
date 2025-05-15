from setuptools import setup, find_packages
import os

current_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_path, "README.md"), encoding="utf-8") as f:
    page_description = f.read()

with open(os.path.join(current_path, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="meubanco",
    version="0.1.3",
    author="Fernando Nascimento",
    author_email="fernando.cs.rj@gmail.com",
    description="Um sistema bancário modularizado em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oakwid/DIO-desafios/meubanco",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "meubanco=meubanco.main:main_menu"
        ]
    },
)