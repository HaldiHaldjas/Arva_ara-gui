from Controller import Controller
class Game:
    def __init__(self): #  konstruktor, mis käivitatakse iga kord
        game = Controller()
        game.view.main()  #  Teeb põhiakna nähtavaks

if __name__ == "__main__":  #  käivitab selle faili
        Game()

