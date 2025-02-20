import cv2
import os
from stegano import lsb

def decrypt_message():
    img_path = input("Enter the encoded image path: ")
    if not os.path.exists(img_path):
        print("Error: Image file not found!")
        return

    try:
        hidden_data = lsb.reveal(img_path)
        if not hidden_data:
            print("Error: No hidden message found!")
            return

        password_input = input("Enter the password for decryption: ")
        stored_password, hidden_message = hidden_data.split('|', 1)

        if password_input == stored_password:
            print("Decrypted Message:", hidden_message)
        else:
            print("Incorrect password! Access Denied.")
    except:
        print("Error: Could not retrieve message. Ensure you selected the correct image.")

if __name__ == "__main__":
    decrypt_message()
