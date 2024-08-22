# import tkinter as tk
# import customtkinter as ctk 

# from PIL import ImageTk 
# # from authtoken import auth_token


# import torch 
# from torch import autocast 
# from diffusers import StableDiffusionPipeline

# # create app
# app = tk.Tk()
# app.geometry("532x622")
# app.title("Stable Bud")
# ctk.set_appearance_mode("dark")

# prompt = ctk.CTkEntry(height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white")
# prompt.place(x=10, y=10)



# app.mainloop()



import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk 
# from authtoken import auth_token

import torch 
from torch import autocast 
from diffusers import StableDiffusionPipeline

# create app
app = tk.Tk()
app.geometry("532x622")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

# create an entry widget with the master argument
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), fg_color="white", text_color="black")


# place the widget in the window (use pack, grid, or place)
prompt.pack(pady=20)

app.mainloop()
