"""
File to connect to our SGBD and perform necesary queries.


GENERAL DATA DEFINITIONS:
    event_type: str
        Options: "Ambos", "Casamento", "Festa"

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
    with open("src/sample_table.sql", "r") as input_file:
        data = [line.rstrip() for line in input_file]

    # Join multiple lines in 1 comamnd
    for line in data:
        if ";" in line:
            commands.append(command + line)
            command = ""
        else:
            command += line

    database = connect_database()

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

    query = QtSql.QSqlQuery("SELECT * FROM organizador", database)
    model.setQuery(query)
    model.submitAll()

    return model


def search_events(event_type, date_start, date_end, organizer_cpf, organizer_name):
    """
    Searches all events for events that match the users options.

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


def create_uni_event(date, organizer_cpf):
    """
    Creates a new university event.

    Return:
        message: str
    The message should contain sucess or error information.
    """
    return "Testando a inserção"    # TODO: Remove


def update_uni_event(date, organizer_cpf, new_date, new_cpf):
    """
    Updates a university event with new information

    Return:
        message: str
    The message should contain sucess or error information.
    """
    return "Testing"    # TODO: Remove


def localization_service(cep, create):
    """
    Adds or removes a localization service

    Return:
        messsage: str
    The message should contain sucess or error information.
    Parameters:
        cep: str
            ex: "99999-999"
        create: bool
    If create is True, create the guy in the database;
        If False, remove him
    """
    return "Testing"    # TODO: Remove


def update_localization_service(cep, price):
    """
    Updates a localization service of a party with a different price
    If the party hasn't hired that cep a error should be returned

    Return:
        messsage: str
    The message should contain sucess or error information.
    Parameters:
        cep: str
            ex: "99999-999"
        create: int
            ex: 1000
            No floating points are accepeted
    """
    return "Testing"


def tickets_service(date, organizer_cpf, ticket_id=None):
    """
    Adds or removes a ticket of a university party.
    If ticket_id is a number (not None) we should remove that ticket from the database.
    If the ticket_id is None, it means we want to add a new ticket.
        Use the Serial proprierty in the database to insert it as the next available number.

    Return:
        messsage: str
    The message should contain sucess or error information.
    Parameters
        cep: str
            ex: "99999-999"
        ticket_id: int
        create: bool
    If create is True, create the ticket and associate it with the party
        If False, remove the ticket from the party
    """
    return "Testing"    # TODO: Remove



def connect_database():
    database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    database.setDatabaseName('src/test_events.db')

    # TODO: Handle the error  (or not....)
    if not database.open():
        print("Something went wront")
        exit(1)

    return database


def create_table():
    # TODO
    # This should call Marcelos script to create the table
    pass


def populate_table():
    # TODO
    # This should call SOMEONES script to populate the table
    pass


def main():
    """
    Should call the necessary scripts for creating the table and populate it.
    """
    create_table()
    populate_table()


if __name__ == "__main__":
    main()
