import os
import setuptools
from setuptools.command.build_ext import build_ext
import subprocess
import datetime

def generate_version():
    base_version = "0.1.0"
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return f"{base_version}.{timestamp}"




class cmake_build_ext(build_ext):
    def build_extensions(self):
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', '../../'], cwd=self.build_temp)
        subprocess.check_call(['make', 'bssl'], cwd=self.build_temp)
        ext_path = self.get_ext_fullpath('boringssl')
        subprocess.check_call(['cp', self.build_temp + '/ssl/libssl.so', ext_path])


setuptools.setup(
    name='boringssl-binary-build',
    version=generate_version(),
    author="boring",
    author_email="boring",
    description='Build BoringSSL',
    long_description='Build BoringSSL',
    package_dir={"boringssl_binary_build": "."},
    packages=["boringssl_binary_build"],
    python_requires='>=3.9',
    ext_modules=[setuptools.extension.Extension('boringssl', sources=[])],
    cmdclass={'build_ext': cmake_build_ext},
)
