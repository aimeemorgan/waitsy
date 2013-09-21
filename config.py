import redis

source = './waits.txt'
db = redis.StrictRedis(host='localhost', port=6379, db=1)