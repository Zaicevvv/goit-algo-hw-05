from sys import argv
from pathlib import Path

def main():
    current_dir = Path(__file__).parent
    
    def read_file(path, log_level):
        try:
            with open(current_dir / path) as file:
                lines = file.readlines()
                result = {}
                if log_level:
                    print(f"Reading {log_level}")
                    return
                print(file.readlines())
        except Exception as e:
            print(f"Error: {e}")

    if len(argv) > 1:
        read_file(argv[1], argv[2] if len(argv) > 2 else None)
        

if __name__ == '__main__':
    main()

#py task3.py log_file.txt error
    
def parse_log_line(line: str) -> dict:
    pass
def load_logs(file_path: str) -> list:
    pass
def filter_logs_by_level(logs: list, level: str) -> list:
    pass
def count_logs_by_level(logs: list) -> dict:
    pass
def display_log_counts(counts: dict) -> None:
    pass