import requests

def meu_endereco(cep):
    url = f"http://viacep.com.br/ws/{cep}/json"
    retorno = requests.get(url)
    dici = retorno.json()
    logradouro = dici['logradouro']
    cidade = dici['localidade']
    print(f"{logradouro} - {cidade}")
    retorno.status_code


def validar_cep(cep):

    def validar_comprimento(cep):
        return len(cep) == 8

    def validar_digitos(cep):
        return cep.isdigit()

    def validar_cep_completo(cep):
        return validar_comprimento(cep) and validar_digitos(cep)

    cep = cep.replace('-', '').strip()

    validacoes = {
        'comprimento': validar_comprimento,
        'digitos': validar_digitos,
        'completo': validar_cep_completo,
    }

    resultado = {}

    for chave, funcao in validacoes.items():
        resultado[chave] = funcao(cep)


    if resultado['completo']:
        print("O CEP é válido e contém 8 dígitos.")
        return True
    elif not resultado['digitos']:
        print("O CEP contém caracteres inválidos (não numéricos).")
        return False
    elif not resultado['comprimento']:
        print("O CEP não contém exatamente 8 dígitos.")
        return False
    else:
        print("O CEP é inválido.")
        return False

cep = str(input("Digite o CEP: "))
resultado = validar_cep(cep)
if resultado:
    meu_endereco(cep)
