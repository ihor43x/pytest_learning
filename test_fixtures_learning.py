from db_learning import StudentDB
import pytest


@pytest.fixture(scope='module')
def db():
    # print('-------setup-------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    # print('-------teardown-------')
    db.close()


def test_scott_data(db):
    scot_data = db.get_data('Scott')
    assert scot_data['id'] == 1
    assert scot_data['name'] == 'Scott'
    assert scot_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
