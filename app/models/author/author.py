from typing import TypedDict
from datetime import datetime
from app.utils.files import file
from app.utils.register.register import registerModel

class AuthorDto(TypedDict):
    name: str
    email: str

class Author:
    def __init__(self, data: AuthorDto):
        self.name = data['name']
        self.email = data['email']
        self.createdAt = datetime.now().isoformat()

    def getAuthor(self, dataName, fileExt):
        data = file.readFile(dataName, fileExt)
        if(data == False): return { dataName: [] }

        author = filter(lambda author: author['email'] == self.email, data)
        return { dataName: list(data), "item": list(author) }

    def addAuthor(self, modelKey, modelData, payload):
        return registerModel(modelKey, modelData, payload)

    @classmethod
    def factory(cls, data):
        author = cls(data)
        authorData = author.getAuthor('authors', 'json')

        authorPayload = {
            "name": author.name,
            "email": author.email,
            "createdAt": author.createdAt
        }

        author.addAuthor(
            modelKey='authors', 
            modelData=authorData, 
            payload=authorPayload
        )
