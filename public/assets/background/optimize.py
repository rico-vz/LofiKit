from PIL import Image
import os

# Get the current working directory
folder = os.getcwd()

# Set a counter for renaming the images
counter = 1

# Loop through all files in the folder
for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # If the filename only contains numbers, it's already been optimized (ignore the extension)
        if filename[:-4].isdigit():
            print("Skipping " + filename + "...")
            continue
        # Open the image
        img = Image.open(os.path.join(folder, filename))
        # Resize the image to 1080p
        img = img.resize((1920, 1080), Image.LANCZOS)
        # Save the optimized image with the new numbered name
        new_filename = str(counter) + ".jpg"
        img.save(os.path.join(folder, new_filename), format='JPEG', optimize=True)
        counter += 1
        # Delete file
        os.remove(os.path.join(folder, filename))