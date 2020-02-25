import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
def main():
    if len(sys.argv) == 1:
        print("args: <input file> <target var>")
        exit(0)
    fn_in = sys.argv[1]
    dg = pd.read_csv( fn_in )
    target = sys.argv[2]
    data = list()
    for row in dg.iterrows():
        data.append(row[1][target])
    print("mean = ",np.mean(data))
    print("mode = ",stats.mode(data))
    print("median = ",np.median(data))
    print("std  = ",np.std(data))
    #plt.plot(data)
    x_axis = np.linspace(min(data),max(data))
    y_axis = stats.norm.pdf(x_axis,np.mean(data),np.std(data))
    plt.plot(x_axis,y_axis)
    plt.show()

if __name__ == "__main__":
    main()
