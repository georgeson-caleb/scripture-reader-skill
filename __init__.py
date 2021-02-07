from mycroft import MycroftSkill, intent_file_handler
import random

class ScriptureReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.scripture.intent')
    def handle_reader_scripture(self, message):

        self.speak_dialog('reader.scripture')


def create_skill():
    return ScriptureReader()

def getRandomScripture():
   # Choose a random volume (number between 1 and 5)
   # 1: Old Testament
   # 2: New Testament
   # 3: Book of Mormon
   # 4: D&C
   # 5: Pearl of Great Price
   volume = random.randint(1, 5)

   # Choose a random book
   #   - Get the number of books in the volume (Using the COUNT() query)
   #   - Choose a random number between 1 and that number
   num_books_query = "SELECT COUNT(*) FROM books WHERE volume_id={};".format(volume) 
   num_books = 5 # Query the DB to get this number
   book = random.randint(1, num_books)

   # Choose a random chapter
   #   - Same as above
   num_chapters_query = "SELECT COUNT(*) FROM chapters WHERE book_id={};".format(book)
   num_chapters = 10 # Query the DB to get this number
   chapter = random.randint(1, num_chapters)

   # Choose a random verse
   #   - Same as above
   num_verses_query = "SELECT COUNT(*) FROM verses WHERE chapter_id={}".format(chapter)
   num_verses = 15 # Query the DB to get this number
   verse = random.randint(1, num_verses)

   # Query the DB for the scripture
   scripture_query = "SELECT b.book_title book, c.chapter_number chapter, v.verse_number verse, v.scripture_text words FROM verses v INNER JOIN chapters c ON v.chapter_id = c.id INNER JOIN books b ON c.book_id = b.id WHERE b.id = {} AND c.id = {} AND v.id = {};".format(book, chapter, verse)

   # Format the scripture string

   # Read the scripture out loud
