from flask import Flask, render_template,url_for,redirect,request, make_response, Blueprint
from controller import Functionality

manage = Blueprint('manage', __name__, url_prefix='/')



@manage.route("/")
@manage.route("index")
@manage.route("home")
def index():
    return render_template('index.html')


@manage.route("gallery")
def display_gallery():
    return render_template('gallery.html')


@manage.route("offers")
def display_offers():
    return render_template('offers.html')


@manage.route("reservation", methods=['POST', 'GET'])
def display_reservation():
    if request.method == "GET":
        return render_template('reserve.html')
    elif request.method == "POST":

        # store data input by the users into their various db fields.
        # allocate the paths to be more precise
        first = request.form["firstName"]
        middle = request.form["MiddleName"]
        last = request.form["lastName"]
        work = request.form["occupation"]
        email = request.form["email"]
        arrival = request.form["arrivalDate"]
        departure = request.form["departureDate"]

        Functionality.db_access(first,middle,last,work,email,arrival,departure)
        Functionality.generate_pdf(first,middle, last)
        return redirect(url_for('manage.index'))

    return render_template('reserve.html')

