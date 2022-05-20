from pprint import pprint as pp
from app.posts.dao.posts_dao import PostsDAO

d = PostsDAO("data/posts.json")

p = d.get_all()

pp(p)