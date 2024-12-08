import os
import setuptools
from setuptools.command.build_ext import build_ext
import subprocess

class cmake_build_ext(build_ext):
    def build_extensions(self):
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        # Configure with CMake
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', '../../'], cwd=self.build_temp)
        # Build with Make
        subprocess.check_call(['make', 'bssl'], cwd=self.build_temp)
        # Copy the built library to the output directory
        ext_path = self.get_ext_fullpath('boringssl')
        subprocess.check_call(['cp', self.build_temp + '/ssl/libssl.so', ext_path])

setuptools.setup(
    name='boringssl-zanze-binary-build',  # Change this to your unique name
    version='0.0.1',
    author="Your Name",
    author_email="yourname@example.com",
    description='Build BoringSSL',
    long_description='Build BoringSSL',
    package_dir={"boringssl_binary_build": "."},
    packages=["boringssl_binary_build"],
    python_requires='>=3.6',
    ext_modules=[setuptools.extension.Extension('boringssl', sources=[])],
    cmdclass={'build_ext': cmake_build_ext},
)
