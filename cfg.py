import random

class Production:
	def produce(self):
		pass
	def is_terminal(self):
		pass

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
	def is_terminal(self):
		return False

class NounPhrase(Production):
	def produce(self):
		return Noun()
	def is_terminal(self):
		return False

class VerbPhrase(Production):
	def produce(self):
		return Verb()
	def is_terminal(self):
		return False

class Noun(Production):
	nouns = ("dog", "I", "John")
	def produce(self):
		word = random.choice(self.nouns)
		return Word(word)
	def is_terminal(self):
		return False

class Verb(Production):
	verbs = ("be", "have", "go")
	def produce(self):
		word = random.choice(self.verbs)
		return Word(word)
	def is_terminal(self):
		return False

class Word(Production):
	def __init__(self, word):
		self.word = word
	def __str__(self):
		return self.word
	def produce(self):
		pass
	def is_terminal(self):
		return True

sentence = Sentence()
sentence.produce()
print(sentence)

