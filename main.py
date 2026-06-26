from src.data_loader import DataLoader, Song
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
import pandas as pd
import src.data_cleaner 
import uuid # for generate random track_id by using hex
import sys
from time import sleep
from emoji import emojize
import os

green = "\033[92m"
cyan = "\033[96m"
reset = "\033[0m"
    

def menu():

    
    print(f"{cyan}╔═════════════════════════════════════════════════════════════════════════╗{reset}")
    print(emojize(f"{cyan}║{reset}            {green}Spotify Data Studio & Management System 🎵{reset}                   {cyan}║{reset}"))
    print(f"{cyan}╠═════════════════════════════════════════════════════════════════════════╣{reset}")
    print(f"{cyan}║{reset}  1. Load Dataset & View Missing Values Report                           {cyan}║{reset}")
    print(f"{cyan}║{reset}  2. Clean Missing Values (Mean / Median / KNN)                          {cyan}║{reset}")
    print(f"{cyan}║{reset}  3. Handle Outliers (IQR / Z-Score)                                     {cyan}║{reset}")
    print(f"{cyan}║{reset}  4. Add a New Song to the Dataset (Interactive Input)                   {cyan}║{reset}")
    print(f"{cyan}║{reset}  5. Calculate Genre Insights & Correlation Matrix                       {cyan}║{reset}")
    print(f"{cyan}║{reset}  6. Generate Advanced Visualizations (Plots)                            {cyan}║{reset}")
    print(f"{cyan}║{reset}  7. Exit                                                                {cyan}║{reset}")
    print(f"{cyan}╚═════════════════════════════════════════════════════════════════════════╝{reset}")

def main():
    visualizer = DataVisualizer(charts="charts")
    loader = DataLoader('Data/dataset.csv')
    dataset_loaded = False
    analyzer = None
    df_before_clean = None # for box plot

    while True:
        menu()
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if not choice:
                print("give me a number please (1-7) !")
                sleep(2)
                os.system('cls')
                continue

            elif choice == '1':
                print("\nLoading dataset ...")
                sleep(2)
                
                loader.load_data()
                analyzer = DataAnalyzer(loader.songs)
                df_before_clean = analyzer.df.copy()
                dataset_loaded = True
                print(f"\n{cyan}Dataset loaded successfully!{reset} ✅")
                sleep(3)
                os.system('cls')

            elif choice =='2':
                if not dataset_loaded :
                    sleep(3)
                    print("\nError : please load dataset first (option 1)")
                    sleep(3)
                    os.system('cls')
                    continue
                else:
                    print('Wait...')
                    sleep(2)
                    while True:
                        choice2 = input('Clean Missing Values by (Mean?/ Median? / KNN?) : ')
                        columns_impute =['popularity', 'danceability', 'energy', 'loudness', 'tempo']
                        if choice2 == 'Mean':
                            print('Using Mean...')
                            sleep(2)
                            imputer = src.data_cleaner.MeanImputer()
                            analyzer.df = imputer.impute(analyzer.df, columns_impute)
                            print('Mean used!')
                            sleep(2)
                            os.system('cls')
                            break
                        elif choice2 == 'Median':
                            print('Using Median...')
                            sleep(2)
                            imputer= src.data_cleaner.MedianImputer()
                            analyzer.df = imputer.impute(analyzer.df, columns_impute)
                            print('Median used!')
                            sleep(2)
                            os.system('cls')
                            break
                        elif choice2 == "KNN":
                            print('Using KNN...')
                            sleep(2)
                            imputer = src.data_cleaner.KNNImputer()
                            analyzer.df = imputer.impute(analyzer.df, columns_impute)
                            print('KNN used!')
                            sleep(2)
                            os.system('cls')
                            break
                        else : 
                            print("please give these option (Mean or Median or KNN)")
                        sleep(2)
            
            elif choice == '3':
                if not dataset_loaded:
                        sleep(3)
                        print("\nError: Please load the dataset first (Option 1).")
                        sleep(3)
                        os.system('cls')
                        continue
                else:
                    while True:
                        choice3 = input('which one ? (IQR / Z-Score) : ')
                        columns_handle =['popularity', 'danceability', 'energy', 'loudness', 'tempo']

                        if choice3 == 'IQR':
                            sleep(2)
                            handler = src.data_cleaner.IQROutllierHandler()
                            analyzer.df = handler.handle(analyzer.df, columns_handle)
                            sleep(3)
                            print('IQR Outlier Handleing used successfully !')
                            sleep(3)
                            os.system('cls')
                            break

                        elif choice3 =='Z-Score':
                            handler = src.data_cleaner.ZScoreOutlierHandler()
                            analyzer.df = handler.handle(analyzer.df, columns_handle)
                            sleep(3)
                            print('Z-Score Out lier handling used successfully !')
                            sleep(3)
                            os.system('cls')
                            break

                        else :
                            print('Write correctly and give me an option (IQR or Z-Score)')
                            sleep(4)
                        
            elif choice == '4':

                if not dataset_loaded :
                    sleep(3)
                    print("\nError: Please load the dataset first (Option 1).")
                    sleep(3)
                    os.system('cls')
                    continue

                print("\n" + "="*20 + " Add a New Song " + "="*20)
                try:
                    track_name = input("Enter track name: ").strip()
                    artists = input("Enter artist: ").strip()
                    genre = input("Enter genre: ").strip()
                    
                    if not track_name or not artists or not genre:
                        sleep(2)
                        raise ValueError("Track name, artists, and genre cannot be empty!")

                    popularity = int(input("Enter popularity (0-100): "))

                    default_audio_features = {
                        'duration_ms': 200000,
                        'danceability': 0.5,
                        'energy': 0.5,
                        'loudness': -6.0,
                        'speechiness': 0.05,
                        'acousticness': 0.2,
                        'instrumentalness': 0.0,
                        'liveness': 0.1,
                        'valence': 0.5,
                        'tempo': 120.0
                    }

                    random_track_id = uuid.uuid4().hex[:22] 

                    new_song = Song(
                        track_id=random_track_id,
                        artists=artists, 
                        album_name="Unknown",
                        track_name=track_name,
                        popularity=popularity, duration_ms=default_audio_features['duration_ms'], 
                        danceability=default_audio_features['danceability'],
                        energy=default_audio_features['energy'],
                        loudness=default_audio_features['loudness'],
                        speechiness=default_audio_features['speechiness'],
                        acousticness=default_audio_features['acousticness'],
                        instrumentalness=default_audio_features['instrumentalness'],
                        liveness=default_audio_features['liveness'],
                        valence=default_audio_features['valence'],
                        tempo=default_audio_features['tempo'],
                        track_genre=genre,
                        key=0,
                        mode=1,
                        explicit=False,
                        time_signature=4
                    )

                    # update csv datafile
                    loader.append_song(new_song)

                    # update dataframe
                    new_row = {field: getattr(new_song, field) for field in new_song.Features}
                    analyzer.df = pd.concat([analyzer.df, pd.DataFrame([new_row])], ignore_index=True)

                    sleep(3)
                    print("\nnew song created successfully and append!")
                    sleep(3)
                    os.system('cls')

                except ValueError as ve:
                    print(f"\n Input Validation Error: {ve}")
                except Exception as e:
                    print(f"\n An error while adding the song: {e}")
            
            elif choice == '5':
                if not dataset_loaded:
                    sleep(3)
                    print("\nError: Please load the dataset first (Option 1).")
                    sleep(3)
                    os.system('cls')
                    continue
                else :
                    print("\nCalculate Genre Insights & Correlation Matrix ...")
                    sleep(3)
                    matx = analyzer.get_matrix()
                    print("matrix generated !")
                    sleep(3)
                
            elif choice == '6':
                if not dataset_loaded:
                    sleep(3)
                    print("\nError: Please load the dataset first (Option 1).")
                    sleep(3)
                    os.system('cls')
                    continue
                else :
                    print("\nGenerating Advanced Visualizations ...")
                    my_features = 'tempo'
                    visualizer.box(df_before= df_before_clean, df_after= analyzer.df , feature_name= my_features)
                    matx = analyzer.get_matrix()
                    visualizer.heatmap_matrix(matrix= matx)
                    visualizer.scatter(df=analyzer.df)
                    print("\ncharts genertad and saved in 'charts' directory !")
                    sleep(2)
            
            elif choice == '7':
                print("\n Thank you for using Spotify Data Studio. good bye ")
                sleep(2)
                sys.exit()
            
            else :
                print("\nInvalid choice! Please select a number from 1 to 7.")
                sleep(4)
                os.system('cls')
        except Exception as e:
            print(f"\n An unexpected error: {e}")
            print(" Returning  to the main menu...")
            sleep(3)

if __name__ == "__main__":
    main()