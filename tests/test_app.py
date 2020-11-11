import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Todos


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                          SECRET_KEY='TEST_SECRET_KEY',
                          DEBUG=True
                          )
        return app

    def setUp(self):
        db.create_all()

        sample1 = Todos(name="Test-Todo")

        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestAdd(TestBase):
    def test_add_todo(self):
        response = self.client.post(
            url_for('add'),
            data=dict(name="Tester")
        )
        self.assertIn(b'Tester', response.data)
