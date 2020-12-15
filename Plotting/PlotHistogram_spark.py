import matplotlib
import matplotlib.pyplot as plt

# path to fetch report
report_path = "./report.report"
# path to save the figure
save_path = "./"


# Experiemnt 2 #
# executor pattern
comb_settings = ["1*4","2*2","4*1"]


# Experiemnt 3 #
# 1. parallelism
para_parallelsim_settings = [2,4,8,12,16]
para_parallelsim_str_settings = ["0.5x","1x","2x","3x","4x"]

# 2. base time, can be obtained from report, used to calculate speed_up
base_time= 27.947


# Experiemnt 4 #
# values that will be assigned to the changing scale
para_scale_settings = ["set1","set2","set3","set4","set5"]


# name of the output parameter that you want to fetch from the report
output_thro = "Throughput(bytes/s)"
output_dura = "Duration(s)"

# store necessary info for plotting
duration = list()
throughput = list()
speed_up = list()
efficiency = list()

# fetch necessary info from report
def fetch_data():
    try:
        with open(report_path, "r") as r_f:
            flist = r_f.readlines()
            for line in flist:
                split = line.split()
                if (("Type" in split) or (len(split) == 0)):
                    # skip first line and empty line
                    continue
                # datasize.append(float(split[3]))
                duration.append(float(split[4]))
                throughput.append(float(split[5]))
    except FileNotFoundError:
        print("File not found or cannot be opened!\n")


#########################
######### Exp_2 #########
#########################

# generate the histogram of duration and throughput
def comb_histogram():
    plt.rcParams['axes.labelsize'] = 12  # xy axis label size
    plt.rcParams['xtick.labelsize'] = 9  # x axis ticks size
    plt.rcParams['ytick.labelsize'] = 12  # y axis ticks size
    plt.rcParams['legend.fontsize'] = 10  # legend size

    # gap between histogram
    width = 0.3  # width
    x1_list = []
    x2_list = []
    for i in range(len(comb_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # create layer
    fig, ax1 = plt.subplots()

    # in the bar chart, x, y must be of the same length
    assert(len(x1_list) == len(duration))
    # set left side y axis figure
    ax1.set_ylabel('Duration(s)')
    ax1.set_ylim(min(duration)*0.8, max(duration)*1.2)  # set range of y axis
    ax1.bar(x1_list, duration, width=width,
            color='lightseagreen', align='edge', label='Duration')
    ax1.set_xticklabels(ax1.get_xticklabels())  # set common x axis

    # set right side y axis figure
    assert(len(x2_list) == len(throughput))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput(bytes/s)')
    ax2.set_ylim(min(throughput)*0.8, max(throughput)*1.1)  # set range of y axis
    ax2.bar(x2_list, throughput, width=width, color='tab:blue',
            align='edge', tick_label=comb_settings, label='Throughput')

    # for tick in ax1.get_xticklabels():  # rotate x-axis for 30 degree
    #     tick.set_rotation(30)

    # legend
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/comb_para2_d&t.png", dpi=1024)
    # plt.show()


#########################
######### Exp_3 #########
#########################

# calculate speedup
def para_cal_speedup():
    single_node_exe_time = base_time
    for i in range(0,5):
        speed_up.append(float(single_node_exe_time) / float(duration[i]))

# calculate efficiency
def para_cal_efficiency():
    for i in range(0,5):
        efficiency.append(float(speed_up[i]) / float(para_parallelsim_settings[i]))

# generate the histogram of duration and throughput
def para_dnt_histogram():
    plt.rcParams['axes.labelsize'] = 12  # xy axis label size
    plt.rcParams['xtick.labelsize'] = 9  # x axis ticks size
    plt.rcParams['ytick.labelsize'] = 12  # y axis ticks size
    plt.rcParams['legend.fontsize'] = 10  # legend size

    # gap between histogram
    width = 0.3  # width
    x1_list = []
    x2_list = []
    for i in range(len(para_parallelsim_str_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # create layer
    fig, ax1 = plt.subplots()

    # in the bar chart, x, y must be of the same length
    assert(len(x1_list) == len(duration))
    # set left side y axis figure
    ax1.set_ylabel('Duration(s)')
    ax1.set_ylim(min(duration)*0.8, max(duration)*1.2)  # set range of y axis
    ax1.bar(x1_list, duration, width=width,
            color='lightseagreen', align='edge', label='Duration')
    ax1.set_xticklabels(ax1.get_xticklabels())  # set common x axis

    # set right side y axis figure
    assert(len(x2_list) == len(throughput))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput(bytes/s)')
    ax2.set_ylim(min(throughput)*0.8, max(throughput)*1.1)  # set range of y axis
    ax2.bar(x2_list, throughput, width=width, color='tab:blue',
            align='edge', tick_label=para_parallelsim_str_settings, label='Throughput')

    # legend
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/parallelsim_d&t.png", dpi=1024)
    # plt.show()

# generate the histogram of speedup and efficiency
def para_spe_eff_histogram():
    # calculate speed_up and efficiency
    para_cal_speedup()
    para_cal_efficiency()

    plt.rcParams['axes.labelsize'] = 12  # xy axis label size
    plt.rcParams['xtick.labelsize'] = 9  # x axis ticks size
    plt.rcParams['ytick.labelsize'] = 12  # y axis ticks size
    plt.rcParams['legend.fontsize'] = 12  # legend size

    # gap between histogram
    width = 0.3  # width
    x1_list = []
    x2_list = []
    for i in range(len(para_parallelsim_str_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # create layer
    fig, ax1 = plt.subplots()

    # set left side y axis figure
    # in the bar chart, x, y must be of the same length
    assert(len(x1_list) == len(speed_up))
    ax1.set_ylabel('Speed Up')
    ax1.set_ylim(min(speed_up)*0.8, max(speed_up)*1.2)  # set range of y axis
    ax1.bar(x1_list, speed_up, width=width,
            color='lightseagreen', align='edge', label='Speed Up')

    ax1.set_xticklabels(ax1.get_xticklabels())  # set common x axis

    # set right side y axis figure
    assert(len(x2_list) == len(efficiency))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Efficiency')
    ax2.set_ylim(min(efficiency)*0.8, max(efficiency)*1.1)  # set range of y axis
    ax2.bar(x2_list, efficiency, width=width, color='tab:blue',
            align='edge', tick_label=para_parallelsim_str_settings, label='Efficiency')

    # legend
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/parallelsim_speff_new.png", dpi=1024)
    # plt.show()


#########################
######### Exp_4 #########
#########################

# generate the histogram with scale (data size) changes
def scale_histogram():
    plt.rcParams['axes.labelsize'] = 12  # xy axis label size
    plt.rcParams['xtick.labelsize'] = 9  # x axis ticks size
    plt.rcParams['ytick.labelsize'] = 12  # y axis ticks size
    plt.rcParams['legend.fontsize'] = 10  # legend size

    # gap between histogram
    width = 0.3  # width
    x1_list = []
    x2_list = []
    for i in range(len(para_scale_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # create layer
    fig, ax1 = plt.subplots()

    # in the bar chart, x, y must be of the same length
    assert(len(x1_list) == len(duration))
    # set left side y axis figure
    ax1.set_ylabel('Duration(s)')
    ax1.set_ylim(min(duration)*0.8, max(duration)*1.2)  # set range of y axis
    ax1.bar(x1_list, duration, width=width,
            color='lightseagreen', align='edge', label='Duration')
    ax1.set_xticklabels(ax1.get_xticklabels())  # set common x axis

    # set right side y axis figure
    assert(len(x2_list) == len(throughput))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput(bytes/s)')
    ax2.set_ylim(min(throughput)*0.8, max(throughput)*1.1)  # set range of y axis
    ax2.bar(x2_list, throughput, width=width, color='tab:blue',
            align='edge', tick_label=para_scale_settings, label='Throughput')

    # for tick in ax1.get_xticklabels():  # rotate x-axis for 30 degree
    #     tick.set_rotation(30)

    # legend
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/scale.png", dpi=1024)
    # plt.show()



def main():
    fetch_data()

    # graph cannot be drawn at the same time due to the difference of three settings

    # Experiemnt 2 #
    comb_histogram()

    # Experiemnt 3 #
    # para_dnt_histogram()
    # para_spe_eff_histogram()

    # Experiemnt 4 #
    # scale_histogram()


main()