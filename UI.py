import tkinter
from tkinter import *
from win32api import GetSystemMetrics

class Button:
    def __init__(self, window, width, height,image_path, target_function, x_relative, y_relative, name):
        # get image
        self.image = PhotoImage(file=r"C:\Users\maxce\Downloads\2769159.png")
        #image.zoom(image_width_scale, image_height_scale)
        # resize
        # create button
        button = tkinter.Button(window, text='name', image = self.image, height=height, width=width)
        button = tkinter.Button(width=25, height=25, image=self.image)
        # get absolute position
        window_height = window.winfo_vrootheight()
        window_width = window.winfo_vrootwidth()
        button_x = x_relative*window_width
        button_y = y_relative*window_height


        button.place(x=button_x,y=button_y)



def placeholder():
    print('heyo')

# get size
monitor_Width =GetSystemMetrics(0)
monitor_Height =GetSystemMetrics(1)
resolution_string = f'{monitor_Width}x{monitor_Height}'

# initiate Window
window = Tk()
window.geometry(resolution_string)
window.title('Trust')



buttons = [] #item, name
# popout button



Button = Button(window, 250, 250, r"C:\Users\maxce\Downloads\2769159.png", placeholder, 0, 0, 'popout')

image = PhotoImage(file=r"C:\Users\maxce\Downloads\2769159.png")
print(image)
popout_button = tkinter.Button(width=25, height=25,image=image )
popout_button.place(x=100, y=1)



window.mainloop()
