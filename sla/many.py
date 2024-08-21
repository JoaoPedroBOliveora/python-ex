#LITTLE E QUIABO


#n1 = int(input('digite um numero:'))
#print(f'a tabuada de {n1} é: ')

#for i in range(1,11):
    #print(f'{n1} x {i} = {n1*i}')

#n1=int(input('digite um numero:'))
#a=n1-1
#s=n1+1
#print(f'o antecessor de ({n1}) é: {a}\n7e seu sucessor é: {s}')
 

#n1=int(input('digite o numero desejado:'))
#if n1 ==0:
    #binario='0'
#else:
    #binario=''
    #while n1 >0:
        #resto= n1%2
        #binario=str(resto) + binario
        #n1=n1//2
#print(f'o numero em binario é :{binario}')



#numero=int(input('digite o numero desejado:'))
#if (numero %2 == 0):
    #print('este numero é par')
#else:
    #print('este numero é impar')

#n1=int(input('digite o primeiro numero:'))
#n2=int(input("digite o segundo numero:"))
#if n1<n2:
    #print('a ordem crescente é:', n1,' ', n2)
#else:
    #print('a ordem crescente é:', n2,' ', n1)
#if n1>n2:
    #print('a ordem decrescente é:', n1,' ', n2)
#else:
 #   print('a ordem devrescente é:', n2,' ', n1)


#n1=int(input('digite o primeiro numero:'))
#N2=int(input("digite o segundo numero:"))
#if n1<n2:
 #  print(n1,'é numero é menor que esse', n2)
#else:
 #   print(n2, ' é maior que esse', n1)


n1=int(input('digite o primeiro numero:'))
n2=int(input("digite o segundo numero:"))
n3=int(input('digite o terceiro numero:'))

if n1<n2 and n1<n3:
    menor = n1
elif n2<n1 and n2<n3:
    menor = n2
else: n3<n1 and n3<n2
menor = n3

print(f'o menor numero é {menor}')
