from mycroft import MycroftSkill, intent_file_handler


class FocusDefinition(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('definition.focus.intent')
    def handle_definition_focus(self, message):
        self.speak_dialog('definition.focus')


def create_skill():
    return FocusDefinition()

