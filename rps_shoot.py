
import tkinter as tk
from random import choice

def choice_frame(labeltext, choice1, choice2, choice3, command1, command2, command3):
    clear_window()
    label = tk.Label(root,
                 text=labeltext,
                 font=('Norse', 25),  #downloaded font
                 fg='#FDF5AA',
                 bg='#113F67',
                 wraplength=800, # Wrap text at 800 pixels
                 justify='center') # Align text to the center

    label.pack(padx=50, pady=50)

    frame = tk.Frame(root, bd=5, relief='sunken', bg='#34699A')
    frame.pack()

    button1 = tk.Button(frame,
                        text=choice1,
                        command=command1,
                        width=25, #width of buttom
                        font=('fixedsys', 16),
                        bd=5, relief='raised',
                        activebackground='#6DA589',
                        bg='#005c5b',
                        fg='#F1BB5C')
    button1.grid(sticky='nsew',pady=2,padx=5)

    button2 = tk.Button(frame,activebackground='#6DA589',
                        bg='#005c5b',
                        fg='#F1BB5C',bd=5, relief='raised', text=choice2, command=command2, width=25, font=('fixedsys', 16))
    button2.grid(sticky='nsew',pady=2,padx=5)

    button3 = tk.Button(frame,activebackground='#6DA589',
                        bg='#005c5b',
                        fg='#F1BB5C', bd=5, relief='raised', text=choice3, command=command3, width=25, font=('fixedsys', 16))
    button3.grid(sticky='nsew',pady=2,padx=5)

def clear_window(): #clears the window to create new window
    for widget in root.winfo_children(): #list of widgets
        widget.destroy()

def rock():
    clear_window()

    l=['👊', '📃', '✂']
    
    CompChoice=choice(l)

    label=tk.Label(root, text=CompChoice,font=('Arial',60),bg='#113F67',fg='#FDF5AA')
    label.pack()

    if CompChoice=='📃':
        labelOutCome=tk.Label(root, text='You Lose',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    elif CompChoice=='✂':
        labelOutCome=tk.Label(root, text='You Win',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    else:
        labelOutCome=tk.Label(root, text='Draw',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    labelOutCome.pack()

    restartbutton=tk.Button(root, text='Restart', font=('fioxedsys', 15), command=restart)
    restartbutton.pack()


def paper():
    clear_window()

    l=['👊', '📃', '✂']
    
    CompChoice=choice(l)

    label=tk.Label(root, text=CompChoice,font=('Arial',60),bg='#113F67',fg='#FDF5AA')
    label.pack()

    if CompChoice=='📃':
        labelOutCome=tk.Label(root, text='Draw',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    elif CompChoice=='✂':
        labelOutCome=tk.Label(root, text='You Lose',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    else:
        labelOutCome=tk.Label(root, text='You Win',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    labelOutCome.pack()

    restartbutton=tk.Button(root, text='Restart', font=('fioxedsys', 15), command=restart)
    restartbutton.pack()

def scissors():
    clear_window()

    l=['👊', '📃', '✂']
    
    CompChoice=choice(l)

    label=tk.Label(root, text=CompChoice,font=('Arial',60),bg='#113F67',fg='#FDF5AA')
    label.pack()

    if CompChoice=='📃':
        labelOutCome=tk.Label(root, text='You Win',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    elif CompChoice=='✂':
        labelOutCome=tk.Label(root, text='Draw',font=('fixedsys', 25),bg='#113F67',fg='#FDF5AA')

    else:
        labelOutCome=tk.Label(root, text='You lose',font=('fixedsys', 25),bg='#113F67', fg='#FDF5AA')

    labelOutCome.pack()

    restartbutton=tk.Button(root, text='Restart', font=('fioxedsys', 15), command=restart)
    restartbutton.pack()


def restart():
    clear_window()

    choice_frame('Rock, Paper, \nScissors, SHOOT!',
             '👊','📃', '✂', rock, paper, scissors)

        

    


root=tk.Tk()
root.geometry('400x400')
root.title('RPS game')
root.config(bg='#113F67')

choice_frame('Rock, Paper, \nScissors, SHOOT!',
             '👊','📃', '✂', rock, paper, scissors)


root.mainloop()


