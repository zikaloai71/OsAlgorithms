
from tkinter import * 
from tkinter import ttk

from tkinter import messagebox
import matplotlib.pyplot as plt


from DMA import DMA
from RMA import RMA



class UI:
    def __init__(self):
        #create tkinter window
        self.root = Tk()    
        #title of window
        self.root.title("Os Project")
#        name of tinker object we create prefer name it with your project name concatenated with your name 
        self.root.geometry("530x500+400+100")
        self.root.config(bg="red")

        self.inputFrame = Frame(self.root, bg="#DDDDDD")
        self.inputFrame.pack(fill=X)
        self.inputFrame.columnconfigure(0, weight=2)
        self.inputFrame.columnconfigure(6, weight=2)

        self.rtEntries = []   #  to enter release time 
        self.ptEntries = []  #  to enter periodic time 
        self.etEntries = []   #  to enter execution time 
        self.dtEntries = []    #  to enter deadline  time 
        self.tasks =[]   #   to enter no. of tasks 
        
#        grid    show grid composed of table with no. of rows and no.of column
        self.algorithm_type = StringVar()
        Label(self.inputFrame, text="No.Tasks: ", font=("times new roman", 12, "bold"), bg="#DDDDDD").grid(row=1, column=1, pady=5)
        Label(self.inputFrame, text= "Scheduling type: ", font=("times new roman", 12, "bold"), bg="#DDDDDD").grid(row=2,column=1,pady=5)  

        self.algorithm_chosen = ttk.Combobox(self.inputFrame,width=12, textvariable=self.algorithm_type)
        self.algorithm_chosen['value']=( "MLF", "EDF", "DMA", "RMA")
        self.algorithm_chosen.grid(row=2,column=2,pady=5)
        self.algorithm_chosen.current(0)
        self.algorithm_type.set("MLF")


#       bg background color, fg font color, pad  for padding y direction as canvas composed of x , y 
        self.useAlgorithm = 0
        Button(self.inputFrame, text="submit", font=("times new roman", 10), bg="green", fg="white", command= self.set_algorithm_type).grid(row=3, column=2, pady=5)
      

        self.noTasks = IntVar()
#        Tkinter contains built-in programming types which work like a normal python type with additional features used to manipulate values of widgets like Label and Entry more effectively, which makes them different from python data types.
        self.noTasks.set(0)

        self.numberOfTasks= Entry(self.inputFrame , validate="key", validatecommand=(self.inputFrame.register(self.validate_input_noTasks), '%P'), textvariable=self.noTasks, font=("times new roman", 12))
#        declare inputs for this tab
        self.numberOfTasks.grid(row=1, column=2, pady=5)
        self.numberOfTasks.config(bg="gray", fg="white", justify=CENTER)
        self.tasksFrame()


        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.mainloop()
   
    def validate_input_noTasks(input_string):
        if int(input_string):
            return True
        elif input_string == "":
            return True
        else:
            return False

    def get_input_noTasks(self):
        input_str = self.numberOfTasks.get()
        if input_str == "":
            return 0
        else:
            return int(input_str)
    
    def set_algorithm_type(self):
        if self.algorithm_type.get() == "MLF":
            self.MLF()
        elif self.algorithm_type.get() == "EDF":
            self.EDF()
        elif self.algorithm_type.get() == "DMA":
            self.DMA()
        elif self.algorithm_type.get() == "RMA":
            self.RMA()
        else:
            self.errorMessage("please choose an algorithm to use.")    
        self.refresh()
#        stop execution of python program

    def exit(self):
        self.root.quit()
        self.root.destroy()

    def MLF(self):
        self.algorithmUsed.config(text="Algorithm: Minimum Laxity First")
        self.useAlgorithm = 1

    def EDF(self):
        self.algorithmUsed.config(text="Algorithm: Earliest Deadline First")
        self.useAlgorithm = 2

    def DMA(self):
        self.algorithmUsed.config(text="Algorithm: Deadline Monotonic Assignment")
        self.useAlgorithm = 3

    def RMA(self):
        self.algorithmUsed.config(text="Algorithm: Rate Monotonic Assignment")
        self.useAlgorithm = 4

    def tasksFrame(self):
        my_canvas = Canvas(self.root, bg="#2069e0")
        my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add A Scrollbar To The Canvas
        my_scrollbar = Scrollbar(self.root, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.itemconfig('frame', width=my_canvas.winfo_width()))

        # Create ANOTHER Frame INSIDE the Canvas
        self.second_frame = Frame(my_canvas, bg="#444444")
        self.second_frame.columnconfigure(2, weight=2)

        self.algorithmUsed = Label(self.second_frame, text="Algorithm: ", font=("times new roman", 14, "bold"), bg="#444444", fg="#8C5ADF")
        self.algorithmUsed.pack()

        self.runFrame = Frame(self.second_frame, bg="#444444")
        Button(self.runFrame, text="RUN", font=("times new roman", 13, "bold"), bg="green", fg="white", bd=0, command= self.Run).pack(side=RIGHT, padx=5, pady=5)

        Label(self.runFrame, text="Max Time:", font=("times new roman", 12), bg="#444444", fg="white").pack(side=LEFT, padx=5, pady=5)

        self.maxtimeEntry = Entry(self.runFrame, font=("times new roman", 12), justify= CENTER)
        self.maxtimeEntry.pack(side=LEFT, padx=5, pady=5)
        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw", tags='frame')

        self.second_frame.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    def task(self, num):
        self.runFrame.pack_forget()
        f = Frame(self.second_frame, bg="#4AA080")
        f.pack(fill=X, expand=True,pady=5)
        self.tasks.append(f)
        Label(f, text=f"Task no.{num}", font=("times new roman", 12, "bold"), bg="#4AA080", fg="white").grid(row=0, column=0)
        Label(f, text="_____________________________________________________________________________________________________", bg="#4AA080", fg="white").grid(row=1, column=0)

        f2 = Frame(f, bg="#4AA080")
        f2.grid(row=2, column=0)
        f2.columnconfigure(0, weight=2)

        Label(f2, text= "Release time: ", font =("times new roman", 12), bg="#4AA080", fg="white").grid(row=0, column=1)
        rtEntry = Entry(f2, font=("times new roman", 12), justify= CENTER)
        rtEntry.grid(row=0, column=2)
        self.rtEntries.append(rtEntry)

        Label(f2, text= "Execution time: ", font =("times new roman", 12), bg="#4AA080", fg="white").grid(row=1, column=1)
        etEntry = Entry(f2, font=("times new roman", 12), justify= CENTER)
        etEntry.grid(row=1, column=2)
        self.etEntries.append(etEntry)

        Label(f2, text= "Period: ", font =("times new roman", 12), bg="#4AA080", fg="white").grid(row=0, column=3)
        ptEntry = Entry(f2, font=("times new roman", 12), justify= CENTER)
        ptEntry.grid(row=0, column=4)
        self.ptEntries.append(ptEntry)

        Label(f2, text="Deadline: ", font=("times new roman", 12), bg="#4AA080", fg="white").grid(row=1, column=3)
        dtEntry = Entry(f2, font=("times new roman", 12), justify= CENTER)
        dtEntry.grid(row=1, column=4)
        self.dtEntries.append(dtEntry)
        Label(f, text="_____________________________________________________________________________________________________", bg="#4AA080", fg="white").grid(row=3, column=0)
        self.runFrame.pack()



    def refresh(self, *args):
        
        tasksNum = self.get_input_noTasks()

        if tasksNum == len(self.tasks):
            pass
        if tasksNum > len(self.tasks):  #add more tasks
            for i in range(len(self.tasks)+1, tasksNum+1):
                self.task(i)
        else:
            for i in range(len(self.tasks)-tasksNum): #remove some tasks
                self.tasks.pop(-1).destroy()
                self.rtEntries.pop(-1)
                self.etEntries.pop(-1)
                self.ptEntries.pop(-1)
                self.dtEntries.pop(-1)

        if tasksNum == 0:
            self.runFrame.pack_forget()

    def Run(self):
        tasks = []
       
        try:
            maxtime = int(self.maxtimeEntry.get())
        except:
            self.errorMessage("Please ensure that the max time is an integer number")


        if self.checkEntries():
            results = []
            if self.useAlgorithm == 1:
                for arg in range(len(self.rtEntries)):
                    tasks.append({"name": f"T{arg + 1}", "releaseTime": float(self.rtEntries[arg].get()), "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                results = mlfos(tasks, maxtime).getResults()
            elif self.useAlgorithm==2:
                for arg in range(len(self.rtEntries)):
                         tasks.append({"name": f"T{arg + 1}", "releaseTime": float(self.rtEntries[arg].get()), "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                results = edfos(tasks, maxtime).getResults()
            elif self.useAlgorithm==3:
                for arg in range(len(self.rtEntries)):
                           tasks.append({"name": f"T{arg + 1}", "releaseTime": float(self.rtEntries[arg].get()), "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                DMA(tasks, maxtime)
            elif self.useAlgorithm==4:
                for arg in range(len(self.rtEntries)):
                           tasks.append({"name": f"T{arg + 1}", "releaseTime": float(self.rtEntries[arg].get()), "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                RMA(tasks, maxtime)
            else:
                self.errorMessage("please choose an algorithm to use.")
            if results:
                self.resultsWindow(results)


    def errorMessage(self, msg):
        messagebox.showerror("Error", msg)

    def checkEntries(self):
        for entry in range(len(self.rtEntries)):
            try:
              float(self.rtEntries[entry].get())
              float(self.ptEntries[entry].get())
              float(self.etEntries[entry].get())
              float(self.dtEntries[entry].get())
            except:
                self.errorMessage("Please ensure that all entries are filled either with integer or float numbers")
                return False
        return True

UI()