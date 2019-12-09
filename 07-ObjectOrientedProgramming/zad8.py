class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        self.message = message.capitalize() + ' BYE'
        print(self.message)
        
a = Message()
a.set_message('adasdas')