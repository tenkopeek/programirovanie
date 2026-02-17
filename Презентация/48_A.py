class LampRow:
    def __init__(self):
        self.__state = "00000000"
        
    def __getState(self):
        return self.__state 
    
    def __setState(self, state):
        if len(state) != 8:
            state = "00000000"
        self.__state = state
        
    def show(self):
        print(self.__state.replace('0', '-').replace('1', '*'))
        
    state = property(__getState, __setState)


lamps = LampRow()
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()                
