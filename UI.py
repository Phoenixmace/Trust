import tkinter
from tkinter import *
from win32api import GetSystemMetrics
import os



# Variables
global active_popout
active_popout = True
global current_view
current_view = 'all_mails'

# initiate window

# get size
monitor_Width =GetSystemMetrics(0)
monitor_Height =GetSystemMetrics(1)
resolution_string = f'{monitor_Width}x{monitor_Height}'

# initiate Window
window = Tk()
window.geometry(resolution_string)
window.title('Trust')


# layouts
def generate_popout(inboxes):
    pass
def reload():
    global current_view
    global active_popout
    if active_popout:
        generate_popout

def toggle_popout():
    global active_popout
    if active_popout:
        active_popout = False
        reload()
    else:
        active_popout = True

    print(active_popout)


# Buttons
def get_button(height, width, icon_name,  command,text='Place'):
    # get path
    path = os.path.abspath(__file__)
    path = path.split('\\')
    path = path[0:-1]
    image_path = ''
    for i in path:
        image_path +=f'{i}\\'
    image_path += f'images\\{icon_name}'

    # get_icon
    image = PhotoImage(file=image_path)
    original_width = image.width()
    original_height = image.height()
    print(image.width(), image.height())
    image = image.zoom(width)
    print(image.width(), image.height())
    image = image.subsample(original_width)
    print(original_width,original_height)



    button = tkinter.Button(window, text='name', image = image, height=height, width=width, command=command)
    button.image = image
    return button

# actual buttons
popout = get_button(25, 25, r'popout.png', command=toggle_popout)
popout.place(x=1, y=1)






window.mainloop()
