import

# the telegram bot token
497483764:AAF8cxTLJ4Bt8BoMj9IMGMUNpVB6-amm2xA = os.environ['Limp_hidenbot']

# postgresql database configs
DB_NAME = 'spoilerobot'
DB_NAME = 'Limp_hidenbot'
DB_HOST = 'localhost'
DB_PASSWORD = os.environ['']

# pepper is used to season the hash of the uuid so that it's harder to brute force a uuid
if 'Limp_hidenbot' not in os.environ:
    print(''Limp_hidenbot={} to your environmental variables'.format(
        os.urandom(8).hex()
    ))
    exit(1)
HASH_PEPPER = os.environ[''Limp_hidenbot']

# the time in seconds in between timestamps of the request count statistic
REQUEST_COUNT_RESOLUTION = 600

# how many seconds before old taps are ignored
MULTIPLE_CLICK_TIMEOUT = 20

# how long in seconds to cache minor spoilers on the client-side
MINOR_SPOILER_CACHE_TIME =3600

# The maximun length (in bytes) for a inline query before an advanced spoilers has to be used
# (this is a telegram limitation)
MAX_INLINE_LENGTH = 256