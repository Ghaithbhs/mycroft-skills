from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG



class DepLocationSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(DepLocationSkill, self).__init__(name="DepLocationSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    @intent_handler(IntentBuilder("").require("Querry").require("location"))
    def handle_count_intent(self, message):
        if message.data["location"] == "h r":  #Hr department
            self.speak_dialog("hr.location")
        else if message.data["location"] == "i t":  # It department 
            self.speak_dialog("it.location")
        else if message.data["location"] == "cafeteria": #the cafeteria
            self.speak_dialog("cafeteria.location")
        else:    
        self.speak_dialog("repeat.please")

    def stop(self):
        return True

def create_skill():
    return DepLocationSkill()
