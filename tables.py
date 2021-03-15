from connection import get_db

def creat_tables():
    # Creates all the tables
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''
        create table if not exists user
        (
            "id" integer primary key autoincrement,
            "username" text,
            "email" text,
            "hashed_password": text,
        )
    ''')

def migrate_tables():
    # Use this function to alter tables
    pass

def dump_database():
    # This function dumps the database so that we have a backup
    pass

def load_backup_database():
    # This function loads a backup of the database from a dump file
    pass