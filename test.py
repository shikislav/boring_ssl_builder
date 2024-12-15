import argparse
from cffi import FFI

ffi = FFI()

# Define BoringSSL's functions and structures
ffi.cdef("""
typedef struct ssl_st SSL;
typedef struct ssl_ctx_st SSL_CTX;
typedef struct ssl_method_st SSL_METHOD;

SSL *SSL_new(SSL_CTX *ctx);
SSL_CTX *SSL_CTX_new(const SSL_METHOD *method);
const SSL_METHOD *TLS_method(void);
""")

def test_boringssl(lib_path):
    try:
        bssl = ffi.dlopen(lib_path)

        # Initialize SSL context and objects
        ctx = bssl.SSL_CTX_new(bssl.TLS_method())
        assert ctx != ffi.NULL, "Failed to create SSL_CTX"

        ssl = bssl.SSL_new(ctx)
        assert ssl != ffi.NULL, "Failed to create SSL"

        print("BoringSSL FFI test passed!")
    except Exception as e:
        print(f"BoringSSL FFI test failed: {e}")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test BoringSSL FFI compatibility.")
    parser.add_argument("--lib-path", required=True, help="Path to the BoringSSL shared library.")
    args = parser.parse_args()

    test_boringssl(args.lib_path)
