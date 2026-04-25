import random

class Symbol():
	pass

class Terminal(Symbol):
	def __str__(self):
		return self.word

class Production(Symbol):
	def __str__(self):
		symbols = [str(i) for i in self.symbols]
		symbol_string = " ".join(symbols)
		return symbol_string

# Productions

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
		self.symbols = []
		if random.random() > 0.5:
			self.symbols.append(Determiner())
		self.symbols.append(Noun())

class VerbPhrase(Production):
	def __init__(self):
		self.symbols = [Verb()]

# Terminals

class Noun(Terminal):
	nouns = ("dog", "I", "John")
	def __init__(self):
		self.word = random.choice(self.nouns)

class Verb(Terminal):
	verbs = ("be", "have", "go")
	def __init__(self):
		self.word = random.choice(self.verbs)

class Determiner(Terminal):
	determiners = ("the", "a", "that", "this", "which", "whose")
	def __init__(self):
		self.word = random.choice(self.determiners)

sentence = Sentence()
print(sentence)

