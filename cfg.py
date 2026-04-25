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
		if random.random() > 0.5:
			self.symbols.append(AdjectivePhrase())
		self.symbols.append(Noun())

class VerbPhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Verb())
		if random.random() > 0.5:
			self.symbols.append(AdverbPhrase())

class AdjectivePhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Adjective())

class AdverbPhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Adverb())

# Terminals

class Noun(Terminal):
	nouns = ("dog", "house", "time", "people", "man", "day", "way", "year", "work", "goverment")
	def __init__(self):
		self.word = random.choice(self.nouns)

class Verb(Terminal):
	verbs = ("be", "have", "go", "let", "get", "do", "take", "make", "put")
	def __init__(self):
		self.word = random.choice(self.verbs)

class Adjective(Terminal):
	adjectives = ("other", "new", "good", "old", "different", "local", "great", "small")
	def __init__(self):
		self.word = random.choice(self.adjectives)

class Adverb(Terminal):
	adverbs = ("up", "then", "out", "now", "only", "just", "more", "also", "very")
	def __init__(self):
		self.word = random.choice(self.adverbs)

class Determiner(Terminal):
	determiners = ("the", "a", "that", "this", "which", "whose", "his", "their", "her")
	def __init__(self):
		self.word = random.choice(self.determiners)

sentence = Sentence()
print(sentence)

