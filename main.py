from tkinter import *

root = Tk()
root.title(" To-Do List ")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasks.txt", "w") as file:
            for task in task_list:
                file.write(f"{task}\n")  
    listbox.delete(ANCHOR)

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tasks.txt", "a") as file:
            file.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def openTaskFile():
    try:
        global task_list
        with open("tasks.txt", "r") as file:
            for task in file:
                if(task != '\n'):
                    task_list.append(task)
                    listbox.insert(END, task)
    except:
        file=open("tasks.txt", "w")
        file.close()



# icon
image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False, image_icon)

# top bar
top_image = PhotoImage(file="images/topbar.png")
Label(root, image=top_image).pack()

# dock
dock_image = PhotoImage(file="images/dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

# note
note_image = PhotoImage(file="images/task.png")
Label(root, image=note_image, bg="#32405b").place(x=30, y=25)

# heading
heading = Label(root, text="ALL TASKS", font=(
    "Arial", 20, "bold"), bg="#32405b", fg="#ffffff")
heading.place(x=130, y=20)

# main frame
frame = Frame(root, width=400, height=50, bg="#ffffff")
frame.place(x=0, y=100)
task = StringVar()
task_entry = Entry(frame, width=18, font=(
    "Arial", 15), bd=0, textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

# listbox
listbox_frame = Frame(root, bd=3, width=700, height=500, bg="#32405b")
listbox_frame.pack(pady=(160, 0))

listbox = Listbox(listbox_frame, width=40, height=16, font=("Arial", 12), bd=0, bg="#32405b",
                  fg="#ffffff", highlightthickness=0, cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# delete task
delete_icon = PhotoImage(file="images/delete.png")
Button(root, image=delete_icon, bd=0,command=deleteTask).pack(side=BOTTOM, pady=13)


# button
button = Button(frame, text="Add Task", font=("Arial", 15),
                width=10, bd=0, bg="#32405b", fg="#ffffff", command=addTask)
button.place(x=250,y=0)


root.mainloop()
