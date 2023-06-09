import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def FCFS(tasks , maxtime):
    # Sort tasks based on arrival time (assuming tasks is a list of dictionaries with "arrival" and "burst" keys)
    sorted_tasks = sorted(tasks, key=lambda x: x["arrival"])
    print(sorted_tasks)
    order=[]
    # Calculate waiting time and turn around time for each task

    turn_around_time = 0
    total_turn_around_time = 0

    print("Tasks\t\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for task in sorted_tasks:
        # Calculate waiting time for current task
        # Calculate start time for current task
        start_time = max(task["arrival"], total_turn_around_time)

        # Calculate turn around time for current task
        turn_around_time = start_time + task["burst"]

        # Update total waiting time and total turn around time
        total_turn_around_time += turn_around_time - start_time

        # Append the task to the order list
        order.append({"name": task["name"], "start_time": start_time, "finish_time": turn_around_time})

        # Print task details
    drawGantt(order, maxtime)


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
    plt.title('First Come First Serve Scheduling')
    plt.grid(True)
    # plt.xlabel("Real-Time clock")
    # plt.ylabel("HIGH------------------Priority--------------------->LOW")
    plt.xticks(range(maxtime+1))
    plt.show()  