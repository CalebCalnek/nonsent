import random
from words import WORDS

class Terminal():
	def __str__(self):
		return self.word

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

