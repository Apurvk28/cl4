# Function to assign grade
def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'D'


# Mapper Function
def mapper(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Format: Name Marks
            name, marks = line.strip().split()
            marks = int(marks)
            
            grade = get_grade(marks)
            yield (name, grade)


# Reducer Function
def reducer(mapped_data):
    result = {}
    
    for name, grade in mapped_data:
        result[name] = grade   # one grade per student
    
    return result


# Driver Function
def main():
    file_path = "students.txt"

    # Map Phase
    mapped = list(mapper(file_path))

    # Reduce Phase
    reduced = reducer(mapped)

    # Output
    print("Student Grades:")
    for name, grade in reduced.items():
        print(f"{name} -> {grade}")


if __name__ == "__main__":
    main()