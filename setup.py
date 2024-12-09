import os
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class cmake_build_ext(build_ext):
    def build_extensions(self):
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        # Assuming BoringSSL source is in `boringssl/`
        src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'boringssl'))
        build_dir = os.path.join(src_dir, 'build')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        # Run CMake and make
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', '..'], cwd=build_dir)
        subprocess.check_call(['make', '-j', 'bssl'], cwd=build_dir)

        # Copy libs to the extension output directory
        ext = self.extensions[0]
        ext_path = self.get_ext_fullpath(ext.name)
        ext_dir = os.path.dirname(ext_path)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)

        ssl_lib = os.path.join(build_dir, 'ssl', 'libssl.so')
        crypto_lib = os.path.join(build_dir, 'crypto', 'libcrypto.so')
        subprocess.check_call(['cp', ssl_lib, ext_dir])
        subprocess.check_call(['cp', crypto_lib, ext_dir])

setup(
    name='boringssl-binary-build',
    version='0.0.6',
    author="boring",
    author_email="boring@gmail.com",
    description='Build and bundle BoringSSL',
    long_description='Build and bundle BoringSSL for easy installation.',
    python_requires='>=3.10',
    packages=["boringssl_binary_build"],
    package_dir={"boringssl_binary_build": "."},
    package_data={"boringssl_binary_build": ["*.so"]},
    ext_modules=[Extension('boringssl', sources=[])],
    cmdclass={'build_ext': cmake_build_ext},
)

