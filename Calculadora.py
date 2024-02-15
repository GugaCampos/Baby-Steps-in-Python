#!/usr/bin/env python
# coding: utf-8

# In[88]:


def conta():
    print('Bem-vindo')
    while True:

        for o in operação:
            print(o)

        I = input('Por favor, faça sua escolha: ')

        if I == 'A':
            print('Você escolheu SOMA, agora:')
            X = int(input('Escolha seu primeiro numero '))
            Y = int(input('Escolha seu segundo numero '))
            print('X + Y =', Soma(X, Y))
        elif I == 'B':
            print('Você escolheu SUBTRAÇÃO, agora:')
            X = int(input('Escolha seu primeiro numero '))
            Y = int(input('Escolha seu segundo numero '))
            print('X - Y =', Subtração(X, Y))
        elif I == 'C':
            print('Você escolheu MULTIPLICAÇÃO, agora:')
            X = int(input('Escolha seu primeiro numero '))
            Y = int(input('Escolha seu segundo numero '))
            print('X * Y =', Multiplicação(X, Y))
        elif I == 'D':
            print('Você escolheu DIVISÃO, agora:')
            X = int(input('Escolha seu primeiro numero '))
            Y = int(input('Escolha seu segundo numero '))
            print('X / Y =', Divisão(X, Y))
        else:
            print('Favor, escolha uma opção válida')

        P = input('Deseja fazer mais uma conta? (sim/não): ')
        if P.lower() != 'sim':
            break



# In[83]:


def Soma(X,Y):
    return X+Y
def Subtração(X,Y):
    return X-Y
def Multiplicação(X,Y):
    return X*Y
def Divisão(X,Y):
    return X/Y

operação = ['A. Soma','B. Subtração','C. Multiplicação','D. Divisão']


# In[86]:


conta()


# In[ ]:




