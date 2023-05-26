from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(pwd: str):
    return pwd_context.hash(pwd)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)