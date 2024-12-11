import os
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


def _generate_random_str():
    import string
    import random
    return ''.join([random.choice(string.ascii_lowercase+ string.digits) for _ in range(7)])

class cmake_build_ext(build_ext):
    def build_extensions(self):
        # Absolute paths for clarity
        repo_dir = os.path.abspath(os.path.dirname(__file__))
        src_dir = os.path.join(repo_dir, 'boringssl')
        build_dir = os.path.abspath(self.build_temp)

        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        # Configure and build BoringSSL using CMake
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', src_dir], cwd=build_dir)
        subprocess.check_call(['make', '-j', 'bssl'], cwd=build_dir)

        # Place the resulting shared library where Python expects the extension
        ext = self.extensions[0]
        ext_path = self.get_ext_fullpath(ext.name)
        ext_dir = os.path.dirname(ext_path)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)

        target_so = os.path.join(ext_dir, "_boringssl.so")
        subprocess.check_call(['cp', os.path.join(build_dir, 'ssl/libssl.so'), target_so])

setup(
    name='boringssl-binary-build',
    version=f"0.0.7.dev0+{_generate_random_str()}",
    author="",
    author_email="",
    description='Build and bundle BoringSSL',
    long_description='Build and bundle BoringSSL for easy installation.',
    python_requires='>=3.9',
    packages=["boringssl_binary_build"],
    package_dir={"boringssl_binary_build": "."},
    package_data={"boringssl_binary_build": ["_boringssl.so"]},
    include_package_data=True,
    ext_modules=[Extension('boringssl', sources=[])],
    cmdclass={'build_ext': cmake_build_ext},
)

