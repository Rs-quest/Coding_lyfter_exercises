def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        
        for number, line in enumerate(lines, start=1):
            print(f"Line {number}: {line.strip()}")

read_file_by_lines('songs.txt')