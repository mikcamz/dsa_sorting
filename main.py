import sys
import time
from typing import List
import matplotlib.pyplot as plt
from custom import mergesort, quicksort, heapsort
import numpy as np

sys.setrecursionlimit(2000000)

data = "output/data.txt"
output_graph = "output/result.png"
output = "output/time.txt"

def bench(sort, data):
    temp = data.copy()
    
    start = time.perf_counter()
    res = sort(temp)
    end = time.perf_counter()
    
    return end - start, res

def numpysort(arr: List[int]):
    return np.sort(arr).tolist()

def graphplot(quick: List[float], heap: List[float], merge: List[float], numpy: List[float]):
    """
    AI generated graph plotting function
    """

    # ensure input lists are non-empty and align lengths
    lists = [quick, heap, merge, numpy]
    min_len = min((len(l) for l in lists), default=0)
    if min_len == 0:
        return

    quick = quick[:min_len]
    heap = heap[:min_len]
    merge = merge[:min_len]
    numpy_arr = numpy[:min_len]  # avoid shadowing numpy module

    # labels for each data line and an extra label for averages
    labels = [str(i + 1) for i in range(min_len)]
    labels_with_avg = labels + ["avg"]

    # compute averages
    avgs = [sum(quick) / min_len, sum(heap) / min_len, sum(merge) / min_len, sum(numpy_arr) / min_len]

    # build data matrix (algorithms x columns)
    data_matrix = np.array([quick, heap, merge, numpy_arr])
    avg_column = np.array(avgs).reshape(4, 1)
    data_with_avg = np.hstack([data_matrix, avg_column])  # shape (4, min_len+1)
    data_for_plot = data_with_avg.T  # shape (min_len+1, 4)

    # plotting grouped bars
    n_groups = data_for_plot.shape[0]
    ind = np.arange(n_groups)
    width = 0.18

    fig, ax = plt.subplots(figsize=(max(8, n_groups * 0.6), 5))
    algo_names = ["Quicksort", "Heapsort", "Mergesort", "Numpysort"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

    for i in range(4):
        ax.bar(ind + (i - 1.5) * width, data_for_plot[:, i], width, label=algo_names[i], color=colors[i])

    ax.set_xticks(ind)
    ax.set_xticklabels(labels_with_avg)
    ax.set_xlabel("Array")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Sorting algorithm timings per dataset and average")
    ax.legend()
    plt.tight_layout()

    # save plot next to textual output if possible
    plt.savefig(output_graph)
    plt.close()


def main():
    """
    Main wrapper for running my custom code and numpys code
    Handles comparision and graph plotting
    """

    quick_time = [0] * 10
    heap_time = [0] * 10
    merge_time = [0] * 10
    numpy_time = [0] * 10

    with open(output, "w") as out:
        with open(data, "r") as f:

            i = 0
            a = []
            for line in f:
                if(i < 5): 
                    a = list(map(float, line.split()))
                else:
                    a = list(map(int, line.split()))
                
                quick_time[i], quick = bench(quicksort, a) 
                heap_time[i], heap = bench(heapsort, a) 
                merge_time[i], sort = bench(mergesort, a) 
                numpy_time[i], num = bench(numpysort, a) 
                # res = [quicksort(a.copy()), heapsort(a.copy()), mergesort(a.copy()), numpy.sort(a.copy()).tolist()] 

                if quick==heap==sort==num:
                    print(f"Round {i}: Correct result!\n")
                    print(f"[{i}] Quicksort time: {quick_time[i]}\n")
                    print(f"[{i}] Heapsort time: {heap_time[i]}\n")
                    print(f"[{i}] Mergesort time: {merge_time[i]}\n")
                    print(f"[{i}] Numpysort time: {numpy_time[i]}\n")

                    out.write(f"[{i}] Quicksort time (ms): {quick_time[i] * 1e3}\n")
                    out.write(f"[{i}] Heapsort time (ms): {heap_time[i] * 1e3}\n")
                    out.write(f"[{i}] Mergesort time (ms): {merge_time[i] * 1e3}\n")
                    out.write(f"[{i}] Numpysort time (ms): {numpy_time[i] * 1e3}\n")
                    out.write("\n")
                    i+=1
                else:
                    print("Bad result")
                    exit()

        # calculate avg time of each algorithm
        avgs = [sum(quick_time) / 10, sum(heap_time) / 10, sum(merge_time) / 10, sum(numpy_time) / 10]
        out.write(f"[***] Average Quicksort time (ms): {avgs[0] * 1e3}\n")
        out.write(f"[***] Average Heapsort time (ms): {avgs[1] * 1e3}\n")
        out.write(f"[***] Average Mergesort time (ms): {avgs[2] * 1e3}\n")
        out.write(f"[***] Average Numpysort time (ms): {avgs[3] * 1e3}\n")
        
    graphplot(quick_time, heap_time, merge_time, numpy_time)


if __name__ == "__main__":
    main()