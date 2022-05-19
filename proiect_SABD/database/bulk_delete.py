from models import *
from main import Session, engine
from sqlalchemy import event

local_session = Session(bind=engine)

@event.listens_for(local_session, 'after_bulk_delete')
def bulk_delete_trigger(local_session):
    pass

bulk_delete = local_session.query(Tracks.Name).filter(Tracks.AlbumId == 1).all()

print(bulk_delete)