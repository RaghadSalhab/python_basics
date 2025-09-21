def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

file_path = "veryLargeFile.txt"
for line in read_large_file(file_path):
    if "error" in line:
        print(line)
