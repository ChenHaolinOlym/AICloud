import re
import numpy as np
import matplotlib.pyplot as plt

# save path
save_path = "./"

# Log file path
batch64_results = "./Image_to_Text_epoch5_batch64.log"
batch128_results = "./Image_to_Text_epoch5_batch128.log"
batch256_results = "./Image_to_Text_epoch5_batch256.log"

# used for subtract necessary information from image to text log file, 
# can be modified according to different format of log file
p1 = re.compile(r'[[](.*?)[/]', re.S)

# recorded step size in each epoch of each batch size
step_epoch_64 = 647
step_epoch_128 = 323
step_epoch_256 = 161


def main():

###########################################
################ Part 1 ###################
######## Fetch necessary information ######
###########################################

    batch64_loss = []
    batch64_perplexity = []
    batch64_total_step = []
    with open(batch64_results, "r") as f:
        line_list = f.readlines()
        for idx, line in enumerate(line_list):
                line_split = line.split()

                # get necessary info for plotting
                epoch = int(re.findall(p1, line_split[1])[0])
                step = int(re.findall(p1, line_split[3])[0])
                total_step = epoch * step_epoch_64 + step/10

                loss = float(line_split[5][:6])
                perplexity = float(line_split[7])

                batch64_loss.append(loss)
                batch64_perplexity.append(perplexity)
                batch64_total_step.append(total_step)


    batch128_loss = []
    batch128_perplexity = []
    batch128_total_step = []
    with open(batch128_results, "r") as f:
        line_list = f.readlines()
        for idx, line in enumerate(line_list):
                line_split = line.split()

                # get necessary info for plotting
                epoch = int(re.findall(p1, line_split[1])[0])
                step = int(re.findall(p1, line_split[3])[0])
                total_step = epoch * step_epoch_128 + step/10

                loss = float(line_split[5][:6])
                perplexity = float(line_split[7])

                batch128_loss.append(loss)
                batch128_perplexity.append(perplexity)
                batch128_total_step.append(total_step)


    batch256_loss = []
    batch256_perplexity = []
    batch256_total_step = []
    with open(batch256_results, "r") as f:
        line_list = f.readlines()
        for idx, line in enumerate(line_list):
                line_split = line.split()

                # get necessary info for plotting
                epoch = int(re.findall(p1, line_split[1])[0])
                step = int(re.findall(p1, line_split[3])[0])
                total_step = epoch * step_epoch_256 + step/10
 
                loss = float(line_split[5][:6])
                perplexity = float(line_split[7])

                batch256_loss.append(loss)
                batch256_perplexity.append(perplexity)
                batch256_total_step.append(total_step)



# Note: 
# There are two parts for plotting, which should be executed seperately.
# The details can be modified to fit other parameters changing.

###########################################
################ Part 2 ###################
#### Plot Loss and Perplexity together ####
###########################################

    # start plot
    fig = plt.figure()

    # plot batch 64 loss
    ax1 = fig.add_subplot(111)
    l_b64loss = ax1.plot(batch64_total_step, batch64_loss, 'b--', alpha=0.8, label='Batch 64 Loss')
    max_loss = max(max(batch64_loss), max(batch128_loss), max(batch256_loss))
    ax1.set_ylim(0,max_loss)
    ax1.set_ylabel('Loss')
    ax1.set_xlabel('Step Size')
    ax1.set_title("Loss & Perplexity Convergence")

    # plot batch 64 perplexity
    ax2 = ax1.twinx()  # this is the important function
    l_b64perp = ax2.plot(batch64_total_step, batch64_perplexity, 'b--', alpha=0.8, label='Batch 64 Perplexity')
    max_perplexity = max(max(batch64_perplexity), max(batch128_perplexity), max(batch256_perplexity))
    ax2.set_ylim(0,max_perplexity)
    ax2.set_ylabel('Perplexity')

    # plot batch 128 loss & perplexity
    l_b128loss = ax1.plot(batch128_total_step, batch128_loss, 'r*-', alpha=0.8, label='Batch 128 Loss')
    l_b28perp = ax2.plot(batch128_total_step, batch128_perplexity, 'r*-', alpha=0.8, label='Batch 128 Perplexity')

    # plot batch 256 loss & perplexity
    l_b256loss = ax1.plot(batch256_total_step, batch256_loss, 'g+-', alpha=0.8, label='Batch 256 Loss')
    l_b256perp = ax2.plot(batch256_total_step, batch256_perplexity, 'g+-', alpha=0.8, label='Batch 256 Perplexity')

    # split line
    plt.hlines(100, min(batch64_total_step)+100, max(batch64_total_step)-100, 'black', '--', alpha=0.8)

    # legend
    ax1.legend(loc='upper center', bbox_to_anchor=(0.8,0.8), bbox_transform=ax1.transAxes)
    ax2.legend(loc='lower center', bbox_to_anchor=(0.8,0.05), bbox_transform=ax2.transAxes)

    plt.savefig(f"{save_path}test.png", dpi=2048)
    plt.show()


##############################################
################ Part 3 ######################
#### Plot Loss and Perplexity tSeperately ####
##############################################

    l1, = plt.plot(batch64_total_step, batch64_loss, 'b--', label='Batch Size 64')
    l2, = plt.plot(batch128_total_step, batch128_loss, 'r*-', label='Batch Size 128')
    l3, = plt.plot(batch256_total_step, batch256_loss, 'g+-', label='Batch Size 256')

    l1, = plt.plot(batch64_total_step, batch64_perplexity, 'b--', label='Batch Size 64')
    l2, = plt.plot(batch128_total_step, batch128_perplexity, 'r*-', label='Batch Size 128')
    l3, = plt.plot(batch256_total_step, batch256_perplexity, 'g+-', label='Batch Size 256')

    plt.title('Loss Convergence')
    plt.xlabel('Step Size')
    plt.ylabel('Loss')

    plt.title('Perplexity Convergence')
    plt.xlabel('Step Size')
    plt.ylabel('Perplexity')

    plt.legend(handles = [l1, l2, l3, ], labels = ['Batch Size 64', 'Batch Size 128', 'Batch Size 256'], loc = 'best')
    plt.savefig(f"{save_path}test.png", dpi=2048)

    plt.show()

main()
