from data.jobs import Jobs
from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# Первая работа

def main():
    db_session.global_init("db/mars_explorer_.db")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'exploration of mineral resources'
    job.work_size = 15
    job.collaborators = '4, 3, 6'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'development of a management system'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 4
    job.job = 'analysis of atmospheric air samples'
    job.work_size = 15
    job.collaborators = '4, 5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 5
    job.job = 'Mars Rover maintenance'
    job.work_size = 5
    job.collaborators = '4'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 7
    job.job = 'preventive vaccinations of the crew'
    job.work_size = 7
    job.collaborators = '3'
    job.is_finished = False

    session.add(job)

    session.commit()


if __name__ == '__main__':
    main()