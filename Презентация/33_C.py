class Parrot:
    def __init__(self, phrase):
        self.phrase = phrase
    
    def say(self):
        print(self.phrase)
        
    def newText(self, phrase):
        self.phrase = phrase
        

p1 = Parrot("Гав!")
p1.say()
p1.newText("Мяу!")
p1.say()
        