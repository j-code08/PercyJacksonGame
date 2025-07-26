import tkinter as tk

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
        
def pick_one():
    print("You picked choice 1!")

def pick_two():
    print("You picked choice 2!")

def pick_three():
    print("You picked choice 3!")

def choice_frame(root, labeltext, choice1, choice2, choice3, command1, command2, command3):
    root.title('demo')
    root.geometry('1000x600')
    root.config(bg='#113F67')


    label = tk.Label(root,
                 text=labeltext,
                 font=('norse', 25),  
                 fg='#FDF5AA',
                 bg='#113F67',
                 wraplength=800, # Wrap text at 800 pixels
                 justify='center') # Align text to the center

    label.pack(padx=100, pady=100)

    frame = tk.Frame(root, bd=5, relief='sunken', bg='#34699A')
    frame.pack()

    button1 = tk.Button(frame,
                        text=choice1,
                        command=command1,
                        width=50,
                        font=('fixedsys', 16),
                        bd=5, relief='raised',
                        activebackground='#6DA589',
                        bg='#005c5b',
                        fg='#F1BB5C')
    button1.grid(sticky='nsew',pady=2,padx=5)

    button2 = tk.Button(frame,activebackground='#6DA589',
                        bg='#005c5b',
                        fg='#F1BB5C',bd=5, relief='raised', text=choice2, command=command2, width=50, font=('fixedsys', 16))
    button2.grid(sticky='nsew',pady=2,padx=5)

    button3 = tk.Button(frame,activebackground='#6DA589',
                        bg='#005c5b',
                        fg='#F1BB5C', bd=5, relief='raised', text=choice3, command=command3, width=50, font=('fixedsys', 16))
    button3.grid(sticky='nsew',pady=2,padx=5)

def scene1():
    clear_window()

    choice_frame(root,
           "Miss Dodds’ wings burst from her back. \n‘You stole the bolt, thief!’\n Her claws gleam under the streetlights. What do you do?",
           'Fight Barehanded (HP Check)',
           "Use Riptide (MP Cost: 5)",
           "Beg for Mercy (Aura Check)",
           pick_one,
           pick_two,
           pick_three)


def start():
    startlabel = tk.Label (root, text='Percy Jackson\n Game', font=('norse', 30))
    startlabel.pack()
    startbutton = tk.Button (root, text='Start', 
                             font=('fixedsys',15),
                            command=scene1)
    startbutton.pack()
    

# Main program
root = tk.Tk()

start()

root.mainloop()