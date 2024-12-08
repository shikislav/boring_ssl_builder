#!/bin/bash -ex

# Install dependencies
yum install -y cmake gcc g++ make

# Set Python version for building (example: Python 3.12)
PYTHON_VERSION=cp312-cp312

# Build the wheel
/opt/python/${PYTHON_VERSION}/bin/python setup.py bdist_wheel

# Use auditwheel to make the wheel manylinux compatible
auditwheel repair dist/*.whl

# Move repaired wheel to the dist directory
mv wheelhouse/*.whl dist/
