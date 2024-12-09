#!/bin/bash -ex
echo "Building wheels for Python: $PYTHON_VERSION"
yum -y install golang make cmake
cd /github/workspace

/opt/python/${PYTHON_VERSION}/bin/python setup.py bdist_wheel
auditwheel repair dist/*.whl

WHEEL_NAME=$(ls wheelhouse/*manylinux*.whl)
FINAL_NAME=boringssl_binary_build-0.0.6-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
mv $WHEEL_NAME wheelhouse/$FINAL_NAME

/opt/python/${PYTHON_VERSION}/bin/pip install twine
twine upload --verbose --repository testpypi wheelhouse/*.whl
