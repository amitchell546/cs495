def create_window():
    # most of this stolen from class notes
    import tkinter as tk

    global win
    win = tk.Tk()
    win.geometry('640x480')

    global genLabel
    genLabel = tk.Label(win, text="Start typing! Press the button when finished.")
    genLabel.grid(row=0, column=0)
    win.mainloop


def save_file(name, saveText):
    #creating a function to save the user's writing

    # making sure they actually named the file
    if len(name) == 0:
        name = 'default'

    # finally we write the big string to the file
    with open(name, 'w') as file:
        file.write(saveText)


# got this code and learned about the Text method in tk
# from this website, https://www.geeksforgeeks.org/python-tkinter-text-widget/
def take_input():
    userText = textBox.get("1.0", "end-1c")
    return userText


if __name__ == '__main__':

    # importing tkinter to make a gui
    import tkinter as tk

    create_window()
    textBox = tk.Text(win)
    textBox.grid(row=1, column=0, columnspan=5)

    fileLabel = tk.Label(win, text='Type the name of your file here, if blank, file name is "default"')
    fileLabel.grid(row=2, column=0)

    fileInputVar = tk.StringVar()
    fileInput = tk.Entry(win, textvariable=fileInputVar)
    fileInput.grid(row=2, column = 2)

    def onclack():
        win.mainloop
        fileName = fileInputVar.get()
        save_file(fileName, take_input())

    saveButton = tk.Button(win, text="Save", command=onclack)
    saveButton.grid(row=2, column=3)

    win.mainloop()
