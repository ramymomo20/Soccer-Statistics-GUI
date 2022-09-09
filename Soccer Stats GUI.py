from tkinter import * 
from tkinter.messagebox import showinfo
from gui_logic import *
import collections
collections.Callable = collections.abc.Callable


root = Tk()
root.geometry("500x500")
frame = Frame(root)
frame.pack()

selections = ('English Premier League','La Liga', 'Ligue 1', 
            'Bundesliga', 'Serie A', 'Eredivisie', 'Russian League', 
            'Liga Primera', 'Super Lig')

selection_var = StringVar(value=selections)
tablestr = StringVar()
scorerstr = StringVar()

def you_selected(event):
    label1 = Entry(root, borderwidth=2,relief=RIDGE,width=35,justify='center')
    label1.configure(text = '', font = 'arial 8 italic bold')
    label1.place(x=141,y=295)
    label1.config(state='readonly')

    selected_indice = listbox.curselection()

    global indice
    indice = int(selected_indice[0])+1
    
    selected = ",".join([listbox.get(i) for i in selected_indice])
    txt = f"You Selected: {selected}"

    label1.config(state='normal')
    label1.insert("end",txt)
    label1.config(state=DISABLED)

      
    

def goal_on_click():
    newWindow = Toplevel(root)
    newWindow.title("Top Goalscorers")
    newWindow.geometry("650x650")

    widget = Text(newWindow,width=65,height=26)
    widget.insert('end',(Scorers.getScorers(indice)))
    widget.pack()

    #Button(newWindow,command=alltop,borderwidth=1,relief=RIDGE, text = "All Top GoalScorers", font="Arial 8 italic", bg='lightblue', fg='black', activebackground="teal",padx=25, pady=10 ).place(x=151,y=400)
    

def table_on_click():
    newWindow1 = Toplevel(root)
    newWindow1.title("League Table")
    newWindow1.geometry("850x850")

    widget1 = Text(newWindow1,width=98,height=22)
    widget1.insert('end',(Start.gettable(indice)))
    widget1.pack()


root.title("Soccer Statistics of Europe's Big Leagues") 

label1 = Label(root,text = "Welcome!\n\n We will provide to you statistics from the Top Leagues in Europe!",justify='center',font='arial 9 bold') 
label1.pack(pady=15)
label2 = Label(root,text = "Choose the League to Analyze:",justify='center',font='arial 10')  
label2.pack(pady=10)  

listbox = Listbox(root,height= 9,justify='center',listvariable=selection_var,selectmode='browse',width=25)  
listbox.pack()
listbox.bind('<<ListboxSelect>>', you_selected)


leaguetable = Button(root,command=table_on_click,borderwidth=1,relief=RIDGE, text = "League Table", font="Arial 11 italic", bg='lightblue', fg='black', activebackground="teal", padx=10, pady=10 ).pack(side='right',padx=60)
goalscorer = Button(root,command=goal_on_click,borderwidth=1,relief=RIDGE, text = 'Top Goalscorers', font="Arial 11 italic", bg='lightblue', fg='black', activebackground="teal", padx=10, pady=10 ).pack(side='left',padx=60)

root.mainloop()