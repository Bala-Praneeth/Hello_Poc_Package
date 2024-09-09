"""
sample_package.py - A simple, single-file Python package

This file contains all the functionality of the sample package in one place.
It can be imported and used as a regular Python module.

Usage:
    from sample_package import hello
    print(hello())
"""

__version__ = "0.1.0"
__author__ = "Bala Praneeth"
__email__ = "lbalapraneethreddy@karunya.edu.in"

def hello():
    """Return a greeting message."""
    return "Hello from the sample package!"

def main():
    """Main function to demonstrate package usage."""
    print(hello())

# Note: Remove the following lines when renaming to __init__.py
if __name__ == "__main__":
    main()
