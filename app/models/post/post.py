from typing import TypedDict
from app.utils.files import file
from app.models.author.author import Author
from app.utils.register.register import registerModel

class PostDto(TypedDict):
    title: str
    excerpt: str
    content: str

class Post:
    def __init__(self, data: PostDto):
        self.slug = data['title'].replace(' ', '-').lower()
        self.title = data['title']
        self.excerpt = data['excerpt']
        self.content = data['content']
        self.authors = []

    def getPost(self, dataName, fileExt):
        data = file.readFile(dataName, fileExt)
        if(data == False): return { dataName: [] }

        post = filter(lambda post: post['slug'] == self.slug, data)
        return { dataName: list(data), "item": list(post) }

    def assignAuthors(self, author):
        return self.authors.append(author)

    def addPost(self, modelKey, modelData, payload):
        if (len(self.authors) < 1): raise ValueError('Author cannot be empty') 
        return registerModel(modelKey, modelData, payload)

    @classmethod
    def factory(cls, data):
        post = cls(data)
        postData = post.getPost('posts', 'json')

        for author in data['authors']:
            Author.factory(author)
            post.assignAuthors(author)

        postPayload = {
            "slug": post.slug,
            "title": post.title,
            "excerpt": post.excerpt,
            "content": post.content,
            "authors": data['authors']
        }

        post.addPost(
            modelKey='posts', 
            modelData=postData, 
            payload=postPayload
        )

    