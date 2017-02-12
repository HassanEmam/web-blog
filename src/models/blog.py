import datetime
import uuid

from src.common.database import Database
from src.models.post import Post


class Blog(object):

    def __init__(self, author, title, description, author_id, _id=None):
        self.author = author
        self.title= title
        self.description = description
        self.autho_id = author_id
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def from_mongo(cls, id):
        data = Database.find_one(table='blogs', data={'_id':id})
        return cls(**data)

    def get_posts(self):
        return Post.from_blog(self._id)

    def new_post(self, title, comment, date=datetime.datetime.utcnow()):

        new_post = Post(blog_id=self._id,
                        title=title,
                        comment=comment,
                        author=self.author,
                        date=date)

        new_post.save_to_mongo()

    def save_to_mongo(self):
        Database.insert('blogs', self.json())

    def json(self):
        return {'author':self.author,
                'title': self.title,
                'description': self.description,
                '_id': self._id,
                'author_id': self.autho_id}

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(table='blogs',
                              data={'author_id': author_id})
        return [cls(**blog) for blog in blogs]