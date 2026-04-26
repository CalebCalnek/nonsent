import random
from terminals import *

class Production():
	def __str__(self):
		symbols = [str(i) for i in self.symbols]
		symbol_string = " ".join(symbols)
		return symbol_string

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

