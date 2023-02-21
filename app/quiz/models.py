from dataclasses import dataclass

from sqlalchemy import Column, BigInteger, Text, Boolean, ARRAY

from app.store.database.sqlalchemy_base import db


@dataclass
class Theme:
    id: int == None
    title: str


@dataclass
class Question:
    id: int == None
    title: str
    theme_id: int
    answers: list["Answer"]


@dataclass
class Answer:
    title: str
    is_correct: bool


class ThemeModel(db):
    __tablename__ = "themes"
    id = Column(BigInteger, primary_key=True)
    title = Column(Text, nullable=False)


class QuestionModel(db):
    __tablename__ = "questions"
    id = Column(BigInteger, primary_key=True)
    title = Column(Text, nullable=False)
    theme_id = Column(BigInteger, nullable=False)


class AnswerModel(db):
    __tablename__ = "answers"
    id = Column(BigInteger, primary_key=True)
    title = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False)
