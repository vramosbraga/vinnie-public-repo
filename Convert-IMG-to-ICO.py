import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def convert_to_ico():
    # Get the selected image file path
    input_image_path = selected_image_path.get()
    if input_image_path:
        # Convert the image to .ico format
        output_ico_path = input_image_path.split(".")[0] + "-icone.ico"
        convert_image(input_image_path, output_ico_path)
        status_label.config(text="Image converted and saved as {}".format(output_ico_path), wraplength=300)

def convert_image(input_image_path, output_ico_path):
    # Open the input image
    image = Image.open(input_image_path)

    # Ensure the input image is in RGBA format
    image = image.convert("RGBA")

    # Create a new image with the correct size for .ico format
    ico_image = image.resize((256, 256), Image.LANCZOS)

    # Save the image as .ico format
    ico_image.save(output_ico_path, format="ICO")

def select_image():
    # Prompt the user to select an image file
    input_image_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if input_image_path:
        # Set the selected image path
        selected_image_path.set(input_image_path)

        # Update the image preview
        update_image_preview(input_image_path)

def update_image_preview(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Resize the image to fit the preview window
    width, height = 200, 200
    image = image.resize((width, height), Image.LANCZOS)

    # Convert the image to Tkinter PhotoImage format
    photo = ImageTk.PhotoImage(image)

    # Update the image preview label
    image_label.config(image=photo)
    image_label.image = photo

# Create the Tkinter application window
window = tk.Tk()
window.title("Image to .ico Converter")
window.geometry("450x450")
# Set the window icon
try:
    window.iconbitmap(r"path/to/icon.ico")  # Replace "path/to/icon.ico" with the actual path to your icon file
except:
    pass

# Create a label for displaying the selected image path
selected_image_path = tk.StringVar()
selected_image_path_label = tk.Label(window, textvariable=selected_image_path, wraplength=300)
selected_image_path_label.pack(pady=10)

# Create a button to select an image file
select_button = tk.Button(window, text="Select Image", command=select_image)
select_button.pack()

# Create an image preview label
image_label = tk.Label(window)
image_label.pack(pady=10)

# Create a button to convert the selected image to .ico
convert_button = tk.Button(window, text="Convert to .ico", command=convert_to_ico)
convert_button.pack(pady=10)

# Create a label to display the conversion status
status_label = tk.Label(window, text="conversion status")
status_label.pack()

# Run the Tkinter event loop
window.mainloop()
