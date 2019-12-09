class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
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
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print("LISTA KANAŁÓW TV:")
        for x in range(len(self.channels)):
            print(self.channels[x])
            
pom = TV()
pom.show_status()
pom.on()
pom.show_status()
pom.show_channels()
pom.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox'])
pom.show_channels()
pom.show_status()
pom.off()
