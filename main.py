import pickle as pkl
import csv
import mysql.connector as sql

subject_code = {'027': 'History', '028': 'Political Science', '029': 'Geography', '030': 'Economics',
                '037': 'Psychology', '039': 'Sociology', '040': 'Philosophy', '041': 'Mathematics', '042': 'Physics',
                '043': 'Chemistry', '044': 'Biology', '048': 'Physical Education', '049': 'Painting',
                '054': 'Business Studies', '055': 'Accountancy', '064': 'Home Science', '065': 'Informatics Practice',
                '066': 'Entrepreneurship', '056': 'Dance', '073': 'Legal Studies', '083': 'Computer Science',
                '301': 'English Core', '302': 'Hindi Core', '241': 'Applied Mathematics'}

subject_order = ["History", "Political Science", "Geography", "Economics", "Psychology", "Sociology", "Philosophy",
                 "Mathematics", "Physics", "Chemistry", "Biology", "Physical Education", "Painting", "Business Studies",
                 "Accountancy", "Home Science", "Informatics Practice", "Entrepreneurship", "Dance", "Legal Studies",
                 "Computer Science", "English Core", "Hindi Core", "Applied Mathematics"]


def seperator_all():
    file_object_bin = open('temp.dat', 'rb')
    data_container = [['Roll Number', 'Name', 'Result']]
    for i in subject_order:
        data_container[0].append(i)
    data_container[0].append('Others')
    while True:
        data_list = []
        try:
            # Creating an array to be added to the csv file containing roll number and name
            data = pkl.load(file_object_bin)
            data_list.extend([int(data.pop(0)), data.pop(0), data.pop(-1)])
            # Creating a dictionary of sorted marks, later to be added in array
            result = {'Others': ''}
            for i in subject_order:
                try:
                    if data[0][i]:
                        result[i] = int(data[0][i][0])
                    for j in data[0].keys():
                        if j[0: 11] == '<ANONYMOUS>':
                            result['Others'] += f'{data[0][j][0], data[0][j][1][0], data[0][j][1][1]}'
                            del data[0][f"{j}"]
                            break
                        continue
                except KeyError:
                    result[i] = ''

            # Adding the generated result dictionary to the array
            for i in subject_order:
                data_list.append(result[i])
            data_list.append(result['Others'])
            data_container.append(data_list)

        except EOFError:
            file_object_bin.close()
            break
    return data_container


def seperator_single(subject):
    file_obj = open('temp.dat', 'rb')
    data_container = [['Roll Number', 'Name', f'{subject} Marks', 'Grades']]
    while True:
        try:
            data = pkl.load(file_obj)
            data_list = [int(data.pop(0)), data.pop(0)]
            try:
                if data[0][subject]:
                    data_list.extend([int(data[0][subject][0]), data[0][subject][1]])
                    data_container.append(data_list)
            except KeyError:
                continue
        except EOFError:
            break
    file_obj.close()
    return data_container


def database_connect(_host, _user, _passwd, database, table, result_type, subject=''):
    def single_query_generator():
        data = seperator_single(subject)
        data_heading = data.pop(0)
        cursor.execute(f"CREATE TABLE {table}"
                       f"({data_heading[0].replace(' ', '_')} INT PRIMARY KEY,"
                       f"{data_heading[1].replace(' ', '_')} VARCHAR(30) NOT NULL,"
                       f"{data_heading[2].replace(' ', '_')} VARCHAR(20),"
                       f"{data_heading[3]} char(2))")
        for j in data:
            cursor.execute(f'INSERT INTO {table} VALUES'
                           f'({j[0]}, "{j[1]}", "{j[2]}", "{j[3]}")')
        sql_connection.commit()

    def all_query_generator():
        data = seperator_all()
        data_heading = data.pop(0)
        data_heading.pop(-1)
        query = f"CREATE TABLE {table}" \
                f"({data_heading.pop(0).replace(' ', '_')} INT PRIMARY KEY," \
                f"{data_heading.pop(0).replace(' ', '_')} VARCHAR(30) NOT NULL," \
                f"{data_heading.pop(0).replace(' ', '_')} VARCHAR(10) NOT NULL,"
        for j in data_heading:
            query += f"{j.replace(' ', '_')} INT NULL,"
        query += f"Others TEXT)"
        cursor.execute(query)
        for j in data:
            query = f'INSERT INTO {table} VALUES ('
            for k in j:
                if type(k) == int:
                    query += f'{k}, '
                elif type(k) == str:
                    if k:
                        query += f'"{k}",'
                    else:
                        query += f"NULL,"
            cursor.execute(query[0: len(query) - 1] + ')')
            sql_connection.commit()

    sql_connection = sql.connect(host=_host, user=_user, passwd=_passwd)
    if not sql_connection.is_connected():
        return -1
    cursor = sql_connection.cursor()
    # Checking for existence of database
    cursor.execute('SHOW DATABASES')
    for i in cursor.fetchall():
        if i[0] == database:
            cursor.execute(f'USE {database}')
            break
    else:
        cursor.execute(f'CREATE DATABASE {database};')
        cursor.execute(f'USE {database}')

    # Checking for existence of table
    cursor.execute('SHOW TABLES')
    for i in cursor.fetchall():
        if i[0] == table:
            sql_connection.close()
            return -1
    if result_type == 1:
        single_query_generator()
    else:
        all_query_generator()
    sql_connection.close()


def add_csv(file_name, subject):
    # csv file objects
    file_obj_csv = open(file_name, 'w', newline='\n')
    writer_object = csv.writer(file_obj_csv)
    writer_object.writerows(seperator_single(subject))
    file_obj_csv.close()


def add_csv_all(file_name):
    # csv file objects
    file_object_csv = open(file_name, 'w', newline='\n')
    writer_object = csv.writer(file_object_csv)
    writer_object.writerows(seperator_all())
    file_object_csv.close()


def get_details(data):
    data = data.split()
    # For getting roll number
    roll_number = data.pop(0)
    # For getting name
    name = ''
    while True:
        if data[0].isdigit():
            break
        else:
            name += data[0] + ' '
            data.pop(0)
    # For getting marks {subject: [marks, grades]}
    marks = {}
    entry = 1
    for i in range(0, len(data), 3):
        try:
            if data[i].isdigit():
                marks[subject_code[data[i]]] = [data[i+1], data[i+2]]
        except KeyError:
            marks[f'<ANONYMOUS> {entry}'] = [
                f"Subject code: {data[i]}",
                [f"marks:{data[i+1]}", f"grades:{data[i+2]}"]
            ]
            entry += 1
    # For getting result
    result = data[-1]
    return [roll_number, name, marks, result]


def read_file(file_path):
    file_object = open(file_path, 'r')
    file_obj_bin = open('temp.dat', 'wb')
    while True:
        file_data = file_object.readline()
        if file_data == '':
            break
        elif file_data[0].isalpha():
            continue
        else:
            details = get_details(file_data)
            pkl.dump(details, file_obj_bin)
    file_obj_bin.close()
    file_object.close()
