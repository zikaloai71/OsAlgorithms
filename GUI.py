
from tkinter import * 
from tkinter import ttk

from tkinter import messagebox
import matplotlib.pyplot as plt


from DMA import DMA
from RMA import RMA
from EDF import EDF
from LST import LST
from RRv2 import roundRobin

class UI:
    def __init__(self):
        #create tkinter window
        self.root = Tk()    
        #title of window
        self.root.title("Os Project")
        #size of window and it's position "width x height+top+left"
        self.root.geometry("650x550+400+100")
        #background color of window
        self.root.config(bg="red")
        #child of root window for no.of tasks input and choosing algorithm
        self.inputFrame = Frame(self.root, bg="#DDDDDD")
        #fill x means fill the window in x direction
        self.inputFrame.pack(fill=X)
        #keep the content of input frame in center when resizing the window 
        self.inputFrame.columnconfigure(0, weight=2)
        self.inputFrame.columnconfigure(6, weight=2)

        
        self.ptEntries = []  #  to enter periodic time 
        self.etEntries = []   #  to enter execution time 
        self.dtEntries = []    #  to enter deadline  time 
        self.atEntries = []    #  to enter arrival time
        self.btEntries = []    #  to enter burst time
        self.tasks =[]   #   to enter no. of tasks 
        

      
        #label for input frame tasks number
        Label(self.inputFrame, text="No.Tasks: ", font=("times new roman", 12, "bold"), bg="#DDDDDD").grid(row=1, column=1, pady=5)
        #label for input frame algorithm type
        Label(self.inputFrame, text= "Scheduling type: ", font=("times new roman", 12, "bold"), bg="#DDDDDD").grid(row=2,column=1,pady=5)  
        #select box
        self.algorithm_chosen = ttk.Combobox(self.inputFrame,width=12,justify=CENTER)
        #options for select box
        self.algorithm_chosen['value']=( "LST", "EDF", "DMA", "RMA","RR")
        self.algorithm_chosen.grid(row=2,column=2,pady=5)
        #default value for select box
        self.algorithm_chosen.current(0)
        

        #submit the no. of tasks and the algorithm type
        Button(self.inputFrame, text="submit", font=("times new roman", 10), bg="green", fg="white", command= self.set_algorithm_type).grid(row=3, column=2, pady=5)
      
        
        self.noTasks = IntVar()

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
        if self.algorithm_chosen.get() == "LST":
            self.LST()
        elif self.algorithm_chosen.get() == "EDF":
            self.EDF()
        elif self.algorithm_chosen.get() == "DMA":
            self.DMA()
        elif self.algorithm_chosen.get() == "RMA":
            self.RMA()
        elif self.algorithm_chosen.get() == "RR":
            self.RR()
        else:
            self.errorMessage("please choose an algorithm to use.")    
        self.refresh()
       
#        stop execution of python program

    def exit(self):
        self.root.quit()
        self.root.destroy()

    def LST(self):
        self.algorithmUsed.config(text="Algorithm: Least Slack Time")
      

    def EDF(self):
        self.algorithmUsed.config(text="Algorithm: Earliest Deadline First")
       

    def DMA(self):
        self.algorithmUsed.config(text="Algorithm: Deadline Monotonic Assignment")
        

    def RMA(self):
        self.algorithmUsed.config(text="Algorithm: Rate Monotonic Assignment")
        
    def RR(self):
        self.algorithmUsed.config(text="Algorithm: Round Robin")

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
 

        if(self.algorithm_chosen.get() == "RR"):
            Label(f2, text= "Arrival time: ", font =("times new roman", 12), bg="#4AA080", fg="white").grid(row=0, column=1)
            arrivalTime = Entry(f2, font=("times new roman", 12), justify= CENTER)
            arrivalTime.grid(row=0, column=2)
            self.atEntries.append(arrivalTime)

            Label(f2, text= "Burst time: ", font =("times new roman", 12), bg="#4AA080", fg="white").grid(row=1, column=1)
            burstTime = Entry(f2, font=("times new roman", 12), justify= CENTER)
            burstTime.grid(row=1, column=2)
            self.btEntries.append(burstTime)
        else:
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
        
      
        for i in range(len(self.tasks)):
            self.tasks[i].destroy()

        self.tasks = []
        self.etEntries = []
        self.ptEntries = []
        self.dtEntries = []
        self.atEntries = []
        self.btEntries = []
      
        for i in range(tasksNum):
            self.task(i+1)
        
      
           
      
    

        
           

    def Run(self):
        tasks = []
       
        try:
            maxTime = int(self.maxTimeEntry.get())
            quantum = int(self.quantumEntry.get())
        except:
            self.errorMessage("Please ensure that the max time is an integer number")


        if self.checkEntries():
            if self.algorithm_chosen.get() == "LST":
                for arg in range(len(self.ptEntries)):
                    tasks.append({"name": f"T{arg + 1}", "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                LST(tasks, maxTime)
            elif self.algorithm_chosen.get() == "EDF":
                for arg in range(len(self.ptEntries)):
                         tasks.append({"name": f"T{arg + 1}", "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                EDF(tasks, maxTime)
            elif self.algorithm_chosen.get() == "DMA":
                for arg in range(len(self.ptEntries)):
                           tasks.append({"name": f"T{arg + 1}", "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                DMA(tasks, maxTime)
            elif self.algorithm_chosen.get() == "RMA":
                for arg in range(len(self.ptEntries)):
                           tasks.append({"name": f"T{arg + 1}", "periodTime": float(self.ptEntries[arg].get()),"deadLine": float(self.dtEntries[arg].get()), "executionTime": float(self.etEntries[arg].get())})
                RMA(tasks, maxTime)
            elif self.algorithm_chosen.get() == "RR":
                for arg in range(len(self.atEntries)):
                    tasks.append({"name": f"T{arg + 1}", "arrival": float(self.atEntries[arg].get()), "burst": float(self.btEntries[arg].get())})
                roundRobin(tasks, quantum, maxTime)
            else:
                self.errorMessage("please choose an algorithm to use.")
        


    def errorMessage(self, msg):
        messagebox.showerror("Error", msg)

    def checkEntries(self):
        for entry in range(len(self.ptEntries)):
            try:
              float(self.ptEntries[entry].get())
              float(self.etEntries[entry].get())
              float(self.dtEntries[entry].get())
              float(self.atEntries[entry].get())
              float(self.btEntries[entry].get())
            except:
                self.errorMessage("Please ensure that all entries are filled either with integer or float numbers")
                return False
        return True

UI()