from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/jobs').json)
print(get('http://127.0.0.1:8080/api/v2/jobs/13145515781234').json)
print(get('http://127.0.0.1:8080/api/v2/jobs/blda').json)

print(post('http://127.0.0.1:8080/api/v2/jobs').json)
print(post('http://127.0.0.1:8080/api/v2/jobs', json={'job': 'Mars'}).json)
print(post('http://127.0.0.1:8080/api/v2/jobs', json={'adag': 'Mars'}).json)
print(post('http://127.0.0.1:8080/api/v2/jobs', json={'team_leader': 2,
                                                      'job': 'deployment of residential modules 1 and 2',
                                                      'work_size': 15,
                                                      'collaborators': '2, 3',
                                                      'is_finished': False}).json)

print(delete('http://127.0.0.1:8080/api/v2/jobs/9999999999').json)
print(delete('http://127.0.0.1:8080/api/v2/jobs/1').json)
