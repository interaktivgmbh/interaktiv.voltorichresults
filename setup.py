from os import path

from setuptools import find_packages, setup

# Package metadata
NAME = 'interaktiv.voltorichresults'
DESCRIPTION = 'Plone 6 backend addon for managing Google Rich Results (schema.org JSON-LD) in Volto.'
URL = 'https://github.com/interaktivgmbh/interaktiv.voltorichresults'
EMAIL = 'support@interaktiv.de'
AUTHOR = 'Interaktiv GmbH'
REQUIRES_PYTHON = '~=3.11'
VERSION = '1.0.0'
REQUIRES_PLONE_VERSION = '6.0.0'

# Additional package requires
REQUIRED = [
    'setuptools',
    'Products.CMFPlone>=' + REQUIRES_PLONE_VERSION,
    'plone.restapi'
]
EXTRAS = {
    'test': ['plone.app.testing']
}

this_directory = path.abspath(path.dirname(__file__))

# Load long description from README.md
try:
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: Addon",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone volto seo rich-results schema.org json-ld structured-data',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license='GPL version 2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['interaktiv'],
    include_package_data=True,
    zip_safe=False,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
)
