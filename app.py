from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    new_user = User(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)