import pdfkit
from flask import Flask, render_template,url_for,redirect,request, make_response
from app.models import Users, Booking, Base,engine
from sqlalchemy.orm import sessionmaker
import smtplib


# The declarative_base() base class contains a MetaData object where newly defined Table objects are collected.
# This object is intended to be accessed directly for MetaData - specific operations.Such as,
# to issue CREATE statements for all tables:
Base.metadata.create_all(engine)

# Maybe binding the engine to the created db
Base.metadata.bind = engine

# Making an instance of the session and binding the engine which is collected alongside the Table Objects
DBsession =  sessionmaker(bind = engine)

sessionRep = DBsession()

class Functionality:


    @staticmethod
    def db_access(first, middle, last, work, email,arrival, departure):
        """
        # Now setup an instance of the tables we are going to interact with in order to store data
        # instantiate the variables just declared up there with the relevant field in the table that the data will go to
        # giving it a path

        :param first:
        :param middle:
        :param last:
        :param work:
        :param email:
        :return:
        """
        email_string = "Hello, " + first + middle+last +" you have made a reservation for " + arrival + " to "+ departure
        clients = Users(f_name=first, m_name=middle, l_name=last, occupation=work, email_address=email)

        duration = Booking(arrival_date=arrival, departure_date=departure)
        Functionality.send_email(email_string, email)

        # then add these new stored infor to the current user session
        # commit the changes
        sessionRep.add(clients)
        sessionRep.add(duration)
        sessionRep.commit()

    @staticmethod
    def generate_pdf(first, middle, last):
        rendered = render_template('reserve.html', first = request.form["firstName"], middle = request.form["MiddleName"],
                               last=request.form["lastName"])
        pdf = pdfkit.from_string(rendered, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename = bookings.pdf'

        return response

    @staticmethod
    def send_email(response, receiver):

        # setting up the smtp server details to use
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.ehlo()

        server.starttls()

        server.login('kiraguwinnie@gmail.com', 'nimzbett')

        server.sendmail(to_addrs=receiver, from_addr='kiraguwinnie@gmail.com', msg=response)

        server.close()


