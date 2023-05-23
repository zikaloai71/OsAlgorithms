def shiftCL(queue):
    temp = queue[0]
    for i in range(len(queue)-1):
        queue[i] = queue[i+1]
    queue[len(queue)-1] = temp
    return queue

def roundRobin(tasks,quantum):
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
                for g in range (time,time+quantum):
                    chart.append(queue[0]["name"])
                time+=quantum
                queue[0]["burst"]-=quantum
            else:   
                for g in range(time,time+queue[0]["burst"]):
                    chart.append(queue[0]["name"])
                time+=queue[0]["burst"]
                queue[0]["burst"]=0
                done+=1 
                readyProcesses-=1
            start=1       
    return chart

tasks=[
    {"name":"t1","burst":3,"arrival":0},
    {"name":"t2","burst":5,"arrival":1},
    {"name":"t3","burst":4,"arrival":2},
    {"name":"t4","burst":2,"arrival":3},
]

result = roundRobin(tasks,2)

output = []
for i,value in enumerate(result):
    output.append((value,i))

print(output)