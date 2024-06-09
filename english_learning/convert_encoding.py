import os
import chardet

def convert_to_utf8(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        raw_data = f.read()
                        result = chardet.detect(raw_data)
                        encoding = result['encoding']

                    if encoding != 'utf-8':
                        with open(filepath, 'r', encoding=encoding) as f:
                            content = f.read()
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Converted {filepath} from {encoding} to utf-8")
                except UnicodeDecodeError as e:
                    print(f"Encoding error in file: {filepath}\nError: {e}")

convert_to_utf8('C:/Windows/System32/EnglishLearningApp/english_learning')
