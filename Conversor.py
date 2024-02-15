#!/usr/bin/env python
# coding: utf-8

# In[378]:


Celcius_Fahrenheit = lambda i: round((i*(9/5)+32))
Mt_Feet = lambda i: i/0.3048
Mil_Oz = lambda i: round(i/29.5735)
Cm_inch = lambda i: i/2.54
Lit_Oz = lambda i: round((i/29.5735)*1000)
Mt_Yard = lambda i: round(i/0.9144)
Km_Miles = lambda i: i/1.60934
                        


# In[379]:


Fahrenheit_Celcius = lambda i: round((i-32)*(5/9))
Feet_Mt = lambda i: i*0.3048
Oz_Mil = lambda i: round(i*29.5735)
Inch_cm = lambda i: i*2.54
Oz_Lit = lambda i: round((i*29.5735)/1000)
Yard_Mt = lambda i: round(i*0.9144)
Miles_km = lambda i: i*1.60934


# In[380]:


A=Celcius_Fahrenheit
B=Mt_Feet
C=Mil_Oz
D=Cm_inch
E=Lit_Oz
F=Mt_Yard
G=Km_Miles


# In[381]:


H = Fahrenheit_Celcius
I = Feet_Mt
J =Oz_Mil 
K = Inch_cm
L =Oz_Lit 
M = Yard_Mt 
N = Miles_km 


# In[382]:


conversao_imperial = ['A.Fahrenheit para Celsius', 'B.Pés para metros', 'C.Onças para milimetros', 'D.polegadas para centimentos', 'E.onças para litros', 'F.jardas para metros', 'G.milhas para kilometros']


# In[383]:


conversao_metrica = ['A. Celsius para Fahrenheit', 'B.Metros para pés ', 'C. Milimetros para onças', 'D. Centímetros para polegadas', 'E.Litros para onças', 'F. Metros para jardas', 'G. Kilometros para milhas']


# In[384]:


import time


# In[385]:


print('Bem-vindo a este conversor de valores.')


# In[397]:


def conversor():
    while True:
        print('Você quer converter um valor em métrico para imperial? Digite: "M" para métrico ou se for para imperial para métrico, digite: "I"')


        
        
    
        x = input().upper()
        if x == ('M'):
            print('''
            Escolha o tipo de conversão digitando sua letra correspondente:
            ''')
        
            for tipo_metrico in conversao_metrica:
                print(tipo_metrico)
            
            x2 = input().upper()
       
            if x2 == 'A':
                 print('Muito bem, escolha o valor a ser convertido')
                 i = float(input())
                 print('%i °C são' %i ,round(A(i)),'°F' )
            
            elif x2 == 'B':
                print('Muito bem, escolha o valor a ser convertido')
                i = float(input())
                print('%i metros equivale à' %i ,(B(i)),'pés' )

            elif x2 == 'C':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i ml equivale à' %i ,round(C(i)),'onças' )

            elif x2 == 'D':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i cm equivale à' %i ,(D(i)),'polegadas' )

            elif x2 == 'E':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i l equivale à' %i ,round(D(i)),'onças' )

            elif x2 == 'F':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i metros equivale à' %i ,(F(i)),'jardas' )

            elif x2 == 'G':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i km equivale à' %i ,(D(i)),'milhas' )

        if x == ('I'):
            print('''
            Escolha o tipo de conversão digitando sua letra correspondente:
            ''')

            for tipo_imperial in conversao_imperial:
                print(tipo_imperial)

            y = input().upper()

            if y == 'A':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i °F são' %i ,round(H(i)),'°C' )
            elif y == 'B':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i pés são' %i ,(I(i)),'em metros' )
            elif y == 'C':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i onças são' %i ,round(J(i)),'ml' )
            elif y == 'D':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i polegadas são' %i ,round(K(i)),'cm' )
            elif y == 'E':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i onças são' %i ,round(L(i)),'l' )
            elif y == 'F':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i jardas são' %i ,(M(i)),'mt' )
            elif y == 'G':
                print('Muito bem, escolha o valor a ser convertido')
                i = eval(input())
                print('%i milhas são' %i ,(N(i)),'km' )

        else:
            print('Gostaria de realizar outra converão? (s/n)')
            z =input().lower()
            if z == ('s'):
                conversor()
            if z =='n':
                print('byebye')
                time.sleep(2)
                break
                


    
            
            




        
        
            
            
        
            
        
    
        
        

    


    


# In[311]:


conversor()

