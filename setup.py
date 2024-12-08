import os
import setuptools
from setuptools.command.build_ext import build_ext
import subprocess
from distutils.extension import Extension  # Correct import


class cmake_build_ext(build_ext):
    def build_extensions(self):
        # Ensure the build directory exists
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        # Path to the BoringSSL source directory
        boringssl_source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'boringssl'))

        # Verify that the BoringSSL source exists
        if not os.path.exists(boringssl_source_dir):
            raise RuntimeError(f"BoringSSL source directory not found: {boringssl_source_dir}")

        # Configure with CMake
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', boringssl_source_dir], cwd=self.build_temp)

        # Build with Make
        subprocess.check_call(['make'], cwd=self.build_temp)

        # Copy the built libraries to the package directory
        ext_path = os.path.dirname(self.get_ext_fullpath('boringssl'))
        os.makedirs(ext_path, exist_ok=True)
        subprocess.check_call(['cp', os.path.join(self.build_temp, 'ssl/libssl.so'), ext_path])
        subprocess.check_call(['cp', os.path.join(self.build_temp, 'crypto/libcrypto.so'), ext_path])


setuptools.setup(
    name='boringssl-binary-build',
    version='0.0.1',
    description='Python package bundling prebuilt BoringSSL binaries',
    ext_modules=[
        Extension('boringssl', sources=[])  # Use `distutils.extension.Extension`
    ],
    cmdclass={'build_ext': cmake_build_ext},
)

