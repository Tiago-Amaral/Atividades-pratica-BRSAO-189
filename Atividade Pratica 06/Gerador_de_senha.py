import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Informe a quantidade de caracteres para a senha: "))
senha = gerar_senha(tamanho)
print("Senha gerada:", senha)
