import cv2
import os
import string

# Load the image (ensure the path is correct)
img = cv2.imread("/Users/raghu/Downloads/Stenography-main/photo.jpg")  # Replace with the correct image path

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

# Create dictionaries for encoding and decoding
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Define the initial indices for image manipulation
m = 0
n = 0
z = 0

# Embed the secret message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3  # Wrap the channel index (z) for RGB

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Use 'open' to open the image on macOS (instead of 'start' on Windows)
os.system("open encryptedImage.jpg")  # macOS command to open the file

# Ask for the passcode to decrypt
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    # Decrypt the message from the image
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Wrap the channel index (z) for RGB
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
