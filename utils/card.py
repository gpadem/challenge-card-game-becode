class Symbol(self,color,icon):
    """class defining a symbol by its two attributes color and icon"""
    def __init__(self,color,icon):
        self.color = ["Red","Black"]
        self.icon = [♥, ♦, ♣, ♠]

class Card(Symbol):
    """class that inherits from the class Symbol and gets a new attribute about its value"""
    def __init__(self,color,icon,value):
        Symbol.__init__(self,color,icon)
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

