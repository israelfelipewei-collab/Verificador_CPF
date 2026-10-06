import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto_1 = (soma_1 * 10) % 11
    digito_1 = 0 if resto_1 == 10 or resto_1 == 11 else resto_1

    soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto_2 = (soma_2 * 10) % 11
    digito_2 = 0 if resto_2 == 10 or resto_2 == 11 else resto_2

    return cpf[-2:] == f"{digito_1}{digito_2}"

print("=" * 35)
print("      VALIDADOR DE CPF INTERATIVO     ")
print("=" * 35)

entrada_usuario = input("Digite o CPF para validação: ")

if validar_cpf(entrada_usuario):
    print("\n🟢 Resultado: O CPF digitado é VÁLIDO!")
else:
    print("\n🔴 Resultado: O CPF digitado é INVÁLIDO.")
print("=" * 35)
