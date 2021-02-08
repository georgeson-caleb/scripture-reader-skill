from mycroft import MycroftSkill, intent_file_handler
import random
import requests

books = [
 "Genesis",
 "Exodus",
 "Leviticus",
 "Numbers",
 "Deuteronomy",
 "Joshua",
 "Judges",
 "Ruth",
 "1 Samuel",
 "2 Samuel",
 "1 Kings",
 "2 Kings",
 "1 Chronicles",
 "2 Chronicles",
 "Ezra",
 "Nehemiah",
 "Esther",
 "Job",
 "Psalms",
 "Proverbs",
 "Ecclesiastes",
 "Song of Solomon",
 "Isaiah",
 "Jeremiah",
 "Lamentations",
 "Ezekiel",
 "Daniel",
 "Hosea",
 "Joel",
 "Amos",
 "Obadiah",
 "Jonah",
 "Micah",
 "Nahum",
 "Habakkuk",
 "Zephaniah",
 "Haggai",
 "Zechariah",
 "Malachi",
 "Matthew",
 "Mark",
 "Luke",
 "John",
 "Acts",
 "Romans",
 "1 Corinthians",
 "2 Corinthians",
 "Galatians",
 "Ephesians",
 "Philippians",
 "Colossians",
 "1 Thessalonians",
 "2 Thessalonians",
 "1 Timothy",
 "2 Timothy",
 "Titus",
 "Philemon",
 "Hebrews",
 "James",
 "1 Peter",
 "2 Peter",
 "1 John",
 "2 John",
 "3 John",
 "Jude",
 "Revelation",
 "1 Nephi",
 "2 Nephi",
 "Jacob",
 "Enos",
 "Jarom",
 "Omni",
 "Words of Mormon",
 "Mosiah",
 "Alma",
 "Helaman",
 "3 Nephi",
 "4 Nephi",
 "Mormon",
 "Ether",
 "Moroni",
 "Doctrine and Covenants",
 "Moses",
 "Abraham",
 "Joseph Smith--Matthew",
 "Joseph Smith--History",
 "Articles of Faith"
]

class ScriptureReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.scripture.intent')
    def handle_reader_scripture(self, message):
        scripture_name = message.data.get('book') + " " + message.data.get('chapter') + ":" + message.data.get('verse')
       
        r = requests.get('http://api.nephi.org/scriptures/?q={}'.format(scripture_name)
                         
        print(r)
       
        self.speak(scripture_name)


#def getRandomScripture():
   # Choose a random volume (number between 1 and 5)
   # 1: Old Testament
   # 2: New Testament
   # 3: Book of Mormon
   # 4: D&C
   # 5: Pearl of Great Price
#   volume = random.randint(1, 5)

   # Choose a random book
   #   - Get the number of books in the volume (Using the COUNT() query)
   #   - Choose a random number between 1 and that number
#   num_books_query = "SELECT COUNT(*) FROM books WHERE volume_id={};".format(volume) 
#   num_books = 5 # Query the DB to get this number
#   book = random.randint(1, num_books)

   # Choose a random chapter
   #   - Same as above
#   num_chapters_query = "SELECT COUNT(*) FROM chapters WHERE book_id={};".format(book)
#   num_chapters = 10 # Query the DB to get this number
#   chapter = random.randint(1, num_chapters)

   # Choose a random verse
   #   - Same as above
#   num_verses_query = "SELECT COUNT(*) FROM verses WHERE chapter_id={}".format(chapter)
#   num_verses = 15 # Query the DB to get this number
#   verse = random.randint(1, num_verses)

   # Query the DB for the scripture
#   scripture_query = "SELECT b.book_title book, c.chapter_number chapter, v.verse_number verse, v.scripture_text words FROM verses v INNER JOIN chapters c ON v.chapter_id = c.id INNER JOIN books b ON c.book_id = b.id WHERE b.id = {} AND c.id = {} AND v.id = {};".format(book, chapter, verse)

   # Format the scripture string

   # Read the scripture out loud


def create_skill():
    return ScriptureReader()
