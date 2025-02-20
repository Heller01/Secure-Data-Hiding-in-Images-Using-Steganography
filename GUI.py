from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import cv2
import os
from PIL import Image, ImageTk
from stegano import lsb

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filename:
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img

def hide_message():
    global secret
    if 'filename' not in globals():
        messagebox.showerror("Error", "Please select an image first.")
        return
    
    message = text1.get(1.0, END).strip()
    if not message:
        messagebox.showerror("Error", "Please enter a message to hide.")
        return
    
    password = simpledialog.askstring("Password", "Enter a password for encryption:", show='*')
    if not password:
        messagebox.showerror("Error", "Password is required for encryption.")
        return
    
    encrypted_message = password + '|' + message  # Store password with message
    secret = lsb.hide(filename, encrypted_message)
    messagebox.showinfo("Success", "Message successfully hidden!")

def show_message():
    if 'filename' not in globals():
        messagebox.showerror("Error", "Please select an image first.")
        return
    
    try:
        hidden_data = lsb.reveal(filename)
        if not hidden_data:
            messagebox.showerror("Error", "No hidden message found!")
            return
    
        password_input = simpledialog.askstring("Password", "Enter the password for decryption:", show='*')
        stored_password, hidden_message = hidden_data.split('|', 1)
    
        if password_input == stored_password:
            text1.delete(1.0, END)
            text1.insert(END, hidden_message)
        else:
            messagebox.showerror("Error", "Incorrect password!")
    except:
        messagebox.showerror("Error", "Failed to retrieve message. Ensure the correct image is selected.")

def save_image():
    if 'secret' not in globals():
        messagebox.showerror("Error", "No hidden image to save.")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG file", "*.png"), ("All Files", "*.*")])
    if save_path:
        secret.save(save_path)
        messagebox.showinfo("Success", "Image saved successfully!")

root = Tk()
root.title("Steganography - Secure Text Hiding")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#2F4155")

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

Label(root, text="Secure Steganography", bg="#2F4155", fg="white", font="arial 25 bold").place(x=180, y=20)

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)
lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

f2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

Scrollbar1 = Scrollbar(f2)
Scrollbar1.place(x=320, y=0, height=300)
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

f3 = Frame(root, bd=3, bg="#2F4115", width=330, height=100, relief=GROOVE)
f3.place(x=10, y=370)
Button(f3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(f3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save_image).place(x=180, y=30)
Label(f3, text="Picture, Image, Photo File", bg="#2F4155", fg="yellow").place(x=20, y=5)

f4 = Frame(root, bd=3, bg="#2F4115", width=330, height=100, relief=GROOVE)
f4.place(x=360, y=370)
Button(f4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=hide_message).place(x=20, y=30)
Button(f4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show_message).place(x=180, y=30)
Label(f4, text="Picture, Image, Photo File", bg="#2F4155", fg="yellow").place(x=20, y=5)

root.mainloop()
