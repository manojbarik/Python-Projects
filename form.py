import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Required for images

root = tk.Tk()
root.title("Student Form")

# Note: .ico files are for Windows. On Mac, we usually skip this 
# or use a .png/.gif with root.iconphoto()
# root.iconbitmap("pixel2.ico") # Commented out to prevent Mac errors

root.geometry('500x500+0+0')
root.configure(background="#C4E8DC")

# Image handling - Ensure 'star.png' is in the SAME folder as this script
try:
    img = Image.open('star.png')
    resize_img = img.resize((100, 70))
    img_tk = ImageTk.PhotoImage(resize_img)
    img_label = tk.Label(root, image=img_tk, bg='#00704A')
    img_label.pack(pady=10, padx=20)
except Exception as e:
    print(f"Image not found: {e}")

# Text labels
text_label = tk.Label(root, text="Giet Bucks", font=('Arial', 18, 'bold'), bg='#00704A', fg='white')
text_label.pack(pady=10, padx=20)

email_label = tk.Label(root, text="Email", font=('Arial', 18, 'bold'), bg='#00704A', fg='white')
email_label.pack(pady=(20, 5))

# Note: bg/fg on Mac Entry widgets can sometimes look different than Windows
email_entry = tk.Entry(root, font=('Arial', 18), fg='black', bg='white')
email_entry.pack(pady=(5, 10))

password_label = tk.Label(root, text="Password", font=('Arial', 18, 'bold'), bg='#00704A', fg='white')
password_label.pack(pady=(20, 5))

password_entry = tk.Entry(root, font=('Arial', 18), show="*", fg='black', bg='white')
password_entry.pack(pady=(5, 10))

login_btn = tk.Button(root, text="Login", font=('Arial', 18, 'bold'))
login_btn.pack(pady=(5, 10))

root.mainloop()