"""
Common interfacte to git and hg
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='wib',
    version='0.2.2',
    url='https://github.com/chengsoonong/wib',
    license='BSD',
    author='Cheng Soon Ong',
    author_email='chengsoon.ong@anu.edu.au',
    description='Common interface to git and hg',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'wib = wib.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
