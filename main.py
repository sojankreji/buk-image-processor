from PIL import Image 
import os

def convert_to_gray(file_name):
    print(file_name)
    image_file = Image.open("in/Recept/"+file_name) # open colour image
    image_file = image_file.convert('LA') # convert image to black and white
    image_file = image_file.convert("RGB")
    image_file.save("out/Recept/"+file_name)


directory = os.fsencode("in/Recept")
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jpg") or filename.endswith(".png"): 
         convert_to_gray(filename)
     else:
         continue

