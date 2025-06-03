from stats import get_num_words, get_char_counts

def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	char_counts = get_char_counts(text)
	
	print(f"{num_words} words found in the document")
	print(f"Character counts: {char_counts}")
	
def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

#if __name__ == "__main__":
main()
