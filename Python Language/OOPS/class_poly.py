class dog:
    def sound(self):
        print("Bark")

class cat:
    def sound(self):
        print("Meow")
    
for animal in (dog(), cat()):
    animal.sound()