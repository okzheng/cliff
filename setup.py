#!/usr/bin/env python

PROJECT = 'democli'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Demo app for cliff',
    long_description=long_description,

    author='Doug Hellmann',
    author_email='doug.hellmann@gmail.com',

    url='https://github.com/openstack/cliff',
    download_url='https://github.com/openstack/cliff/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'democli = democli.main:main'
        ],
        'demo.cli': [
            'simple = democli.simple:Simple',
            'found = democli.simple:Found',
            'two_part = democli.simple:Simple',
            'error = democli.simple:Error',
            'list files = democli.list:Files',
            'files = democli.list:Files',
            'file = democli.show:File',
            'show file = democli.show:File',
            'unicode = democli.encoding:Encoding',
            'hooked = democli.hook:Hooked',
        ],
        'demo.cli.hooked': [
            'sample-hook = democli.hook:Hook',
        ],
    },

    zip_safe=False,
)
