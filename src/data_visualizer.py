import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd
import os
from time import sleep

class DataVisualizer:
    def __init__(self, charts = "charts" ): #name of output file
        self.charts = charts
        
        if not os.path.exists(self.charts):
            os.makedirs(self.charts)

        sbn.set_theme(style="whitegrid") #backgrond of charts
    
    def box(self, df_before : pd.DataFrame, df_after : pd.DataFrame, features: list) :

        if df_before.empty :
            print("I can't found any data!")
            return
        
        valid_features_before = [f for f in features if f in df_before.columns]
        
        if df_after is None or df_after.empty :
            fig, axis = plt.subplots(figsize=(10, 6))
            sbn.boxenplot(data=df_before[valid_features_before], ax=axis, palette="vlag")
            axis.set_title("Primary Data")
            axis.tick_params(axis='x', rotation = 45)
        else:
            fig, axis = plt.subplots(1, 2, figsize=(14, 6)) #general shape of box-plot

            # before clean
            sbn.boxenplot(data=df_before[valid_features_before], ax = axis[0], palette="vlag")
            axis[0].set_title("Before cleaning data")
            axis[0].tick_params(axis='x', rotation = 45)

            # after clean
            valid_features_after = [f for f in features if f in df_after.columns]
            sbn.boxenplot(data=df_after[valid_features_after], ax = axis[1], palette="deep")
            axis[1].set_title("After cleaning data")
            axis[1].tick_params(axis='x', rotation = 45)

        plt.tight_layout() # cut and edit
        plt.savefig(f"{self.charts}/box-chart.png")
        print('box chart created and saved in charts folder !')
        sleep(2)
        

    def scatter(self, df: pd.DataFrame):
        if df.empty:
            return
        
        genres = ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues', 'brazil']
        
        sbn.set_style("whitegrid")
        plt.figure(figsize=(10, 6)) #draw chart


        if 'track_genre' in df.columns:
            filtered_df = df[df['track_genre'].isin(genres)]
            sbn.scatterplot(data=filtered_df, x='danceability', y = 'energy', hue='track_genre', alpha= 0.6, edgecolor = 'white', linewidth = 0.5) 
        else:
            sbn.scatterplot(data=df, x='danceability', y='energy', alpha=0.6, color = 'purple', edgecolor = 'white', linewidth = 0.5)

        plt.title("Scatter chart : Danceability & Energy", fontsize =12, pad = 12)
        plt.xlabel("Danceability", fontsize = 10)
        plt.ylabel("Energy", fontsize = 10)

        if 'track_genre' in df.columns:
            plt.legend(title = 'Genres', bbox_to_anchor =(1.02, 1), loc = 'upper left', borderaxespad =0, frameon = True)
        
        plt.tight_layout()
        plt.savefig(f"{self.charts}/scatter-chat.png", dpi = 300, bbox_inches='tight') # dpi for better picture
        print('scatter chart created and saved in charts folder !')
        sleep(2)
    
    def heatmap_matrix(self, matrix : pd.DataFrame):
        if matrix.empty:
            print("matrix is empty")
            return
        
        plt.figure(figsize=(10, 8))

        sbn.heatmap(matrix, annot=True , cmap="coolwarm", fmt=".2f", vmin=-1, vmax= 1 , square= True, linewidths=0.5)

        plt.title("heatmap matrix for audio features")
        plt.tight_layout()
        plt.savefig(f"{self.charts}/heatmap_matrix_chart.png")
        print('heatmap matrix chart created and saved in charts folder !')
        sleep(2)
