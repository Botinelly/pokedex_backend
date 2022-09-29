from src.db.database import Database
import pytest
from src.config.config import settings


DATABASE_TEST_HOST = settings.DATABASE_DOCKER_HOST
DATABASE_PORT = settings.DATABASE_PORT


def test_connection_fail():
    Database.initialize(host='error', port='ad')
    res = Database.connect_to_db()
    assert False is res


def test_connection_ok():
    Database.initialize(host=DATABASE_TEST_HOST, port=DATABASE_PORT)
    res = Database.connect_to_db()
    assert True is res


def test_connection_with_number_error():
    Database.initialize(host=DATABASE_TEST_HOST, port='dasd')
    res = Database.connect_to_db()
    assert False is res


# @pytest.mark.skip(reason="this connection should return False")
def test_connection_with_host_wrong_error():
    Database.initialize(host='business_rules_d', port=DATABASE_PORT)
    res = Database.connect_to_db()
    assert False is res


# @pytest.mark.skip(reason="this connection should return False")
def test_connection_check_conection_ok():
    Database.initialize(host=DATABASE_TEST_HOST, port=DATABASE_PORT)
    Database.connect_to_db()
    res = Database.check_connection()
    assert True is res


def test_connection_check_conection_fail():
    Database.initialize(host='business_rules_d', port=DATABASE_PORT)
    Database.connect_to_db()
    res = Database.check_connection()
    assert False is res


def test_connection_disconnet_OK():
    Database.initialize(host=DATABASE_TEST_HOST, port=DATABASE_PORT)
    Database.connect_to_db()
    Database.check_connection()
    res = Database.disconnect_from_db()
    assert True is res


@pytest.mark.skip(reason="the method close always return true")
def test_connection_disconnet_FAIL():
    Database.initialize(host='business_rules_d', port=DATABASE_PORT)
    Database.connect_to_db()
    res = Database.disconnect_from_db()
    assert False is res


def test_connection_disconnet_FAIL_2():
    Database.initialize(host='business_rules_d', port=DATABASE_PORT)
    res = Database.disconnect_from_db()
    assert False is res
