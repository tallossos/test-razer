#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="openrazer_daemon",
    version="3.2.0",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
