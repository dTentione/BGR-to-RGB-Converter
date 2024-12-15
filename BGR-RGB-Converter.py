import os
from tkinter import Tk, filedialog, messagebox, Label, Button, StringVar, Radiobutton
from PIL import Image

def convert_bgr_to_rgb(image_path, output_folder):
    """
    Converts a BGR PNG image to RGB and saves it to the output folder, preserving transparency.
    """
    try:
        img = Image.open(image_path)
        # Check if image has an alpha channel
        if img.mode == "RGBA":
            r, g, b, a = img.split()  # Split channels including alpha
            rgb_img = Image.merge("RGBA", (b, g, r, a))  # Rearrange RGB channels and keep alpha
        else:
            # Convert to RGB mode if necessary
            if img.mode != "RGB":
                img = img.convert("RGB")
            r, g, b = img.split()
            rgb_img = Image.merge("RGB", (b, g, r))

        # Save the image in the output folder
        base_name = os.path.basename(image_path)
        output_path = os.path.join(output_folder, base_name)
        rgb_img.save(output_path)
        return True
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return False

def convert_rgb_to_bgr(image_path, output_folder):
    """
    Converts an RGB PNG image to BGR and saves it to the output folder, preserving transparency.
    """
    try:
        img = Image.open(image_path)
        # Check if image has an alpha channel
        if img.mode == "RGBA":
            r, g, b, a = img.split()  # Split channels including alpha
            bgr_img = Image.merge("RGBA", (b, g, r, a))  # Rearrange RGB channels and keep alpha
        else:
            # Convert to RGB mode if necessary
            if img.mode != "RGB":
                img = img.convert("RGB")
            r, g, b = img.split()
            bgr_img = Image.merge("RGB", (b, g, r))

        # Save the image in the output folder
        base_name = os.path.basename(image_path)
        output_path = os.path.join(output_folder, base_name)
        bgr_img.save(output_path)
        return True
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return False

def select_files():
    """
    Opens a file dialog for the user to select PNG files.
    """
    file_paths = filedialog.askopenfilenames(
        title="Select PNG files",
        filetypes=[("PNG Files", "*.png")]
    )
    return file_paths

def select_output_folder():
    """
    Opens a folder dialog for the user to select an output folder.
    """
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    return folder_path

def process_images(conversion_mode):
    """
    Handles the conversion process: selects files, converts them, and saves the output.
    """
    files = select_files()
    if not files:
        messagebox.showwarning("No Files Selected", "Please select at least one PNG file.")
        return

    output_folder = select_output_folder()
    if not output_folder:
        messagebox.showwarning("No Output Folder Selected", "Please select an output folder.")
        return

    success_count = 0
    for file in files:
        if conversion_mode == "BGR to RGB":
            if convert_bgr_to_rgb(file, output_folder):
                success_count += 1
        elif conversion_mode == "RGB to BGR":
            if convert_rgb_to_bgr(file, output_folder):
                success_count += 1

    messagebox.showinfo(
        "Conversion Complete",
        f"Successfully converted {success_count} out of {len(files)} files."
    )

# Set up the GUI
root = Tk()
root.title("BGR and RGB Converter")
root.geometry("400x300")

# Conversion mode variable
conversion_mode = StringVar(value="BGR to RGB")

# Add labels and buttons
label = Label(root, text="Convert between BGR and RGB", font=("Arial", 14))
label.pack(pady=20)

bgr_to_rgb_button = Radiobutton(root, text="BGR to RGB", variable=conversion_mode, value="BGR to RGB", font=("Arial", 12))
bgr_to_rgb_button.pack()

rgb_to_bgr_button = Radiobutton(root, text="RGB to BGR", variable=conversion_mode, value="RGB to BGR", font=("Arial", 12))
rgb_to_bgr_button.pack()

convert_button = Button(root, text="Select and Convert PNGs", command=lambda: process_images(conversion_mode.get()), font=("Arial", 12))
convert_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=10)

# Start the main loop
root.mainloop()

