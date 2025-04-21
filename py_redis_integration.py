import redis
import json
import unittest

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('mykey', 'Hello Anmol')
value = r.get('mykey')
print(value.decode()) 

r = redis.Redis()
data = {'name': 'Anmol', 'age': 22}
r.set('user:1000', json.dumps(data))
user_data = json.loads(r.get('user:1000'))
print(user_data['name']) 
print(user_data['age'])


class TestRedisIntegration(unittest.TestCase):
    def setUp(self):
        self.r = redis.Redis(decode_responses=True)
        self.r.flushdb()

    def test_set_and_get(self):
        self.r.set('key', 'value')
        self.assertEqual(self.r.get('key'), 'value')

    def test_store_dict_as_json(self):
        import json
        data = {'anmol': 'jain'}
        self.r.set('dict', json.dumps(data))
        loaded = json.loads(self.r.get('dict'))
        self.assertEqual(loaded['anmol'], 'jain')

if __name__ == '__main__':
    unittest.main()