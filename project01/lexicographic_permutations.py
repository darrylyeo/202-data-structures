# Takes a string consisting of 0 or more unique lower-case letters in alphabetical order as a single input argument.
# Returns a lexicographically-ordered list of strings where each string represents a permutation of the input string.

def perm_gen_lex(chars):
	return [
		result
		
		# For each character in the input string:
		for char in chars
		
		# Form a simpler string by removing the character from the input string
		for other_chars in [chars.replace(char, '')]
		
		# Generate all permutations of the simpler string recursively (i.e. call the perm_gen_lex function with the simpler string)
		for permutation in perm_gen_lex(other_chars) or ['']
		
		# Add the removed character to the front of each permutation of the simpler string
		for result in [char + permutation]
		
		# ...and add the resulting permutation to the list
		
	] if len(chars) else []