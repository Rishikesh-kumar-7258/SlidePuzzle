

class StateMachine :

    """
    This is a statemaching - It changes the state of the game
    """

    def __init__(self, states={}): 

        self.empty = {}

        self.states = states or {}
        self.current = self.empty

    def change(self, state) : 
        assert state in self.states

        self.current = self.states[state]
        self.current.enter()
    
    def update(self, params=None) : 

        self.current.update()