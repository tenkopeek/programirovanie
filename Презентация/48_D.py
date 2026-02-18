class LampRow:
    def __init__(self, length):
        self.__length = length
        self.__state = 0
        
    def __getState(self):
        return f"{self.__state:0{self.__length}d}" 
    
    def __setState(self, state):
        if len(state) != self.__length:
            state = 0
        self.__state = int(state)
        
    def show(self):
        print(f"{self.__state:0{self.__length}d}".replace('0', '-').replace('1', '*').replace('2', 'o'))
        
    state = property(__getState, __setState)


lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10201010"
print(lamps.state)
lamps.show()
                