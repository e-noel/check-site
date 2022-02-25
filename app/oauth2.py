from jose import JWTError, jwt
from datetime import datetime, timedelta
# Define secret key, algorithm and expiration time for token

SECRET_KEY = "398HNha0348LAweoiAWERou3678cbvaskYywe8091Ah3L4J209fbaJAVBXHNS"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded