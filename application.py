from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)




@app.route('/')
def index():
    return "Hello!"


# now we need to create tabl;es for orur DB
#@ we can do this through models
#models are represnetation on how a database should look abnd what field/columns it should have
# this sounds familiar - classes
class Books(db.Model):
    # setup our db kind of similar to how we would in sql with a couple iof changes
    # w elist our dat field . culums and data tyoes and any othe rparams beed for col 
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.column(db.String(90))
    author = db.column(db.String(120))
    publisher = db.column(db.String(120))
    # the oithe rthings abotu model this is uniqe instea dof jus tusing raw sql quries, is you can add method or functions
    # oen commone is the __repr__ funcrtion that when you xcall the drinks nametills return its name and descritpion
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"