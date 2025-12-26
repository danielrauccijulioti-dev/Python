
# os tipos primitivos que aprendi até agora foram = int:usado para calcular numeros inteiros,float: que são basicamente numero "quebrados", bool: que dependendo do seu comando como um "isnumber" ele diz ser verdadeiro ou falso e o str: que seria usado para escrever frases dentro do comando. colocarei um exemplo de cada...

#int:
n1= int(input('digite um numero'))
n2= int(input('digite outro numero'))
s = n1+n2
print('a soma entre', n1,n2,'vale',s)

#float:
preco = 10.50
desconto = 2.25

total = preco - desconto
print(total)

#bool:
n = bool=(input('digite alguma coisa:'))
print(n.isalpha())

#str:
n = str=(input('digite seu nome:'))
nome= str
print('prazer em conhece-lo',str,'!')
