from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database URL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'  # Using SQLite as db
db = SQLAlchemy(app)

# Defining the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Creating the database tables
with app.app_context():
    db.create_all()

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message": "Person created successfully"}), 201

@app.route('/api/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_person(user_id):
    person = Person.query.get_or_404(user_id)

    if request.method == 'GET':
        return jsonify({"id": person.id, "name": person.name})

    if request.method == 'PUT':
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({"error": "Name is required"}), 400

        person.name = name
        db.session.commit()
        return jsonify({"message": "Person updated successfully"})

    if request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
