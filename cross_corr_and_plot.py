import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

def main():
    if len(sys.argv) == 1:
        print("args: <filename> <y axis> <x axis> <x threshold> <y threshold> <row name?>")
        exit(0)
    fn_in = sys.argv[1]
    data =  pd.read_csv( fn_in )
    target = sys.argv[2]
    if len(sys.argv) >= 5:
        target2 = sys.argv[3]
        xThresh = float(sys.argv[4])
        yThresh = float(sys.argv[5])
    else:
        xThresh = 0
        yThresh = 0
        target2 = get_correlated_vars(data,target,0)
    if len(sys.argv) == 7:
        spec_target_name = sys.argv[6].split(',')
    else:
        spec_target_name = list()
    plot_target_vars(data,target2,target,spec_target_name,xThresh,yThresh)

#ptv: given a column as an x and y axis, plot the two against each other.
def plot_target_vars(data,target1,target2,name,xThresh,yThresh):
    xaxis = list()
    yaxis = list()
    data = data.sort_values(by=[target1])
    for row in data.iterrows():
        if xThresh and row[1][target1] < xThresh:
            continue
        if yThresh and row[1][target2] < yThresh:
            continue
        if name and str(row[1][1]) in name:
            plt.text(row[1][target1],row[1][target2],str(row[1][1]))
        xaxis.append(row[1][target1])
        yaxis.append((row[1][target2]))
    plt.title(str(target2)+" over "+str(target1))
    plt.xlabel(target1)
    plt.ylabel(target2)
    plt.plot(np.unique(xaxis), np.poly1d(np.polyfit(xaxis, yaxis, 1))(np.unique(xaxis)))
    plt.scatter(xaxis,yaxis)
    plt.plot(xaxis,yaxis,'rs')
    plt.show()

#gcv: given a target variable, looks for a correlation between each column and 
#returns the best fitting column
def get_correlated_vars(data,target,cor_thresh):
    best_col = ""
    best_score = 0
    for col in data.columns:
        try:
            cross_corr = data[col].corr(data[target])
            if abs(cross_corr) > cor_thresh:
                print(col," ",cross_corr)
            if abs(cross_corr) > best_score and not(col == target):
                best_score = abs(cross_corr)
                best_col = col
        except:
            continue
    return best_col

if __name__ == "__main__":
    main()
