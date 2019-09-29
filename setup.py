import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="pelican-linkclass",
    version="1.0.0",
    description="Allows the setting of the class attribute of `<a>` elements according to whether the link is external or internal to the Pelican-generated site.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rlaboiss/pelican-linkclass",
    author="Rafael Laboissière",
    author_email="rafael@laboissiere.net",
    packages=['pelican_linkclass'],
    include_package_data=True,
    install_requires=[
        'pelican>=3.4',
        'Markdown>=3.0.1',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Framework :: Pelican :: Plugins',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
