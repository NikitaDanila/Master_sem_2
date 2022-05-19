from sqlalchemy import Column, Integer, String, ForeignKey, DATE, Float
from sqlalchemy.orm import relationship
from main import Base


class Genres(Base):
    __tablename__ = 'genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String(120))
    Tracks_relationship = relationship(
        'Tracks', back_populates='Genres_relationship')

    def __repr__(self) -> str:
        return f"Genres(GenreId = {self.GenreId}, Name = {self.Name})"


class Tracks(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String(200))
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    UnitPrice = Column(Float)
    Albums_relationship = relationship(
        'Albums', back_populates='Tracks_relationship', cascade='all, delete')
    Genres_relationship = relationship(
        'Genres', back_populates='Tracks_relationship')

    def __repr__(self) -> str:
        return f'Tracks(\n TrackId = {self.TrackId}\n Name = {self.Name}\n AlbumId = {self.AlbumId}\n\
                GenreId = {self.GenreId}\n\
                \n UnitPrice = {self.UnitPrice}\n\n)'


class Artist(Base):
    __tablename__ = 'artist'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(200))
    Albums_relationship = relationship(
        'Albums', back_populates='Artist_relationship')

    def __repr__(self) -> str:
        return f"\nArtist(\nArtistId = {self.ArtistId}\nName = {self.Name})\n\n"


class Albums(Base):
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String(50))
    ArtistId = Column(Integer, ForeignKey('artist.ArtistId'))
    Artist_relationship = relationship(
        'Artist', back_populates='Albums_relationship')
    Tracks_relationship = relationship(
        'Tracks', back_populates='Albums_relationship', cascade='all, delete')

    def __repr__(self) -> str:
        return f'\nAlbums(\nAlbumId = {self.AlbumId}\nTitle = {self.Title}\nArtistId = {self.ArtistId})\n\n'


class Invoices(Base):
    __tablename__ = 'invoices'

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer)
    InvoiceDate = Column(DATE)
    BillingAddress = Column(String(200))
    BillingCity = Column(String(50))

    def __repr__(self) -> str:
        return f'Invoices(InvoiceId = {self.InvoiceID}\nCustomerID = {self.CustomerId}\n\
            InvoiceDate = {self.InvoiceDate}\nBillingAddress = {self.BillingAddress}\n\
             BillingCity = {self.BillingCity})'


class Invoice_items(Base):
    __tablename__ = "invoice_items"

    InvoiceItemId = Column(Integer, primary_key=True)
    InvoiceId = Column(Integer)
    TrackId = Column(Integer)
    UnitPrice = Column(Float)
    Quantity = Column(Integer)

    def __repr__(self) -> str:
        return f'Invoice_items(InvoiceItemId = {self.InvoiceItemId}\nInvoiceID = {self.InvoiceId}\n\
            TrackId = {self.TrackId}\nUnitPrice = {self.UnitPrice}\nQuantity = {self.Quantity})'


class Customers(Base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Address = Column(String(50))
    Phone = Column(String(50))
    Email = Column(String(50))

    def __repr__(self) -> str:
        return f'Customers(CustomerID = {self.CustomerId}\nFirst Name = {self.FirstName}\nLast Name = {self.LastName}\n\
            Address = {self.Address}\n Phone = {self.Phone}\nEmail = {self.Email})'


class Employees(Base):
    __tablename__ = 'employees'

    EmployeeId = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    # CustomerId = Column(Integer,

    def __repr__(self) -> str:
        return f'Employees(Employee Id={self.EmployeeId}\nFirst Name={self.FirstName}\nLast Name={self.LastName}\n'
