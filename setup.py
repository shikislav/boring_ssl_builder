import os
import subprocess
import setuptools
from setuptools.command.build_ext import build_ext

class cmake_build_ext(build_ext):
    def build_extensions(self):
        # Ensure build directory exists
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        # Change to the build directory for running cmake & make
        build_dir = os.path.abspath(self.build_temp)
        src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'boringssl'))

        # Run cmake to configure the build
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', '..'], cwd=os.path.join(src_dir, 'build'))
        # Run make to build BoringSSL (ssl and crypto libs)
        subprocess.check_call(['make', '-j', 'bssl'], cwd=os.path.join(src_dir, 'build'))

        # The extension name here should match the extension in ext_modules
        ext_name = self.extensions[0].name
        ext_path = self.get_ext_fullpath(ext_name)

        # Create the extension output directory if necessary
        ext_dir = os.path.dirname(ext_path)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)

        # Copy the built libraries into the package directory
        # Adjust paths as needed based on BoringSSL build structure
        ssl_lib = os.path.join(src_dir, 'build', 'ssl', 'libssl.so')
        crypto_lib = os.path.join(src_dir, 'build', 'crypto', 'libcrypto.so')

        subprocess.check_call(['cp', ssl_lib, ext_dir])
        subprocess.check_call(['cp', crypto_lib, ext_dir])

        # Rename the main extension file to something like "_boringssl.so" if needed
        # Since we have no actual extension C code, we can leave it as is.
        # The libraries will be available in the package directory.

setuptools.setup(
    name='boringssl-binary-build',
    version='0.0.6',
    author="Jonatron",
    author_email="jon.ath.4n+boring@gmail.com",
    description='Build and bundle BoringSSL',
    long_description='Build and bundle BoringSSL for easy installation.',
    python_requires='>=3.10',
    # Point the package directory to current dir and ensure the package is found
    package_dir={"boringssl_binary_build": "."},
    packages=["boringssl_binary_build"],
    # Include the shared libraries in the wheel
    package_data={
        "boringssl_binary_build": ["*.so"]
    },
    ext_modules=[
        # This creates a dummy extension named 'boringssl', which triggers
        # the build_ext command. We don't provide actual C sources here.
        setuptools.Extension('boringssl', sources=[])
    ],
    cmdclass={'build_ext': cmake_build_ext},
)

