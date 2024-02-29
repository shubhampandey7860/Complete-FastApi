from passlib.context import CryptContext

pwd_cx = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:

    def bcrypt(password: str):
        return pwd_cx.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_cx.verify(plain_password, hashed_password)
