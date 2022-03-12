import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="reprdle",
    version="1.0.0",
    description="Play wordle in the repl with the power of __repr__!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/torshepherd/reprdle",
    author="Tor Shepherd",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["wordle"],
    include_package_data=True,
    install_requires=["colored"]
)
