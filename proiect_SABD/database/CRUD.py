
from sqlalchemy import event
from main import engine, Session
from models import *

local_session = Session(bind=engine)

'''READ/SELECT'''


def show_albums_with_ArtistId_10():

    minecraft = local_session.query(Albums).filter(Albums.ArtistId == 10).all()

    print(f'\n\nshow_albums_with_ArtistId_10 {minecraft}')


def show_tracks_on_album_13():
    print('hello')
    tracks_on_13 = local_session.query(
        Tracks).filter(Tracks.AlbumId == 1).all()

    print(f'\n\nshow_tracks_on_album_13 {tracks_on_13}')


'''DELETE'''


def delete_track():
    # album_to_delete_from = local_session.query(Albums).filter(Albums.AlbumId==1).first()
    track_to_delete = local_session.query(
        Tracks).filter(Tracks.AlbumId == 13).first()

    local_session.delete(track_to_delete)
    local_session.commit()
    show_tracks_on_album_13()


"""UPDATE"""


def update_employee_name(id, update):
    employee = local_session.query(Employees).filter(
        Employees.EmployeeId == id).first()
    print(f'Employee before update: {employee}')
    employee.FirstName = update
    local_session.commit()
    print(f'Employee after update: {employee}')


"""CREATE"""

@event.listens_for(local_session, 'after_commit')
def print_something(local_session):
    print('Trigger is ok')

def add_customer(_FirstName, _LastName, _Address, _Phone, _Email):
    customer = Customers()
    customer.FirstName = _FirstName
    customer.LastName = _LastName
    customer.Address = _Address
    customer.Phone = _Phone
    customer.Email = _Email

    local_session.add(customer)
    local_session.commit()


"""JOIN"""


def join_tables_Albums_Tracks():

    join_result = local_session.query(Albums, Tracks).join(Tracks).all()

    for album, track in join_result:
        print(album.Title, track.Name)


def join_tables_Albums_Tracks_Artist():
    '''Left join on table Albums'''
    join_result = local_session.query(Artist, Albums, Tracks).select_from(
        Albums).join(Tracks).join(Artist).all()

    for artist, album, track in join_result:
        print(
            f'Artist Name = {artist.Name} Album Title =  {album.Title} Track Name = {track.Name}')


def join_tables_with_filter():
    join_result = local_session.query(Artist.ArtistId, Artist.Name, Albums.Title).join(Albums).filter(Artist.ArtistId == 14).all()
    print(join_result)

# show_albums_with_ArtistId_10()
# show_tracks_on_album_13()
# delete_track()
# update_employee_name(1, 'Robert')
# add_customer('Henry', 'Coanda', 'str. Aviatorilor',
#              '00000000', 'henry@email.com')
# add_customer('Marius', 'Enache', 'str. fara_numar',
#              '11111111', 'mariusica@email.com')
# add_customer('test', 'inca un test', 'str. fara_numar',
#              '11111111', 'mariusica@email.com')
# # join_tables_Albums_Tracks()
join_tables_Albums_Tracks_Artist()
# join_tables_with_filter()