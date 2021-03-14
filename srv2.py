from flask import Flask, jsonify
from flask_restful import Api

from data import db_session
from data.jobs import Jobs
from data.users import User
from flask import make_response
from data import db_session, news_api, jobs_api, news_resources, users_resource
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


# @app.errorhandler(404)
# def not_found(error):
#    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    app.register_blueprint(news_api.blueprint)
    app.register_blueprint(jobs_api.blueprint)
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()
    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.email = "email@email.ru"
    db_sess.add(user)
    db_sess.commit()
    app.run(port=8080)


api.add_resource(news_resources.NewsListResource, '/api/v2/news')
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')
if __name__ == '__main__':
    main()
