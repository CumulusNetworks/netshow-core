# pylint: disable=c0111

from netshow._version import get_version
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages
setup(
    name='netshow-core',
    version=get_version(),
    url="http://github.com/CumulusNetworks/netshow",
    description="Linux Network Troubleshooting Tool",
    author='Cumulus Networks',
    author_email='ce-ceng@cumulusnetworks.com',
    packages=find_packages(),
    namespace_packages=['netshow'],
    install_requires=[
        "netshow-core-lib"
    ],
    zip_safe=False,
    scripts=['bin/netshow'],
    license='GPLv2',
    classifiers=[
        'Topic :: System :: Networking',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux'
    ],
)