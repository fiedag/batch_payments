from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in batch_payments/__init__.py
from batch_payments import __version__ as version

setup(
	name="batch_payments",
	version=version,
	description="Permit multiple purchase invoices to be paid in one batch",
	author="Fiedler Consulting",
	author_email="alex@fiedlerconsulting.com.au",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
