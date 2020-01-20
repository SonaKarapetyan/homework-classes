class Book:
	def __init__(self, title, author, genre, with_content, annotation, age_group, number_of_pages, book_type):
		self.title = title
		self.author = author
		self.genre = genre
		self.with_content = with_content
		self.annotation = annotation
		self.age_group = age_group
		self.number_of_pages = number_of_pages
		self.book_type = book_type

	def open(self):
		print(self.title + " book has been openend")

	def close(self):
		print(self.title + " book has been closed")

	def turn_page(self):
		print("page has been turned")

	def get_book_details(self):
		print(
			'Title: ' + self.title + '\n' +
			'Author: ' + self.author + '\n' +
			'Genre: ' + self.genre + '\n' +
			'Annotation: ' + self.annotation + '\n' +
			'Age Group: ' + self.age_group + '\n' +
			'Number Of Pages: ' + self.number_of_pages + '\n' +
			'Book Type: ' + self.book_type
		)


the_little_prince = Book(
	"The Little Prince", 
	"Antoine de Saint-Exupery", 
	"Children's literature",
	True, 
	"The Little Prince is a novella by French aristocrat, writer, and aviator Antoine de Saint-Exupery. It was first published in English and French in the US by Reynal & Hitchcock in April 1943, and posthumously in France following the liberation of France as Saint-Exupery's works had been banned by the Vichy Regime",
	"7-15",
	"116",
	"hard cover"
)

# the_little_prince.open()
# the_little_prince.close()
# the_little_prince.turn_page()
the_little_prince.get_book_details()
