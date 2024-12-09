#!/bin/bash -ex

# Install dependencies
sudo yum install -y cmake gcc g++ make

# Clone and build BoringSSL
git clone https://boringssl.googlesource.com/boringssl
cd boringssl
mkdir build
cd build
cmake -DBUILD_SHARED_LIBS=1 ..
make
mkdir -p ../boringssl_binary_build/.libs
cp ssl/libssl.so ../boringssl_binary_build/.libs/
cp crypto/libcrypto.so ../boringssl_binary_build/.libs/

# Ensure pip and setuptools are available for the current Python version
python -m ensurepip
python -m pip install --upgrade pip setuptools wheel

# Build the wheel
python setup.py bdist_wheel
