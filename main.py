import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = ''
database = 'database_telegram_groups'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(database=database, host=host, user=username, password=password, port=port)
cur = conn.cursor()

def __read_query():
    with open("query.sql", "r") as f:
        lines = f.readlines()
    return lines

def query_result(query_num: int):
    query = __read_query()[query_num - 1]
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def first_query_data():
    result = query_result(1)
    data = {
        'Username': [i[0] for i in result],
        'Number of groups': [i[1] for i in result],
    }
    return data


def second_query_data():
    result = query_result(2)
    data = {
        'Year': [i[0] for i in result],
        'Number of groups': [i[1] for i in result],
    }
    return data


def third_query_data():
    result = query_result(3)
    data = {
        'Group name': [i[0] for i in result],
        'Subscribers': [i[1] for i in result],
    }
    return data

first_data = first_query_data()
second_data = second_query_data()
third_data = third_query_data()

data_username = first_data['Username']
data_number_of_groups = first_data['Number of groups']

fig, ax = plt.subplots()

ax.bar(data_username, data_number_of_groups)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig1, ax1 = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)

years = second_data["Year"]
number_of_groups = second_data["Number of groups"]

wedges, texts, autotexts = ax1.pie(number_of_groups,
                        autopct='%.1f%%',
                        textprops=dict(color="w"),
                        colors=plt.cm.Dark2.colors,
                        startangle=140)

ax1.legend(wedges, ['2013', '2014', '2015'], loc="best", bbox_to_anchor=(1,1))
plt.show()

data_group_name = third_data['Group name']
data_subs = third_data['Subscribers']

fig2, ax2 = plt.subplots()

ax2.bar(data_group_name, data_subs)

ax2.set_facecolor('seashell')
fig2.set_facecolor('floralwhite')
fig2.set_figwidth(12)
fig2.set_figheight(6)

plt.show()

