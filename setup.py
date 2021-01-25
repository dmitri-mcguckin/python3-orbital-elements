import setuptools
import orbital_elements as oe

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=oe.APP_NAME,
    version=oe.APP_VERSION,
    author=oe.APP_AUTHOR,
    license=oe.APP_LICENSE,
    description=oe.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=oe.APP_URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: User Interfaces",
    ],
    install_requires=[
        "numpy",
        "pytz",
        "datetime2",
        "matplotlib",
        "ConfigArgParse",
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "pytest",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
            "python-can"
        ]
    },
    python_requires='>=3.8.5',
    entry_points={
        "console_scripts": [
            f'{oe.APP_NAME} = orbital_elements.__main__:main',
        ]
    }
)
