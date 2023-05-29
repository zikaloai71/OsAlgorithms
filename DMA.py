# This code is from https://github.com/amirhnajafiz-university/S8ER01/blob/main/RTOS_HW1.py
# I do not claim any ownership or responsibility for this code.

import numpy as np
import matplotlib.pyplot as plt





def DMA (tasks,maxtime) :
    # Hyperperiod or LCM
    print (tasks, maxtime)
    hyperperiod = maxtime

    # Deadline monotonic priority assignment
    tasks.sort(key=lambda task: task["deadLine"])
    for i, task in enumerate(tasks):
        task["priority"] = i + 1

    # Scheduling
    schedule = []
    ready_queue = []
    time = 0
    while time < hyperperiod:
        # Add new arrivals to ready queue
        for task in tasks:
            if time % task["periodTime"] == 0:
                ready_queue.append(task.copy())
        # Sort ready queue by priority
        ready_queue.sort(key=lambda task: task["priority"])
        # Execute the highest priority task
        if ready_queue:
            current_task = ready_queue.pop(0)
            schedule.append((time, current_task["name"]))
            time += current_task["executionTime"]
        else:
            schedule.append((time, None))
            time += 1

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.hlines(
        y=[task["name"] for task in tasks],
        xmin=[0] * len(tasks),
        xmax=[hyperperiod] * len(tasks),
        color="gray",
    )
    # Use a color map or a list of colors to assign a color to each task
    cmap = plt.get_cmap("tab10")
    for start, name in schedule:
        if name:
            end = start + [task["executionTime"] for task in tasks if task["name"] == name][0]
            plt.hlines(
                y=name,
                xmin=start,
                xmax=end,
                color=cmap([task["name"] for task in tasks].index(name)),
                linewidth=10,
                label=name if name not in plt.gca().get_legend_handles_labels()[1] else "",
            )
    plt.legend(loc="lower right")
    plt.xticks(range(hyperperiod+1))
    plt.grid(True)
    plt.xlabel("Time")
    plt.ylabel("Task")
    plt.title("Deadline Monotonic Scheduling")


    plt.show()


# DMA([{"name": "p1", "periodTime": 20,"deadLine": 7, "executionTime": 3} ,
#         {"name": "p2", "periodTime": 5,"deadLine": 4, "executionTime": 2} ,
#         {"name": "p3", "periodTime": 10,"deadLine": 8, "executionTime": 2}
# ], 20)