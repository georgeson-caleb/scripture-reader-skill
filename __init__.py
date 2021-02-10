from mycroft import MycroftSkill, intent_file_handler
import random
import requests
import json


class ScriptureReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def formatBookName(self, book):
        book = book.replace(" st ", "")
        book = book.replace("st ", "")
        book = book.replace("nd ", "")
        book = book.replace("rd ", "")
        book = book.replace("th ", "")
        book = book.replace(" nd ", "")
        book = book.replace(" rd ", "")
        book = book.replace(" th ", "")
        book = book.replace("Psalm"," Psalms")
        book = book.replace("Psalm "," Psalms")

        return book
    
    def readScriptureJsonFile(self):
        filename = "/home/pi/mycroft-core/skills/scripture-reader-skill.georgeson-caleb/lds-scriptures-json.txt"
        f = open(filename)

        scriptures = json.loads(f.read())

        return scriptures

    @intent_file_handler('reader.scripture.intent')
    def handle_reader_scripture(self, message):
        print(message.data.get('book'))

        book = self.formatBookName(message.data.get('book') + "")
        chapter = message.data.get('chapter')
        verse = message.data.get('verse')

        scriptures = self.readScriptureJsonFile()

        self.speak(message.data.get('book') + " chapter " + message.data.get('chapter') + " verse " + message.data.get('verse') + " says " )
        scripture_name = book + " " + message.data.get('chapter') + ":" + message.data.get('verse')

        text = ""

        for s in scriptures:
           if s['verse_title'].lower() == book + " " + chapter + ":" + verse:
              text = s['scripture_text']
              break
        #r = requests.get('http://api.nephi.org/scriptures/?q={}'.format(scripture_name))
        #result = json.loads(r.text)
        
        #text = result['scriptures'][0]['text']

        self.speak(text)

    @intent_file_handler('reader.chapter.intent')
    def handle_reader_chapter(self, message):
        print(message.data.get('book'))
        book = self.formatBookName(message.data.get('book'))
        chapter = message.data.get('chapter')

        self.speak("Reading {} chapter {}".format(book, chapter))

        canLoadMore = True
        
        i = 1
        while (canLoadMore):
           chapter_name = book + " " + chapter + ":" + str(i)
           r = requests.get('http://api.nephi.org/scriptures/?q={}'.format(chapter_name))
           result = json.loads(r.text)

           if len(result['scriptures']) == 0:
              canLoadMore = False
           else:
              self.speak(result['scriptures'][0]['text'])
            
           i += 1

def create_skill():
    return ScriptureReader()
