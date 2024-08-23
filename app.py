import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk 

import torch 
from torch import autocast 
from diffusers import StableDiffusionPipeline
auth_token = "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"
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
device = "cuda" if torch.cuda.is_available() else "cpu"  

if device == "cuda":
    pipe = StableDiffusionPipeline.from_pretrained(
        modelid, 
        revision="fp16", 
        torch_dtype=torch.float16, 
        use_auth_token=auth_token
    )
else:
    pipe = StableDiffusionPipeline.from_pretrained(
        modelid, 
        torch_dtype=torch.float32, 
        use_auth_token=auth_token
    )
pipe.to(device)


def generate():
    prompt_text = prompt.get()  # Get the text input from the user
    with torch.no_grad():  # Disable gradients for inference
        with autocast(device) if device == "cuda" else torch.cuda.amp.autocast(enabled=False):
            image = pipe(prompt_text, guidance_scale=8.5)["images"][0]  # Generate the image
    # img = ImageTk.PhotoImage(image.resize((512, 512)))  # Resize the image to fit the label
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    Imain.configure(image=img)
    Imain.image = img 


trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), fg_color="blue", text_color="white", command=generate)
trigger.configure(text= "Generate")
trigger.place(x=206, y=70)
app.mainloop()
