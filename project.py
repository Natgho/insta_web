from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/insta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class InstaDB(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_pass = db.Column(db.String(50))

    def __init__(self, name, city):
        self.user_name = name
        self.user_pass = city


@app.route('/')
def hello_world():
    return 'Hello World!'

def add_user_test():
    tmp_test = InstaDB('Sezer', 'test_pass')
    db.session.add(tmp_test)
    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    add_user_test()
    app.run(port=5000, debug=True)

