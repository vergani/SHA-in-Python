# SHA-in-python
## SHA ( Secure Hash Algorithms )

Os algoritmos disponíveis são: {'sha256', 'sha384', 'sha224', 'sha512', 'sha1', 'md5'}

Funções:
    encode() : convert a string desejada em bytes aceitáveis pela função hash;
    hexdigest() : retorna o código encodado em formato hexadecimal legível.
    
![sha](https://user-images.githubusercontent.com/35334365/165557271-7d53963d-1b61-4729-b64f-1bef2318568a.png)


    
Explicando: o código ``hash_SHA.py`` acima converte a string em um byte equivalente usando encode() para que ele seja aceitável pela função hash. A função hash do SHA codifica este valor usando função hexdigest(). Em seguida, o valor hexadecimal equivalente é impresso em tela.
