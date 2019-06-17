from setuptools import find_packages, setup

setup(
    name='faust_app',
    version='1.0.0',
    description='Use Faust for FarmDrive internal App',
    author='MobiDev',
    author_email='',
    url='',
    platforms=['any'],
    license='Proprietary',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['faust'],
    python_requires='~=3.6',
    entry_points={
        'console_scripts': [
            'faust_app = faust_app.app:main',
        ],
    },
)
