#!/bin/bash -ex

# Install dependencies
yum install -y cmake gcc g++ make

# List of Python versions to build for
PYTHON_VERSIONS=(
    cp310-cp310
    cp311-cp311
    cp312-cp312
)

for PYTHON_VERSION in "${PYTHON_VERSIONS[@]}"; do
    # Ensure pip and setuptools are available
    /opt/python/${PYTHON_VERSION}/bin/python -m ensurepip
    /opt/python/${PYTHON_VERSION}/bin/python -m pip install --upgrade pip setuptools wheel

    # Build the wheel
    /opt/python/${PYTHON_VERSION}/bin/python setup.py bdist_wheel
done
