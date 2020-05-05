# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-13f", # the name that you will install via pip
    version="1.1",
    author="Ekram Ahmed",
    author_email="ekramullahzaki@gmail.com",
    description="example from assignment",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/Ekram49/ekram-lambdata-13f",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)