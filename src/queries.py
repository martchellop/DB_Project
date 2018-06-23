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
        Type    Date    CPF     Nome
    OBS: If no events match the query, return a empty model
    """
    database = connect_database()

    model = QtSql.QSqlTableModel()
    model.setTable("Eventos")
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    model.select()

    # Queries
    q_ambos = "SELECT "
    q_casamento = "SELECT "
    q_festa = "SELECT "

    if event_type == "Ambos":
        query = QtSql.QSqlQuery(q_ambos, database)
    elif event_type == "Casamento":
        query = QtSql.QSqlQuery(q_casamento)
    elif event_type == "Festa":
        query = QtSql.QSqlQuery(q_festa, database)
    else:
        query - QtSql.QSqlQuery()


    model.setQuery(query)
    model.submitAll()

    return model


def create_uni_event(date, organizer_cpf):
    """
    Creates a new university event.

    Return:
        message: str
    The message should contain sucess or error information.

    """

    database = connect_database()

    organizer_cpf = organizer_cpf.replace('.', '')

    query = QtSql.QSqlQuery()

    query.exec_("INSERT INTO festa_tipo VALUES (to_timestamp('{0}', " \
    "'YYYY-MM-DD'), {1}, 'universitaria')".format(date, organizer_cpf))

    if query.exec_("INSERT INTO universitaria VALUES " \
        "(to_timestamp('{0}', 'YYYY-MM-DD'), {1}), {2}".format(date, organizer_cpf, None)):
        database.close()
        return "Evento inserido"

    return "Falha ao inserir"


def update_uni_event(date, organizer_cpf, new_date, new_cpf):
    """
    Updates a university event with new information

    Return:
        message: str
    The message should contain sucess or error information.
    """

    database = connect_database()

    organizer_cpf = organizer_cpf.replace('.', '')
    new_cpf = new_cpf.replace('.', '')

    query = QtSql.QSqlQuery()

    if query.exec_("UPDATE universitaria SET data = to_timestamp('{0}', 'YYYY-MM-DD')," \
            "organizador = {1} WHERE data = to_timestamp('{2}', 'YYYY-MM-DD')" \
            "AND organizador = {3}".format(new_date, new_cpf, date, organizer_cpf)):
        return "Evento atualizado"

    return "Falha ao atualizar"


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

#    query = QtSql.QSqlQuery()

#    if create and query.exec_("")


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
    If ticket_id is a number (not None) we should remove that
        ticket from the database.
    If the ticket_id is None, it means we want to add a new ticket.
        Use the Serial proprierty in the database to insert it
        as the next available number.

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


def reports(report_type):
    """
    Runs the report and returns the result as a table

    Return:
        model: QtSql.QSqlTableModel()
    Parameters:
        report_type: int
        Represents the user option according to the following key:
            0 As festas que contrataram uma chácara
            1 O custo médio das festas agrupado por tipo
            2 A média e o desvio padrão do custo de cada serviço
            3 A média do preço dos bilhetes que custam mais de 10
            4 A média da quantidade de convidados de uma festa de
                casamento
            5 As empresas que fornecem algum tipo de serviço para
                festa universitária

    OBS: If no events match the query, return a empty model
    """
    return temporary_test()     # TODO: Remove


def create_table():
    command = ""
    commands = []
    data = []

    print('Creating database schema...')

    # Read file
    with open("schema.sql", "r") as input_file:
        data = [line.rstrip() for line in input_file]

    # Join multiple lines in 1 comamnd
    for line in data:
        if ";" in line:
            command = ""
            commands.append(command + line)
        else:
            commands += line

    query = QtSql.QSqlQuery()
    for line in commands:
        query.exec_(line)


def populate_table():
    command = ""
    commands = []
    data = []

    print('Populating database...')

    # Read file
    with open("populate.sql", "r") as input_file:
        data = [line.rstrip() for line in input_file]

    # Join multiple lines in 1 comamnd
    for line in data:
        if ";" in line:
            command = ""
            commands.append(command + line)
        else:
            commands += line

    query = QtSql.QSqlQuery()
    for line in commands:
        query.exec_(line)


def connect_database():
    database = QtSql.QSqlDatabase.addDatabase('QPSQL')
    database.setDatabaseName('src/events.db')
    database.setUserName('user')
    database.setPort(5432)
    if not database.open():
        print('Unable to open database connection')
        print(database.lastError().text())



if __name__ == "__main__":

    connect_database()
    create_table()
    populate_table()


