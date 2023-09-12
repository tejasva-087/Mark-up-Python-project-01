from PIL import ImageTk
import ttkbootstrap as ttk
from tkinter.font import Font


def splash_screen():
    root = ttk.Window()
    # Font for the hero text
    big_font_color = '#333'
    big_font = Font(
        family='Impact',
        size=100,
        weight="normal"
    )
    # Font for hero side text

    # Making it non resizable
    root.resizable(False, False)

    # Making the window spawn in middle
    root.geometry(f'950x600+{int((root.winfo_screenwidth() / 2) - 500)}+{int((root.winfo_screenheight() / 2) - 300)}')

    # ========================================
    """Setting the background of the window"""
    # ========================================
    # Image variable
    bg = ImageTk.PhotoImage(file=r'img/background.png')
    # Canvas Image holder
    bg_canvas = ttk.Canvas(root, width=950, height=550)
    bg_canvas.pack(fill='both', expand=True)
    # Setting image in canvas
    bg_canvas.create_image(0, 0, image=bg, anchor='nw')

    root.mainloop()


splash_screen()
