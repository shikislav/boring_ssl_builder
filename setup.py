from setuptools import setup, find_packages

setup(
    name='boringssl_binary_build',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'boringssl_binary_build': ['bssl_binary/*.so'],
    },
    # Optional: Add other metadata as needed
    author='Your Name',
    author_email='your.email@example.com',
    description='BoringSSL binaries packaged for Python',
    url='https://github.com/yourusername/boringssl_binary_build',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
