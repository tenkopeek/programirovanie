from random import randint


class Parrot:
    def __init__(self, phrase):
        self.phrases = [phrase]
    
    def say(self, count=1):
        phrase = self.phrases[randint(0, len(self.phrases) - 1)]
        print((phrase + ' ') * count)
        
    def newText(self, phrase):
        self.phrases = [phrase]
        
    def learn(self, phrase):
        self.phrases.append(phrase)
        

p = Parrot( "Гав!" )
p.say()
p.learn( "Мяу!" )
p.say()
p.say(3) 
        