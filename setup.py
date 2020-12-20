import os
from setuptools import setup, find_packages

with open(os.path.join("treedir", "version.py"), "r") as f:
    exec(f.read())

with open("README.md", "r") as f:
    description = f.read()

requirements = ["click==7.1.2", "colorama==0.4.4"]

setup(
    name="treedir",
    version=__version__,
    description=description,
    long_description_content_type="text/markdown",
    author="Appaji",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
    keywords="tree directory-structure",
    entry_points="""
        [console_scripts]
        treedir=treedir.cli:cli
    """,
)
