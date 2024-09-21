
from Crypto.Cipher import AES
import base64

clave = "CLAVE RE SECRETA"


mensaje_cifrado = """dV5t6M4m2AcjYWsxC9iO+YXlc0r0ClfwyTGtpuWdPh9fvH+8cejJWOHYq1qH7qA+Kj7Lci133Awj3rnoq42p532+fvbN64oZ8R/TlMkhw47nmIM5gPN+rt45985
jeiIDbdpCu1ig09Rzepl4/kawM1AzFtoMzTvadmx11qSFp+UD81yiRz6HjaFLIIIIQnbzFrmcOIOGEQ6LBEYz2cTW6JPBs7MHpqDrcrzZoLcb7Ah2jQSIId+YZ90JmRt83yTe66a60kqL5SoW7/
463Suyyp9xDhrgFu6YS3ScNDgOamADIcKmLUTxrvYooZIjL7s+thek3aBPrv/yB84YNUhX7MOxjiTiP02nBJ1E1dOA0ew75BeARB4cHKVfLMnPMkjSYyiQ2eTWqYd4cZ+14Z9joNVA1Uei8Pg4KITPfJYy3Mc="""


mensaje_cifrado = base64.b64decode(mensaje_cifrado)

aes = AES.new(clave.encode('utf-8'), AES.MODE_ECB)


mensaje_descifrado = aes.decrypt(mensaje_cifrado)


mensaje_descifrado = mensaje_descifrado.rstrip(b"\x10")

print(mensaje_descifrado)
