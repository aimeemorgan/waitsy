from random import choice
from config import source, db


# read source file into a giant string
# leave or strip punctuation and newlines?
def get_text():
	f_open = open(source)
	text = (f_open.read()).strip().split()
	return text

# build dict of tuples, list of words
def make_chains(text):
	chains = {}
	for i in range(len(text)-2):
		key = (text[i], text[i+1])
		chains.setdefault(key, [])
		chains[key].append(text[i+2])
	return chains

#persist chains in redis?
def persist_chains(chains):
	index = []
	for pair, words in chains:
		pair_string = ' '.join(pair)
		index.append(pair_string)
		for word in words:
			db.lpush(pair_string, word)
	for entry in index:
		db.lpush('index', entry)
	db.save
	return "Chains saved in redis"

# load chains into memory from redis
def load_chains():
	chains = {}
	index = db.get('index')
	for entry in index:
		words = db.get(entry)
		pair = tuple(entry.split())
		chains[pair] = words
	return chains

# build a line for new lyric
# cap length at what?
def build_line(chains):
	# pick a random tuple from dict to start
	line = []
	pair = choice(chains.keys())
	for word in pair:
		line.append(word)
	next_word = choice(chains[pair])
	line.append(next_word)
	while len(line) <= 10:
		pair = (pair[1], next_word)
		next_word = choice(chains[pair])
		line.append(next_word)
	line.append('\n')
	line = ' '.join(line)
	line = line.capitalize()
	return line

# build a stanza from lines
# stanza = list of strings
def build_stanza(chains):
	stanza = []
	for i in range(4):
		line = build_line(chains)
		stanza.append(line)
	return stanza

# build a song from multiple stanzas
# pass a list of list of strings to controller: 3 verses and chorus
def build_song(chains):
	verse1 = build_stanza(chains)
	verse2 = build_stanza(chains)
	verse3 = build_stanza(chains)
	chorus = build_stanza(chains)
	song = [verse1, verse2, verse3, chorus]
	return song

# to do: allow for verses, chorus, lines of varying length
# allow for different song structures
