import os
import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

source_folder = r'C:\Users\renuka.tumati\git\zayo\Zayo_pytest_poc\utils\image_read\images'  

# Specify the destination folder where you want to save the text files
destination_folder = r'C:\Users\renuka.tumati\git\zayo\Zayo_pytest_poc\utils\image_read\images'
# Replace with the path to your destination text folder

# Ensure the destination folder exists, or create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Construct the full path of the source image file
        source_file = os.path.join(source_folder, filename)

        # Open the image file
        image = Image.open(source_file)

        # Perform OCR on the image to extract text
        text = pytesseract.image_to_string(image)

        # Construct the full path of the destination text file
        destination_file = os.path.join(destination_folder, os.path.splitext(filename)[0] + '.txt')

        # Write the extracted text to the destination text file
        with open(destination_file, "w") as text_file:
            text_file.write(text)

        print(f"Text extracted from {filename} and saved to {os.path.basename(destination_file)}")

print("Text extraction completed.")
