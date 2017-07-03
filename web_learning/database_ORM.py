from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
import sqlite3

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    print 'ok!'
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/learning')

DBsession = sessionmaker(bind= engine)

session = DBsession()


# new_user = User(id='5', name='bob')
#
# session.add(new_user)
#
# session.commit()
user = session.query(User).filter(User.id=='5').one()

print user.name
session.close()

