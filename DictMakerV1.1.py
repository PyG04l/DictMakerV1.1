from itertools import combinations
import pyperclip
from random import randint, choice
import sys
import os

def options(op):
	operSist = sys.platform
	if operSist == 'win32':
		if op == 0:
			return os.system('color 0a')
		elif op == 1:
			return os.system('cls')
		elif op == 2:
			return os.system('pause>nul')
		elif op == 3:
			return os.system('chdir')
	elif operSist == 'linux' or operSist == 'linux2':
		if op == 0:
			pass
		if op == 1:
			return os.system('clear')
		elif op == 2:
			return os.system('read -p ""')
		elif op == 3:
			return os.system('pwd')
	else:
		return '¡No se reconoce el sistema operativo!'
		exit()

def gen_pass():
	options(1)
	se = set()
	print ("\n\tAquí puede generar una contraseña aleatoria introduciendo una longitud")
	n1 = int(input ("\t¿Cuantos caracteres desea que tenga la contraseña?: "))
	while len(se) < n1:
		se.add(choice([str(chr(randint(65,90))),str(chr(randint(97,122))),str(chr(36)),str(chr(45)),str(chr(46)),str(chr(95)),str(randint(0, 9))]))
	output_string = ''.join(list(se))
	print ('\n' + output_string)
	print ('')
	print ('A. Atras | R. ReRoll | C. Copy to clipboard y salir | 0. Salir')
	op1 = input ("\t\tElija opción: ")
	if (op1 == 'A') or (op1 == 'a'):
		prinMen()
	elif (op1 == 'R') or (op1 == 'r'):
		gen_pass()
	elif (op1 == 'C') or (op1 == 'c'):
		pyperclip.copy(output_string)
	elif op1 == '0':
		bye()
	else:
		err()

def perm1(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		l = []
		for i in range(len(lst)):
			x = lst[i]
			xs = lst[:i] + lst[i+1:]
			for p in perm1(xs):
				l.append([x] + p)
		return l

def to_str(lis):
	str1=''
	for i in lis:
		str1+=i
	print (str1)
	return str1

def err():
	options(1)
	os.system('color 7c')
	print('\n\tError: Opción incorrecta')
	print ()
	options(2)
	prinMen()

def bye():
	options(1)
	exit()


def prinMen():
	options(0)
	options(1)
	print ("\n\t1. Diccionario en Bloque (todas las opciones para la cadena introducida)")
	print ("\t2. Diccionario en Rango (combinaciones aleatorias con rango de longitud elegido)")
	print ("\t3. Generar contraseña")
	print ("\t0. Exit\n")
	op = input ("\t\tElija opción: ")
	if op == '1':
		options(1)
		lst = list(input ("\n\tEscriba a continuación la cadena de caracteres: " + '\n\n\t\t'))
		data2=[]
		print ('El diccionario será creado en: ' + '\n')
		options(3)
		print()
		options(2)
		for p in perm1(lst):
			data2=to_str(''.join(map(str, p)))
			with open('myDict.txt', 'a') as f:
				f.write(data2 + '\n')
		f.close()
		
	elif op == '2':
		options(1)
		data3 = list(input ("\n\tEscriba a continuación la cadena de caracteres: " + '\n\n\t\t'))
		print ("\n\tAhora digite dos números para delimitar el rango")
		n1 = int(input ("\t\tnum1: "))
		n2 = int(input ("\t\tnum2: "))
		data4 = []
		for r in range(n1, n2+1):
			for i in data3:
				iterList = (list(combinations(data3, r)))
				for p in iterList:
					data4 = to_str(''.join(map(str, p)))
					with open('myDict2.txt', 'a') as f:
						f.write(data4 + '\n')
		f.close()
	elif op == '3':
		gen_pass()
	elif op == '0':
		bye()
	else:
		err()


prinMen()
