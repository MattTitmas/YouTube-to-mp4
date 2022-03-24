import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from pathlib import Path

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 30


class youtubeToMp4(tk.Tk):
    '''
    Main application.
    '''

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Convert URL to mp4")
        self.geometry('360x250')
        self.widgets()

    def widgets(self):
        self.url_label = tk.Label(self, text="Enter\n youtube URL")
        self.url_label.place(x=10,y=10)
        self.url_text_box =tk.Text(self, state='normal',
                                   height=1, width=30)
        self.url_text_box.place(x=97, y=17)
        self.convert_button = tk.Button(self, text="Convert!",
                                        comman=self.convert)
        self.convert_button.place(x=130,y=60,width=100,height=30)

    def convert(self):
        print("Converting!")

def main():
    frame = youtubeToMp4()
    frame.resizable(0, 0)
    frame.update()
    print(frame.url_label.place_info())
    frame.mainloop()



if __name__ == "__main__":
    main()
