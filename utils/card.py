class Symbol():
    """
    class defining a symbol by its two attributes color and icon
    """
    def __init__(self,color,icon):
        self.color = color
        self.icon = icon

    def __repr__(self):
        return f"{self.color} {self.icon}"
        

class Card(Symbol):
    """
    class that inherits from the class Symbol and gets a new attribute for its value
    """
    def __init__(self,color,icon,value):
        Symbol.__init__(self,color,icon)
        self.value= value

    def __str__(self):
        return f"{self.value} of {self.color} {self.icon}"



