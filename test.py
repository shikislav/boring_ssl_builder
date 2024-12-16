from cffi import FFI
import bssl_build

ffi = FFI()

ffi.cdef("""
// boringssl/include/openssl/base.h
typedef struct ssl_st SSL;
typedef struct ssl_ctx_st SSL_CTX;
typedef struct ssl_method_st SSL_METHOD;

typedef struct bio_st BIO;
typedef struct bio_method_st BIO_METHOD;

// boringssl/include/openssl/ssl.h
SSL *SSL_new(SSL_CTX *ctx);
SSL_CTX *SSL_CTX_new(const SSL_METHOD *method);
void SSL_set_bio(SSL *ssl, BIO *rbio, BIO *wbio);
int SSL_connect(SSL *ssl);
const SSL_METHOD *TLS_method(void);

int SSL_set_tlsext_host_name(SSL *ssl, const char *name);
void SSL_CTX_set_grease_enabled(SSL_CTX *ctx, int enabled);
int SSL_CTX_set_strict_cipher_list(SSL_CTX *ctx, const char *str);
int SSL_CTX_set_cipher_list(SSL_CTX *ctx, const char *str);
int SSL_set_alpn_protos(SSL *ssl, const uint8_t *protos, unsigned protos_len);

int SSL_write(SSL *ssl, const void *buf, int num);
int SSL_read(SSL *ssl, void *buf, int num);

int SSL_do_handshake(SSL *ssl);
int SSL_get_error(const SSL *ssl, int ret_code);

// BIO = basic input output
// include/openssl/bio.h
BIO *BIO_new(const BIO_METHOD *method);
BIO *BIO_new_socket(int fd, int close_flag);
BIO *BIO_new_connect(const char *host_and_optional_port);

int BIO_write_all(BIO *bio, const void *data, size_t len);
int BIO_read(BIO *bio, void *data, int len);
""")

libcrypto, libssl = bssl_build.load_bssl_libraries(ffi)

ctx = libssl.SSL_CTX_new(libssl.TLS_method())
print("SSL context created:", ctx)
