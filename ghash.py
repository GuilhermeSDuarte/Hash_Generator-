import hashlib

string = input("Digite o texto a ser gerado a haash: ")

menu = int(input(''' Menu 
1- MD5
2- SHA1
3- SHA256
4- SHA512
Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("A hash da palavra digitada em MD5 é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("A hash da palavra digitada em SHA1 é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("A hash da palavra digitada em SHA256 é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("A hash da palavra digitada em SHA512 é: ", resultado.hexdigest())
else:
    print("Digitou algo invalido")

