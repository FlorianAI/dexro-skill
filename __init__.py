from mycroft import MycroftSkill, intent_file_handler
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
from mycroft.audio import wait_while_speaking
from mycroft.skills.audioservice import AudioService

class Dexro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dexro.intent')
    def handle_dexro(self, message):
        cuvantul = message.data.get('cuvantul')
        surl = "https://dexonline.ro/definitie/"
        if cuvantul !=None:
           surl = surl + cuvantul + "/json"
        elif cuvantul == None:
           surl = "https://dexonline.ro/definitie/json/json"
        print(surl)
        url = urllib.parse.urlsplit(surl)
        url = list(url)
        url[2] = urllib.parse.quote(url[2])
        url = urllib.parse.urlunsplit(url)
        print(url)
        try:
           response = urlopen(url)
           data_json = json.loads(response.read())
           print(data_json)
           print('foarte bine')
           if data_json['definitions'] == []:
              texthtml = 'nu înțeleg, întreabă un singur cuvânt'
           elif data_json['definitions'] != []:
              texthtml = data_json['definitions'][0]['htmlRep']
           repeat1 = BeautifulSoup(texthtml)
           for abbr in repeat1.find_all('abbr', {'class': 'abbrev'}):
              text = abbr.get('data-bs-content')
              print(text)
              abbr.replaceWith(text)
           repeat = repeat1.get_text()
           repeat1 = repeat.replace("@","")
           repeat = repeat1.replace("$","")
           repeat1 = repeat.replace("#","")
#        repeat = repeat1.replace(".","")
           repeat1= repeat.replace("[","")
           repeat1= repeat1.replace("]","")
           self.speak(repeat1.strip())
        except: 
           self.speak('nu înțeleg, întreabă un singur cuvânt') 
#        self.speak_dialog('dexro', repeat1, wait=True)
         #if repeat1 != '':sssss
	#	self.speak(repeat1.strip())
           #   self.speak_dialog('dexro', data={
           #   'cuvantul': cuvantul
           # })
          #elif
    wait_while_speaking()
    def stop(self):
            self.speak_dialog('m-am oprit')         
def create_skill():
    return Dexro()

