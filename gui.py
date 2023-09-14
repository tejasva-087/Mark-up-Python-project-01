from PIL import ImageTk
from tkinter.font import Font
import datetime
import ttkbootstrap as ttk

color_white = '#f8f9fa'
font_family = 'Nueva Std Cond'


def destroy(root):
    root.destroy()


def splash_screen():
    # Basic color and styling
    root = ttk.Window(themename='litera')
    # Setting up font
    big_font = Font (
        family=font_family,
        size=120,        
    )
    
    medium_font = Font (
        family=font_family,
        size=32
    )

    # Title
    root.title('Mark Up')

    # Hiding titlebar
    root.overrideredirect(True)

    # Making it non resizable
    root.resizable(False, False)

    # Making the window spawn in middle
    root.geometry(f'950x600+{int((root.winfo_screenwidth()/2)-500)}+{int((root.winfo_screenheight()/2)-350)}')

    # ========================================
    """Setting the background of the window"""
    # ========================================
    # Image variable
    bg = ImageTk.PhotoImage(file=r'img/background.png')
    # Canvas Image holder
    bg_canvas = ttk.Canvas(root, width=950, height=550)
    bg_canvas.place(x=0, y=0, relheight=1, relwidth=1)

    # Setting image in canvas
    bg_canvas.create_image(0, 0, image=bg, anchor='nw')

    # ========================================
    """Hero text"""
    # ========================================
    # Setting up text
    bg_canvas.create_text(300, 150, text='Mark up', font=big_font, fill=color_white)
    bg_canvas.create_text(180, 220, text='Edition: 2.0', font=medium_font, fill=color_white)

    # ========================================
    """footer icon"""
    # ========================================
    # Image variable
    footer_icon = ImageTk.PhotoImage(file=r'img/mark-up-logo.jpg')
    # Image set up
    bg_canvas.create_image(135, 450, image=footer_icon)

    # ========================================
    """Footer text"""
    # ========================================
    big_font = Font(
        family=font_family,
        size=18
    )
    bg_canvas.create_text(280, 500, text=f'Created by Tejasva Khandelwal. © All rights reserved {datetime.date.today().year}', fill=color_white)

    # Destroying within 3 seconds
    root.after(3000, lambda: destroy(root))

    root.mainloop()

splash_screen()