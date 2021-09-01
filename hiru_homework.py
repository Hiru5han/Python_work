books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}

def search(search_term):
  check = 0
  for author, titles in books.items():
    for book in titles:
      if search_term == book:
        print("{:s} wrote {:s}".format(author, book))
        check = 1
        break
  if check == 0:
    print("Book not found")

# Ask the user for which book they want
search_term = str(input("What book are you looking for? "))
#This will capitalise each word in the string!
Search_Term = search_term.title()
#Search for the book
search(Search_Term)