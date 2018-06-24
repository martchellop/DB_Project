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

    database = connect_database('db_project')

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
    # Queries
    ambosQ = "SELECT "
    casamentoQ = "SELECT "
    festaQ = "SELECT * FROM festa_tipo"

    if event_type == "Ambos":
        return select_database(ambosQ)
    elif event_type == "Casamento":
        return select_database(casamentoQ)
    elif event_type == "Festa":
        return select_database(festaQ)


def create_uni_event(date, organizer_cpf):
    """
    Creates a new university event.

    Return:
        message: str
    The message should contain sucess or error information.

    """

    db = connect_database('db_project')

    organizer_cpf = organizer_cpf.replace('.', '')

    query = QtSql.QSqlQuery()

    query.exec_("INSERT INTO festa_tipo VALUES (to_timestamp('{0}', " \
            "'YYYY-MM-DD'), {1}, 'universitaria')".format(date, organizer_cpf))

    if not query.exec_("INSERT INTO universitaria VALUES " \
        "(to_timestamp('{0}', 'YYYY-MM-DD'), {1}, NULL)".format(date, organizer_cpf)):
        return "Falha ao inserir"

    return "Evento inserido"


def update_uni_event(date, organizer_cpf, new_date, new_cpf):
    """
    Updates a university event with new information

    Return:
        message: str
    The message should contain sucess or error information.
    """

    db = connect_database('db_project')

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

    db = connect_database('db_project')
    query = QtSql.QSqlQuery()

    insertQ = ""
    removeQ = ""

    if (create and query.exec_(insertQ)) or
        (not create and query.exec_(removeQ)):
        return "Alterações aplicadas"

    return "Falha ao alterar"


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
    db = connect_database('db_project')
    query = QtSql.QSqlQuery()

    updateQ = ""

    if query.exec_(updateQ):
        return "Alterações aplicadas"

    return "Falha ao alterar"


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
    """

    db = connect_database('db_project')
    query = QtSql.QSqlQuery()

    insertQ = ""
    removeQ = ""

    if (ticket_id == None and query.exec_(insertQ)) or
        (ticket_id != None and query.exec_(removeQ)):
        return "Alterações aplicadas"

    return "Falha ao alterar"


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

    q_0 = "SELECT uni.*\
	FROM universitaria uni\
	INNER JOIN universitaria_espaco ue\
		ON ue.data = uni.data AND\
                ue.organizador = uni.organizador\
	INNER JOIN espaco esp\
		ON ue.espaco = esp.cep\
	WHERE esp.categoria = 'chacara';"

    q_1 = "select tipo, avg(preco) as media from  \
    ((select u.*, ft.tipo from universitaria u inner \
    join festa_tipo ft on u.data = ft.data and \
    u.organizador = ft.organizador) union \
    (select c.data, c.organizador, c.preco, ft.tipo from casamento c \
    inner join festa_tipo ft on c.data = ft.data and \
    c.organizador = ft.organizador)) as z group by tipo;"

    q_2 = "SELECT avg(preco) as media, stddev_samp(preco) as std\
	FROM universitaria_espaco;"

    q_3 = "SELECT avg(preco) as media\
	FROM bilhete\
	WHERE preco > 10;"

    q_4 = "SELECT data, organizador, count(nome) as quantidade\
	FROM lista_casamento\
	GROUP BY data, organizador;"

    q_5 = "SELECT distinct et.tipo, l.empresa\
	FROM universitaria uni\
	INNER JOIN universitaria_espaco ue\
		ON ue.data = uni.data AND \
                ue.organizador = uni.organizador\
	INNER JOIN espaco esp\
		ON ue.espaco = esp.cep\
	INNER JOIN locacao l\
		ON esp.empresa = l.empresa\
	INNER JOIN empresa_tipo et\
		ON l.empresa = et.CNPJ\
UNION\
SELECT distinct et.tipo, t.empresa\
	FROM universitaria uni\
	INNER JOIN aluga a\
		ON uni.data = a.data and uni.organizador = a.organizador\
	INNER JOIN transporte t\
		ON a.empresa = t.empresa\
	INNER JOIN empresa_tipo et\
		ON t.empresa = et.CNPJ;"


    if(report_type == 0):
        return select_database(q_0)
    elif(report_type == 1):
        return select_database(q_1)
    elif(report_type == 2):
        return select_database(q_2)
    elif(report_type == 3):
        return select_database(q_3)
    elif(report_type == 4):
        return select_database(q_4)
    elif(report_type == 5):
        return select_database(q_5)


def exec_database(inputF):
    command = ""
    commands = []
    data = []

    db = connect_database('db_project')

    # Read file
    with open(inputF, "r") as input_file:
        data = [line.rstrip() for line in input_file]

    # Join multiple lines in 1 comamnd
    for line in data:
        if ";" in line:
            commands.append(command + line)
            command = ""
        else:
            command += line

    query = QtSql.QSqlQuery()
    for line in commands:
        print(line)
        print(query.exec_(line))


def connect_database(name):
    database = QtSql.QSqlDatabase.addDatabase('QPSQL')
    database.setDatabaseName(name)

    if not database.open():
        print('Unable to open database connection')
        print(database.lastError().text())

    return database


def create_database(name):
    p_db = connect_database('postgres')
    query = QtSql.QSqlQuery()
    query.exec_('create database ' + name);
    return True

def select_database(query):
    db = connect_database('db_project')
    model = QtSql.QSqlTableModel()
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

    model.select()

    q = QtSql.QSqlQuery(query, db)

    model.setQuery(q)
    model.submitAll()

    return model



if __name__ == "__main__":
    print('Creating database...')
    create_database('db_project')

    print('Cleaning past executions...')
    exec_database('clean.sql')

    print('Creating database schema...')
    exec_database('schema.sql')

    print('Populating database...')
    exec_database('populate.sql')


