import os
import csv

class Song:
    Featurs = ['track_id', 'artists', 'album_name', 'track_name', 'popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature', 'track_genre']
   
    def __init__(self, track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre):
        self._track_id = track_id
        self._artists = artists
        self._album_name = album_name # (_) for avoid from settar error (read-only)
        self._track_name = track_name
        self._track_genre = track_genre
        self.popularity = int(popularity)
        self.duration_ms =  int(duration_ms)
        self.explicit = explicit if isinstance(explicit, bool) else (str(explicit).lower() == "true")
        self.danceability = float(danceability)
        self.energy = float(energy)
        self.key = int(key)
        self.loudness = float(loudness)
        self.mode = int(mode)
        self.speechiness = float(speechiness)
        self.acousticness = float(acousticness)
        self.instrumentalness = float(instrumentalness)
        self.liveness = float(liveness)
        self.valence = float(valence)
        self.tempo = float(tempo)
        self.time_signature = int(time_signature)
    
    def _check(self, Feature : str, val: float, min_v : float = 0.0, max_v : float = 1.0): # for avoid from repeat (dry)
        if not (min_v <= val <= max_v):
            raise ValueError(f"{Feature}  range error ! it must be in range (({min_v})-({max_v})) not {val}")
        else:
            return val
        
    @property
    def popularity(self):
        return self._popularity
    
    @popularity.setter
    def popularity(self, value):
        self._popularity = self._check("popularity", value, 0, 100)

    @property
    def danceability(self):
        return self._danceability
    
    @danceability.setter
    def danceability(self, value):
        self._danceability = self._check("danceability", value, 0, 1)

    @property
    def energy(self):
        return self._energy
    
    @energy.setter
    def energy(self, value):
        self._energy = self._check("energy", value, 0, 1)

    @property 
    def duration_ms(self):
        return  self._duration_ms
    
    @duration_ms.setter
    def duration_ms(self, value):
        self._duration_ms = self._check("duration", value, 1000, 600000)
    
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, value):
        self._key = self._check("key", value, -1, 15)

    @property
    def loudness(self):
        return  self._loudness 
    
    @loudness.setter
    def loudness(self, value):
        self._loudness = self._check("loudness", value, -35, -1)

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value):
        self._mode =  self._check("mode", value, 0, 1)

    @property
    def speechiness(self):
        return self._speechiness
    
    @speechiness.setter
    def speechiness(self, value):
        self._speechiness = self._check("speechiness", value, 0, 1)

    @property
    def acousticness(self):
        return self._acousticnees
    
    @acousticness.setter
    def acousticness(self, value):
        self._acousticness = self._check("acousticness", value, 0, 1)

    @property
    def instrumentalness(self):
        return self._instrumentalness
    
    @instrumentalness.setter
    def instrumentalness(self, value):
        self._instrumentalness = self._check("instrumentalness", value, 0, 1)
    
    @property
    def liveness(self):
        return self._liveness
    
    @liveness.setter
    def liveness(self, value):
        self._liveness = self._check("liveness", value, 0, 1)

    @property
    def valence(self):
        return  self._valence 
    
    @valence.setter
    def valence(self, value):
        self._valence = self._check("valence", value, 0, 1)

    @property
    def tempo(self):
        return self._tempo
    
    
    @tempo.setter
    def tempo(self, value):
        self._tempo = self._check("tempo", value, 70, 210)
    
    @property
    def time_signature(self):
        return self._time_singnature

    @time_signature.setter
    def time_signature(self, value):
        self._time_signature = self._check("time_signature", value, 3, 7) 

    @property
    def track_id(self) :
        return self._track_id
    
    @property
    def artists(self):
        return self._artists
    
    @property
    def album_name(self):
        return self._album_name
    
    @property
    def track_name(self):
        return self._track_name
    
    @property
    def track_genre(self):
        return self._track_genre


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.songs = []

    def laod_data(self):
        self.songs= []
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path} does not exists")

        with open(self.file_path, "r", encoding='utf-8') as file:
            for row in csv.DictReader(file):
                try :
                    song = Song(
                        track_id=row['track_id'], artists=row['artists'], album_name=row['album_name'],
                        track_name=row['track_name'], popularity=row['popularity'], duration_ms=row['duration_ms'],
                        explicit=row['explicit'], danceability=row['danceability'], energy=row['energy'],
                        key=row['key'], loudness=row['loudness'], mode=row['mode'], speechiness=row['speechiness'],
                        acousticness=row['acousticness'], instrumentalness=row['instrumentalness'],
                        liveness=row['liveness'], valence=row['valence'], tempo=row['tempo'],
                        time_signature=row['time_signature'], track_genre=row['track_genre']
                    )
                    self.songs.append(song)
                except ValueError as e:
                    print(f"we have {e} Error!")
        
        return self.songs
    
    def append_song(self, song: Song) :
        self.songs.append(song)

        vojod_file = os.path.exists(self.file_path)

        with open(self.file_path, "a", encoding= 'utf-8', newline='') as file :
            writer = csv.DictWriter(file, fieldnames= song.Featurs) # write featurs for any song

            if not vojod_file:
                writer.writeheader() # if col is not exists it writes
            
            new_row = {field : getattr(song, field) for field in song.Featurs}      #getarr = access value of featurs whitout song.featurs and avoid repeat (dry)
            writer.writerow(new_row)

