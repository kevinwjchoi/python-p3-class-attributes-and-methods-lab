class Song:

    all:  list = []
    count: int = 0
    genres: 'list[str]' = []
    artists: 'list[str]' = []
    genre_count: 'dict[str, int]' = {}
    artist_count: 'dict[str, int]' = {}

    def __init__(self, name: str, artist: str, genre: str):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increase_song_count()
        
        Song.add_song_to_all(self)
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)


    @classmethod
    def increase_song_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def add_to_genres(cls, genre, increment=1):
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = increment
        else:
            Song.genre_count[genre] += increment

    @classmethod
    def add_to_artists(cls, artist, increment=1):
        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = increment
        else:
            Song.artist_count[artist] += 1
