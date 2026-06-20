import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd

class DataVisualizer:
    def __init__(self, charts = "charts" ): #name of output file
        self.charts = charts
        
        sbn.set_theme(style="whitegrid") #backgrond of charts
    
    def box(self, df_befor : pd.DataFrame, df_after : pd.DataFrame, featurs: list) :

        if df_befor.empty or df_after.empty:
            print("I can't found any data!")
            return
        fig, axis = plt.subplot(1, 2, figsize=(14, 6)) #general shape of box-plot

        # befor clean
        sbn.boxenplot(data=df_befor[featurs], ax = axis[0], palette="vlag")
        axis[0].set_title("Befor cleaning data")
        axis[0].tick_parms(axis='x', rotation = 45)

        # after clean
        sbn.boxenplot(data=df_befor[featurs], ax = axis[1], palette="Deep")
        axis[0].set_title("After cleaning data")
        axis[0].tick_parms(axis='x', rotation = 45)

        plt.tight_layout() # cut and edit
        plt.savefig(f"{self.charts}/box-plot.png")
        plt.show()