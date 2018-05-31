"""
File to connect to our SGBD and perform necesary queries.


DATA DEFINITIONS:

event_type: str
    "Ambos", "Casamento", "Festa"

date_start: datetime.date

date_end: datetime.date

organizer_cpf: str
    "nnn.nnn.nnn.nn" where "n" is a numeric(0-9)
    None    if the user doesnt care

organizer_name: str
    None    if the user doesnt care
"""

from PyQt5 import QtSql, QtGui


def temporary_test():
    # TODO: Remove after everything is ready.
    command = ""
    commands = []
    data = []
    
    # Read file
    with open("sample_table.sql", "r") as f:
        data = [line.rstrip() for line in f]

    # Join multiple lines in 1 comamnd
    for line in data:
        if ";" in line:
            commands.append(command + line)
            command = ""
        else:
            command += line

    db = connect_database()

    # For temporary executing the scripts
    """
    query = QtSql.QSqlQuery()
    for line in commands:
        query.exec_(line)
    """

    model = QtSql.QSqlTableModel()
    model.setTable('organizador')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)

    model.select()
    print(model.rowCount())

    query = QtSql.QSqlQuery("SELECT * FROM organizador", db)
    model.setQuery(query)
    model.submitAll()

    return model


def search_events(event_type, date_start, date_end, organizer_cpf, organizer_name):
    """
    Return:
        model: QtSql.QSqlTableModel()

    Expected order for weddings:
        Type    Date    CPF     Nome    Conjuge1    Conjuge2

    In case "Ambos" is choosen as event_type, we do not include Conjuges.
    Expected order for parties and both:
        Type    Date    CPF     Nome    Conjuge1    Conjuge2

    OBS: If no events match the query, return a empty model
    """
    return temporary_test()     # TODO: Remove


def connect_database():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test_events.db')

    # TODO: Handle the error 
    if not db.open():
        print("Something went wront")
        exit(1)

    return db


def create_table():
    pass


def populate_table():
    pass


def main():
    """
    Should call the necessary scripts for creating the table and populate it.
    """
    create_table()
    populate_table()


if __name__ == "__main__":
    main()
