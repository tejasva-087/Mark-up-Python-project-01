from converter import Convert


with open('sample-data.txt', 'r') as file_obj:
    while True:
        data = file_obj.readline()
        if data == '':
            break
        else:
            if data[0].isdigit():
                convert_data = Convert(data)
                print(convert_data.get_roll_no())
                print(convert_data.get_name())
                print(convert_data.get_marks())
                print(convert_data.get_result())
