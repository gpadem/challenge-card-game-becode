class Symbol(self,color,icon):
    """class defining a symbol by its two attributes color and icon"""
    def __init__(self,color,icon):
        self.color = ""
        self.icon = [♥, ♦, ♣, ♠]

class Card(Symbol):
    """class that inherits from the class Symbol and gets a new attribute about its value"""
    def __init__(self,color,icon,value):
        Symbol.__init__(self,color,icon)
        self.value

