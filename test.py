from cffi import FFI
import bssl_build

ffi = FFI()

ffi.cdef("""
    typedef struct ssl_st SSL;
    typedef struct ssl_ctx_st SSL_CTX;
    typedef struct ssl_method_st SSL_METHOD;

    SSL *SSL_new(SSL_CTX *ctx);
    SSL_CTX *SSL_CTX_new(const SSL_METHOD *method);
    void SSL_set_bio(SSL *ssl, BIO *rbio, BIO *wbio);
    int SSL_connect(SSL *ssl);
    const SSL_METHOD *TLS_method(void);

    int SSL_write(SSL *ssl, const void *buf, int num);
    int SSL_read(SSL *ssl, void *buf, int num);
""")

libcrypto, libssl = boringssl_binary_build.load_bssl_libraries(ffi)

ctx = libssl.SSL_CTX_new(libssl.TLS_method())
print("SSL context created:", ctx)
