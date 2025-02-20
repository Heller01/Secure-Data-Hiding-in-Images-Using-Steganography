import cv2
import os
from stegano import lsb

def encrypt_message():
    img_path = input("Enter the image path: ")
    if not os.path.exists(img_path):
        print("Error: Image file not found!")
        return

    message = input("Enter secret message: ")
    password = input("Enter a password for encryption: ")

    encrypted_message = password + '|' + message
    secret = lsb.hide(img_path, encrypted_message)

    save_path = input("Enter the output image filename (with .png extension): ")
    secret.save(save_path)
    print("Message hidden successfully in:", save_path)

if __name__ == "__main__":
    encrypt_message()
