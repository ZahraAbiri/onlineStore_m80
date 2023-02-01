from django.test import TestCase
from model_bakery import baker

from users.models import Products


class TestUser(TestCase):
    def test_model_user(self):
        user = Products.objects.create(name='a30', brand='sumsong',count=3,price=820000)
        self.assertEqual(str(user), 'a30-sumsung-3-8200000')

    def test_create_user(self):
        user = baker.make(Products,name='a30', brand='sumsong',count=3,price=820000)
        self.assertEqual(str(user), 'a30-sumsung-3-8200000')
