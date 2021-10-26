# coding: utf-8

"""
    Demisto API
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "demisto-py"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open('requirements.txt') as f:
    REQUIRES = f.read().splitlines()

with open('README.md', 'r') as f:
    readme = f.read()
    

setup(
    use_scm_version={
        'local_scheme': lambda a: ""
    },
    setup_requires=['setuptools_scm'],
    name=NAME,
    description="A Python library for the Demisto API",
    author_email="",
    url="https://github.com/demisto/demisto-py",
    keywords=["Swagger", "Demisto API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    long_description=readme,
    long_description_content_type='text/markdown',
    license='Apache Software License',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',    
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
)
