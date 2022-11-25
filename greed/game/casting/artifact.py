from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        """Contructs a new artifact.
        
        Arg: 
            self._points: Keeps track of the point total.
        """
        super().__init__()
        self._points = 0
    
    
    def calculate_points(self):
        """Calculates user point total.
        
        """

        if (self.get_text() == '*'):
            self._points = 1
        
        else:
            self._points = -1

        return self._points
    