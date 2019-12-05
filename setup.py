import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
    setuptools.setup(
    name="wikidump",
    version="0.0.1",
    author="Ruben Dorado",
    author_email="ruben.dorados@gmail.com",
    description="A utility to extract articles from a wikipedia dump",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdorado/wikidump",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)