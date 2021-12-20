class Cliente:
    
    def __init__(self):
        self._nome = input("USer: ")

    @property
    def nome(self):
        return self._nome

