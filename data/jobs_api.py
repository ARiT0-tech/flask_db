import flask

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not flask.request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in flask.request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return flask.jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=flask.request.json['team_leader'],
        job=flask.request.json['job'],
        work_size=flask.request.json['work_size'],
        collaborators=flask.request.json['collaborators'],
        start_date=flask.request.json['start_date'],
        end_date=flask.request.json['end_date'],
        is_finished=flask.request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
