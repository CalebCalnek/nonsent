import random
from words import WORDS

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
		self.symbols.append(NounPhrase1())

class NounPhrase1(Production):
	def __init__(self):
		self.symbols = []
		if random.random() > 0.5:
			self.symbols.append(AdjectivePhrase())
		self.symbols.append(Noun())

class VerbPhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Verb())
		if random.random() > 0.5:
			self.symbols.append(AdverbPhrase())
		if random.random() > 0.5:
			self.symbols.append(PrepositionalPhrase())

class AdjectivePhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Adjective())

class AdverbPhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Adverb())

class PrepositionalPhrase(Production):
	def __init__(self):
		self.symbols = []
		self.symbols.append(Preposition())
		self.symbols.append(NounPhrase())

# Terminals

class Noun(Terminal):
	def __init__(self):
		self.word = random.choice(WORDS["nouns"])

class Verb(Terminal):
	def __init__(self):
		self.word = random.choice(WORDS["verbs"])

class Adjective(Terminal):
	def __init__(self):
		self.word = random.choice(WORDS["adjectives"])

class Adverb(Terminal):
	def __init__(self):
		self.word = random.choice(WORDS["adverbs"])

class Preposition(Terminal):
	def __init__(self):
		self.word = random.choice(WORDS["prepositions"])

class Determiner(Terminal):
	def __init__(self):
		self.word = random.choice(WORDS["determiners"])

sentence = Sentence()
print(sentence)

