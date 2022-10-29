import getpass
import random

#Usamos tuplas en lugar de listas
opciones = ('Piedra', 'Papel', 'Tijera')

def text():
    print(f'\nHas elegido: {opciones[usuario -1]}')
    print(f'El PC Ha elegido: {opciones[pc -1]}')

print(f'\nJuego de Piedra, Papel, Tijera')

usuario = int( input('Ingrese: \n1 para Piedra, \n2 para Papel, \n3 para Tijera => '))
pc = random.randint(1, 3)

if pc == usuario:
    text()
    print('Empate')
elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
    text()
    print('Has ganado')
elif usuario not in range (1, 3):
    text()
    print('Elegiste perder')
else:
    text()
    print('Has perdido')

getpass.getpass('press enter')
