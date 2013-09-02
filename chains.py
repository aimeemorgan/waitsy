from random import randint

# read source file into a giant string
# leave or strip punctuation and newlines?
def get_text():
	# return source
	pass

# build dict of tuples, list of words
def make_chains(source):
	chains = {}
	return chains

# build a line for new lyric
# cap length at what?
def build_line():
	# pick a random tuple from dict to start
	# return line
	pass

# build a stanza from lines
# stanza = list of strings
def build_stanza():
	stanza = []
	for i in range(4):
		line = build_line()
		stanza.append(line)
	return stanza

# build a song from multiple stanzas
# pass a list of list of strings to controller: 3 verses and chorus
def build_song():
	song = []
	verse1 = build_stanza()
	verse2 = build_stanza()
	verse3 = build_stanza()
	chorus = build_stanza()
	return song

# to do: allow for verses, chorus, lines of varying length
# allow for different song structures
