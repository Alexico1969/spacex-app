from db import get_db
from passlib.hash import pbkdf2_sha256

def add_user(name     = None,
             password = None,
             email    = None,
             role     = None #* Current Roles are admin or scorer
            ):
    connection = get_db()
    sql = connection.cursor()
    if name and password and email:
        user = get_user(email=email)
        if not user:
            hashed = pbkdf2_sha256.hash(password)
            if not role:
                role = 'scorer'
            sql.execute('''
                insert into users (name, password, email, role) values (%s, %s, %s, %s)
            ''', [name, hashed, email, role])
            connection.commit()
            return get_user(email=email)

def get_user(id=None, email=None):
    connection = get_db()
    sql = connection.cursor()
    if id:
        sql.execute('''
            select * from users where id = %s
        ''', [id])
        return sql.fetchone()
    if email:
        sql.execute('''
            select * from users where email = %s
        ''', [email])
        return sql.fetchone()

def verify_user(email=None, password=None):
    user = get_user(email=email)
    if user:
        hashedPassword = user[3]
        checkHash = pbkdf2_sha256.verify(password, hashedPassword)
        if checkHash:
            return user
    return False

def update_user():
    return