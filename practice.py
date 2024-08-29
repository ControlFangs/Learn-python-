# print("this its the start of something amazing Tyler!")
# print("Lets get started")
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
import tkinter as tk

root = tk.Tk()
root.title("Desktop Pet")
root.geometry("200x200")
root.attributes("-topmost", True)
root.attributes("-transparentcolor", root['bg'])  # For transparency (on Windows)
root.overrideredirect(True)  # Remove window borders

pet_label = tk.Label(root, text="Your Pet", font=("Arial", 24))
pet_label.pack()

root.mainloop() 
from PIL import Image, ImageTk

# Load an image
image = Image.open("pet.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
pet_label = tk.Label(root, image=photo)
pet_label.pack()
def move_pet():
    x = pet_label.winfo_x() + 5  # Move 5 pixels to the right
    y = pet_label.winfo_y()
    pet_label.place(x=x, y=y)

    root.after(50, move_pet)  # Repeat every 50 ms

move_pet()
import random

def random_behavior():
    action = random.choice(['move', 'jump', 'sleep'])
    if action == 'move':
        move_pet()
    elif action == 'jump':
        # Implement jump action
        pass
    elif action == 'sleep':
        # Implement sleep action
        pass

    root.after(1000, random_behavior)  # Repeat every second

random_behavior()
import pyautogui

def follow_cursor():
    x, y = pyautogui.position()
    pet_label.place(x=x, y=y)
    root.after(100, follow_cursor)

follow_cursor()