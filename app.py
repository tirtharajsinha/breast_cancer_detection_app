import views
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
# csrf
csrf = CSRFProtect(app)

# config
app.config.from_object('config.Config')

# database connection
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(100), nullable=False)

#######################


# urls
app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])
# app.add_url_rule('/add', view_func=views., methods=['GET', 'POST'])


if __name__ == "__main__":

    # try:
    #     db.create_all()
    # except Exception as e:
    #     print(e)

    app.run(debug=True)
