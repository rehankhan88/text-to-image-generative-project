import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk 
from authtoken import auth_token

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

Imain = ctk.CTkLabel(master=app, width=512, height=512)
Imain.place(x=10, y=110)

modelid= "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtypes=torch.float16, use_auth_token=auth_token)
pipe.to(device)


def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
    img = ImageTk.PhotoImage(image)
    img.save("generatedimage.png")
    Imain.confgure(image=img)


trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), fg_color="blue", text_color="white", command=generate)
trigger.configure(text= "Generate")
trigger.place(x=206, y=70)
app.mainloop()
