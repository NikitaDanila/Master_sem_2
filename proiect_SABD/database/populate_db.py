from main import engine, Session
from models import Albums, Artist, Genres, Tracks, Employees

local_session = Session(bind=engine)


def add_artist():
    artist_array = [
        Artist(ArtistId=0, Name='Akira Yamaoka'),
        Artist(ArtistId=1, Name='William Basinski'),
        Artist(ArtistId=2, Name='Crystal Castles'),
        Artist(ArtistId=3, Name='Slater'),
        Artist(ArtistId=4, Name='Nine Inch Nails'),
        Artist(ArtistId=5, Name='Pendulum'),
        Artist(ArtistId=6, Name='Death Grips'),
        Artist(ArtistId=7, Name='Molchat Doma'),
        Artist(ArtistId=8, Name='Toby Fox'),
        Artist(ArtistId=9, Name='The Cure'),
        Artist(ArtistId=10, Name='C418'),
        Artist(ArtistId=11, Name='Virgil Iantu'),
        Artist(ArtistId=12, Name='Black Eyes Peas'),
        Artist(ArtistId=13, Name='James Shimoji'),
        Artist(ArtistId=14, Name='Run The Jewels'),
        Artist(ArtistId=15, Name='Tool'),
    ]
    for artist in artist_array:
        local_session.add(artist)


def add_album():
    album_array = [
        Albums(AlbumId=0, Title='Silent Hill 2', ArtistId=0),
        Albums(AlbumId=1, Title='Lamentations', ArtistId=1),
        Albums(AlbumId=2, Title='Crystal Castles', ArtistId=2),
        Albums(AlbumId=3, Title='ESI', ArtistId=3),
        Albums(AlbumId=4, Title='The Slip', ArtistId=4),
        Albums(AlbumId=5, Title='Hold Your Colour', ArtistId=5),
        Albums(AlbumId=6, Title='The Money Store', ArtistId=6),
        Albums(AlbumId=7, Title='Etazhi', ArtistId=7),
        Albums(AlbumId=8, Title='Undertale', ArtistId=8),
        Albums(AlbumId=9, Title='Wish', ArtistId=9),
        Albums(AlbumId=10, Title='Minecraft Volume Alpha', ArtistId=10),
        Albums(AlbumId=11, Title='Ieri si Azi', ArtistId=11),
        Albums(AlbumId=12, Title='Monkey Business', ArtistId=12),
        Albums(AlbumId=13, Title='Redline', ArtistId=13),
        Albums(AlbumId=14, Title='Run The Jewels 2', ArtistId=14),
        Albums(AlbumId=15, Title='Lateralus', ArtistId=15),
        Albums(AlbumId=16, Title='Minecraft Volume Beta', ArtistId=10)
    ]
    for album in album_array:
        local_session.add(album)


def add_genre():
    genre_array = [
        Genres(GenreId=0, Name='Electronic'),
        Genres(GenreId=1, Name='Rock'),
        Genres(GenreId=2, Name='Hip Hop'),
        Genres(GenreId=3, Name='Soundtrack'),
        Genres(GenreId=4, Name='Ambient')
    ]
    for genre in genre_array:
        local_session.add(genre)


def add_track():
    track_array = [
        Tracks(TrackId=0, Name='Theme of Laura',
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=1, Name='White Noiz',
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=2, Name='Forest', AlbumId=1,
               GenreId=3, UnitPrice=60),
        Tracks(TrackId=3, Name='A World of Madness',
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=4, Name='Promise (Reprise)',
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=5, Name='Ashes and Ghost',
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=6, Name='Null Moon',
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=7, Name="Heaven's Night",
               AlbumId=1, GenreId=3, UnitPrice=60),
        Tracks(TrackId=8, Name='Yellow Line',
               AlbumId=13, GenreId=3, UnitPrice=60),
        Tracks(TrackId=9, Name='Inuki', AlbumId=13,
               GenreId=3, UnitPrice=60),
        Tracks(TrackId=10, Name='REDLINE Title',
               AlbumId=13, GenreId=3, UnitPrice=60),
        Tracks(TrackId=11, Name="Boy's Memory",
               AlbumId=13, GenreId=3, UnitPrice=60),
        Tracks(TrackId=12, Name='Winner March',
               AlbumId=13, GenreId=3, UnitPrice=60),
        Tracks(TrackId=13, Name='ROBOWORLD TV',
               AlbumId=13, GenreId=3, UnitPrice=60),
        Tracks(TrackId=14, Name='TV Show',
               AlbumId=13, GenreId=3, UnitPrice=60),
        Tracks(TrackId=15, Name='ROBOWORLD',
               AlbumId=13, GenreId=3, UnitPrice=60),
    ]
    for track in track_array:
        local_session.add(track)


def add_employees():
    employee_array = [
        Employees(EmployeeId=0, FirstName='Nikita', LastName='Danila'),
        Employees(EmployeeId=1, FirstName='Robert', LastName='Nicolescu')
    ]
    for employee in employee_array:
        local_session.add(employee)


def add_customers():
    # Customers
    pass


add_artist()
add_album()
add_track()
add_employees()
add_genre()
# add_customers()

local_session.commit()
