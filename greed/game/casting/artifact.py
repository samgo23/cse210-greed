from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        super().__init__()
        self._message = ''
    
    ''' def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The artifact's message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._message = message
    '''
    def calculate_points(self):
        points = 0

        if (self.get_text() == '*'):
            points = 1
        
        else:
            points = -1

        return points
    