# Import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors




def EDF (tasks, maxTime) :
    # Hyperperiod or LCM
    print (tasks)
    hyperperiod = maxTime
    
    # Scheduling
    schedule = []
    ready_queue = []
    time = 0
    while time < hyperperiod:
        # Add any new tasks that arrive at the current time to the ready queue
        for task in tasks:
            if time % task["periodTime"] == 0:
                ready_queue.append(task.copy())
                task["deadline"] = time + task["deadLine"] # update the deadline based on arrival time

        # Sort the ready queue by deadline
        ready_queue.sort(key=lambda task: task["deadLine"])

        # Execute the highest priority task
        if ready_queue:
            current_task = ready_queue.pop(0)
            schedule.append((time, current_task["name"]))
            time += current_task["executiontTime"]
            
            # If the task misses its deadline, print a warning message and remove it from the ready queue
            if time > current_task["deadLine"]:
                print(f"Warning: task {current_task['name']} missed its deadline at time {time}")
                
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
    for start, name in schedule:
        if name:
            end = start + [task["executiontTime"] for task in tasks if task["name"] == name][0]
            plt.hlines(
                y=name,
                xmin=start,
                xmax=end,
                color="purple",
                linewidth=10,
                label=name if name not in plt.gca().get_legend_handles_labels()[1] else "",
            )
    plt.xticks(range(hyperperiod+1))
    plt.xlabel("Time")
    plt.ylabel("Task")
    plt.title("Earliest Deadline First Scheduling")
    plt.show()



