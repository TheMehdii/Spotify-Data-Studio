from src.data_loader import DataLoader, Song
import sys

while True :

    print("--------------------     Spotify Data Studio     --------------------")
    print("\n1. Load Database & Append new song ")
    #
    #
    #
    #
    #
    print("7. Exit")
    print("--------------------")
    print("Enter your choice (1-7) :")
    choice = input()
    if choice == "1":
        data_path = "Data/dataset.csv"
        print("Loading ...")
        all_song = DataLoader.laod_data(data_path)
        print(f"{len(all_song)} song found !")
        break

    if choice == "7":
        print("Good bye")
        break

    else:
        print('write correctly')
        continue