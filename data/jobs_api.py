import flask

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    jobs = db_session.create_session().query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict() for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not flask.request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in flask.request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
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
    jobs_all = db_session.create_session().query(Jobs).all()
    jobs_item = list()
    for item in jobs_all:
        for i in item.to_dict():
            if i == 'team_leader':
                jobs_item.append(item.to_dict()['team_leader'])
    if jobs.team_leader in jobs_item:
        return flask.jsonify({'error': 'Id already exists'})
    db_sess.add(jobs)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
