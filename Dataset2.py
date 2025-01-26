from datasets import load_dataset
from collections import Counter
from tqdm import tqdm

def load_arabic_billion_words(split="train", limit=None):
    
    # Load the dataset
    dataset = load_dataset('lightonai/ArabicWeb24', data_files='ArabicWeb24/**/*.arrow', split=split)
    
    # Take a subset of 8,000,000 samples
    if limit:
        # dataset = dataset.shuffle(seed=42).select(range(limit)) # random sampling 
        dataset = dataset.select(range(limit))
    return dataset

# Load a subset of 6,000,000 samples
subset_size = 6000000
subset_dataset = load_arabic_billion_words(limit=subset_size)

# Print the number of samples in the subset
print(f"Number of samples in the subset: {len(subset_dataset)}")


def compute_word_stats(texts1):
    total_word_count = 0
    word_counter = Counter()

    for i, text in enumerate(tqdm(texts1, desc="Processing texts")):
        try:
            words = text['text'].split()  # Split text into words by spaces
            total_word_count += len(words)
            word_counter.update(words)  # Count unique words
        except Exception as e:
            print(f"Error processing row {i}: {e}")  # Print the row with an error

    vocab_size = len(word_counter)  # Unique words
    return total_word_count, vocab_size, word_counter
    

total_words, vocabulary_size,_ = compute_word_stats(subset_dataset)


print(f"Total Words: {total_words}")
print(f"Vocabulary Size (Unique Words): {vocabulary_size}")

# Total Words: 2,833,628,886
# Vocabulary Size (Unique Words): 37,823,486