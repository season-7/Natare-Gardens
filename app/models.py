from sqlalchemy import Column,String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    client_id = Column(Integer, primary_key=True, autoincrement=True  )
    f_name = Column(String())
    m_name = Column(String())
    l_name = Column(String())
    occupation = Column(String())
    email_address = Column(String())
    rate = Column(String())

    def __init__(self, f_name, m_name, l_name, occupation, email_address):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.occupation = occupation
        self.email_address = email_address

    def __repr__(self):
            return '<User %r, First_Name %r, Middle_Name %r, Last_Name %r, Occupation %r, Email %r>' % self.client_id,\
                   self.f_name, self.m_name, self.l_name, self.occupation, self.email_address


class Booking(Base):
    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    arrival_date = Column(String())
    departure_date = Column(String())
    room_type = Column(String())

    user_id = Column(Integer, ForeignKey("users.client_id"))
    var = relationship(Users)


    # initialises the model, creating instances for each field
    def __init__(self, arrival_date, departure_date):
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        # self.room_type = room_type
        # self.var = var
        # , room_type, var


       # represent the object when we query for it.
    def __repr__(self):
        return '<ID %r, Booking_date %r, Arrival_date %r, ' \
               'Departure_date %r, Room_type %r,>'.format(self.booking_id, self.arrival_date, self.departure_date,
                                                                                                    self.room_type)


engine = create_engine("sqlite:///natare.db")
Base.metadata.create_all(engine)