
import os

import csv

import re

from lab5_game_mac import Game
"""
lab5_game_mac did not work well in my environment, so I changed it a little bit.

Akito Motomura
"""





class MultiGame():
    """A class representing a multi-game session."""
    
    def __init__(self) -> None:
        """Initialize MultiGame."""
        self.input = ""
        
    def user_input(self):
        """Take user input to select the game level."""
        print("1. beginner")
        print("2. expert")
        while True:
            _input = input("Enter a level: ")
            if _input == "1":
                self.input = "begginer"
                break
            elif _input == "2":
                self.input = "expert"
                break
            else:
                print("Enter 1 or 2")

    def welcome(self):
        """Welcome message for the player."""
        print("Welcome to the color memory game")
        input_ = input("ready to play?: ")
        pattern = r'\b(y(es+)?|yeah|yah|yup)\b'
        if not(re.match(pattern, input_, re.IGNORECASE)):
            print("Goodbye")
            exit()
        else:
            return input_
    
    def play(self):
        """Start a multi-game session."""
        count = 0
        score_list = []
        self.user_input()
        input_ = self.welcome()
        pattern = r'\b(y(es+)?|yeah|yah|yup)\b'
        while re.match(pattern, input_, re.IGNORECASE):
            print("<game played>")
            g = Game(self.input)
            g.mainloop()
            score_list.append(g._score)
            count += 1
            input_ = input("try again?:")
        print("You've played ", count)
        print("Highest score ", max(score_list))
        print("Average score ", sum(score_list)/len(score_list))


class CustomGame():
    """A class representing a custom game session."""
    
    filename = "/Users/motomuraakiranin/Desktop/player.csv"
                
    
    def __init__(self) -> None:
        """Initialize CustomGame."""
        self.input = ""
        self.user_name = ""
        self.dic = self.create_dic()
        self.score = 0

    def create_dic(self):
        """Create a dictionary from a CSV file."""
        dic = {}
        with open(CustomGame.filename, newline='') as f:
            csvreader = csv.reader(f)
            
            for row in csvreader:
                if row:
                   dic[row[0]] = row[1:]
                else:
                    pass
        
        return dic
    
    def user_input(self):
        """Take user input to select the game level and enter username."""
        self.user_name = input("Enter your name: ").title()
        if self.user_name in self.dic:
            print("Welcome back,", self.user_name)
            print("Playing at", self.dic[self.user_name][0], "level")
            print("Your highest score so far is", self.dic[self.user_name][1])
        else:
            print("Welcome to the game", self.user_name)
        print("b. beginner")
        print("e. expert")

        while True:
            _input = input("Enter a level: ")
            b=re.search(r'\b(b)\b', _input, re.IGNORECASE)
            e=re.search(r'\b(e)\b', _input, re.IGNORECASE)
            if b and not(e):
                self.input = "begginer"
                print("Playing at", self.input, "level")
                break
            elif e and not(b):
                self.input = "expert"
                print("Playing at", self.input, "level")
                break
            else:
                print("Either b or e")

    def max_value(self):
        """Find the maximum value in the score file."""
        max_values = []
        with open(CustomGame.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    value = int(row[-1])
                    if not max_values:
                        max_values.append(value)
                    else:
                        if value == max_values[0]:
                            max_values.append(value)
                        elif value > max_values[0]:
                            max_values = [value]
                else:
                    pass
        
        return max_values
    
    def ajust_file(self, score):
        """Adjust the score file with the new score."""
        data = []
        with open(CustomGame.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    if row[0] == self.user_name:
                        row[1] = self.input
                        if int(row[2]) < score:
                            row[2] = score
                else:
                    pass     
                data.append(row)
        with open(CustomGame.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def write_file(self, score):
        """Write the new score to the score file."""
        temp_file = 'temp_file.csv'
        list_ = [self.user_name, self.input, score]
        with open(CustomGame.filename, 'r', newline='') as csvfile, open(temp_file, 'w', newline='') as new_csvfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(new_csvfile)
            for row in reader:
                writer.writerow(row)
            writer.writerow(list_)
        os.replace(temp_file, CustomGame.filename)

    def play(self):
        """Start a custom game session."""
        self.user_input()
        print("<game played>")
        g = Game(self.input)
        g.mainloop()
        
        print("Your score: ", g._score)
        max_values = self.max_value()
        if max_values:
            if g._score == 0:
                print("Good try")
            elif g._score == max_values[0]:
                print("Congratulations! You are in the top", len(max_values), "of players ")
            elif g._score > max_values[0]:
                print("Congratulations! You're the current top player")
            else:
                print("Good Game")
        else:
            print("Congratulations! You're the current top player")


        if self.user_name in self.dic:
            self.ajust_file(g._score)
        else:
            self.write_file(g._score)










       




            
m=MultiGame()
c=CustomGame()
m.play()
c.play()




    
        


