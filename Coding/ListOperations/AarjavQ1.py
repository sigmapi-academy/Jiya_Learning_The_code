def process_student_data(raw_data_list):
    tutorial_groups = {}  # Step 1: create the main dictionary

    for student_list in raw_data_list:  # Step 2: loop through each student
        # Step 3 & 4: build individual student dictionary, clean data
        student_dict = {
            'TutorialGroup': student_list[0],
            'Student ID': student_list[1],
            'School': student_list[2],
            'Name': student_list[3],
            'Gender': student_list[4],
            'CGPA': float(student_list[5])  # Ensure CGPA is a float
        } 

        group_name = student_list[0]  # Get the tutorial group name

        # Step 6 & 7: If group not present, add it
        if group_name not in tutorial_groups:
            tutorial_groups[group_name] = []

        # Step 8: add student to the appropriate group list
        tutorial_groups[group_name].append(student_dict)

    # Step 9: return structured dictionary
    return tutorial_groups

def main():
    raw_data = [
        ["GroupA", "S101", "SchoolX", "Rashmi", "F", "8.6"],
        ["GroupB", "S102", "SchoolY", "Raghav", "M", "7.2"],
        ["GroupA", "S103", "SchoolX", "Aarjav", "M", "9.0"],
        ["GroupB", "S103", "SchoolX", "Aarjee", "F", "9.2"],
    ]

    result = process_student_data(raw_data)
    print(result)

if __name__ == '__main__' :
    main()
    