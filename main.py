from src.data_loader import DataLoader, Song
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
import src.data_cleaner 

import sys
from time import sleep


def menu():
    green = "\033[92m"
    cyan = "\033[96m"
    reset = "\033[0m"
    
    print(f"{cyan}╔═════════════════════════════════════════════════════════════════════════╗{reset}")
    print(f"{cyan}║{reset}           {green}Spotify Data Studio & Management System{reset}                       {cyan}║{reset}")
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
    
    while True():
        menu()
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if not choice:
                print("give me a number please (1-7) !")
                sleep(2)
                continue

            elif choice == '1':
                print("\n Loading dataset ...")
                sleep(2)
                df = DataLoader.laod_data('dataset.csv')
                dataset_loaded = True
                print("Dataset loaded successfully!")
                sleep(2)

            elif choice =='2':
                if not dataset_loaded :
                    print("\n Error : please load dataset first (option 1)")
                    sleep(2)
                    continue
                else:
                    print('wait ...')
                    sleep(2)
                    while True:
                        choice2 = input('Clean Missing Values by(Mean?/ Median? / KNN?)')
                        if not choice2 : 
                            print("please give these option (Mean or Median or KNN)")
                            sleep(2)
                            continue
                        elif choice2 == 'Mean':
                            src.data_cleaner.MeanImputer()
                            break
                        elif choice2 == 'Median':
                            src.data_cleaner.MedianImputer()
                            break
                        elif choice2 == "KNN":
                            src.data_cleaner.KNNImputer()
                            break
            
            elif choice == '3':
                choice3 = input('Which one ? (IQR / Z-Score)')
                if not dataset_loaded:
                        print("\n[!] Error: Please load the dataset first (Option 1).")
                        continue
                print("\n[+] Handling outliers (IQR/Z-Score)...")
                sleep(2)
                if choice3 == 'IQR':
                    src.data_cleaner.IQROutllierHandler()
                elif choice3 =='Z-Score':
                    src.data_cleaner.ZScoreOutlierHandler()
                
            elif choice == '4':

                if not dataset_loaded or df is None:
                    print("\nError !: Please load the dataset first (Option 1). ")
                    continue

                print("\n" + "="*20 + " Add a New Song " + "="*20)
                try:
                    track_name = input("Enter track name: ").strip()
                    artists = input("Enter artist(s): ").strip()
                    genre = input("Enter genre: ").strip()
                    
                    if not track_name or not artists or not genre:
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

                    track_id = str(len(df) + 1)

                    from src.data_loader import Song
                    new_song = Song(
                        track_id=track_id, track_name=track_name, artists=artists, 
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
                        genre=genre
                    )


                    DataLoader.append_song(new_song)

                    
                    print("\n created successfully!")
                    sleep(2)
                    print(f" Generated Object: {new_song}")
                    sleep(2)

                except ValueError as ve:
                    print(f"\n Input Validation Error: {ve}")
                except Exception as e:
                    print(f"\n An error while adding the song: {e}")
            
            elif choice == '5':
                if not dataset_loaded:
                    print("\n Error !: Please load the dataset first (Option 1).")
                    sleep(2)
                    continue
                else :
                    print("\n Calculate Genre Insights & Correlation Matrix ...")
                    DataAnalyzer.get_matrix(df)
                
            elif choice == '6':
                if not dataset_loaded:
                    print("\n Error !: Please load the dataset first (Option 1).")
                    sleep(2)
                    continue
                else :
                    print("\n Generating Advanced Visualizations ...")
                    DataVisualizer.box(df)
                    DataVisualizer.heatmap_matrix(df)
                    DataVisualizer.scatter(df)
                    print("\n charts genertad and saved in 'charts' directory !")
                    sleep(2)
            
            elif choice == '7':
                print("\n Thank you for using Spotify Data Studio. good bye ")
                sleep(2)
                sys.exit()
            
            else :
                print("\n Invalid choice! Please select a number from 1 to 7.")
        except Exception as e:
            print(f"\n An unexpected error: {e}")
            print(" Returning  to the main menu...")

if __name__ == "__main__":
    main()