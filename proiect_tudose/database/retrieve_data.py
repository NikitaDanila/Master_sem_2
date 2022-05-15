from main import engine, Session
from models import *

local_session = Session(bind=engine)

def show_albums_with_ArtistId_10():

    minecraft = local_session.query(Albums).filter(Albums.ArtistId==10).all()

    print(f'\n\nshow_albums_with_ArtistId_10 {minecraft}')

def show_tracks_on_album_13():
    print('hello')
    tracks_on_13 = local_session.query(Tracks).filter(Tracks.AlbumId==1).all()

    print(f'\n\nshow_tracks_on_album_13 {tracks_on_13}')

def delete_track():
    # album_to_delete_from = local_session.query(Albums).filter(Albums.AlbumId==1).first()
    track_to_delete = local_session.query(Tracks).filter(Tracks.AlbumId==1).first()

    local_session.delete(track_to_delete)
    local_session.commit()
    show_tracks_on_album_13()

# show_albums_with_ArtistId_10()
# show_tracks_on_album_13()
delete_track()
