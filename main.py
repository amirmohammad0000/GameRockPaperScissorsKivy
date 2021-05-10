##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Imports
from kivymd.app import MDApp
from kivy.lang import Builder
from random import randint

##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Imports


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Variables
global Player_one, Player_two, Score_player_one, Score_player_two


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Variables


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Class Main
class MainApp(MDApp):
    # Start Variables
    Player_one = ""
    Player_two = ""
    Score_player_one = 0
    Score_player_two = 0

    # Start Variables

    # Start Function Build
    def build(self):
        return Builder.load_file("styleGame.kv")

    # End Function Build

    # Start Function Adds
    def add_rock(self):
        self.Player_one = "rock"

    def add_paper(self):
        self.Player_one = "paper"

    def add_scissors(self):
        self.Player_one = "scissors"

    # End Function Adds
    # Start Function Get Result
    def get_result(self):
        # Start Variables Result Game
        result = self.root.ids.result
        result_score = self.root.ids.result_score
        # End Variables Result Game

        # Start Section Computer Game
        Number_random = randint(1, 3)
        if Number_random == 1:
            Player_two = "rock"
        elif Number_random == 2:
            Player_two = "paper"
        elif Number_random == 3:
            Player_two = "scissors"
        # End Section Computer Game

        # Start If Main Game
        if self.Player_one == "rock" and Player_two == "rock":
            result.text = "Result Is : Players And Computer Is Tie"
        elif self.Player_one == "rock" and Player_two == "paper":
            result.text = "Result Is : Computer Is Wins"
            self.Score_player_two += 1
        elif self.Player_one == "rock" and Player_two == "scissors":
            result.text = "Result Is : Player Is Wins"
            self.Score_player_one += 1

        if self.Player_one == "paper" and Player_two == "paper":
            result.text = "Result Is : Players And Computer Is Tie"
        elif self.Player_one == "paper" and Player_two == "rock":
            result.text = "Result Is : Player Is Wins"
            self.Score_player_one += 1
        elif self.Player_one == "paper" and Player_two == "scissors":
            result.text = "Result Is : Computer Is Wins"
            self.Score_player_two += 1

        if self.Player_one == "scissors" and Player_two == "scissors":
            result.text = "Result Is : Players And Computer Is Tie"
        elif self.Player_one == "scissors" and Player_two == "rock":
            result.text = "Result Is : Computer Is Wins"
            self.Score_player_two += 1
        elif self.Player_one == "scissors" and Player_two == "paper":
            result.text = "Result Is : Player Is Wins"
            self.Score_player_one += 1

        result_score.text = f"Score Player Is : {self.Score_player_one} ---- And Score Computer Is : {self.Score_player_two}"

        if self.Score_player_one == 3 or self.Score_player_two == 3:
            result.text = f"End Game Score Player Is : {self.Score_player_one} ---- And Score Computer Is : {self.Score_player_two}"
            self.Score_player_one = 0
            self.Score_player_two = 0
            result_score.text = ""
        # End If Main Game
        # End Function Get Result


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Class Main


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Run App
if __name__ == "__main__":
    MainApp().run()
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Run App
