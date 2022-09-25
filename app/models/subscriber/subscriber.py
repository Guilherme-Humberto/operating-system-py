from typing import TypedDict
from datetime import datetime
from app.utils.files import file
from app.utils.register.register import registerModel

class SubscriberDto(TypedDict):
    name: str
    email: str

class Subscriber:
    def __init__(self, data: SubscriberDto):
        self.name = data['name']
        self.email = data['email']
        self.createdAt = datetime.now().isoformat()

    def getSubscriber(self, dataName, fileExt):
        data = file.readFile(dataName, fileExt)
        if(data == False): return { dataName: [] }

        user = filter(lambda user: user['email'] == self.email, data)
        return { dataName: list(data), "item": list(user) }

    def addSubscriber(self, modelKey, modelData, payload):
        return registerModel(modelKey, modelData, payload)

    @classmethod
    def factory(cls, data):
        subscriber = cls(data)
        subscriberData = subscriber.getSubscriber('subscribers', 'json')
        subscriberPayload = {
            "name": subscriber.name,
            "email": subscriber.email,
            "createdAt": subscriber.createdAt
        }
        subscriber.addSubscriber(
            modelKey='subscribers', 
            modelData=subscriberData, 
            payload=subscriberPayload
        )