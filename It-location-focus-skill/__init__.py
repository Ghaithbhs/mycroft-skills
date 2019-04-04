from mycroft import MycroftSkill, intent_file_handler


class HrlocationFocusCorp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hr.location.intent')
    def handle_definition_focus(self, message):
        self.speak_dialog('hr.location')


def create_skill():
    return HrlocationFocusCorp()

