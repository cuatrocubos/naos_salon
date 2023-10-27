from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in naos_salon/__init__.py
from naos_salon import __version__ as version

setup(
	name="naos_salon",
	version=version,
	description="Naos Salon Customizations",
	author="Cuatrocubos Soluciones",
	author_email="jgiron@cuatrocubos.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
