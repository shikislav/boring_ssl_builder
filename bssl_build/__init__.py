import pathlib
from cffi import FFI

current_dir = pathlib.Path(__file__).parent

libcrypto_path = current_dir.joinpath('libcrypto.so').resolve()
libssl_path = current_dir.joinpath('libssl.so').resolve()

def load_bssl_libraries(ffi: FFI):
    """
    Loads the BoringSSL libraries (libcrypto and libssl) using the provided FFI instance.
    This function assumes `ffi.cdef` has already been called by the user.
    
    Args:
        ffi (FFI): The CFFI instance with the necessary definitions (cdef).

    Returns:
        tuple: A tuple containing the loaded libcrypto and libssl libraries.
    """
    # Load libraries using ffi.dlopen
    libcrypto = ffi.dlopen(str(libcrypto_path))
    libssl = ffi.dlopen(str(libssl_path))
    
    return libcrypto, libssl
