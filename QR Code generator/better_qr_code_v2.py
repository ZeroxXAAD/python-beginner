import customtkinter, qrcode, os
from pathlib import Path
from PIL import ImageTk, Image

#global check message
check = None

#global error message
error = None

#global error2 message
error_2 = None

#global error length message
error_length = None

#generation function
def generation():
    global check, error, error_length, display_window, error_2
    website_link = get_text()
    #qr code size
    qr = qrcode.QRCode(box_size = 5, border = 5)
    #check for length to display an error message if the text is too long to put in a qrcode
    if len(website_link)<2331:
        qr.add_data(website_link)
        qr.make()
    else:
        error_length = customtkinter.CTkLabel(app, text="The text is too long to encode in a QR code.")
        error_length.pack(pady=20)
            
    #show the colors
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    
    # Get the path to the user's Downloads folder
    downloads_path = str(Path.home() / "Downloads")
    
    #gets name of file written by user
    name = get_name()
    
    #invalid characters list
    invalid_chars = r'\/:*?"<>|'
    
    #defines
    file_path = os.path.join(downloads_path, f'{name}.png')
    
    #destroys previous error messages
    for widget in [check, error, error_2, error_length]:
        if widget:
            widget.destroy()
    
    #check if wrong character in name file
    if any(char in name for char in invalid_chars):
        error_2 = customtkinter.CTkLabel(app, text = '''File name cannot contain the following characters : \/:*?"<>|''')
        error_2.pack()
    #check if a file with same name as the one about to be generated already exists, to avoid deleting a random .png on the user pc
    if os.path.exists(file_path):
        error = customtkinter.CTkLabel(app, text="A file with this name already exists! Please put in another name or delete the previous file!")
        error.pack()
    else:
        # Save the QR code image to the Downloads folder
        img.save(os.path.join(file_path))
        #check message
        check = customtkinter.CTkLabel(app, text=f"QR Code saved in your download file as {name}.png")
        check.pack()

        #checkbox for qr code showing in new window
        if check_var.get():
            display_window = customtkinter.CTkToplevel(app)
            display_window.title(f"{name}.png")
            display_window.geometry("300x300")
            #makes the qr code window appear on top right after generating
            display_window.lift()
            display_window.attributes('-topmost', True)
            display_window.after_idle(display_window.attributes, '-topmost', False)
            #detect the version of qrcode
            version = qr.version
            #get the image
            img = Image.open(file_path)
            base_size = 250
            scale_factor = version/15
            if scale_factor>1:
                scaled_size = int(base_size*scale_factor)
            else:
                scaled_size = base_size
            #scales the window size so that its 50 pixels bigger than the qrcode size
            scaled_window = scaled_size + 50
            img = img.resize((scaled_size, scaled_size))
            img = ImageTk.PhotoImage(img)
            display_window.geometry(f"{scaled_window}x{scaled_window}")
            #display the image
            image = customtkinter.CTkLabel(display_window, text="", image=img)
            image.pack(pady=20, expand=True)
            
    

#gettext function
def get_text():
    link = entry.get()
    return link

#getname function
def get_name():
    name = entry_2.get()
    return name

#creates app
app = customtkinter.CTk()
app.geometry("600x400")
app.title("QR Code Generator")

#description text
description = customtkinter.CTkLabel(app, text="Enter the link or text that you want to turn into a QR Code!")
description.pack(pady=10)

#length warning message
warning = customtkinter.CTkLabel(app, text="WARNING : Max length generable is around 2300 characters")
warning.pack(pady=10)

#entry of link
entry = customtkinter.CTkEntry(app, width=500)
entry.pack()

#description text 2
description_2 = customtkinter.CTkLabel(app, text="Enter the name you want your file to be saved as")
description_2.pack(pady=20)

#entry of name
entry_2 = customtkinter.CTkEntry(app, width=500)
entry_2.pack(pady=10)

#check variable
check_var = customtkinter.BooleanVar()
display_checkbox = customtkinter.CTkCheckBox(app, text = "Display generated QR Code", variable = check_var)
display_checkbox.pack(pady=10)

#button start
button = customtkinter.CTkButton(app, command=generation, text="Generate QR Code")
button.pack(pady=10)


app.mainloop()