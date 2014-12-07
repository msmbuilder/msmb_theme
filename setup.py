# -*- coding: utf-8 -*-

"""`msmb_theme` is a slight modification of `sphinx_rtd_theme`
    
    `sphinx_rtd_theme` lives on `Github`_.

.. _github: https://www.github.com/snide/sphinx_rtd_theme

"""
from setuptools import setup
import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'msmb_theme/_version.py'
versioneer.versionfile_build = 'msmb_theme/_version.py'
versioneer.tag_prefix = '' # tags are like 1.2.0
versioneer.parentdir_prefix = 'msmb_theme-' # dirname like 'myproject-1.2.0'

setup(
   name='msmb_theme',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/snide/sphinx_rtd_theme/',
    license='MIT',
    author='Dave Snider',
    author_email='dave.snider@gmail.com',
    description='ReadTheDocs.org theme for Sphinx, 2013 version.',
    zip_safe=False,
    packages=['msmb_theme'],
    package_data={'msmb_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
