class Cache:
    USER_CACHE_DIR = "tmp/user.txt"

    def save(cls, key, value):
        with open(cls.USER_CACHE_DIR, 'w') as cache:
            cache.write(f"{key}:{value}")

    def read(cls, key):
        try:
            with open(cls.USER_CACHE_DIR, 'r') as cache:
                for line in cache.readlines():
                    if key in line:
                        value = line.split(':')[1]
                        return value
        except:
            return None