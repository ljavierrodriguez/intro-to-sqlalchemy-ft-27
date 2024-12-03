from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Profile, Task

# mysql://<user>:<pass>@<host>:<port>/<database> # pymysql 
# postgresql://<user>:<pass>@<host>:<port>/<database> # psycopg2.binary
#
#engine = create_engine("sqlite:///database.db")
engine = create_engine("mysql+pymysql://root:root@localhost:3306/prueba_ft27")
#engine = create_engine("postgresql://postgres:postgres@localhost:5432/prueba_ft27")
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(engine)

if __name__ == '__main__':
    #print("Tablas creadas")
    session = SessionLocal()

    user = User()
    user.username = "john.doe@gmail.com"
    user.password = "123456"
    user.nickname = "john.doe"

    profile = Profile()
    profile.biography = "I'm student"

    user.profile = profile

    session.add(user) # INSERT INTO users (username, password, nickname) VALUES (?,?,?)
    session.commit()

    #profile = Profile()
    #profile.user_id = user.id

    #session.add(profile)
    #session.commit()

    task1 = Task(title="Task 1", priority=0, done=False, user_id=1)
    task2 = Task(title="Task 2", priority=0, done=False, user_id=1)

    session.add(task1)
    session.add(task2)
    session.commit()

    # SELECT * FROM users WHERE nickname="john.doe" LIMIT 1
    #user = session.query(User).filter_by(nickname="john.doe").first() # <User 1> : None 

    if user:
        print(user.username)
        print("Total Tareas: ", len(user.tasks))
        for task in user.tasks:
            print("Tarea: ",task.title)
        
        #task3 = Task(title="Task 3", priority=0, done=False)
        #user.tasks.append(task3)
        #session.commit()

    else:
        print("Usuario no encontrado")