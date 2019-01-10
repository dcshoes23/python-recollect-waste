import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recollect_waste",
    version="0.0.1",
    author="stealthhacker",
    description="Python 3 API for Recollect Waste to track waste pickup and types.",
    url="https://github.com/stealthhacker/recollect-waste",
    packages=['recollect_waste'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)