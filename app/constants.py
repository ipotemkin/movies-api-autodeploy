from app.config import settings

JWT_KEY = settings.jwt_key
PWD_HASH_SALT = settings.pwd_hash_salt

# PWD_HASH_SALT = b"the highest secret possible"
# JWT_KEY = "SkyPro2021!"

PWD_HASH_ITERATIONS = 100_000
AC_TOKEN_EXP_TIME_MIN = 30
R_TOKEN_EXP_TIME_DAYS = 1
JWT_METHOD = "HS256"
ITEMS_ON_PAGE = 2
