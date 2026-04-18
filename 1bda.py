# Mapper function
def mapper(file_path):
    word_pairs = []
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()  # normalize
                word_pairs.append((word, 1))
    
    return word_pairs


# Reducer function
def reducer(mapped_data):
    reduced_data = {}
    
    for word, count in mapped_data:
        if word in reduced_data:
            reduced_data[word] += count
        else:
            reduced_data[word] = count
    
    return reduced_data


# Main function to get frequency of a specific word
def word_frequency(file_path, target_word):
    mapped = mapper(file_path)
    reduced = reducer(mapped)
    
    target_word = target_word.lower()
    
    return reduced.get(target_word, 0)


# Example usage
if __name__ == "__main__":
    file_path = "sample.txt"
    target_word = "data"
    
    freq = word_frequency(file_path, target_word)
    print(f"Frequency of '{target_word}':", freq)