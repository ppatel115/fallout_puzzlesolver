
import sys 

tries = int(input("Enter number of tries: "));
word_list = [str(x) for x in input("Enter terminal words: ").split()]


def hacker (tries_left, words):
	# Quit if no tries left
	if(tries_left == 0):
		print("RIP")
		sys.exit()

	print("Current list: ")
	print(*words)

	# Input selected word, remove from word list
	selected_word = input("Selected word: ")
	for x in words:
		if x == selected_word:
			words.remove(x)
		# If selected word was correct, quit program
	if input("Correct answer? (Y or N): ").lower() == 'y':
		sys.exit()
	else:
		tries_left = tries_left - 1;
		# Find similarity of word to correct answer
		likeness = int(input("Likeness value?: "))
		# If none of the letters are correct, remove all words with matching letters
		if likeness == 0:
			# remove all words with any of the same letters in the same places
			words = disparateness_finder(words, selected_word)
		else:
			# find all words with matching likeness, form new word list
			words = likeness_finder(words, selected_word, likeness)
		hacker(tries_left, words)

def disparateness_finder(words, key):
	for x in words:
		# Find all words with any similarity and remove from the list
		if sum([int(i==j) for i,j in zip(x, key)]) > 0:
			words.remove(x)
	return words

def likeness_finder(words, key, likeness):
	possible_answers = []
	for x in words:
		# If similarities between key and word are the same as the likeness value, they are potential answers
		if sum([int(i==j) for i,j in zip(x, key)]) == likeness:
			possible_answers.append(x)
	return possible_answers

hacker(tries, word_list)