import textwrap
import os
import time
# clear screen
def cls():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
# Error1
def Error1():
	print("KEY ERROR: At least one character can not be used(For example: \ or capital characters )! Wait for updates in the future...")
	time.sleep(7)
	main_menu()
# Error2
def Error2():
	print("Wrong input: Please enter 1 or 2 or 3 | Not a string !")
	time.sleep(5)
	main_menu()
# About
def about():
	cls()
	print("A message encrypter named jujcrypt that is programmed with python | Programmers: @arkarimi and @SepyMovasat")
	time.sleep(6)
	main_menu()
# Encrypter
def enc():
	try:
		alphabet = {
		'a': 'juj',
		'b': 'lul',
		'c': 'bub',
		'd': 'zuz',
		'e': 'sus',
		'f': 'vuv',
		'g': 'nun',
		'h': 'egh',
		'i': 'lal',
		'j': 'jaj',
		'k': 'bob',
		'l': 'deh',
		'm': 'juf',
		'n': 'you',
		'o': 'pas',
		'p': 'heh',
		'q': 'pop',
		'r': 'wew',
		's': 'viv',
		't': 'jij',
		'u': 'bib',
		'v': 'tiz',
		'w': 'miz',
		'x': 'viz',
		'y': 'pis',
		'z': 'lil',
		' ': 'uiu',
		'.': 'bob',
		'!': 'ogf',
		':': '092',
		')': '121',
		'|': '874',
		',': '987',
		'?': '461',
		'=': 'e97',
		'+': 'p65',
		'-': 'dy7',
		'0': 'olf',
		'1': 'ra5',
		'2': 'er4',
		'3': 'lk1',
		'4': '2lo',
		'5': '90i',
		'6': 'ez3',
		'7': 'l1o',
		'8': 'ox1',
		'9': 'lo1',
		'#': 'zrc',
		'@': 'por',
		'$': 'fgr',
		'%': 'wty',
		'^': 'kjh',
		'&': 'zkl',
		'*': 'dfr',
		'(': 'kqo',
		'_': 'suh',
		'/': 'dft',
		'"': 'adm',
		"'": 'vub',
		';': 'ssy',
		'}': 'fer',
		'{': 'SUS',
		'[': 'fwe',
		']': 'sdl'
		}

		FUN = input('Enter your FUN sentence : ')
		jujlist = []
		majid = ''
		for lol in FUN:
			majid += alphabet[lol]
		print("Encrypted message:",majid)
		time.sleep(8)
		main_menu()
	except KeyError:
		Error1()
# Decrypter
def dec():
	alphabet = {
		'juj': 'a',
		'lul': 'b',
		'bub': 'c',
		'zuz': 'd',
		'sus': 'e',
		'vuv': 'f',
		'nun': 'g',
		'egh': 'h',
		'lal': 'i',
		'jaj': 'j',
		'bob': 'k',
		'deh': 'l',
		'juf': 'm',
		'you': 'n',
		'pas': 'o',
		'heh': 'p',
		'pop': 'q',
		'wew': 'r',
		'viv': 's',
		'jij': 't',
		'bib': 'u',
		'tiz': 'v',
		'miz': 'w',
		'viz': 'x',
		'pis': 'y',
		'lil': 'z',
		'uiu': ' ',
		'bob': '.',
		'ofg': '!',
		'092': ':',
		'121': ')',
		'874': '|',
		'987': ',',
		'461': '?',
		'e97': '=',
		'p65': '+',
		'dy7': '-',
		'olf': '0',
		'ra5': '1',
		'er4': '2',
		'lk1': '3',
		'2lo': '4',
		'90i': '5',
		'ez3': '6',
		'l1o': '7',
		'ox1': '8',
		'lo1': '9',
		'zrc': '#',
		'por': '@',
		'fgr': '$',
		'wty': '%',
		'kjh': '^',
		'zkl': '&',
		'dfr': '*',
		'kqo': '(',
		'suh': '_',
		'dft': '/',
		'adm': '"',
		'vub': "'",
		'ssy': ';',
		'fer': '}',
		'SUS': '{',
		'fwe': '[',
		'sdl': ']'
		}



	entry = input('Enter your FUN sentence: ')
	listentry = textwrap.wrap(entry, 3)

	jujbet = ''


	for items in listentry:
		jujbet += alphabet[items]

	print("Decrypted message:",jujbet)
	time.sleep(8)
	main_menu()
# Main menu
def main_menu():
	try:
		cls()
		print("Welcome to Jujcrypter!")
		print("1: Encrypt message")
		print("2: Decrypt message")
		print("3: About")
		print("4: Exit")
		print("A program by @SepyMovasat and @arkarimi")
		main_inp = int(input("Which one ? [1,2,3,4] "))
		if main_inp == 1:
			enc()
		elif main_inp == 2:
			dec()
		elif main_inp == 3:
			about()
		elif main_inp == 4:
			time.sleep(1)
			exit()
		else:
			print("ERROR: Please choose from 1 or 2 or 3 or 4")
	except (ValueError,TypeError):
		Error2()
main_menu()
