import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique = True)
    mail = Column(String, unique = True)
    password = Column(String)
    description = Column(String, nullable = True)
    profile_img = Column(String)
    tlf = Column(String)
    age = Column(String, nullable = True)
    gender = Column(String, nullable = True)


class Followers(Base):
    __tablename__ = 'Followers'
    
    followers_id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer)
    user_to_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_link = relationship("User", back_populates="parent", uselist=False)


class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True)
    text = Column(String, nullable = True)
    location = Column(String)
    time = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))
    user_link = relationship("User", back_populates="parent", uselist=False)
    media_id = Column(Integer)
    media_link = relationship("Media", back_populates="parent", uselist=False)
    like_id = Column(Integer)
    like_link = relationship("Like", back_populates="parent", uselist=False)   


class Media(Base):
    __tablename__ = 'media'

    media_id = Column(Integer, primary_key=True)
    url = Column(String)
    type_media = Column(Enum) 

    post_id = Column(Integer, ForeignKey('post.id'))
    post_link = relationship("Post", back_populates="parent", uselist=False)
    

class Like(Base):
    __tablename__ = 'like'

    like_id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user_link = relationship("User", back_populates="parent", uselist=False)


class Comment(Base):
    __tablename__ = 'comment'
    
    comment_id = Column(Integer, primary_key=True)
    text = Column(String)

    post_id = Column(Integer, ForeignKey('post_id'))
    post_link = relationship("Post", back_populates="parent", uselist=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_link = relationship("User", back_populates="parent", uselist=False)
    like_id = Column(Integer, ForeignKey('like.id'))
    like_link = relationship("Like", back_populates="parent", uselist=False)
    

def to_dict(self):
    return {}


render_er(Base, 'diagram.png')