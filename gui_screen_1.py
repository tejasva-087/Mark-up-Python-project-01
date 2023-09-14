from PIL import ImageTk
from tkinter.font import Font
import datetime
import ttkbootstrap as ttk
from tkinter import filedialog
import main

color_white = '#f8f9fa'
color_black = '#212529'
color_grey = '#868e96'
color_green = '#51cf66'
color_red = '#d9480f'
font_family = 'Nueva Std Cond'


def file_open():
    pass


def check_name(name, widget, text):
    if name.isalpha():
        widget.configure(foreground = color_green)
        text.set(f'{greet()} {name}!')
    else:
        widget.configure(foreground = color_red)
        text.set('enter correct name')


def activate_input_clear(var, widget):
    var.set('')
    widget.configure(state="active")


def greet():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        return "good morning"
    elif current_time.hour < 17:
        return "good afternoon"
    else:
        return "good evening"



def gui_screen_1():
    root = ttk.Window(themename='litera')
    
    # Setting up font
    small_font = Font(
        family=font_family,
        size=16
    )

    small_font_2 = Font(
        family=font_family,
        size=12
    )
    # Title
    root.title('Mark Up')

    # Making it non resizable
    root.resizable(False, False)

    # Making the window spawn in middle
    root.geometry(f'950x600+{int((root.winfo_screenwidth()/2)-500)}+{int((root.winfo_screenheight()/2)-350)}')

    # ========================================
    """Setting the background of the window"""
    # ========================================
    # Image variable
    bg = ImageTk.PhotoImage(file=r'img/background-screen-2.png')
    # Canvas Image holder
    bg_canvas = ttk.Canvas(root, width=950, height=550)
    bg_canvas.place(x=0, y=0, relheight=1, relwidth=1)

    # Setting image in canvas
    bg_canvas.create_image(0, 0, image=bg, anchor='nw')

    # ========================================
    """Input setup"""
    # ========================================
    # Frame
    frame_details = ttk.Frame(root, padding=20)
    frame_details.place(relx=0.5, rely=0.5, width=320, anchor='center')

    """Name"""
    # Input
    input_text = ttk.StringVar()

    input_name = ttk.Entry(frame_details, width=26, bootstyle='dark', textvariable=input_text)
    input_name.grid(row=1, column=0)
    input_name.configure(state='disable')
    input_text.set('Enter name..')
    
    # Label sub
    label_text = ttk.StringVar()
    label_text.set('')
    label_check = ttk.Label(frame_details, font=small_font_2, width=31, textvariable=label_text)
    label_check.grid(row=2, column=0)
    # Button
    ttk.Button(frame_details, text='→', padding=5, bootstyle='dark', command=lambda: check_name(input_text.get(), label_check, label_text)).grid(row=1, column=1, padx=1)
    # Event binds
    input_name.bind('<Return>', lambda event: check_name(input_text.get(), label_check, label_text))
    input_name.bind("<Button-1>", lambda event: activate_input_clear(input_text, input_name))

    """File"""
    ttk.Button(frame_details, text='Browse', padding=5, bootstyle='dark', width=30, command=lambda: file_open()).grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()

