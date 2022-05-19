from models import *
from main import Session, engine
from sqlalchemy import event

local_session = Session(bind=engine)


@event.listens_for(local_session, 'after_bulk_delete')
def bulk_delete_trigger(local_session, query=local_session.query(Tracks).filter(Tracks.AlbumId == 1).delete()):
    query

bulk_delete = local_session.query(Albums).filter(Albums.AlbumId == 1).delete()

local_session.commit()

print(bulk_delete)
