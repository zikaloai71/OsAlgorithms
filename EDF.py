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
                # update the deadline based on arrival time
                task["deadLine"] = time + task["deadLine"]
                ready_queue.append(task.copy())
                

        # Sort the ready queue by deadline
        ready_queue.sort(key=lambda task: task["deadLine"])

        # Execute the highest priority task
        if ready_queue:
            current_task = ready_queue.pop(0)
            # Check if the task misses its deadline before executing it
            if time > current_task["deadLine"]:
                print(f"Warning: task {current_task['name']} missed its deadline at time {time}")
            else:
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
    plt.xticks(range(hyperperiod+1))
    plt.xlabel("Time")
    plt.ylabel("Task")
    plt.grid(True)
    plt.title("Earliest Deadline First Scheduling")
    plt.legend(loc="lower right")
    plt.show()


