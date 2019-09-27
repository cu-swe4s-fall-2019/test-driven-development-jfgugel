import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math_lib.py
import get_data.py


def boxplot(L, scatter.png):
   
    width=3
    height=3
    
    fig = plt.figure(figsize=(width, height) dpi=300)
    
    ax = fig.add_subplot(1, 1, 1)
    
    ax.plot(X, Y, '.')
    
    plt.savefig(scatter.png,box_inches='tight')
    
    pass


def histogram(L, hist.png):
    
    width=3
    height=3
    
    fig = plt.figure(figsize=(width,height), dpi=300)
    
    ax = fig.add_subplot(1, 1, 1)
    
    ax.hist(D, '.')
    
    plt.savefig(hist.png,bbox_inches='tight')
    
    pass


def combo(L, combo.png):
    
    width=6
    height=3
    
    fig = plt.figure(figsize=(width, height), dpi = 300)
    
    ax = fig.add_subplot(1, 2, 1)
    
    ax.plot(X, Y, '.')
    
    ax = fig.add_subplot(1, 2, 2)
    
    ax.hist(D, '.') 

    plt.savefig(combo.png,bbox_inches='tight')
    
    pass
