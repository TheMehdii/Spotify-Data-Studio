import pandas as pd

class DataAnalyzer :
    def __init__(self, songs_list):
        
        data = []
        for s in songs_list:
            row = {field : getattr(s, field) for field in s.Features}
            data.append(row)

        self.df = pd.DataFrame(data)
    
    def report_missing(self):
        print("\n" + "="*15 + " Missing Values Report " + "="*15)
        missing = self.df.isnull().sum()

        if missing.sum() > 0:
            print(missing[missing > 0])
        
        else:
            print("Perfect! No missing values found in the dataset.")
        print("="*53)
    
    def get_matrix(self):

        numeric_cols = [
            'popularity', 'duration_ms', 'danceability', 'energy', 
            'key', 'loudness', 'speechiness', 'acousticness', 
            'instrumentalness', 'liveness', 'valence', 'tempo'
        ]

        valid_cols = [c for c in numeric_cols if c in self.df.columns]
        return self.df[valid_cols].corr()