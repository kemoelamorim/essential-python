idade = int(input("Digite sua idade: "))
print(f'Sua idade é {idade}')
qtd_pessoas = int(input("Quantas pessoas: "))

acompanhado = qtd_pessoas >= 2

# Condicional
if(idade >= 18):
    print('Maior de idade')
    print('Entrada permitida')
elif(idade < 18 and acompanhado):
    print('É menor de idade, mais está acompanhado')
    print('Entrada permitida')
else:
    print('Menor de idade')
    volte = 18 - idade
    print(f'Volte daqui a {volte} anos')

