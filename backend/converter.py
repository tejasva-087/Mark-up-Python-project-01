class Convert:
    subject_code = {'027': 'History', '028': 'Political Science', '029': 'Geography', '030': 'Economics',
                    '037': 'Psychology', '039': 'Sociology', '040': 'Philosophy', '041': 'Mathematics',
                    '042': 'Physics',
                    '043': 'Chemistry', '044': 'Biology', '048': 'Physical Education', '049': 'Painting',
                    '054': 'Business Studies', '055': 'Accountancy', '064': 'Home Science',
                    '065': 'Informatics Practice',
                    '066': 'Entrepreneurship', '056': 'Dance', '073': 'Legal Studies', '083': 'Computer Science',
                    '301': 'English Core', '302': 'Hindi Core', '241': 'Applied Mathematics'}

    """Class to convert the data from text file to give specific data and other needs"""
    def __init__(self, string: str):
        self.string = string

    def get_roll_no(self):  # Getting roll number of student
        if self.string.split()[0].isnumeric():
            return self.string[0:8]
        else:
            return False

    def get_name(self):  # Getting name of student
        arr = self.string.split()
        arr.pop(0)
        name = ''
        for i in range(len(arr)):
            # Checking if i(subject code) is numeric and i+1(marks) is numeric and finally i+2(grades) are of length 2
            if arr[i].isnumeric() and arr[i + 1].isnumeric() and len(arr[i + 2]) == 2:
                break
            elif arr[i].isalnum():
                name += arr[i] + ' '
        if name == '':
            return False
        else:
            return name.strip()

    def get_marks(self):
        grade = {}
        num = 1
        arr = self.string.split()
        # Checking for last index(result) to be 'pass' and after that the last marks excluding \
        # (INTEL-SUB) at index -2, -3, -4 and (grades) at index -5
        if arr[-1].lower() == 'pass' and arr[-6].isnumeric() and arr[-7].isnumeric():
            # Deleting the last elements that includes INTEL-SUB and Result
            del arr[len(arr) - 4: len(arr)]
            # Reversing the array free from the last 4 elements
            arr.reverse()
            for i in range(0, len(arr) - 1, 3):  # i = [0, 3, 6, 9, ...]
                # [grades, marks, subject_code] as we reversed the array
                # Checking for marks to be correct pattern
                marks = len(arr[i + 1]) == 3 and arr[i + 1].isnumeric()
                # Checking for subject code
                subject_code = len(arr[i+2]) == 3 and arr[i+2].isnumeric()
                # Checking the array for grades then for the marks and subject code to be numeric and of length 3
                if len(arr[i]) == 2 and marks and subject_code:
                    try:
                        grade[Convert.subject_code[arr[i+2]]] = [arr[i+1], arr[i]]
                    except KeyError:
                        grade[f'subject-code {arr[i+2]}'] =  [arr[i+1], arr[i]]
                        num += 1
                else:
                    break
            return grade

        else:
            return False

    def get_result(self):
        return self.string.split()[-1]
