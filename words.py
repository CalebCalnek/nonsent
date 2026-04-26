def _read_words():
	words = {}
	for category in (
		"nouns",
		"verbs",
		"adjectives",
		"adverbs",
		"prepositions",
		"determiners"
	):
		with open(f"words/{category}.txt", "r", encoding="utf-8") as file:
			words[category] = file.read().splitlines()
	return words

WORDS = _read_words()

