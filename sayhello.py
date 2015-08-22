import os

if os.environ.get('CRYPTOGRAPHY_STATIC_OPENSSL'):
    os.system('figlet hello ' + os.environ['CRYPTOGRAPHY_STATIC_OPENSSL'])
