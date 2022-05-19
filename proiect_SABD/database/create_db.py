from main import Base, engine
from models import *


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
