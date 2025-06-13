import sys

from stats import get_num_words, get_char_counts, get_ordered_char_counts, print_report

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_path = sys.argv[1]
	text = get_book_text(book_path)
	#num_words = get_num_words(text)
	#char_counts = get_char_counts(text)
	#ordered_char_counts = get_ordered_char_counts(text)
	print_report(book_path, text)
		
def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

#if __name__ == "__main__":

main()
