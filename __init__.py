from mycroft import MycroftSkill, intent_file_handler


class ScriptureReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.scripture.intent')
    def handle_reader_scripture(self, message):
        self.speak_dialog('reader.scripture')


def create_skill():
    return ScriptureReader()

