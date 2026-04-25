import random

class Symbol():
	def is_terminal(self):
		pass

class Terminal(Symbol):
	def is_terminal(self):
		return True

class Production(Symbol):
	def produce(self):
		pass
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
	def produce(self):
		while not all([symbol.is_terminal() for symbol in self.symbols]):
			for i in range(len(self.symbols)):
				self.symbols[i] = self.symbols[i].produce()

class NounPhrase(Production):
	def produce(self):
		return Noun()

class VerbPhrase(Production):
	def produce(self):
		return Verb()

class Noun(Terminal):
	nouns = ("dog", "I", "John")
	def __init__(self):
		self.word = random.choice(self.nouns)
	def __str__(self):
		return self.word

class Verb(Terminal):
	verbs = ("be", "have", "go")
	def __init__(self):
		self.word = random.choice(self.verbs)
	def __str__(self):
		return self.word

sentence = Sentence()
sentence.produce()
print(sentence)

