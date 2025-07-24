import tkinter as tk
from .main_app import open_app

def open_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    
    splash_width = 900
    splash_height = 220
    
    #TODO: set splash screen size and position 
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    display_x = (screen_width // 2) - (splash_width // 2)
    display_y = (screen_height // 2) - (splash_height // 2)
    splash.geometry(f"{splash_width}x{splash_height}+{display_x}+{display_y}")
    
    splash.configure(bg="#C00404")
    label = tk.Label(splash, text="You are in HELL", font=("Comic Sans", 50), fg="red", bg="#770808")
    label.pack(expand=True)

    def close_splash():
        splash.destroy()
        open_app()
        
    splash.after(3000, close_splash)
    splash.mainloop()