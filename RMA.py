import matplotlib
import matplotlib.pyplot as plt
import math
import copy
import numpy as np
import statistics as st
from collections import defaultdict
matplotlib.use('Qt5Agg')
# Define the tasks with execution time and periodTime


RealTime_task = dict()
metrics = defaultdict(dict)
dList = {}

# For gantt chart
y_axis  = []
from_x = []
to_x = []

# Calculate the hyperperiod (least common multiple of all periods)
def lcm(a, b):
    # Return the least common multiple of two numbers
    return abs(a * b) // math.gcd(a, b)

def Read_data(tasks) :
    """
    Reading the details of the tasks to be scheduled from the user as
    Number of tasks n:
    Period of task P:
    Worst case excecution time WCET:
    """
    global dList
    n = len(tasks)

    # Storing data in a dictionary
    for  i in range(n):
        dList[tasks[i]['name']] = {"start":[],"finish":[]}

    dList["TASK_IDLE"] = {"start":[],"finish":[]}

def Schedulablity(tasks):
    """
    Calculates the utilization factor of the tasks to be scheduled
    and then checks for the schedulablity and then returns true is
    schedulable else false.
    """
    T = []
    C = []
    U = []
    n = len(tasks)
    for i in range(n):
        T.append(int(tasks[i]["periodTime"]))
        C.append(int(tasks[i]["executionTime"]))
        u = int(C[i])/int(T[i])
        U.append(u)

    U_factor = sum(U)
    if U_factor<=1:

        sched_util = n*(2**(1/n)-1)

        count = 0
        T.sort()
        for i in range(len(T)):
            if T[i]%T[0] == 0:
                count = count + 1

        # Checking the schedulablity condition

        if U_factor <= sched_util or count == len(T):
            print("\n\tTasks are schedulable by Rate Monotonic Scheduling!")
            return True
        else:
            print("\n\tTasks are not schedulable by Rate Monotonic Scheduling!")
            return False
    print("\n\tOverloaded tasks!")
    print("\n\tUtilization factor > 1")
    return False

import math

def check_critical_instance(tasks):
    """
    Checks the existence of a critical instance based on the response time analysis.
    Returns True if a critical instance exists; otherwise, returns False.
    """
    n = len(tasks)

    # Sort tasks in ascending order of periods
    tasks.sort(key=lambda x: int(x["periodTime"]))

    for i, task in enumerate(tasks):
        period = int(task["periodTime"])
        execution_time = int(task["executionTime"])
        for time in range(1, period + 1):
            response_time = execution_time
            for j in range(i):
                prev_task = tasks[j]
                response_time += math.ceil(time / int(prev_task["periodTime"])) * int(prev_task["executionTime"])
            print(response_time, period)
            if response_time > period:
                return True

    return False

def estimatePriority(RealTime_task,tasks, hp):
    """
    Estimates the priority of tasks at each real time periodTime during scheduling
    """
    tempPeriod = hp
    P = -1    #Returns -1 for idle tasks
    for i in range(len(RealTime_task)):
        if (RealTime_task[i]["executionTime"] != 0):
            if (tempPeriod > RealTime_task[i]["periodTime"] or tempPeriod > tasks[i]["periodTime"]):
                tempPeriod = tasks[i]["periodTime"] #Checks the priority of each task based on periodTime
                P = i
    return P

def Simulation(tasks, hp):
    """
    The real time schedulng based on Rate Monotonic scheduling is simulated here.
    """

    # Real time scheduling are carried out in RealTime_task
    global RealTime_task
    global dList
    global y_axis
    global from_x
    global to_x

    RealTime_task = copy.deepcopy(tasks)
    # validation of schedulablity neessary condition
    for i in range(len(tasks)):
        # RealTime_task[i]["DCT"] = RealTime_task[i]["WCET"]
        if (RealTime_task[i]["executionTime"] > RealTime_task[i]["periodTime"]):
            print(" \n\t The task can not be completed in the specified time ! ", i )

    # main loop for simulator
    for t in range(hp):
        # Determine the priority of the given tasks
        priority = estimatePriority(RealTime_task,tasks, hp)
        # print("\n\tPriority of the task: ", priority)
        if (priority != -1):    #processor is not idle
            # Update WCET after each clock cycle
            RealTime_task[priority]["executionTime"] -= 1
            # For the calculation of the metrics
            dList[RealTime_task[priority]["name"]]["start"].append(t)
            dList[RealTime_task[priority]["name"]]["finish"].append(t+1)
            # For plotting the results
            y_axis.append(RealTime_task[priority]["name"])
            from_x.append(t)
            to_x.append(t+1)

        else:    #processor is idle
            # For the calculation of the metrics
            dList["TASK_IDLE"]["start"].append(t)
            dList["TASK_IDLE"]["finish"].append(t+1)
            # For plotting the results
            y_axis.append("IDLE")
            from_x.append(t)
            to_x.append(t+1)

        # Update Period after each clock cycle
        for i in range(len(RealTime_task)):
            RealTime_task[i]["periodTime"] -= 1
            if (RealTime_task[i]["periodTime"] == 0):
                RealTime_task[i] = copy.deepcopy(tasks[i])


def drawGantt(tasks):
	"""
	The scheduled results are displayed in the form of a
	gantt chart for the user to get better understanding
	"""
	colors = ['red','green','blue','orange','yellow']
	fig = plt.figure()
	ax = fig.add_subplot(111)
	# the data is plotted from_x to to_x along y_axis
	ax = plt.hlines(y_axis, from_x, to_x, linewidth=20, color = colors[len(tasks)-1])
	plt.title('Rate Monotonic scheduling')
	plt.grid(True)
	plt.xlabel("Real-Time clock")
	plt.ylabel("HIGH------------------Priority--------------------->LOW")
	plt.xticks(np.arange(min(from_x), max(to_x)+1, 1.0))
	plt.show()

def RMA(tasks, hyperperiod):
    """The main function"""
    Read_data(tasks)
    sched_res = Schedulablity(tasks)
    # bound test for schedulablity  # critical instance test for schedulablity
    if sched_res == True or not check_critical_instance(tasks) :
        Simulation(tasks ,hyperperiod)
        drawGantt(tasks)

    else:
        print("\n\tTasks are not schedulable by Rate Monotonic Scheduling!")

tasks =[
        {"name":"T1","periodTime":20,"executionTime":6},
        {"name":"T2","periodTime":25,"executionTime":2},
        {"name":"T3","periodTime":30,"executionTime":12},
    ]
tasks2 =[

        {"name":"T1","periodTime":2,"executionTime":1},
        {"name":"T2","periodTime":3,"executionTime":1},
        {"name":"T3","periodTime":6,"executionTime":.5},
]
hyperperiod = 100
RMA(tasks2, hyperperiod)
