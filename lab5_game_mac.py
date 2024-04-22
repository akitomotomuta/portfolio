import tkinter as tk
import random 
import time

class Game(tk.Tk) :

    ''' color memory game'''
    

    

    #colors = ['Black','Blue','Green','Red','Yellow','Purple', 'Pink','Cyan']
    colors = ['Black','Blue','Green','Red','Yellow','Purple', 
    'Pink','Cyan',"Brown","Gray","Navy","Gold","Orange","Greenyellow","Ivory","Silver","Skyblue"]
 

    

    def __init__(self, level) :
        

        super().__init__()

        ###############################################

        if level.lower() != 'expert' :

            self._colors = Game.colors[:5]

            self._speed = 1     # number of seconds between color change

        else :

            self._colors = Game.colors

            self._speed = 0.85  # number of seconds between color change

        self._currColors = []

        self._score = 0         # user score for the game   

        self._count = 2         # starting count of colors to be displayed

        ################################################

        self.title("COLOR MEMORY GAME") 

        self._msgLabel = tk.Label(self, text="Press 'Escape' to start", 

                                  font=('Arial', 20), padx=30)

        self._msgLabel.grid(pady=1)       

        self._label = tk.Label(self) 

        self._label.config(width=40, height=30)

        #self._bg_color = self._button["background"]

        #self._button.config(bg=self._bg_color)

        self._label.grid(pady=1) 

        self._e = tk.Entry(self) 

        self._e.grid(pady=20)

        self._scoreLabel = tk.Label(self, text="",font=('Arial', 20), 

                                    padx=30)  

        self._scoreLabel.grid(pady=10) 

        self._endLabel = tk.Label(self, text="", 

                                  font=('Arial', 20), padx=30)

        self._endLabel.grid(pady=10)        

        self.bind('<Escape>', self._startGame)    

        self._e.bind('<Return>', self._user_entry)

        self._no_input = True

        self._gameRunning = False

        self.attributes("-topmost", True)

        self.protocol("WM_DELETE_WINDOW", lambda : "")

        

    def getScore(self) :

        ''' return score '''

        return self._score

        

    def _user_entry(self, event):

        self._no_input = False

        

    def _get_user_input(self):

        while self._no_input:

            time.sleep(0.001)

            self.update()

        self._no_input = True

        return self._e.get()

        

    def _displayColors(self) :
        #label_1 = tk.Label(text="", bg="#FFF")
        #label_1.config(width=40,height=30)
        #label_1.grid(pady=1)
        """

        num = len(self._colors)

        if self._count <= num :

            self._currColors = random.sample(self._colors, self._count)
            print(self._currColors)

        else :

            count = self._count

            self._currColors = random.sample(self._colors, num)
            print(self._currColors)

            for i in range(count - num) :

                colors = random.sample(self._colors, 1)

                while self._currColors[-1] == colors[0] :

                    colors = random.sample(self._colors, 1)

                self._currColors += colors

        
        num = len(self._colors)
        self._currColors = random.sample(self._colors, num)

        for color in self._currColors :
            #label_1 = tk.Label(text="", bg="#FFF")
            #label_1.place(x=150, y=10, width=200, height=300)
            self._label.config(bg=color)
            #self._count += 1
        """
        try:

            for _ in range(1,self._count):
                self._currColors = random.sample(self._colors, self._count)
                #count+=1
            for color in self._currColors:
                #print(color)
                self._label.config(bg=color)

                self._label.update()

                time.sleep(self._speed)
        except ValueError:print("genius")
        

    def _startGame(self, event):

        if self._gameRunning :

            return

        self._gameRunning = True

        while self._gameRunning :

            self._msgLabel.config(text="Enter the colors you see") 

            self._displayColors()

            self._e.focus_set()

            userColors = self._get_user_input().title().split()

            if userColors == self._currColors :

                self._score += 1
                self._count += 1

                self._e.delete(0, tk.END)

                self._scoreLabel.config(text="Score: " + str(self._score))

                self._msgLabel.focus_set()

                self.update()

                time.sleep(1.5)

            else :

                self._msgLabel.config(text="Not quite! Game over")

                self._msgLabel.focus_set()

                self._e.grid_forget()

                self._label.grid_forget()

                self._endLabel.config(text="Click X to close the game")

                self._gameRunning = False

        self.protocol("WM_DELETE_WINDOW", self.closewin)

    

    def closewin(self) :

        self.quit()

        self.destroy()

