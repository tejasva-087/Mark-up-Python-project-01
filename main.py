import pickle as pkl
import csv

subject_code = {'027': 'History', '028': 'Political Science', '029': 'Geography', '030': 'Economics', '037': 'Psychology', '039': 'Sociology',
                '040': 'Philosophy', '041': 'Mathematics', '042': 'Physics', '043': 'Chemistry', '044': 'Biology', '048': 'Physical Education',
                '049': 'Painting', '054': 'Business Studies', '055': 'Accountancy', '064': 'Home Science', '065': 'Informatics Practice',
                '066': 'Enterprenurship', '056': 'Dance', '073': 'Legal Studies', '083': 'Computer Science', '301': 'English Core', '302': 'Hindi Core',
                '241': 'Applied Mathematics'}

subject_order = ["History", "Political Science", "Geography", "Economics", "Psychology", "Sociology", "Philosophy", "Mathematics", "Physics", "Chemistry"
                 "Biology", "Physical Education", "Painting" "Business Studies", "Accountancy", "Home Science", "Informatics Practice", "Enterprenurship",
                 "Dance", "Legal Studies", "Computer Science", "English Core", "Hindi Core", "Applied Mathematics"]


def add_csv_all(file_name):
    # csv file objects
    file_object_csv = open(file_name, 'w', newline='\n')
    writer_object = csv.writer(file_object_csv)
    # binary file object
    file_object_bin = open('temp.dat', 'rb')
    # Adding the subject names in order as the of the above dictionary
    arr_headings = ['Roll Number', 'Name', 'Result']
    for i in subject_order:
        arr_headings.append(i)
    arr_headings.append('Others')
    writer_object.writerow(arr_headings)
    # sorting marks according to the subject
    while True:
        data_list = []
        try:
            # Creating a array to be added to the csv file containing roll number and name
            data = pkl.load(file_object_bin)
            data_list.extend([data.pop(0), data.pop(0), data.pop(-1)])
            # Creating a dictionary of sorted marks, later to be added in array
            result = {}
            result['Others'] = ""
            for i in subject_order:
                try:
                    if data[0][i]:
                        result[i] = data[0][i][0]
                    for j in data[0].keys():
                        if j[0: 11] == '<ANONYMOUS>':
                            result['Others'] += f'{data[0][j]}'
                            break
                        continue
                except KeyError:
                    result[i] = '<NULL>'
            # Adding the generated result dictionary to the array
            for i in subject_order:
                data_list.append(result[i])
            data_list.append(result['Others'])
            
        except EOFError:
            break
        writer_object.writerow(data_list)
    file_object_bin.close()
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


read_file('sample-data.txt')
add_csv_all('csv_file.csv')
print('done')