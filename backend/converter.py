class Convert:
    """Converts a string of given data to separated key value pairs"""

    subject_code = {'027': 'History', '028': 'Political Science', '029': 'Geography', '030': 'Economics',
                    '037': 'Psychology', '039': 'Sociology', '040': 'Philosophy', '041': 'Mathematics',
                    '042': 'Physics',
                    '043': 'Chemistry', '044': 'Biology', '048': 'Physical Education', '049': 'Painting',
                    '054': 'Business Studies', '055': 'Accountancy', '064': 'Home Science',
                    '065': 'Informatics Practice',
                    '066': 'Entrepreneurship', '056': 'Dance', '073': 'Legal Studies', '083': 'Computer Science',
                    '301': 'English Core', '302': 'Hindi Core', '241': 'Applied Mathematics'}

    def __init__(self, string: str):
        self.string = string
        self.roll_no = int(string[0:7])  # Getting the roll number at the start with specific length
        self.result = string.split().pop()  # Retrieving the last characters (PASS / FAIL)

    @property
    def name(self):
        name_str = ''
        arr = self.string.split()[1:]  # Making the array without roll number
        while True:
            # Removing a element to check for digit only string
            arr_pop = arr.pop(0)  # Removing roll number
            # Breaking for digit only string
            if arr_pop.isdigit():
                break
            # Concatenating to join name
            else:
                name_str += arr_pop + ' '
        return name_str.strip()

    @property
    def marks(self):
        score_details = {}
        # Removing the name from string then converting to array
        arr = self.string.replace(f'{self.name}', '').split()
        arr.pop(0)  # removing roll number
        for i in range(0, len(arr), 3):
            if arr[i].isdigit():
                try:
                    score_details[f'{self.subject_code[arr[i]]}'] = [int(arr[i+1]), arr[i+2]]
                except KeyError:
                    score_details[f'SUBJECT-CODE: {arr[i]}'] = [int(arr[i+1]), arr[i+2]]
            else:
                break
        return score_details

    def percentage(self):
        total_num = 0  # For calculating total number of subjects
        sum_ = 0  # For calculating the total marks of subjects
        marks = self.marks
        for i in marks.values():
            sum_ += i[0]
            total_num += 1
        return sum_ / total_num  # Returning the percentage of student

    def __repr__(self):
        return f'(Convert({self.roll_no}, {self.name}, {self.marks}, {self.result}))'

    def __str__(self):
        return f'{self.name} {self.roll_no} scored {self.marks} and is declared {self.result}'
