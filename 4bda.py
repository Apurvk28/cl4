import csv

# Mapper Function
def mapper(file_path):
    mapped = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            survived = row['Survived']
            pclass = row['Pclass']
            sex = row['Sex']
            age = row['Age']

            # Skip missing age
            if age == "":
                continue

            age = float(age)

            # Male and died
            if survived == '0' and sex == 'male':
                mapped.append(("male_age", age))

            # Female and died
            if survived == '0' and sex == 'female':
                mapped.append(("female_class", pclass))

    return mapped


# Reducer Function
def reducer(mapped_data):
    from collections import defaultdict

    male_age_sum = 0
    male_count = 0
    female_class_count = defaultdict(int)

    for key, value in mapped_data:
        if key == "male_age":
            male_age_sum += value
            male_count += 1
        elif key == "female_class":
            female_class_count[value] += 1

    avg_age = male_age_sum / male_count if male_count > 0 else 0

    return avg_age, female_class_count


# Driver Code
def main():
    file_path = "titanic.csv"

    mapped = mapper(file_path)
    avg_age, female_counts = reducer(mapped)

    print("Average age of males who died:", round(avg_age, 2))

    print("\nDead females in each class:")
    for cls, count in sorted(female_counts.items()):
        print(f"Class {cls}: {count}")


if __name__ == "__main__":
    main()