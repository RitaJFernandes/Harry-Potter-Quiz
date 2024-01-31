import tkinter as tk
import os, sys
from PIL import Image,ImageTk

'''Get absolute path for pyinstaller'''
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


'''Parent window'''
root = tk.Tk()
root.geometry('600x800')
root.title('Harry Potter Quiz')
root.config(bg='white')

def main():
    # All Next buttons that forget the current frame and packs the next one
    def Next1():
        if house.get() and len(player_name.get()) != 0:
            frame1.pack_forget()
            frame2.pack()
            
    def Next2():
        if Q1var.get():    
            frame2.pack_forget()
            frame3.pack()
            
    def Next3():    
        if Q2var.get():
            frame3.pack_forget()
            frame4.pack()
        
    def Next4():    
        if Q3var.get():
            frame4.pack_forget()
            frame5.pack()

    def Next5():
        if Q4var.get():    
            frame5.pack_forget()
            frame6.pack()

    def Next6():
        if Q5var.get():    
            frame6.pack_forget()
            frame7.pack()
                       
    # Gets player name
    def get_name():
        name = player_name.get()
        label_name = tk.Label(frame7, text=f'Congratulations {name}! You finished the quiz!', font=('Harry P', 30), bg='white')
        label_name.pack(pady=20)
            
    # Gets player's score and house
    def result_and_house():     
        score = 0
        if Q1var.get()==1:
            score = score+1
        if Q2var.get()==3:
            score = score+1
        if Q3var.get()==2:
            score = score+1
        if Q4var.get()==1:
            score = score+1
        if Q5var.get()==4:
            score = score+1
        score_label = tk.Label(frame7, text=f'You got {score}/5 correct answers!', font=('Harry P', 30), bg='white')
        score_label.pack()
            
        value = house.get()
        if value == 1:
            player_house = 'Gryffindor'
            pic = tk.Label(frame7, image=Gryffindor_pic, bg='white')
            pic.pack()        
        elif value ==2:
            player_house =  'Slytherin'
            pic = tk.Label(frame7, image=Slytherin_pic, bg='white')
            pic.pack()        
        elif value ==3:
            player_house = 'Ravenclaw'
            pic = tk.Label(frame7, image=Ravenclaw_pic, bg='white')
            pic.pack()      
        elif value ==4:
            player_house = 'Hufflepuff'
            pic = tk.Label(frame7, image=Hufflepuff_pic, bg='white')
            pic.pack()   
        player_house_label = tk.Label(frame7, text=f'\n{score*10} points to {player_house}', font=('Harry P', 30), bg='white')
        player_house_label.pack()

    # Restarts the program
    def restart():
        frame7.pack_forget()
        main()

    # Creates restart and close buttons in frame7
    def create_buttons():
        restart_button = tk.Button(frame7, text='restart', command=restart, font=('Harry P', 30))
        restart_button.pack(pady=50)
        close_button = tk.Button(frame7, text='close', command=root.destroy, font=('Harry P', 30))
        close_button.pack()

    # Frames to put questions in
    frame1 = tk.Frame(bg='white')
    frame1.pack()
    frame2 = tk.Frame(bg='white')
    frame3 = tk.Frame(bg='white')
    frame4 = tk.Frame(bg='white')
    frame5 = tk.Frame(bg='white')
    frame6 = tk.Frame(bg='white')
    frame7 = tk.Frame(bg='white')
          
    # Welcome label + image
    label1 = tk.Label(frame1, text='Welcome to the Harry Potter quiz!', font=('Harry P', 30), bg='white')
    img1 = ImageTk.PhotoImage(Image.open(resource_path('images/logo.png')))
    label1.grid(column=0, row=0, columnspan=2, pady=20)

    img1_label = tk.Label(frame1, image=img1, bg='white')
    img1_label.grid(column=0, row=1, columnspan=2)

    # VarVars
    player_name = tk.StringVar()
    house = tk.IntVar()
    
    # Player name
    label2 = tk.Label(frame1, text='\nWhat is your Wizard/Witch name?', font=('Harry P', 20), bg='white')
    label2.grid(column=0, row=2, columnspan=2)
    entry_name = tk.Entry(frame1, textvariable=player_name, width=20, font=('Times', 15), justify='center', bg='white')
    entry_name.grid(column=0, row=3, columnspan=2)

    # Player house
    label3 = tk.Label(frame1, text='\nPlease, select your house', font=('Harry P', 20), bg='white')
    label3.grid(column=0, row=4, columnspan=2)

    Gryffindor_pic = ImageTk.PhotoImage(Image.open(resource_path('images/Gryffindor.jpg')).resize((120,150)))
    Slytherin_pic = ImageTk.PhotoImage(Image.open(resource_path('images/Slytherin.jpg')).resize((120,150)))
    Ravenclaw_pic = ImageTk.PhotoImage(Image.open(resource_path('images/Ravenclaw.jpg')).resize((120,150)))
    Hufflepuff_pic = ImageTk.PhotoImage(Image.open(resource_path('images/Hufflepuff.jpg')).resize((120,150)))

    Gryffindor_button = tk.Radiobutton(frame1, variable=house, value=1, bg='white')
    Gryffindor_button.grid(row=5, column=0)
    Gryffindor = tk.Label(frame1, image=Gryffindor_pic, bg='white')
    Gryffindor.grid(row=6, column=0)

    Slytherin_button = tk.Radiobutton(frame1, variable=house, value=2, bg='white')
    Slytherin_button.grid(row=5, column=1)
    Slytherin = tk.Label(frame1, image=Slytherin_pic, bg='white')
    Slytherin.grid(row=6, column=1)

    Ravenclaw_button = tk.Radiobutton(frame1, variable=house, value=3, bg='white')
    Ravenclaw_button.grid(row=7, column=0)
    Ravenclaw = tk.Label(frame1, image=Ravenclaw_pic, bg='white')
    Ravenclaw.grid(row=8, column=0)

    Hufflepuff_button = tk.Radiobutton(frame1, variable=house, value=4, bg='white')
    Hufflepuff_button.grid(row=7, column=1)
    Hufflepuff = tk.Label(frame1, image=Hufflepuff_pic, bg='white')
    Hufflepuff.grid(row=8, column=1)

    # Questions, Answers and Options
    Q_A = {"What are the names of Harry's parents?":"James and Lily", "At what age Harry found to be a wizard?":11, "Which Wirzarding school did Harry attend?":'Gryffindor', "Who is Harry's best friend?":'Ron Weasley', "And where did they meet?":'Kings Cross Station'}

    OptionsQ1 = ['James and Lily', 'Arthur and Molly', 'Lucius and Narcisa', 'John and Mary']
    OptionsQ2 = [10, 13, 11, 12]
    OptionsQ3 = ['Ravenclaw', 'Gryffindor', 'Slytherin', 'Hufflepuff']
    OptionsQ4 = ['Ron Weasley', 'Draco Malfoy', 'Neville Longbottom', 'Luna Lovegood']
    OptionsQ5 = ['Hogwarts', 'Platform 9 3/4', 'Burrow', 'Kings Cross Station']

    # Labels for each question
    key = list(Q_A.keys())
    Q1label = tk.Label(frame2, text=key[0], bg='white', font=('Harry P', 30))
    Q2label = tk.Label(frame3, text=key[1], bg='white', font=('Harry P', 30))
    Q3label = tk.Label(frame4, text=key[2], bg='white', font=('Harry P', 30))
    Q4label = tk.Label(frame5, text=key[3], bg='white', font=('Harry P', 30))
    Q5label = tk.Label(frame6, text=key[4], bg='white', font=('Harry P', 30))

    img1_label2 = tk.Label(frame2, image=img1, bg='white')
    img1_label3 = tk.Label(frame3, image=img1, bg='white')
    img1_label4 = tk.Label(frame4, image=img1, bg='white')
    img1_label5 = tk.Label(frame5, image=img1, bg='white')
    img1_label6 = tk.Label(frame6, image=img1, bg='white')

    Q1label.pack(pady=20)
    img1_label2.pack()
    Q2label.pack(pady=20)
    img1_label3.pack()
    Q3label.pack(pady=20)
    img1_label4.pack()
    Q4label.pack(pady=20)
    img1_label5.pack()
    Q5label.pack(pady=20)
    img1_label6.pack()

    # Radiobuttons and VarVars for each question
    Q1var = tk.IntVar()
    Q2var = tk.IntVar()
    Q3var = tk.IntVar()
    Q4var = tk.IntVar()
    Q5var = tk.IntVar()

    for i in range(0,4):
        Q1buttons = tk.Radiobutton(frame2, text=OptionsQ1[i], font='Calibri 20', variable=Q1var, value=i+1, bg='white')
        Q2buttons = tk.Radiobutton(frame3, text=OptionsQ2[i], font='Calibri 20', variable=Q2var, value=i+1, bg='white')
        Q3buttons = tk.Radiobutton(frame4, text=OptionsQ3[i], font='Calibri 20', variable=Q3var, value=i+1, bg='white')
        Q4buttons = tk.Radiobutton(frame5, text=OptionsQ4[i], font='Calibri 20', variable=Q4var, value=i+1, bg='white')
        Q5buttons = tk.Radiobutton(frame6, text=OptionsQ5[i], font='Calibri 20', variable=Q5var, value=i+1, bg='white')
        Q1buttons.pack(pady=20)
        Q2buttons.pack(pady=20)
        Q3buttons.pack(pady=20)
        Q4buttons.pack(pady=20)
        Q5buttons.pack(pady=20)
     
    # Next buttons
    next1 = tk.Button(frame1, text='Next', width=10, height=1, font=('Harry P', 25), command=Next1)
    next1.grid(row=9, column=0, columnspan=2)
    
    next2 = tk.Button(frame2, text='Next', width=10, height=1, font=('Harry P', 25), command= Next2)
    next2.pack(pady=50)
    
    next3 = tk.Button(frame3, text='Next', width=10, height=1, font=('Harry P', 25), command= Next3)
    next3.pack(pady=50)
            
    next4 = tk.Button(frame4, text='Next', width=10, height=1, font=('Harry P', 25), command= Next4)
    next4.pack(pady=50)
          
    next5 = tk.Button(frame5, text='Next', width=10, height=1, font=('Harry P', 25), command= Next5)
    next5.pack(pady=50)
          
    next6 = tk.Button(frame6, text='Next', width=10, height=1, font=('Harry P', 25), command= lambda:[Next6(), get_name(), result_and_house(), create_buttons()])
    next6.pack(pady=50)

    root.mainloop()
    
main()
