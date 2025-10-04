import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

root = tk.Tk()
root.title('Моя програма')
root.geometry("500x400")
name_label = tk.StringVar()

label = tk.Label(root, text="Введіть ваше ім'я", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

def get_name():
    text = entry.get()
    name_label.set("Name: " + text)

#button
get_name_button = tk.Button(root, text="Отримати ім'я", command=get_name)
get_name_button.pack()

label2 = tk.Label(root, textvariable=name_label, font=("Arial", 14))
label2.pack(pady=10)

text_widget = tk.Text(root, height=5, width=40)
text_widget.pack(pady=5)

check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text='Згідний', variable=check_var)
checkbox.pack(pady=5)

def show_message():
    messagebox.showwarning('Інформація', 'Це інформаційне вікно')
mb_button = tk.Button(root, text="Message", command=show_message)
mb_button.pack(pady=5)


# start program
root.mainloop()