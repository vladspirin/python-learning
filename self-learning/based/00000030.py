class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

mona_lisa = Painting(input(), input(), int(input()))
print(f'"{mona_lisa.title}" by {mona_lisa.artist} ({mona_lisa.year}) hangs in the {mona_lisa.museum}.')

