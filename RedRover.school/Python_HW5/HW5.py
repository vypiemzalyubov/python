# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов - как минимум один атрибут должен быть с уровнем доступа private. 
#      Соответственно, для получания значений этого атрибута нужно использовать методы get и set

class Music():
    def __init__(self, genre, bpm, creation_date, artist = 'NoName', festival = 'Some of kind'):
        self.genre = genre
        self.bpm = bpm
        self.creation_date = creation_date
        self.artist = artist
        self.festival = festival
    
    def information(self, fields=['genre', 'bpm', 'creation_date', 'artist', 'festival']):
        for field in fields:
            print(f'{field.capitalize()}: {getattr(self, field)}')
    

house_music = Music('House', 128, 1980, 'David Guetta', 'Tommorowland')
rap_music = Music('Rap', 85, 1974, 'Eminem', 'Hip Hop Kemp')
house_music.information()
print()
rap_music.information()
print()


class Album(Music):
    def __init__(self, release_date, album_name, duration, price, genre, artist):
        super().__init__(genre, None, None, artist)
        self.release_date = release_date
        self.album_name = album_name
        self.duration = duration
        self._price = price

    def get_duration(self, duration):
        print(f'{duration} it is duration of album')
        return duration
    
    def get_price(self):
        return self._price
    
    def set_price(self, value):
        self._price = value

    def album_information(self):
        super().information(fields=['genre', 'artist'])
        print(f'Release date of album: {self.release_date}')
        print(f'Album name: {self.album_name}')
        print(f'Duration of album: {self.duration} min')
        print(f'Price of album: {self._price}$')

house_album = Album(release_date=2009, album_name='One Love', duration=60, price=10, genre='House', artist='David Guetta')
house_album.set_price(20)
rap_album = Album(release_date=2002, album_name='The Eminem Show', duration=77, price=30, genre='Rap', artist='Eminem')

house_album.album_information()
print()
rap_album.album_information()