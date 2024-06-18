# Apresentação e solicitação dos dados
print('Olá, seja bem-vindo(a) ao calculador de imc')
peso = float(input('Digite o seu peso(Kg): '))
altura = float(input('Digite a sua altura(m): '))
imc = peso / (altura * altura)
print('O seu imc é:', imc)
# Verificação dos dados
if 18.5 > imc:
    print('Você está abaixo do peso')
else:
    if 18.5 <= imc < 24.9:
        print('Você está com o peso normal')
    else:
        if 25 <= imc < 29.9:
            print('Você está com excesso de peso')
        else:
            if 30 <= imc < 34.9:
                print('Você está obeso')
            else:
                if 35 < imc:
                    print('Você apresenta obesidade extrema')

print('Espero ter ajudado!')
input('')
