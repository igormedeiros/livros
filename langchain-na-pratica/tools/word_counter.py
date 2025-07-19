import argparse
import re

def count_words(filepath):
    """Counts the number of words in a given markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Remove markdown formatting (headers, links, etc.)
    content = re.sub(r'#.*\n', '', content) # Headers
    content = re.sub(r'\[.*?\]\(.*?\)', '', content) # Links
    content = re.sub(r'\*\*.*?\*\*', '', content) # Bold
    content = re.sub(r'\*.*?\*', '', content) # Italic
    content = re.sub(r'_.*?_', '', content) # Italic
    content = re.sub(r'\n', ' ', content) # Newlines to spaces

    # Count words
    words = content.split()
    return len(words)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count words in a markdown file.")
    parser.add_argument("filepath", type=str, help="Path to the markdown file.")
    args = parser.parse_args()

    word_count = count_words(args.filepath)
    print(f"The file {args.filepath} contains {word_count} words.")
