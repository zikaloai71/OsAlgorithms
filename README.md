# Operating Systems Scheduling Algorithms

This repo contains a GUI application that implements various operating systems scheduling algorithms for different tasks. The algorithms are:

- DMA: Direct Memory Access
- EDF: Earliest Deadline First
- FCFS: First Come First Serve
- LST: Least Slack Time
- RMA: Rate Monotonic Algorithm
- RR: Round Robin

## Installation

To run this application, you need to have Python 3 installed on your system. You also need to install the following libraries:

- Tkinter: for creating the GUI
- Matplotlib: for plotting the graphs

You can install them using pip:

```bash
pip install tk matplotlib
```

## Usage

To launch the application, run the following command in the terminal:

```bash
python3 GUI.py
```

You will see a window like this:

![Screenshot from 2023-10-06 22-29-23](https://github.com/zikaloai71/OsAlgorithms/assets/91837017/a79d2417-88d2-4ad7-88f5-7bc00b7d8c7c)

You can enter the number of tasks and choose the algorithm type, then enter the data of each task like period, execution time and deadline.

Then, enter the max time for the whole process and press run, The application will show you a graph of how the tasks are scheduled according to the chosen algorithm.

You can also save the graph as an image file by clicking on the "Save" button icon 💾.

## References

This application is based on the following sources:

- [Operating System Scheduling algorithms](^2^)
- [CPU Scheduling in Operating Systems](^3^)
- [Scheduling Algorithms in OS (Operating System)](^4^)


