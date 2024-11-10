import tkinter as tk
from tkinter import filedialog
from rembg import remove
root = tk.Tk()




# Code to add widgets will go here...
# input box to input image files
def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.jpg"),("image files", "*.jpeg"),("image files", "*.png")])
    if file_path:
        input_path = file_path
        # service part
        input_fh=open(input_path,"rb")
        binary_content = input_fh.read()
        output_bin=remove(binary_content)
        output_fh=open(file_path[:file_path.rfind("/")]+"/removed.png","wb")
        output_fh.write(output_bin)
        print("Done")
	

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack(pady=100)
# image preview option
# button to click and remove background

root.mainloop()