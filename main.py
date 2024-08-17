def get_book_content():
  with open('./books/frankenstein.txt') as f:
    return f.read()

def count_book_words(book_content):
  words = book_content.split()
  return len(words)

def sort_on(dict):
  return dict["occurences"]

def count_char_occurence(text):
  letters_occurences = []
  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  for char in chars:
    letters_occurences.append({"letter": char, "occurences": text.lower().count(char)})

  letters_occurences.sort(reverse=True, key=sort_on)
  for letter_occurence in letters_occurences:
    if not letter_occurence["letter"].isalpha():
      continue
    print(f"The '{letter_occurence["letter"]}' was found {letter_occurence["occurences"]} times")

def main():
  content = get_book_content()
  words_count = count_book_words(content)

  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words_count} words found in the document \n")
  count_char_occurence(content)
  print("--- End report ---")

main()
