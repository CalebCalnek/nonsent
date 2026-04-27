import sys
from productions import Sentence

exec_count = 1

if len(sys.argv) > 1 and sys.argv[1] == "--help":
	print("usage: python cfg.py [-n exec_count]")
	exit(1)

for i in range(1, len(sys.argv)):
	if sys.argv[i] == "-n":
		i += 1
		exec_count = int(sys.argv[i])

for i in range(exec_count):
	sentence = Sentence()
	print(sentence)

