from db_learning import StudentDB
import pytest
db = None


def setup_module(module):
    print('-------setup-------')
    global db
    db = StudentDB()
    db.connect('data.json')


def teardown_module(module):
    print('-------teardown-------')
    db.close()


def test_scott_data():
    scot_data = db.get_data('Scott')
    assert scot_data['id'] == 1
    assert scot_data['name'] == 'Scott'
    assert scot_data['result'] == 'pass'


def test_mark_data():
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
