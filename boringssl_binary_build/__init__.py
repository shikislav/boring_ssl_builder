import os
import ctypes

# Path to the shared libraries
LIB_DIR = os.path.join(os.path.dirname(__file__), ".libs")
LIBSSL_PATH = os.path.join(LIB_DIR, "libssl.so")
LIBCRYPTO_PATH = os.path.join(LIB_DIR, "libcrypto.so")

# Load the shared libraries
try:
    libssl = ctypes.CDLL(LIBSSL_PATH)
    libcrypto = ctypes.CDLL(LIBCRYPTO_PATH)
    print("Loaded BoringSSL libraries successfully")
except OSError as e:
    raise RuntimeError(f"Failed to load BoringSSL libraries: {e}")
