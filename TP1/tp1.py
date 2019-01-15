import string


def treat_word(input_string):
	#alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for letter in input_string:
		if letter not in string.letters:
		#if letter not in alphabet:
			#print letter, 'is not a letter'
			input_string=input_string.replace(letter,"")
		#elif letter not in alphabet:
		#	print letter, "is a letter"	
	return input_string		

def count_words_line_to_dictionary(f):
	for line in f:
		for word in line.split():
			word = treat_word(word)
			if word in d:
				d[word]=d[word]+1
			else:
				d[word]=1
	return d

def print_dictionary_alphabetical_by_key(d):
	for key, value in sorted(d.items()): # Note the () after items!
	    print key,":",  value

class Extended_word:
	def __init__(self, mot, forme, lemme):
	    self.mot = mot
	    self.forme = forme
	    self.lemme=lemme
	def display_Extended_word(self):
		print self.mot, self.forme, self.lemme

def text_to_list_Extended_word(f):
	l=[]
	for line in f:
		mot=""
		forme=""
		lemme=""
		i=0
		for word in line.split():
			if i==0:
				mot=word
			elif i==1:
				forme=word
			else:
				lemme=word 
			i=i+1
		l.append(Extended_word(mot, forme, lemme))
	return l

def print_list(l):
	for extended_word in l:
		extended_word.display_Extended_word()


f= open("/home/ludwig/Documents/UPSSITECH/txt_conv","r")
#d = count_words_line_to_dictionary(f)
l=text_to_list_Extended_word(f)
#print_dictionary_alphabetical_by_key(d)
print_list(l)