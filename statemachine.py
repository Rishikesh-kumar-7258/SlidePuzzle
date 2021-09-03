

class StateMachine :

    """
    This is a statemaching - It changes the state of the game
    """

    def __init__(self, states): 

        self.empty = {}

        self.states = states or {}
        self.current = empty

    def change(self, state) : 
        assert state in self.states

        self.current = states[state]
        self.current.enter()
    
    def update(self, params) : 

        self.current.update(params)