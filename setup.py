import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastatocsv",
    version="0.0.2",
    author="Andrew Kessler",
    author_email="drew.kessler.21@bishops.com",
    description="A package to convert .fasta files into .csv files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewk2021/fastatocsv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
