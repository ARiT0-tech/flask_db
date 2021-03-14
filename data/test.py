from requests import get

print(get('http://localhost:8080/api/v2/news').json)
print(get('http://127.0.0.1:8080/api/v2/users').json)
