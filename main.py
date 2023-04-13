from tkinter import *
from PIL import Image, ImageTk

# Define the recoloring function
def recolor_image():
    # Load the original image
    img = Image.open("image.png")

    # Get the RGB values from the sliders
    r = int(red_slider.get())
    g = int(green_slider.get())
    b = int(blue_slider.get())

    # Recolor the image using the new RGB values
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        if item[3] == 0:
            new_data.append(item)
        else:
            new_data.append((r, g, b, item[3]))
    img.putdata(new_data)

    # Display the new image in the GUI
    tk_img = ImageTk.PhotoImage(img)
    output_image.configure(image=tk_img)
    output_image.image = tk_img

    # Save the repainted image
    img.save("image_repainted.png")

# Create the Tkinter GUI
root = Tk()
root.title("Recolor Image")

# Load the original image and display it in the GUI
original_img = Image.open("image.png")
tk_original_img = ImageTk.PhotoImage(original_img)
original_image = Label(root, image=tk_original_img)
original_image.grid(row=0, column=0, padx=10, pady=10)

# Create the sliders for adjusting the color values
red_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL, label="Red", length=200)
red_slider.set(128)
red_slider.grid(row=0, column=1, padx=10, pady=10)

green_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL, label="Green", length=200)
green_slider.set(128)
green_slider.grid(row=1, column=1, padx=10, pady=10)

blue_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL, label="Blue", length=200)
blue_slider.set(128)
blue_slider.grid(row=2, column=1, padx=10, pady=10)

# Create the button for recoloring the image
recolor_button = Button(root, text="Recolor", command=recolor_image)
recolor_button.grid(row=3, column=1, padx=10, pady=10)

# Create the label for the output image preview
output_image = Label(root)
output_image.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

root.mainloop()
