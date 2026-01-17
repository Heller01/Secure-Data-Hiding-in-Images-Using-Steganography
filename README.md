# Secure Image Steganography Tool

This Python-based tool provides a user-friendly way to hide and retrieve text messages within images using the Least Significant Bit (LSB) steganography technique.  It includes a graphical user interface (GUI) and password protection for enhanced security.

## Features

*   **Image Steganography:** Embeds text messages within PNG, JPG, and JPEG image files.
*   **Password Protection:**  Secures hidden messages with a user-provided password, preventing unauthorized access.
*   **User-Friendly GUI:**  Provides a simple and intuitive graphical interface for image selection, message input, and data extraction.
*   **Multiple Image Format Support:** Works with common image formats, including PNG, JPG, and JPEG.

## Requirements

*   Python 3.13
*   Tkinter (usually included with Python)
*   OpenCV (cv2): `pip install opencv-python`
*   Pillow (PIL): `pip install Pillow`
*   stegano: `pip install stegano`

## How to Use

1.  **Clone the Repository (or download the script):**  [If you have a repository, include the cloning instructions here.  Otherwise, just mention downloading the script.]
2.  **Install Dependencies:** Open a terminal or command prompt and run the following command to install the required libraries:
    ```bash
    pip install opencv-python Pillow stegano
    ```
3.  **Run the Application:** Navigate to the directory where you saved the script (e.g., `steganography_app.py`) and run it using:
    ```bash
    python steganography_app.py
    ```
4.  **Using the GUI:**
    *   **Open Image:** Click the "Open Image" button to select the image file you want to use.
    *   **Enter Message:** Type your secret message in the text box.
    *   **Hide Data:** Click the "Hide Data" button. You'll be prompted to enter a password to encrypt the message.
    *   **Save Image:** Click the "Save Image" button to save the steganographic image (the image containing the hidden message).
    *   **Show Data:** Open the steganographic image using the "Open Image" button. Then, click "Show Data."  You'll be prompted for the password.  If the password is correct, the hidden message will be displayed in the text box.


## Author

Ayushman Maurya
