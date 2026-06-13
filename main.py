class Song:
    def __init__(self, selftrack_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre):
        self.selftrack_id = selftrack_id
        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name
        self.popularity = popularity
        self.duration_ms =  duration_ms
        self.explicit = explicit
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valecne = valence
        self.tempo = tempo
        self.time_signature = time_signature
        self.track_genre = track_genre