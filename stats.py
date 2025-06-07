def get_num_words(text):
	words = text.split()
	return len(words)

def get_char_counts(text):
	counts = {}
	lower_text = text.lower()
	for char in lower_text:
		counts[char] = counts.get(char, 0) + 1
	return counts

def get_ordered_char_counts(text):
	char_counts = get_char_counts(text)
	char_list = []
	for char in char_counts:
		if not char.isalpha():
			continue
		num = char_counts[char]
		char_list.append({'char': char, 'num': num})	
			
	char_list.sort(key=lambda x: x['num'], reverse=True)
	return char_list
	

def print_report(book_path, text):
	num_words = get_num_words(text)
	char_list = get_ordered_char_counts(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for dict in char_list:
		print(f"{dict['char']}: {dict['num']}")
	print("============= END ===============")

	