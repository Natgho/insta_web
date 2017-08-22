from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_def import User

engine = create_engine('sqlite:///test.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

user = User("python", "python")
session.add(user)

user = User("jumpiness", "python")
session.add(user)

# commit the record the database
session.commit()

# Test connection
# resp = session.query(User.username.in_(["admin"]), User.password.in_(["password"]))
# print(resp.first())