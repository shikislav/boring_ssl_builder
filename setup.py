import os
import setuptools

# Define the package version. This will be updated by the GitHub Actions workflow.
VERSION = os.getenv('VERSION', '0.0.1')

setuptools.setup(
    name='boringssl-binary-build',
    version=VERSION,
    description='Python package bundling prebuilt BoringSSL binaries',
    packages=['boringssl_binary_build'],
    package_data={'boringssl_binary_build': ['.libs/*.so']},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    # If you have any dependencies, list them here
    install_requires=[
        # e.g., 'requests>=2.25.1',
    ],
)

