import matplotlib.pyplot as plt
from utilities import FileReader

def plot_errors(filename, legend):
    
    headers, values=FileReader(filename).read_file()
    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append(val[-1] - first_stamp)

    fig, axes = plt.subplots(1,2, figsize=(14,6))

    axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    axes[0].set_title("e_dot vs e")
    axes[0].set_xlabel(headers[0])
    axes[0].set_ylabel(headers[1])
    axes[0].grid()

    axes[1].set_title("e, e_dot, e_int vs time")
    for i in range(0, len(headers) - 1):
        axes[1].plot(time_list, [lin[i] for lin in values], label=headers[i] + legend)
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Values")
    axes[1].legend()
    axes[1].grid()

    plt.show()
    
    
import argparse

if __name__=="__main__":

    
    
    print("plotting the files")
    file_linear = r'linear.csv'
    file_angular = r'angular.csv'

    # file_linear = r'.\Lab2_Data\part5_klp0.9_klv0.5_kli0.4_kap1.2_kav0.8_kai0.4\linear.csv'
    # file_angular = r'.\Lab2_Data\part5_klp0.9_klv0.5_kli0.4_kap1.2_kav0.8_kai0.4\angular.csv'
    
    plot_errors(file_linear, ' linear')
    plot_errors(file_angular, ' angular')