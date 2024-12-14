from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext

class CustomBuild(build_ext):
    def run(self):
        # Ensure BoringSSL binaries are included
        self.copy_file('bssl_build/crypto/libcrypto.so', 'bssl_binary')
        self.copy_file('bssl_build/ssl/libssl.so', 'bssl_binary')

setup(
    name='boringssl_binary_build',
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('bssl_binary', ['bssl_build/crypto/libcrypto.so', 'bssl_build/ssl/libssl.so'])
    ],
    cmdclass={'build_ext': CustomBuild},
)
