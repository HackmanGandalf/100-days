from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # dictionary = {}

        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price
    # })

@app.route("/all")
def get_all():
    list = []
    all_cafes = db.session.query(Cafe).all()
    # return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

    for cafe in all_cafes:
        item = cafe.to_dict()
        list.append(item)
    return jsonify(cafes=list)

@app.route("/search")
def search():
    location = request.args.get("loc")
    search = db.session.query(Cafe).filter_by(location=location).first()
    if search:
        return jsonify(cafe=search.to_dict())
    else:
        return jsonify(error={"location not found": "please try another location"})

@app.route("/add", methods=["POST"])
def add():
    new = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_socket")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffe_prices")
    )

    db.session.add(new)
    db.session.commit()
    return jsonify(response = {"Success": "Your new cafe has been added successfully."})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    new = request.args.get("new_price")
    search = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if search:
        price_to_update = Cafe.query.get(cafe_id)
        price_to_update.coffee_price = new
        db.session.commit()
        return jsonify({"success": "price updated successfully."}), 200
    else:
        return jsonify(error = {"Not found": "A cafe with that id was not found in our database."}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    key = request.args.get("api-key")
    if key == "TOPSECRETKEY":
        search = db.session.query(Cafe).filter_by(id=cafe_id).first()
        if search:
            cafe_to_delete = Cafe.query.get(cafe_id)
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"success": "Cafe deleted successfully."}), 200
        else:
            return jsonify(error = {"Not found": "A cafe with that id was not found in our database."}), 404
    else:
            return jsonify(error = {"Wrong api-key": "You're not allowed to perform that task. Make sure you have the correct api-key."}), 403


if __name__ == '__main__':
    app.run(debug=True)


