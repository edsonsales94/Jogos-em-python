class Cliente:
    
    def __init__(self):
        self.__nome = input("USer: ")
    pass
    @property
    def nome(self):
        return self.__nome

