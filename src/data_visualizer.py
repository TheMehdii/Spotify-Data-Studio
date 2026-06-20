import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd
import os

class DataVisualizer:
    def __init__(self, charts = "charts" ): #name of output file
        self.charts = charts
        
        if os.path.exists(self.charts):
            os.makedirs(self.charts)

        sbn.set_theme(style="whitegrid") #backgrond of charts
    
    def box(self, df_befor : pd.DataFrame, df_after : pd.DataFrame, featurs: list) :

        if df_befor.empty or df_after.empty:
            print("I can't found any data!")
            return
        fig, axis = plt.subplots(1, 2, figsize=(14, 6)) #general shape of box-plot

        # befor clean
        sbn.boxenplot(data=df_befor[featurs], ax = axis[0], palette="vlag")
        axis[0].set_title("Befor cleaning data")
        axis[0].tick_params(axis='x', rotation = 45)

        # after clean
        sbn.boxenplot(data=df_after[featurs], ax = axis[1], palette="Deep")
        axis[1].set_title("After cleaning data")
        axis[1].tick_params(axis='x', rotation = 45)

        plt.tight_layout() # cut and edit
        plt.savefig(f"{self.charts}/box-chart.png")
        plt.show()

    def scatter(self, df: pd.DataFrame):
        if df.empty:
            return
        
        plt.figure(figsize=(8, 6)) #draw chart


        if 'genre' in df.columns:
            sbn.scatterplot(data=df, x='danceability', y = 'energy', hue='genre', alpha= 0.6, palette='viridis') 
        else:
            sbn.scatterplot(data=df, x='danceability', y='energy', alpha=0.6, color = 'purple')

        plt.title("Scatter chart : Danceability & Energy")
        plt.xlabel("Danceability")
        plt.ylabel("Energy")

        if 'genre' in df.columns:
            plt.legend(bbox_to_anchor=(1.05, 1), loc = 'upper left')
        
        plt.tight_layout()
        plt.savefig(f"{self.charts}/scatter-chat.png")
    
    def heatmap_matrix(self, matrix : pd.DataFrame):
        if matrix.empty:
            print("matrix is empty")
            return
        
        plt.figure(figsize=(10, 8))

        sbn.heatmap(matrix, annot=True , cmap="coolwarm", fmt=".2f", vmin=-1, vmax= 1 , square= True, linewidths=0.5)

        plt.title("heatmap matrix for audio features")
        plt.tight_layout()
        plt.savefig(f"{self.charts}/heatmap_matrix_chart.png")
        plt.show()
