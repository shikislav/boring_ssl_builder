from setuptools import setup, find_packages
import datetime

def generate_version():
    base_version = "0.1.0"
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return f"{base_version}.{timestamp}"

setup(
    name="boringssl_binary_build",  # Replace with your desired package name
    version=generate_version(),
    author="boring",
    description="Python interface for BoringSSL using FFI",
    packages=find_packages(),  # Automatically finds the package directories
    python_requires=">=3.10",
    install_requires=["cffi"],
    package_data={
        "": ["bssl_binary/libssl.so"],  # Specify relative path to shared library
    },
    include_package_data=True,  # Ensures `package_data` files are included
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
