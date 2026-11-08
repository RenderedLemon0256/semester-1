# Worksheet 1.3: Task 3

# Your code for the overall grade classification
def gradeClassification(average):
    """Returns the grade classification given the entered average marks"""
    if average >= 70:
        return "1"
    elif average >= 60:
        return "2:1"
    elif average >= 50:
        return "2:2"
    elif average >= 40:
        return "3"
    else:
        return "F"

def calculateAverage(student):
    """Returns the average mark from the given student"""
    parts = student.split(',')
    total = 0
    moduleCount = 0
    for module in parts:
        try:
            mark = int(module)
            total += mark
            moduleCount +=1
        except:
            continue
    return total / moduleCount
def getStudentId(student):
    """Returns the student Id of the given student"""
    parts = student.split(',')
    return parts[0]

# ask for filename of the student file
fileName = input("Enter the student file to read from: ")

# open the file
with open(fileName) as f:
    with open(fileName+"_out.csv",'w') as f2:
# read in the data, and for each student calculate their average grade and classification
        student = f.readline()
        studentId = getStudentId(student)
        average = calculateAverage(student)
        classification = gradeClassification(average)
        f2.write(f"{studentId},{average:.2f},{classification}")


# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder