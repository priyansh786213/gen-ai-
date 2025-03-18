import random

# Function to build the Markov chain model
def build_markov_chain(text, n=2):
    markov_chain = {}
    words = text.split()

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])  # Create a tuple key for the Markov chain
        value = words[i + n]
        
        if key not in markov_chain:
            markov_chain[key] = []
        
        markov_chain[key].append(value)

    return markov_chain

# Function to generate text using the Markov chain model
def generate_text(markov_chain, length=50):
    # Start with a random key from the Markov chain
    current_key = random.choice(list(markov_chain.keys()))
    generated_words = list(current_key)

    for _ in range(length):
        if current_key in markov_chain:
            next_word = random.choice(markov_chain[current_key])
            generated_words.append(next_word)
            current_key = tuple(generated_words[-len(current_key):])
        else:
            break

    return ' '.join(generated_words)

# Read the input text file
def read_input_text(filename):
    with open(filename, 'r') as file:
        return file.read()

# Main function
def main():
    input_filename = "input.txt"  # Change this to your file's name
    text = read_input_text(input_filename)

    # Build the Markov chain with the text
    markov_chain = build_markov_chain(text, n=2)

    # Generate text using the Markov chain
    generated_text = generate_text(markov_chain, length=50)

    print("Generated Text:\n")
    print(generated_text)

if __name__ == "__main__":
    main()
