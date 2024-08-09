"""
Calculadora
Autor: João Pedro
Função: fazer calculos simples
"""

print('Calculadora')

sair = False

while sair == False:
    
    num1 = input('Digite o primeiro numero: ')
    num1 = int(num1)
    operador = input('Digite o operador: ')
    num2 = input('Digite o segundo numero: ')
    num2 = int(num2)

    # + soma
    if operador == '+':
        operacao = num1 + num2
    # - subtração
    if operador == '-':
        operacao = num1 - num2
    # * multiplicação
    if operador == '*':
        operacao = num1 * num2
    # / divisão
    if operador == '/':
        operacao = num1 / num2
        
    print("Resultado: ", operacao)
    
    teste = input('Deseja sair? [S/N]: ')
    if teste == 'S' or teste =='s':
        sair = True