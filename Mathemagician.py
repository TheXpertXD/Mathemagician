# Defining Functions with Mathematics

import winsound
import time
import sys
print("Would you like music? Y/N... WARNING: Loud")
Music = raw_input()
if Music == "Y" or Music == "y":
    winsound.PlaySound("smw.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
else:
    winsound.PlaySound(None, winsound.SND_ASYNC)

def add():
    print'Alrighty, Adding it is.'
    print'Firstly, how many integers are you adding together? 2 or 3?'
    integ=input()
    if integ==2:
        print'Ok, so what is the first number in your equation?'
        coea=input()
        print'And the next number?'
        coeas=input()
        print'Lets add them up!'
        print'The final solution would be...  '+str(float(coea) + float(coeas))+'.'
        end=input()
    if integ==3:
        print'Ok, so what is the first number in your equation?'
        coea=input()
        print'And the next number?'
        coeas=input()
        print'Last one?'
        coeat=input()
        print'Lets add them up!'
        print'The final solution would be...  '+str(float(coea) + float(coeas) + float(coeat))+'.'
        end=input()

def sub():
    print'So you wanna subtract some numbers, eh...'
    print'How many numbers do you want in the problem? 2 or 3?'
    integs=input()
    if integs==2:
        print'Right, so what is the first number in your equation?'
        coes=input()
        print'And the next number?'
        coess=input()
        print'Lets see what we get!'
        print'The final solution would be...  '+str(float(coes) - float(coess))+'.'
        end=input()
    if integs==3:
        print'Right, so what is the first number in your equation?'
        coes=input()
        print'And the next number?'
        coess=input()
        print'Last one?'
        coest=input()
        print'Lets see what we get!'
        print'The final solution would be...  '+str(float(coes) - float(coess) - float(coest))+'.'
        end=input()

def mult():
    print'My favorite!'
    print' What will be in the problem? 2 or 3 numbers?'
    integm=input()
    if integm==2:
        print'Cool cool, so whats the first number in your equation?'
        coem=input()
        print'And the next number?'
        coems=input()
        print'Lets see what we get!'
        print'The final solution would be...  '+str(float(coem) * float(coems))+'.'
        end=input()
    if integm==3:
        print'Right, so what is the first number in your equation?'
        coem=input()
        print'And the next number?'
        coems=input()
        print'Last one?'
        coemt=input()
        print'Lets see what we get!'
        print'The final solution would be...  '+str(float(coem) * float(coems) * float(coemt))+'.'
        end=input()

def div():
    print'Lets get to splitting some numbers!'
    print'How many numbers will be in the problem?'
    integd=input()
    if integd==2:
        print'Cool cool, so whats the numerator?'
        coed=input()
        print'And the denominator?'
        coeds=input()
        print'Lets see what we get!'
        print'The final solution would be...  '+str(float(coed) / float(coeds))+'.'
        end=input()
    if integd==3:
        print'Right, so what is the first number in your equation?'
        coed=input()
        print'And the next number?'
        coeds=input()
        print'Last one?'
        coedt=input()
        print'Lets see what we get!'
        print'The final solution would be...  '+str(float(coed) / float(coeds) / float(coedt))+'.'
        end=input()
        
print('''
      Hello! Welcome to the Mathemagician! Here you can get help
      with any of your basic math functions, including Addition,
      Subtraction, Multiplication, or Division.
      ''')
print('What do you need help with today?')
print('''
       1. Addition
       2. Subtraction
       3. Multiplication
       4. Division
       ''')

model=input()
if model==1:
    add()
if model==2:
    sub()
if model==3:
    mult()
if model==4:
    div()

