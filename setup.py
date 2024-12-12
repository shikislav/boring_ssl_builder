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
    packages=find_packages(),  # Automatically finds the `bssl_binary` folder
    python_requires=">=3.10",
    install_requires=["cffi"],
    package_data={
        "boringssl_binary_build": ["libssl.so"],  # Include the BoringSSL shared library
    },
    include_package_data=True,  # Ensures `package_data` files are included
)
