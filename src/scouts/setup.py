from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in scouts/__init__.py
from scouts import __version__ as version

setup(
	name="scouts",
	version=version,
	description="Scouts Tasmania ERP Intergration",
	author="scouts.com.au",
	author_email="admin@lanceolata.com.au",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
