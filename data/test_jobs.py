from requests import get, post, delete

print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 4,
                                                   'job': 'deployment of reфвфidential modules 1 and 2',
                                                   'work_size': 1512,
                                                   'collaborators': '3',
                                                   'is_finished': False}).json)
# Добавление не полной информации
print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 1,
                                                   'job': 'deployment of reфвфidential modules 1 and 2',
                                                   'is_finished': False}).json)
# Добавление уже существующего
print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 1,
                                                   'job': 'deployment of reфвфidential modules 1 and 2',
                                                   'work_size': 1512,
                                                   'collaborators': '3',
                                                   'start_date': '123',
                                                   'end_date': '234',
                                                   'is_finished': False}).json)
# Добавление пустого запроса
print(post('http://127.0.0.1:8080/api/jobs').json)

print(get('http://127.0.0.1:8080/api/jobs').json)
