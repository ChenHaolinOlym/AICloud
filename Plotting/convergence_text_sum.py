# import numpy as np
import matplotlib.pyplot as plt

save_path = "./text_summarization"
batch100_results = "./train_iter5000_batch100_MLE.log"
batch200_results = "./train_iter5000_MLE.log"
batch500_results = "./train_iter5000_batch500_MLE.log"
stop = 300

def main():
    batch100_loss = []
    batch100_iteration = []
    with open(batch100_results, "r") as f:
        line_list = f.readlines()
        for idx, line in enumerate(line_list):
            if (idx % 4 == 0 and idx != 0):
                line_list = line.split()
                # print(line_list)
                batch100_iteration.append(int(line_list[1]))
                batch100_loss.append(float(line_list[3]))
            if idx > stop:
                break
    
    batch200_loss = []
    batch200_iteration = []
    with open(batch200_results, "r") as f:
        line_list = f.readlines()
        for idx, line in enumerate(line_list):
            if (idx % 4 == 0 and idx != 0):
                line_list = line.split()
                # print(line_list)
                batch200_iteration.append(int(line_list[1]))
                batch200_loss.append(float(line_list[3]))
            if idx > stop:
                break

    batch500_loss = []
    batch500_iteration = []
    with open(batch500_results, "r") as f:
        line_list = f.readlines()
        for idx, line in enumerate(line_list):
            if (idx % 4 == 0 and idx != 0):
                line_list = line.split()
                # print(line_list)
                batch500_iteration.append(int(line_list[1]))
                batch500_loss.append(float(line_list[3]))
                if idx > stop:
                    break 


    l1, = plt.plot(batch100_iteration, batch100_loss, 'b--', label='Batch Size 100')
    l2, = plt.plot(batch200_iteration, batch200_loss, 'r*-', label='Batch Size 200')
    l3, = plt.plot(batch500_iteration, batch500_loss, 'g+-', label='Batch Size 500')
    plt.title('Loss Convergence')
    plt.xlabel('Iteration Times')
    plt.ylabel('MLE Loss')
    plt.legend(handles = [l1, l2, l3, ], labels = ['Batch Size 100', 'Batch Size 200', 'Batch Size 500'], loc = 'best')
    plt.savefig(f"{save_path}convergence.png", dpi=2048)

    plt.show()

main()
