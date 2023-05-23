# Import modules
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
matplotlib.use('Qt5Agg')

def LST (tasks, maxTime) :
    # Hyperperiod or LCM
    print (tasks)
    hyperperiod = maxTime
    
    # Scheduling
    schedule = []
    ready_queue = []
    time = 0
    previous_task = None # keep track of the previous task
    
    # Store the original deadlines of each task
    original_deadlines = [task["deadLine"] for task in tasks]
    
    while time < hyperperiod:
        # Add any new tasks that arrive at the current time to the ready queue
        for i, task in enumerate(tasks):
            if time % task["periodTime"] == 0:
                # update the deadline and remaining execution time based on arrival time
                # use the original deadline value to avoid cumulative errors
                task["deadLine"] = time + original_deadlines[i]
                task["remaining"] = task["executionTime"]
                ready_queue.append(task.copy())
                
        # Calculate the slack time of each task in the ready queue
        for task in ready_queue:
            task["slack"] = calculate_slack(task, time)

        # Sort the ready queue by slack time and break ties by EDF criterion
        ready_queue.sort(key=lambda task: (task["slack"], task["deadLine"]))

        # Execute the highest priority task
        if ready_queue:
            current_task = ready_queue.pop(0)
            # Check if the task misses its deadline before executing it
            if time > current_task["deadLine"]:
                print(f"Warning: task {current_task['name']} missed its deadline at time {time}")
                # Remove the missed task from the ready queue and mark it as missed
                current_task["missed"] = True
            else:
                schedule.append((time, current_task["name"]))
                current_task["remaining"] -= 1
                # Update the previous task to the current task name
                previous_task = current_task["name"]
                # Check if the task is completed or needs to be added back to the ready queue
                if current_task["remaining"] == 0:
                    print(f"Task {current_task['name']} is completed.")
                else:
                    ready_queue.append(current_task)
            
                
        else:
            schedule.append((time, None))
            
        # Increment the current time by one unit    
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
            end = start + 1 # assuming one unit of execution time per cycle
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
    plt.title("Least Slack Time Scheduling")
    plt.legend(loc="lower right")
    plt.show()

# A function to calculate the slack time of a task
def calculate_slack(task, time):
    return task['deadLine'] - time - task['remaining']




