import datetime
import uuid

from src.common.database import Database


class Post:
    def __init__(self, blog_id, title, comment, author, date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.author = author
        self.comment = comment
        self._id = uuid.uuid4().hex if _id is None else _id
        self.date = date

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'title': self.title,
            'comment': self.comment,
            'date': self.date
        }

    @classmethod
    def from_mongo(cls, id):
        data = Database.find_one(table='posts', data={'_id': id})
        return cls(**data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(table='posts', data={'blog_id': id})]
