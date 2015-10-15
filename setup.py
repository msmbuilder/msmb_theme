# -*- coding: utf-8 -*-

"""`msmb_theme` is a slight modification of `sphinx_rtd_theme`
    
    `sphinx_rtd_theme` lives on `Github`_.

.. _github: https://www.github.com/snide/sphinx_rtd_theme

"""
from setuptools import setup
import versioneer

setup(
    name='msmb_theme',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/msmbuilder/msmb_theme/',
    license='MIT',
    author='Matthew Harrigan',
    author_email='matthew.harrigan@outlook.com',
    description='Modification to sphinx_rtd_theme',
    zip_safe=False,
    packages=['msmb_theme'],
    package_data={'msmb_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
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
