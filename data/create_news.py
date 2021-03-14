import flask

from data import db_session
from data.news import News

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/news', methods=['POST'])
def create_news():
    if not flask.request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in flask.request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return flask.jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    news = News(
        title=flask.request.json['title'],
        content=flask.request.json['content'],
        user_id=flask.request.json['user_id'],
        is_private=flask.request.json['is_private']
    )
    db_sess.add(news)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
