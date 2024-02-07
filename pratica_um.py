# EXERCICIO 01

# print('Abaixo temos a atividade 1')
# print('Python na Escola de Programação da Alura.\n')

# var_nome = input('Informe o seu nome: ')
# var_idade= input('Informe a sua idade: ')
# print(f'O seu nome é {var_nome} e você tem {var_idade} anos!\n')

# print('A\n L\n U\n R\n A\n')

# print('Outra atividade,vamos descobrir o valor de pi\n')
# var_pi = input('Informe o valor de pi, iremos arredondar: \n')
# print('O valor arredondado de pi é: {:.2f}'.format(var_pi))


# ------------------------------------------------

# EXERCICIO 02 - 

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# var_numero = float (input('Insira um número: '))
# número = var_numero % 2

# if número == 0:
#     print('O número inserido é PAR')
# else:
#     print('O número inserido é IMPAR')


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

# var_idade = int (input('Qual é a sua idade? '))

# if var_idade >= 0 and var_idade <= 12:
#     print('Criança')
# elif var_idade >= 13 and var_idade <=18:
#     print('Adolescente')
# else:
#     print('Adulto')


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
# usuario_correto = 'soueu'
# senha_correta = 'abcd123'

# usuario =  input('Digite o nome de usuário: \n')
# senha =  input('Digite a senha: \n')

# if usuario == usuario_correto and senha == senha_correta:
#     print('Login bem sucedido!')
# else:
#     print('Usuário ou senha incorreta!')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# var_x = int (input  ('Informe a coordenada de X: '))
# var_y = int (input  ('Informe a coordenada de Y: '))

# if var_x > 0 and var_y > 0:
#     print('Primeiro Quadrante')
# elif var_x < 0 and var_y > 0:
#     print('Segundo Quadrante')
# elif var_x < 0 and var_x < 0:
#     print('Terceiro Quadrante')
# elif var_x  > 0 and var_y < 0:
#     print('Quarto Quadrante')
# else:
#     print('O ponto está localizado no eixo ou origem')


# ---------------------------------------

# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# var_lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
# var_lista_de_nomes = [Marcos, Gabriel, Nicolas, João]
# var_anos= [1998,2024]



# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# alunos = ['Marcos', 'Gabrie', 'João', 'Matheus', 'Pedro', 'Henrique']
# for aluno in alunos:
#     print(f'O aluno: {aluno}, está na lista!')


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# soma_impares = 0
# for i in range(1, 11, 2):
#     soma_impares += i
# print(soma_impares)


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
# for i in range(10, 0, -1):
#     print(i)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# numero_tabuada = int(input("Digite um número para a tabuada: "))
# for i in range(1, 11):
#     resultado = numero_tabuada * i
#     print(f"{numero_tabuada} x {i} = {resultado}")


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
# lista_numeros = [10, 5, 8, 3, 7]
# soma = 0

# try:
#     for numero in lista_numeros:
#         soma += numero
#     print(f"Soma dos elementos: {soma}")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
# lista_valores = [15, 20, 25, 30]
# soma_valores = 0

# try:
#     for valor in lista_valores:
#         soma_valores += valor
#     media = soma_valores / len(lista_valores)
#     print(f"Média dos valores: {media}")
# except ZeroDivisionError:
#     print("A lista está vazia, não é possível calcular a média.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

#---------------------------------------------------------------------------------


# Exercícios
# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:
pessoa = [{'nome': 'Marcos', 'idade':'25', 'cidade':'Brasília'}]
print(pessoa)

pessoa['idade'] = 26



# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.