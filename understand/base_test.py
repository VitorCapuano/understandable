import codecs
import json
import os

import pytest
import vcr

CASSETTES_PATH = os.path.join(
    os.path.abspath(
        os.path.dirname(__file__)
    ), 'fixtures/cassettes'
)


class BaseTestCase(object):

    @classmethod
    @pytest.fixture(scope='class', autouse=True)
    def setup(cls):
        cassettes_dir = 'understand/fixtures/cassettes'

        cls.vcr = vcr.VCR(
            serializer='json',
            cassette_library_dir=cassettes_dir,
            record_mode='once'
        )

    @staticmethod
    def load_fixture_object(name):

        object_path = 'fixtures/objects/{name}.json'.format(
            name=name
        )

        obj = {}

        with open(object_path, 'rb') as _file:
            reader = codecs.getreader('utf-8')
            obj = json.load(reader(_file))

        return obj

    @staticmethod
    def get_cassette(cassette_name):
        with open(
            os.path.join(
                CASSETTES_PATH, cassette_name
            ), 'r'
        ) as cassette:
            return json.load(cassette)
