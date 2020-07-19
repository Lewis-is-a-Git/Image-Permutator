import os as os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil

# global variables
folderName = ""  # directory to folder
listing = [""]  # list of all images in selected folder

# Open the file explorer
def open_folder():
    global folderName
    global listing
    folderName = filedialog.askdirectory()  # choose directory
    # Change label contents
    label_file_explorer.configure(text="Folder Opened: " + folderName)
    # create list of items in directory
    listing = os.listdir(folderName)
    listing = [f for f in listing if f.__contains__('.')]  # filter list to remove folders


# modify the images based on selection
def modify_images():
    global listing
    global folderName
    flip_foldername = folderName + "/"
    if max_permutations: # Max permutations goes through all the combinations to generate the most amount of images
        for filename in listing:
            for lr in range(2): # left-right
                for ud in range(2): # up-down
                    for ro in range(2): # rotate 180
                        im = Image.open(flip_foldername + filename)
                        permutation = "" # add the permutation to the file name
                        if (lr):
                            im = im.transpose(Image.FLIP_LEFT_RIGHT)
                            permutation = permutation + "lr_"
                        if (ud):
                            im = im.transpose(Image.FLIP_TOP_BOTTOM)
                            permutation = permutation + "ud_"
                        if (ro):
                            im = im.transpose(Image.ROTATE_180)
                            permutation = permutation + "ro_"
                        im.save(flip_foldername + permutation + filename) # save the new image also overwrites the same old one
    else: 
        for filename in listing:
            im = Image.open(flip_foldername + filename)
            if (left_right):
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
                im.save(flip_foldername + "lr_" + filename)
            if (up_down):
                im = im.transpose(Image.FLIP_TOP_BOTTOM)
                im.save(flip_foldername + "ud_" + filename)
            if (rotated):
                im = im.transpose(Image.ROTATE_180)
                im.save(flip_foldername + "ro_" + filename)


# Create the root window
window = tk.Tk()
# Set window title
window.title('Image Permutator')
# Set window size
window.geometry("400x400")
window.minsize(width=400, height=400)
# set up gui
frm_options = tk.Frame(master=window)
frm_buttons = tk.Frame(master=window)

# Create a File Explorer label
label_file_explorer = tk.Label(frm_options,
                               text="Start by opening a folder...",
                               width=100, height=4,
                               fg="blue")
label_file_explorer.pack()

button_explore = tk.Button(frm_options,
                           text="Open Folder",
                           command=open_folder).pack()

# Checkboxes
left_right = tk.IntVar()
tk.Checkbutton(frm_options, text="left_right", variable=left_right).pack()
up_down = tk.IntVar()
tk.Checkbutton(frm_options, text="up_down", variable=up_down).pack()
rotated = tk.IntVar()
tk.Checkbutton(frm_options, text="rotated", variable=rotated).pack()
max_permutations = tk.IntVar()
tk.Checkbutton(frm_options, text="max_permutations", variable=max_permutations).pack()


# Button
btn_flip = tk.Button(
    frm_buttons,
    text="Begin",
    width=25,
    height=5,
    bg="green",
    font=("Courier", 14, 'bold'),
    fg="white",
    command=modify_images
).pack(padx=50, pady=10, side=tk.LEFT)

# pack frames
frm_options.pack(fill=tk.X, expand=True)
frm_buttons.pack(fill=tk.X, expand=True, side=tk.TOP)

window.mainloop()
