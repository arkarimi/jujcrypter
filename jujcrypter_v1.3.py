import textwrap
import os
import time
import random
import string
# random string for more heavy encryption ! in the new release: v_1.3
letters = string.punctuation
ran = ''.join(random.choice(letters) for i in range(3))
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
		'a': 'juj' + ran,
		'b': 'lul' + ran,
		'c': 'bub' + ran,
		'd': 'zuz' + ran,
		'e': 'sus' + ran,
		'f': 'vuv' + ran,
		'g': 'nun' + ran,
		'h': 'egh' + ran,
		'i': 'lal' + ran,
		'j': 'jaj' + ran,
		'k': 'bob' + ran,
		'l': 'deh' + ran,
		'm': 'juf' + ran,
		'n': 'you' + ran,
		'o': 'pas' + ran,
		'p': 'heh' + ran,
		'q': 'pop' + ran,
		'r': 'wew' + ran,
		's': 'viv' + ran,
		't': 'jij' + ran,
		'u': 'bib' + ran,
		'v': 'tiz' + ran,
		'w': 'miz' + ran,
		'x': 'viz' + ran,
		'y': 'pis' + ran,
		'z': 'lil' + ran,
		' ': 'uiu' + ran,
		'.': 'fzp' + ran,
		'!': 'ogf' + ran,
		':': '092' + ran,
		')': '121' + ran,
		'|': '874' + ran,
		',': '987' + ran,
		'?': '461' + ran,
		'=': 'e97' + ran,
		'+': 'p65' + ran,
		'-': 'dy7' + ran,
		'0': 'olf' + ran,
		'1': 'ra5' + ran,
		'2': 'er4' + ran,
		'3': 'lk1' + ran,
		'4': '2lo' + ran,
		'5': '90i' + ran,
		'6': 'ez3' + ran,
		'7': 'l1o' + ran,
		'8': 'ox1' + ran,
		'9': 'lo1' + ran,
		'#': 'zrc' + ran,
		'@': 'por' + ran,
		'$': 'fgr' + ran,
		'%': 'wty' + ran,
		'^': 'kjh' + ran,
		'&': 'zkl' + ran,
		'*': 'dfr' + ran,
		'(': 'kqo' + ran,
		'_': 'suh' + ran,
		'/': 'dft' + ran,
		'"': 'adm' + ran,
		"'": 'vub' + ran,
		';': 'ssy' + ran,
		'}': 'fer' + ran,
		'{': 'SUS' + ran,
		'[': 'fwe' + ran,
		']': 'sdl' + ran,
        'ا': 'kjd' + ran,
        'ا': 'fd1' + ran,
        'ب': 'lk5' + ran,
        'پ': 'kj8' + ran,
        'ت': 'f5j' + ran,
        'ث': 'bv9' + ran,
        'ج': 'lkq' + ran,
        'چ': 'kuz' + ran,
        'ح': 'mn0' + ran,
        'خ': 'kvm' + ran,
        'د': 'l0w' + ran,
        'ذ': 'j@3' + ran,
        'ر': '%hj' + ran,
        'ز': 'djf' + ran,
        'ژ': 'ds4' + ran,
        'س': 'fd4' + ran,
        'ش': 'fj#' + ran,
        'ص': '*$f' + ran,
        'ض': 'P!0' + ran,
        'ط': 'b#2' + ran,
        'ظ': 'fd*' + ran,
        'ع': 'ps4' + ran,
        'غ': 'tju' + ran,
        'ف': 'y#s' + ran,
        'ق': 'j6j' + ran,
        'ک': 't&3' + ran,
        'گ': 'r3a' + ran,
        'ل': 'cr#' + ran,
        'م': 'lk^' + ran,
        'ن': 'ku4' + ran,
        'و': '!lf' + ran,
        'ه': 'h43' + ran,
        'ی': '#f#' + ran
        
		}

		FUN = input('Enter your FUN sentence : ')
		jujlist = []
		majid = ''
		for lol in FUN:
			majid += alphabet[lol]
		print("Encrypted message:",majid)
		print("Random encryiption key:",ran)
		time.sleep(12)
		main_menu()
	except KeyError:
		Error1()
# Decrypter
def dec():
	entry = input('Enter your FUN sentence: ')
	ran_num_inp = input("Random encryiption key: ")
	alphabet = {
		'juj' + ran_num_inp: 'a',
		'lul' + ran_num_inp: 'b',
		'bub' + ran_num_inp: 'c',
		'zuz' + ran_num_inp: 'd',
		'sus' + ran_num_inp: 'e',
		'vuv' + ran_num_inp: 'f',
		'nun' + ran_num_inp: 'g',
		'egh' + ran_num_inp: 'h',
		'lal' + ran_num_inp: 'i',
		'jaj' + ran_num_inp: 'j',
		'bob' + ran_num_inp: 'k',
		'deh' + ran_num_inp: 'l',
		'juf' + ran_num_inp: 'm',
		'you' + ran_num_inp: 'n',
		'pas' + ran_num_inp: 'o',
		'heh' + ran_num_inp: 'p',
		'pop' + ran_num_inp: 'q',
		'wew' + ran_num_inp: 'r',
		'viv' + ran_num_inp: 's',
		'jij' + ran_num_inp: 't',
		'bib' + ran_num_inp: 'u',
		'tiz' + ran_num_inp: 'v',
		'miz' + ran_num_inp: 'w',
		'viz' + ran_num_inp: 'x',
		'pis' + ran_num_inp: 'y',
		'lil' + ran_num_inp: 'z',
		'uiu' + ran_num_inp: ' ',
		'fzp' + ran_num_inp: '.',
		'ofg' + ran_num_inp: '!',
		'092' + ran_num_inp: ':',
		'121' + ran_num_inp: ')',
		'874' + ran_num_inp: '|',
		'987' + ran_num_inp: ',',
		'461' + ran_num_inp: '?',
		'e97' + ran_num_inp: '=',
		'p65' + ran_num_inp: '+',
		'dy7' + ran_num_inp: '-',
		'olf' + ran_num_inp: '0',
		'ra5' + ran_num_inp: '1',
		'er4' + ran_num_inp: '2',
		'lk1' + ran_num_inp: '3',
		'2lo' + ran_num_inp: '4',
		'90i' + ran_num_inp: '5',
		'ez3' + ran_num_inp: '6',
		'l1o' + ran_num_inp: '7',
		'ox1' + ran_num_inp: '8',
		'lo1' + ran_num_inp: '9',
		'zrc' + ran_num_inp: '#',
		'por' + ran_num_inp: '@',
		'fgr' + ran_num_inp: '$',
		'wty' + ran_num_inp: '%',
		'kjh' + ran_num_inp: '^',
		'zkl' + ran_num_inp: '&',
		'dfr' + ran_num_inp: '*',
		'kqo' + ran_num_inp: '(',
		'suh' + ran_num_inp: '_',
		'dft' + ran_num_inp: '/',
		'adm' + ran_num_inp: '"',
		'vub' + ran_num_inp: "'",
		'ssy' + ran_num_inp: ';',
		'fer' + ran_num_inp: '}',
		'SUS' + ran_num_inp: '{',
		'fwe' + ran_num_inp: '[',
		'sdl' + ran_num_inp: ']',
        'fd1' + ran_num_inp: 'ا',
        'lk5' + ran_num_inp: 'ب',
        'kj8' + ran_num_inp: 'پ',
        'f5j' + ran_num_inp: 'ت',
        'bv9' + ran_num_inp: 'ث',
        'lkq' + ran_num_inp: 'ج',
        'kuz' + ran_num_inp: 'چ',
        'mn0' + ran_num_inp: 'ح',
        'kvm' + ran_num_inp: 'خ',
        'l0w' + ran_num_inp: 'د',
        'j@3' + ran_num_inp: 'ذ',
        '%hj' + ran_num_inp: 'ر',
        'djf' + ran_num_inp: 'ز',
        'ds4' + ran_num_inp: 'ژ',
        'fd4' + ran_num_inp: 'س',
        'fj#' + ran_num_inp: 'ش',
        '*$f' + ran_num_inp: 'ص',
        'P!0' + ran_num_inp: 'ض',
        'b#2' + ran_num_inp: 'ط',
        'fd*' + ran_num_inp: 'ظ',
        'ps4' + ran_num_inp: 'ع',
        'tju' + ran_num_inp: 'غ',
        'y#s' + ran_num_inp: 'ف',
        'j6j' + ran_num_inp: 'ق',
        't&3' + ran_num_inp: 'ک',
        'r3a' + ran_num_inp: 'گ',
        'cr#' + ran_num_inp: 'ل',
        'lk^' + ran_num_inp: 'م',
        'ku4' + ran_num_inp: 'ن',
        '!lf' + ran_num_inp: 'و',
        'h43' + ran_num_inp: 'ه',
        '#f#' + ran_num_inp: 'ی'
		}


	listentry = textwrap.wrap(entry, 6)

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
			time.sleep(4)
			main_menu()
	except (ValueError,TypeError):
		Error2()
main_menu()
