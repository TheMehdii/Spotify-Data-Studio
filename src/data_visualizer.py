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
    
    def box(self, df_before : pd.DataFrame, df_after : pd.DataFrame, feature_name : str) :

        if df_before.empty :
            print("I can't found any data!")
            return
        

        if feature_name not in df_before.columns:
            print(f'Feature {feature_name} not found in df_before !')
            return
        
        # getting data 
        data_before = df_before[feature_name].squeeze()
        data_after = df_after[feature_name].squeeze()        
        
        
        if data_after is None or data_after.empty :
            fig, axis = plt.subplots(figsize=(10, 6))
            sbn.boxenplot(x=data_before, ax=axis, color="#4c72b0")
            axis.set_title(f"Primary Data ({feature_name.capitalize()})")
        else:
            fig, axis = plt.subplots(2, 1, figsize=(14, 6)) #general shape of box-plot

            # before clean
            sbn.boxenplot(x=data_before, ax = axis[0], color="#c44e52")
            axis[0].set_title(f"Before cleaning data ({feature_name.capitalize()})")

            # after clean
            sbn.boxenplot(x=data_after, ax = axis[1], color="#55a868")
            axis[1].set_title(f"After cleaning data ({feature_name.capitalize()})")


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
