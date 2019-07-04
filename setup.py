"""
https://github.com/pypa/sampleproject/blob/master/setup.py
"""

import subprocess

# To use a consistent encoding
from codecs import open
from os import path

import versioneer
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def githash():
    return subprocess.check_output(["git", "rev-parse", "HEAD"])


setup(
    name="dualplot",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Plot with dual axis",
    long_description=long_description,
    url="",
    author="Michele Vascellari",
    author_email="michele.vascellari@gmail.com",
    license="",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish (should match "license" above)
        "License :: ",
        # Specify the Python versions you support here.
        # In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or
        # both.
        # 'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.5",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["matplotlib", "versioneer"],
    setup_requires=["pytest-runner"],
    test_requires=["pytest"],
)
