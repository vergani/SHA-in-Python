import hashlib
# Coleta a string
str = "Geek forever"

# Codificando str usando encode() então envia para SHA256()
resultado = hashlib.sha256(str.encode())
# Imprimi o valor hexadecimal equivalente.
print("The hexadecimal equivalent of SHA256 is : ")
print(resultado.hexdigest())
print ("\r")

# Codificando str usando encode() então envia para SHA384()
resultado = hashlib.sha384(str.encode())
# Imprimi o valor hexadecimal equivalente.
print("Hexadecimal equivalente em SHA384 é: ")
print(resultado.hexdigest())
print ("\r")

# Codificando str usando encode() então envia para SHA224()
resultado = hashlib.sha224(str.encode())
# Imprimi o valor hexadecimal equivalente.
print("Hexadecimal equivalente em SHA224 é: ")
print(resultado.hexdigest())
print ("\r")

# Codificando str usando encode() então envia para SHA512()
resultado = hashlib.sha512(str.encode())
# Imprimi o valor hexadecimal equivalente.
print("Hexadecimal equivalente em SHA512 é: ")
print(resultado.hexdigest())
print ("\r")

# Codificando str usando encode() então envia para SHA1()
resultado = hashlib.sha1(str.encode())
# Imprimi o valor hexadecimal equivalente.
print("Hexadecimal equivalente em SHA1 é: ")
print(resultado.hexdigest())
print ("\r")

# Codificando str usando encode() então envia para MD5()
resultado = hashlib.md5(str.encode())
# Imprimi o valor hexadecimal equivalente.
print("Hexadecimal equivalente em MD5 é: ")
print(resultado.hexdigest())
