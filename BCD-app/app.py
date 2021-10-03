import views
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
# csrf
csrf = CSRFProtect(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
# db = SQLAlchemy(app)
# urls
app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])
# app.add_url_rule('/add', view_func=views., methods=['GET', 'POST'])

# config
app.config.from_object('config.Config')
if __name__ == "__main__":
    app.run(debug=True)
