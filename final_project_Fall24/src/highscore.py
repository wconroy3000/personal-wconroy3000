import json

class Highscore:
    def __init__(self):
        '''
        Initializes the highscore file and loads the current highscore
        '''
        self.file = "assets/highscore.json"
        self.current_highscore = self.load_highscore()

    def load_highscore(self):
        '''
        Reads the highscore from the file and returns it
        return:
            int: the highscore
        '''
        with open(self.file, "r") as file:
            highscore = json.load(file)
            return highscore.get("highscore")

    def update_highscore(self, score):
        '''
        Determines if the highscore from the played game is higher then the saved one, and if so it replaces it
        args:
            score: int - the new highscore
        '''
        if score > self.current_highscore:
            self.current_highscore = score
            with open(self.file, "w") as file:
                json.dump({"highscore": self.current_highscore}, file)
