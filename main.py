from app.models.post.post import Post
from app.models.subscriber.subscriber import Subscriber

dataSubscriber = { 'name': 'Guilherme', 'email': 'guilherme@email.com' }
dataPost = {
    'title': 'Titulo da postagemm',
    'excerpt': 'Resumo da postagem',
    'content': 'Conteudo da postagem',
    'authors': [
        { 'name': 'Guilherme', 'email': 'guilherme@email.com' },
        { 'name': 'Rafael', 'email': 'rafa@email.com' },
        { 'name': 'Samuel', 'email': 'samuel@email.com' }
    ]
}

Subscriber.factory(dataSubscriber)
Post.factory(dataPost)