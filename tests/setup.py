from setuptools import setup, find_packages

setup(
    name="evillan",
    version="1.0.0",
    description="A CLI tool for advanced payload encoding and CVE testing",
    author="y_mo4n1ngst3r",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={"console_scripts": ["evillan=src.cli:main"]},
)
