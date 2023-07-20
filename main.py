import pickle as pkl

subject_code = {'027': 'History', '028': 'Political Science', '029': 'Geography', '030': 'Economics', '037': 'Psychology', '039': 'Sociology',
                '040': 'Philosophy', '041': 'Mathematics', '042': 'Physics', '043': 'Chemistry', '044': 'Biology', '048': 'Physical Education',
                '049': 'Painting', '054': 'Business Studies', '055': 'Accountancy', '064': 'Home Science', '065': 'Informatics Practice',
                '066': 'Enterprenurship', '056': 'Dance', '073': 'Legal Studies', '083': 'Computer Science', '301': 'English Core', '302': 'Hindi Core',
                '241': 'Applied Mathematics'}


def add_bin(data):
    file_object = open('temp.dat', 'wb')
    pkl.dump(data, file_object)
    file_object.close()


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
            marks[f'<ANONYMOUS> {entry}'] = [f"Subject code: {data[i]}", [data[i+1], data[i+2]]]
            entry += 1
    # For getting result
    result = data[-1]
    return print([roll_number, name, marks, result])


def read_file(file_path):
    file_object = open(file_path, 'r')
    while True:
        file_data = file_object.readline()
        if file_data == '':
            break
        elif file_data[0].isalpha():
            continue
        else:
            add_bin(get_details(file_data))
    file_object.close()


read_file('data.txt')
