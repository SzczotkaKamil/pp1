class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print("Telewizor jest włączony.",f"kanał {self.channel_no}")
        else:
            print("Telewizor jest wyłączony.")
    def set_channel(self,new_channel_no):
        self.channel_no  = new_channel_no
            
pom = TV()
pom.show_status()
pom.on()
pom.show_status()
pom.set_channel(5)
pom.show_status()
pom.off()
pom.show_status()