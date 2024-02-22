"""_summary_
"""

from setuptools import find_packages, setup

VERSION = '0.0.1'
DESCRIPTION = 'A sample test package'

setup(
    name='ft_package',
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/eagle/ft_package",
    author="eagle",
    author_email="eagle@42.com",
    license="MIT",
    license_file="LICENSE",
    packages=find_packages(),
    install_requires=[],
    classifiers=[]
)
