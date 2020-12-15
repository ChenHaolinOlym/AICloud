import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# path info
# path to fetch report
report_path = "./report.report"
# path to save the figure
save_path = "./"


# executor number and cores per executor
para_num_settings = [1,2,3,4]
para_cores_settings = [1,2,3,4]

# Store the necessary information fetched from report
duration = list()
throughput = list()

# fetch data from report
def fetch_data():
    try:
        with open(report_path, "r") as r_f:
            flist = r_f.readlines()
            for line in flist:
                split = line.split()
                if (("Type" in split) or (len(split) == 0)):
                    # skip first line and empty line
                    continue
                duration.append(float(split[4]))
                throughput.append(float(split[5]))
    except FileNotFoundError:
        print("File not found or cannot be opened!\n")

# plot throughput heatmap
def throughput_heatmap():
    # row_dim = len(para_mapper_settings)
    # col_dim = len(para_reducer_settings)
    row_dim = len(para_num_settings)
    col_dim = len(para_cores_settings)
    data = np.reshape(throughput, (row_dim, col_dim))

    fig,ax = plt.subplots(figsize=(8,8))
    sns.heatmap(data=data, square=False, vmin=min(throughput), vmax=max(
        throughput), cmap="Blues", annot=True, fmt=".4", cbar_kws={"orientation": "horizontal"}) # heatmap settings
    ax.set_xticklabels(list(f'#cores/executor-{i}' for i in para_cores_settings),rotation='horizontal') # horizontal axis
    ax.set_yticklabels(list(f'#executor-{i}' for i in para_num_settings),rotation='vertical') # vertical axis
    plt.title("Throughput (unit: bytes/s) Heatmap") # title of plot
    plt.savefig(f'{save_path}/num_cores_2x_heatmap_throughput.png', dpi=2048) # filename and dpi

# plot duration heatmap
def duration_heatmap():
    row_dim = len(para_num_settings)
    col_dim = len(para_cores_settings)
    data = np.reshape(duration, (row_dim, col_dim))

    fig,ax = plt.subplots(figsize=(8,8))
    sns.heatmap(data=data, square=False, vmin=min(duration), vmax=max(
        duration), cmap="Blues", annot=True, fmt="f", cbar_kws={"orientation": "horizontal"})
    ax.set_xticklabels(list(f'#cores/executor-{i}' for i in para_cores_settings),rotation='horizontal')
    ax.set_yticklabels(list(f'#executor-{i}' for i in para_num_settings),rotation='vertical')
    plt.title("Duration (unit: s) Heatmap")
    plt.savefig(f'{save_path}/num_cores_2x_heatmap_duration.png', dpi=2048)

def main():
    fetch_data()
    throughput_heatmap()
    duration_heatmap()


main()
