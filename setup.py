from setuptools import setup

setup(
    name='py_console_menu',
    version='1.0.0',
    license='MIT',
    author="BaggerFast (Aleksandrov Daniil)",
    author_email='riosha3@gmail.com',
    description='A simple console menu system using curses',
    long_description='Contains: SelectorMenu, MultiSelectorMenu, FunctionalMenu',
    url='https://github.com/BaggerFast/PyConsoleMenu',
    downoload_url='?',
    keywords='?',
    install_requires=[
        "widows-curses; sys_platform == 'win32'"
    ],
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
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
