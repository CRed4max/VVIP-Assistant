import sys
from tkinter import *
from gtts import gTTS
import os
from mpyg321.MPyg123Player import MPyg123Player
import pyttsx3

import gtts  
from playsound import playsound 


sys.path.append('../')
#from chat import get_response, bot_na
# from audio import *
# from middleware import *
from chat import *
from test import *
from inputData import *
from FileManage.tasks.audio import AudioInput
sys.path.append('/')

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
BLUE_COLOR = "#0000FF"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"





class ChatApplication:
    
    def __init__(self):
        self.counter = 0
        self.response = "response"
        self.inputList = []
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("VVIP Assistant: Virtual Voice Interactive Personalized Assistant")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1200, height=800, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome to the VVIP Assistant", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        # self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry = Entry(bottom_label, bg="#FFFFFF", fg=BLUE_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Speak🎤", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):

        if self.counter <= 1 or self.counter < inputCount[self.response]:
            print("counter ", self.counter, "response ", self.response)
            # self._insert_message(self.counter, "Counter")
            # inp = self.msg_entry.get()
            inp = AudioInput()

            if self.counter == 1:
                print("ist 1 ", inp, chat(inp))
                self.response = chat(inp)
            elif self.counter > 1:
                self.inputList.append(inp)

            self._insert_message(inp, "You")
            if(self.counter >0):
                self._insert_message(instructions[self.response][self.counter - 1], "Bot")

                engine = pyttsx3.init()
                # engine.setProperty('volume',1.0)
                engine.setProperty('rate', 100)
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)

                engine.say(instructions[self.response][self.counter - 1])
                engine.runAndWait()
                engine.stop()
                

            print("message crossed", self.inputList)
            if self.counter==0:
                self._insert_message("Enter your input", "Bot")
            self.counter+=1
        else:
            output = invoker(self.response, self.inputList)
            self._insert_message(output, "OUTPUT")
            self._insert_message(self.response, "TASK COMPLETED👌: ")
            self._insert_message("|", "|________________________________|")
            self._insert_message("Bot", "<-------👆🏻 on Speak to start----->|")
            self.counter = 0
            self.inputList = []
            self.response = "response"
            
    def _insert_message(self, msg, sender):
        if not msg:
            print("NOOOOOO ",  msg)
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    print("Hey I am in Main funtiion")
    app = ChatApplication()
    app.run()