from mycroft import MycroftSkill, intent_file_handler


class Dexro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dexro.intent')
    def handle_dexro(self, message):
        cuvantul = message.data.get('cuvantul')

        self.speak_dialog('dexro', data={
            'cuvantul': cuvantul
        })


def create_skill():
    return Dexro()

