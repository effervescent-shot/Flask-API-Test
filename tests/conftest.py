import pytest
from application import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import g
import os
from sqlalchemy_utils import drop_database

basedir = os.path.abspath(os.path.dirname(__file__))
config = {
    'SQLALCHEMY_DATABASE_URI' :'sqlite:///' + os.path.join(basedir, 'db_test.sqlite'),
    'SQLALCHEMY_TRACK_MODIFICATION': False,
    "TESTING": True,
}

@pytest.fixture(scope='session')
def app():
    app = create_app(config=config)
    return app

    # clean up / reset resources here


@pytest.fixture(scope='module')
def appctx(app):
    with app.app_context():
        yield app

@pytest.fixture(scope='function')
def database(appctx):
    # with app.app_context():
    #     if 'db' not in g:
    #         g.db =  SQLAlchemy(app)
    #         g.db.create_all()
    #     yield g.db
    #     g.db.session.remove()
    #     g.db.drop_all()
    from application import db as db_
    from sqlalchemy_utils.functions import create_database, database_exists
    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))
    db_.create_all()

    yield db_

    db_.session.remove()
    db_.drop_all()
        

@pytest.fixture(scope='function')
def db(database): 
    print('*****SETUP*****')
    
    breakpoint()
    import sqlalchemy as sa

    connection = database.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = database.create_scoped_session(options=options)
    session.begin_nested()

    @sa.event.listens_for(session(), 'after_transaction_end')
    def restart_savepoint(sess, trans):
        if trans.nested and not trans._parent.nested:
            session.expire_all()
            session.begin_nested()

    old_session = database.session
    database.session = session

    yield database

    print('*****FLUSH*****')
    session.remove()
    transaction.rollback()
    connection.close()
    database.session = old_session



    #drop_database(app.config['SQLALCHEMY_DATABASE_URI'])
    


@pytest.fixture()
def client(app):
    return app.test_client()


# In case there is a command line interface to be tested
@pytest.fixture()
def runner(app):
    return app.test_cli_runner()