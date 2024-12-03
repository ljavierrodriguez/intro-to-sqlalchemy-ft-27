from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Text, Float, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


users_posts = Table(
    "users_posts", 
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False, primary_key=True),
    Column("post_id", Integer, ForeignKey("posts.id"), nullable=False, primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    active = Column(Boolean, default=True)
    nickname = Column(String)

    profile = relationship("Profile", backref="user", uselist=False) # [<Profile 1>] => <Profile 1>
    posts = relationship("Post", secondary=users_posts)

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    biography = Column(Text, default="")
    twitter = Column(Text, default="")
    facebook = Column(Text, default="")
    instagram = Column(Text, default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    priority = Column(Integer, default=0, comment="0=low, 1=medium, 2=high")
    done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="tasks")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    resume = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    publised_at = Column(DateTime, default=datetime.now())

    users = relationship("User", secondary=users_posts)