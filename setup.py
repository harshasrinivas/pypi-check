from setuptools import setup

setup(name='pypi-check',
    description='Check availability of PyPI package names',
    version='0.1.1',
    author='Harsha Srinivas',
    author_email='95harsha95@gmail.com',
    packages=['pypi_check'],
    entry_points={
        'console_scripts': ['pypi-check=pypi_check:main'],
    },
    url='https://github.com/harshasrinivas/pypi-check/',
    keywords=[ 'CLI', 'python'],
    install_requires=['future', 'pypilist', 'blessings'],
    classifiers=[
        'Operating System :: POSIX',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
  ],)
