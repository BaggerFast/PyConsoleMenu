from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='PyConsoleMenu',
    version='1.0.0',
    license='MIT',
    author="BaggerFast (Aleksandrov Daniil)",
    author_email='riosha3@gmail.com',
    description='A simple console menu system using curses',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BaggerFast/PyConsoleMenu',
    downoload_url='https://github.com/BaggerFast/PyConsoleMenu/archive/v1.0.0.zip',
    keywords='python menu, console menu, menu, curses menu, python console menu',
    install_requires=[
        "widows-curses; sys_platform == 'win32'"
    ],
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
