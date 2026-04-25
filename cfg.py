import random

class Symbol():
	def is_terminal(self):
		""" evaluate whether the symbol is a terminal
		"""
		pass

class Terminal(Symbol):
	def __str__(self):
		return self.word
	def is_terminal(self):
		return True

class Production(Symbol):
	def __str__(self):
		symbols = [str(i) for i in self.symbols]
		symbol_string = " ".join(symbols)
		return symbol_string
	def produce(self):
		for symbol in self.symbols:
			if not symbol.is_terminal():
				symbol.produce()
	def is_terminal(self):
		return False

class Sentence(Production):
	def __init__(self):
		self.symbols = [NounPhrase(), VerbPhrase()]
	def __str__(self):
		symbols = [str(i) for i in self.symbols]
		symbol_string = " ".join(symbols)
		sentence_string = f"{symbol_string}."
		return sentence_string

class NounPhrase(Production):
	def __init__(self):
		self.symbols = [Noun()]

class VerbPhrase(Production):
	def __init__(self):
		self.symbols = [Verb()]

class Noun(Terminal):
	nouns = ("dog", "I", "John")
	def __init__(self):
		self.word = random.choice(self.nouns)

class Verb(Terminal):
	verbs = ("be", "have", "go")
	def __init__(self):
		self.word = random.choice(self.verbs)

sentence = Sentence()
sentence.produce()
print(sentence)

