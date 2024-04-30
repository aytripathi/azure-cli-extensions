#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from codecs import open
from setuptools import setup, find_packages
try:
    from azure_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger
    logger.warn("Wheel is not available, disabling bdist_wheel hook")

# TODO: Confirm this is the right version number you want and it matches your
# HISTORY.rst entry.

VERSION = '1.7.0'

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

# TODO: Add any additional SDK dependencies here
DEPENDENCIES = [
    'kubernetes==24.2.0',
    'pycryptodome==3.14.1',
    'azure-mgmt-hybridcompute==7.0.0'
]

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='connectedk8s',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools Connectedk8s Extension',
    # TODO: Update author and email, if applicable
    author='Microsoft Corporation',
    author_email='k8connect@microsoft.com',
    url='https://github.com/Azure/azure-cli-extensions/tree/main/src/connectedk8s',
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_connectedk8s': ['azext_metadata.json', 'troubleshoot_diagnoser_job_with_proxycert_mount.yaml', 'troubleshoot_diagnoser_job_without_proxycert.yaml']},
)
