from application import db
from application.models import Todos
db.drop_all()
db.create_all()
