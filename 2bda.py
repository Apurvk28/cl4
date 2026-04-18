# Mapper function
def mapper(A, B):
    mapped = []

    # A: (i, k, value)
    for i in range(len(A)):
        for k in range(len(A[0])):
            for j in range(len(B[0])):
                mapped.append(((i, j), ('A', k, A[i][k])))

    # B: (k, j, value)
    for k in range(len(B)):
        for j in range(len(B[0])):
            for i in range(len(A)):
                mapped.append(((i, j), ('B', k, B[k][j])))

    return mapped


# Reducer function
def reducer(mapped_data):
    from collections import defaultdict

    grouped = defaultdict(list)

    # Group by key (i, j)
    for key, value in mapped_data:
        grouped[key].append(value)

    result = {}

    # Compute multiplication
    for key, values in grouped.items():
        a_vals = {}
        b_vals = {}

        for tag, k, val in values:
            if tag == 'A':
                a_vals[k] = val
            else:
                b_vals[k] = val

        total = 0
        for k in a_vals:
            if k in b_vals:
                total += a_vals[k] * b_vals[k]

        result[key] = total

    return result


# Driver code
def main():
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    mapped = mapper(A, B)
    result = reducer(mapped)

    print("Result Matrix:")
    for (i, j), value in sorted(result.items()):
        print(f"C[{i}][{j}] = {value}")


if __name__ == "__main__":
    main()