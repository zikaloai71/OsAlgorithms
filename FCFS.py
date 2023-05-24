import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def findWaitingTime(tasks):
    # Initialize the current time to zero
    current_time = 0
    # Loop through the tasks
    for task in tasks:
        # Calculate the turnaround time as the current time plus the burst time
        task["turnAroundTime"] = current_time + task["executionTime"]
        # Calculate the waiting time as the turnaround time minus the burst time
        task["waitingTime"] = task["turnAroundTime"] - task["executionTime"]
        # Update the current time by adding the burst time
        current_time += task["executionTime"]

def drawGantt(tasks, maxtime):
    """
    The scheduled results are displayed in the form of a
    gantt chart for the user to get better understanding
    """
    y_axis = []
    from_x = []
    to_x = []
    for task in tasks:
        y_axis.append(task["name"])
        from_x.append(task["start_time"])
        to_x.append(task["finish_time"])


    colors = ['red','green','blue','orange','yellow']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # the data is plotted from_x to to_x along y_axis
    ax = plt.hlines(y_axis, from_x, to_x, linewidth=20, color = colors[len(tasks)-1])
    plt.title('Rate Monotonic scheduling')
    plt.grid(True)
    plt.xlabel("Real-Time clock")
    plt.ylabel("HIGH------------------Priority--------------------->LOW")
    plt.xticks(range(maxtime+1))
    plt.show()

def FCFS(tasks, maxtime):
    # Function to find waiting time of all tasks
    findWaitingTime(tasks)
    # Display tasks along with all details
    print("Tasks\t\tBT\t\tPT\t\tWT\t\tTAT")
    # Calculate total waiting time and total turn around time
    total_wt = 0
    total_tat = 0
    # List to store the order of tasks
    order = []
    # Variable to keep track of the current time
    current_time = 0
    orderIndex = 0
    n = len(tasks)
    for i in range(n):
        total_wt = total_wt + tasks[i]["waitingTime"]
        total_tat = total_tat + tasks[i]["turnAroundTime"]
        print(str(tasks[i]["name"]) + "\t\t" + str(tasks[i]["executionTime"]) + "\t\t" + str(tasks[i]["periodTime"]) + "\t\t" + str(tasks[i]["waitingTime"]) + "\t\t" + str(tasks[i]["turnAroundTime"]))
        # Append the process id to the order list
        order.append({"name":tasks[i]["name"], "start_time":current_time, "finish_time":current_time + tasks[i]["executionTime"]})
        orderIndex += 1
        # Update the current time
        current_time += tasks[i]["executionTime"]
        if(current_time >= maxtime):
            order[i]["finish_time"] = maxtime
            print("Time Finished")
            break
    print("Average waiting time = " + str(total_wt / n))
    print("Average turn around time = " + str(total_tat / n))
    # Print the order of tasks
    print("Order of tasks: " + str(order))
    # Draw the gantt chart
    drawGantt(order, maxtime)

# Driver code
tasks = [
    {"name":"Task2", "executionTime":5, "periodTime":15},
    {"name":"Task1", "executionTime":10, "periodTime":20},
    {"name":"Task3", "executionTime":8, "periodTime":25}
]
FCFS(tasks, 20)
