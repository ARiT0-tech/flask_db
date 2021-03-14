from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/users').json)
print(get('http://127.0.0.1:8080/api/v2/users/13145515781234').json)
print(get('http://127.0.0.1:8080/api/v2/users/blda').json)

print(post('http://127.0.0.1:8080/api/v2/users').json)
print(post('http://127.0.0.1:8080/api/v2/users', json={'title': 'Mars'}).json)
print(post('http://127.0.0.1:8080/api/v2/users', json={'adag': 'Mars'}).json)
print(post('http://127.0.0.1:8080/api/v2/users', json={'title': 'Заголовок',
                                                       'content': 'Текст новости',
                                                       'user_id': 1,
                                                       'is_private': False}).json)

print(delete('http://127.0.0.1:8080/api/v2/users/9999999999').json)
print(delete('http://127.0.0.1:8080/api/v2/users/1').json)
