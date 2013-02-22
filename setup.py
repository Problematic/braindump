"""
braindump - record what's on your mind
"""

from setuptools import setup, find_packages
import braindump
from braindump import cmdline

setup(
    name='braindump',
    version=braindump.__version__,
    description=__doc__,
    long_description=cmdline.__doc__,
    author=braindump.__author__,
    author_email='djstobbe@gmail.com',
    packages=find_packages(),
    package_data={'': ['LICENSE-MIT']},
    install_requires=['docopt>=0.6.1'],
    license='MIT',
    url='https://github.com/Problematic/braindump',
    entry_points={
        'console_scripts': [
            'braindump = braindump.cmdline:main'
        ]
    }
)
