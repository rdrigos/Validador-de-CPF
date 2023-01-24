
import re
digitos_cpf = []


def verifica_digito_cpf(substr, multi):  # Função para a verificação dos digitos
    cpf_substring = cpf_str[0:substr]
    indice = 0
    multiplicacao = multi
    calculo = 0

    for i in cpf_substring:
        numero = int(cpf_substring[indice]) * multiplicacao
        indice += 1
        multiplicacao -= 1
        calculo += numero
    digito = (calculo * 10) % 11

    if digito > 9:
        digito = 0

    return digitos_cpf.append(str(digito))


while True:
    cpf_entrada = input('Digite um CPF para a Verificação:\n')  # Verifica se o CPF informado é sequencial
    cpf_str = str(cpf_entrada)
    cpf_enviado_usuario = re.sub(
        r'[^0-9]',
        '',
        cpf_str
    )

    entrada_e_sequencial = cpf_str == cpf_str[0] * len(cpf_str)

    if entrada_e_sequencial:
        print('Você enviou um CPF com números sequenciais.')
    else:
        try:
            verifica_digito_cpf(9, 10)
            verifica_digito_cpf(10, 11)

            str_digitos_cpf = ''.join(digitos_cpf)

            if cpf_str[9:] == str_digitos_cpf:
                print('O CPF informado é válido!')
            else:
                print('O CPF informado é inválido!')
        except ValueError:
            print('O CPF informado contem caracteres inválidos!')

        pesq_novamente = input('Testar outro CPF? [S]im | [N]ão\n').upper()

        if pesq_novamente == 'S':
            continue
        elif pesq_novamente == 'N':
            break
