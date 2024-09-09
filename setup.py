from setuptools import setup

setup(
    name="package",
    version="0.1.0",
    py_modules=["package"],
    author="Bala Praneeth",
    author_email="lbalapraneethreddy@karunya.edu.in",
    description="A sample single-file package for demonstration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bala-Praneeth/Hello_Poc_Package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
