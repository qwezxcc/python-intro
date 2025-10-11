import tkinter as tk


def click(event):


    text = event.widget.cget('text')
    print(text)
    if text == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)


        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Неправильний вираз')
    elif text == 'Del':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END. text)

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entry = tk.Entry(root, font=('Arial', 20), justify="right", borderwidth=5)


entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/', 'Del'],
    ['4', '5', '6', '*', ')'],
    ['1', '2', '3', '-', '('],
    ['0', ',', '%', '+', '='],
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')

    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font=('Arial', 18), relief="ridge", borderwidth=2)


        button.pack(side="left", expand=True, fill='both')
        button.bind('ju', click)



root.mainloop()