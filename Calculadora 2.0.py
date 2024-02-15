#!/usr/bin/env python
# coding: utf-8

# In[163]:


ascii = r"""

   ____     _     _      ____  _   _  _         _     ____    ___   ____      _         ____  ___  __  __  ____   _      _____  ____  
  / ___|   / \   | |    / ___|| | | || |       / \   |  _ \  / _ \ |  _ \    / \       / ___||_ _||  \/  ||  _ \ | |    | ____|/ ___| 
 | |      / _ \  | |   | |    | | | || |      / _ \  | | | || | | || |_) |  / _ \      \___ \ | | | |\/| || |_) || |    |  _|  \___ \ 
 | |___  / ___ \ | |___| |___ | |_| || |___  / ___ \ | |_| || |_| ||  _ <  / ___ \      ___) || | | |  | ||  __/ | |___ | |___  ___) |
  \____|/_/   \_\|_____|\____| \___/ |_____|/_/   \_\|____/  \___/ |_| \_\/_/   \_\    |____/|___||_|  |_||_|    |_____||_____||____/ 
                                                                                                                                      
"""


# In[164]:


operação = ['A. Soma','B. Subtração','C. Multiplicação','D. Divisão','E. Exponenciação','F. Raíz Quadrada']


# In[169]:


def Soma(X,Y):
    return X+Y
def Subtração(X,Y):
    return X-Y
def Multiplicação(X,Y):
    return X*Y
def Divisão(X,Y):
    return X/Y
import math
raiz = lambda X: math.sqrt(X)
Exponenciação = lambda X,Y: X**Y
import time


# In[173]:


def conta():
    print(ascii)
    print('Bem-vindo a calculadora simples! Essa calculadora vai realizar operações básicas entre dois números!')
    while True:
        for o in operação:
            print(o)
        I = (input('Por favor, faça sua escolha digitando a letra relacionada à operação: ').upper())
        if I == 'A':
            print('Você escolheu SOMA, agora:')
            X = eval(input('Escolha seu primeiro número '))
            Y = eval(input('Escolha seu segundo número '))
            print(X,'+', Y, '=', Soma(X, Y))        
        elif I == 'B':
            print('Você escolheu SUBTRAÇÃO, agora:')
            X = eval(input('Escolha seu primeiro número '))
            Y = eval(input('Escolha seu segundo número '))
            print(X, '-', Y, '=', Subtração(X, Y))
        elif I == 'C':
            print('Você escolheu MULTIPLICAÇÃO, agora:')
            X = eval(input('Escolha seu primeiro número '))
            Y = eval(input('Escolha seu segundo número '))
            print(X, '*', Y, '=', Multiplicação(X, Y))
        elif I == 'D':
            print('Você escolheu DIVISÃO, agora:')
            X = eval(input('Escolha seu primeiro número '))
            Y = eval(input('Escolha seu segundo número '))
            if X == 0 or Y == 0:
                print('Não é possível dividir por zero')
            else:
                print(X,'/', Y, '=', Divisão(X, Y))
        elif I == 'E':
            print('Você escolheu EXPONENCIAÇÃO, agora:')
            X = eval(input('Escolha seu primeiro número '))
            Y = eval(input('Escolha seu segundo número '))
            
            print(X, '**', Y, '=', Exponenciação(X, Y))
        elif I == 'F':
            print('Você escolheu RAÍZ QUADRADA, agora:')
            X = eval(input('Escolha seu número '))
            
            print('√',X,'=', raiz(X))
        else:
            print('Por favor, escolha uma operação válida dentre as opções apresentadas acima')
        P = input('Deseja fazer mais uma conta? (sim/não): ')
        if P.lower() != 'sim' and P.lower() != 's':
            print('Obrigado por usar a calculadora simples, até a próxima!')
            time.sleep(3)
            break


# In[172]:


conta()


# In[ ]:




