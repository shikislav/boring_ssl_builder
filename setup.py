import setuptools
import datetime

def generate_version():
    base_version = '0.1.0'
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    return f'{base_version}.{timestamp}'

setuptools.setup(
    name='boringssl-binary-build',
    version=generate_version(),
    author='boring',
    author_email='boring@example.com',
    description='Prebuilt BoringSSL binaries for Python',
    long_description='A package containing prebuilt BoringSSL binaries.',
    package_dir={'': '.'},
    packages=[],
    python_requires='>=3.9',
    install_requires=[
        'cffi>=1.15.0',  # Add required dependencies
    ],
    data_files=[('', ['libssl.so'])],
)

