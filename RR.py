import matplotlib.pyplot as plt

def shiftCL(queue):
    temp = queue[0]
    for i in range(len(queue)-1):
        queue[i] = queue[i+1]
    queue[len(queue)-1] = temp
    return queue

def roundRobin(tasks,quantum, maxTime):
    print(tasks)
    chart = []
    queue = []
    time = 0
    arrivedProcesses = 0
    readyProcesses = 0
    done=0
    start=0

    while(done<len(tasks)):
        for i in range(len(tasks)):
            if(time >= tasks[i]["arrival"]):
                queue.append(tasks[i])
                arrivedProcesses+=1
                readyProcesses+=1
        if(readyProcesses < 1):
            chart.append(0)
            time+=1
            continue

        if start:
           queue = shiftCL(queue)

        if queue[0]["burst"] > 0:
            if(queue[0]["burst"] >quantum):
                for g in range (int(time),int(time+quantum)):
                    chart.append(queue[0]["name"])
                time+=quantum
                queue[0]["burst"]-=quantum
            else:
                for g in range(int(time),int(time+queue[0]["burst"])):
                    chart.append(queue[0]["name"])
                time+=queue[0]["burst"]
                queue[0]["burst"]=0
                done+=1
                readyProcesses-=1
            start=1
    output = []
    for i,value in enumerate(chart):
        output.append((i,value))
    output = output[:maxTime]

    # your list of tuples

    # separate the steps and tasks into two lists
    steps = [x[0] for x in output]
    task_names = [x[1] for x in output]

    # assign a numerical value to each task name
    task_values = []
    task_dict = {}
    value = 0
    for name in task_names:
        if name not in task_dict:
            task_dict[name] = value
            value += 1
        task_values.append(task_dict[name])

    # plot the graph with steps on x-axis and task values on y-axis
    plt.scatter(steps, task_values, c=task_values, cmap='tab10')
    plt.xlabel('Steps')
    plt.xticks(range(maxTime+1))
    plt.yticks(list(task_dict.values()), list(task_dict.keys()))
    plt.ylabel('Tasks')
    plt.title('Task Execution Graph')
    plt.grid(True)
    plt.show()

