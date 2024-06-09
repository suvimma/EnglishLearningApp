import os

def check_encoding(directory, encoding='utf-8'):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding=encoding) as f:
                        f.read()
                except UnicodeDecodeError as e:
                    print(f"Encoding error in file: {filepath}\nError: {e}")

check_encoding('C:/Windows/System32/EnglishLearningApp/english_learning')
