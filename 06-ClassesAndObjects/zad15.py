class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.glosnosc =0
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            if self.channel_no<len(self.channels):
                print("Telewizor jest włączony.",f"kanał {self.channel_no}",f"({self.channels[self.channel_no]})",f"Głośność wynosi : {self.glosnosc}")
            else:
                print("Telewizor jest włączony.",f"kanał {self.channel_no}",f"Głośność wynosi : {self.glosnosc}")
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
    def zwieksz_glosnosc(self):
        if self.glosnosc<10:
            self.glosnosc+=1
    def zmniejsz_glosnosc(self):
        if self.glosnosc>0:
            self.glosnosc-=1
            
pom = TV()
pom.show_status()
pom.on()
pom.show_status()
pom.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Disney XD','Jetix','Cartoon Network'])
pom.zwieksz_glosnosc()
pom.show_status()
pom.zwieksz_glosnosc()
pom.show_status()
pom.zwieksz_glosnosc()
pom.show_status()
pom.zmniejsz_glosnosc()
pom.show_status()
pom.zmniejsz_glosnosc()
pom.show_status()
pom.zmniejsz_glosnosc()
pom.show_status()
pom.zmniejsz_glosnosc()
pom.show_status()
