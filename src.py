import tkinter as tk
from tkinter import PhotoImage

# ----------------------------- #
#         WINDOW SETUP         #
# ----------------------------- #

root = tk.Tk()
root.title('PJO GAME')
root.geometry('1000x600')
root.config(bg='#113F67')


# ----------------------------- #
#         START SCREEN         #
# ----------------------------- #

def start():
    # Start screen
    startlabel = tk.Label (root, text='Percy Jackson\n 𓆝𓆟༝˚｡⋆𓆉︎⋆｡˚༝𓆞𓆝 \n Game',
                           fg='#F1BB5C',
                           bg='#113F67',
                           justify='center',
                           font=('norse', 50))
    
    startlabel.pack(padx=70, pady=100)
    
    startbutton = tk.Button (root, text='Start',
                             font=('fixedsys',15),
                             bd=5, relief='raised',
                             activebackground='#6DA589',
                             bg='#005c5b',
                             fg='#F1BB5C',
                             width=25,
                             command=percy_dialogue)
    startbutton.pack()


# ----------------------------- #
#         MAIN DIALOGUE        #
# ----------------------------- #

def percy_dialogue():
    clear_window()

    dialogue_frame = tk.Frame(root, bd=3,
                              relief='sunken',
                              width=700,bg='#34699A',
                              height=300)
    
    
    dialogue_frame.pack(pady=180)
    dialogue_frame.grid_propagate(False) #to make a non resizable frame
    
    
    image = PhotoImage(file='percy_jackson_100x100.png')

    image_label= tk.Label(dialogue_frame,image=image)
    image_label.grid(sticky='nw')

    
    
    label = tk.Label(dialogue_frame,
                     text='I love Blue Waffles!!\nI love annabeth <3',
                     compound='top',
                     font=('norse', 20),  #downloaded font
                     fg='#FDF5AA',
                     bg='#005c5b',
                     width=59,
                     wraplength=400,
                     justify='left',
                     anchor='w') #aligns text to the west
    
    image_label.image = image  #a reference to avoid garbage collection
    label.grid(sticky='sw',pady=10, padx=20)

    next_button = tk.Button(dialogue_frame,
                            text='Next',
                            command = scene1,
                            font=('fixedsys',),
                            bd=5, relief='raised',
                            activebackground='#6DA589',
                            bg='#005c5b',
                            fg='#F1BB5C')
    next_button.grid(sticky='se',padx=5)


# ----------------------------- #
#         CHOICE SCENE         #
# ----------------------------- #

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


# ----------------------------- #
#         CHOICE FRAME         #
# ----------------------------- #

def choice_frame(root, labeltext, choice1, choice2, choice3, command1, command2, command3):
    clear_window()
    label = tk.Label(root,
                 text=labeltext,
                 font=('Norse', 25),  #downloaded font
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
                        width=50, #width of buttom
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


# ----------------------------- #
#       CHOICE HANDLERS        #
# ----------------------------- #

def pick_one():
    print("NO! You noodle arms")

def pick_two():
    print("Ha! Like YOU could lol")

def pick_three():
    print("The only thing your good at (- <)!")


# ----------------------------- #
#       HELPER FUNCTIONS       #
# ----------------------------- #

def clear_window(): #clears the window to create new window
    for widget in root.winfo_children(): #list of widgets
        widget.destroy()


# ----------------------------- #
#         RUN THE GAME         #
# ----------------------------- #

start()
root.mainloop()




