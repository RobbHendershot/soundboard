import setuptools

setuptools.setup(
    name="soundboard",
    version="0.1.0",
    url=" ",

    author="Robb Hendershot",
    author_email="robb.hendershot@gmail.com",

    description=" ",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    entry_points={
        'gui_scripts': [
            'soundboard = soundboard.__main__:main'
        ]
    },

)
