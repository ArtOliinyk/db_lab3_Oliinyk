import psycopg2

username = 'postgres'
password = ''
database = 'database_telegram_groups'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database)
cursor = conn.cursor()

tables = {
    "accounts(acc_id, username, phone_number, pseudonym, registration_date)": "oliyn/PycharmProjects/DB_lab3/imports/accounts.csv",
    "groups(group_id, group_name, number_of_subscribers, creation_date, invitation_link)": "oliyn/PycharmProjects/DB_lab3/imports/groups.csv",
    "account_group(acc_id, group_id)": "oliyn/PycharmProjects/DB_lab3/imports/account_group.csv",
}

import_table_from_csv_query = "COPY {} FROM '{}' DELIMITER ',' CSV HEADER;"

with conn:
    cur = conn.cursor()

    for table, import_file in tables.items():
        cur.execute(import_table_from_csv_query.format(table, import_file))
