from sys import argv
from pathlib import Path
from collections import Counter

def main():
    current_dir = Path(__file__).parent

    def load_logs(path):
        try:
            with open(current_dir / path) as file:
                return [parse_log_line(line) for line in file.readlines()]
        except Exception as e:
            print(f"Error: {e}")

    def parse_log_line(line):
        date, time, log, *text = line.split()
        text = ' '.join(text)
        return {'date': date, 'time': time, 'log': log, 'text': text}
    
    def count_logs_by_level(list):
        logs = [el['log'] for el in list]
        return dict(Counter(logs)), list

    def display_log_counts(args, level=None):
        logs, list = args
        print()
        print('Рівень логування | Кількість')
        print('-----------------|----------')
        for name, count in logs.items():
            print(f"{name:<17}| {count}")
        if level:
            if level.upper() not in [log for log in logs]:
                print()
                print(f'choose one of this log levels: {[log for log in logs]}')
                print()
                return
            print()
            print(f"Деталі логів для рівня '{level.upper()}':")
            [print(f'{el['date']} {el['time']} - {el['text']}') \
             for el in list if el['log'] == level.upper()]
        print()

    def filter_logs_by_level(logs, level):
        return []

    if len(argv) > 1:
        display_log_counts(count_logs_by_level(load_logs(argv[1])), \
                           level = argv[2] if len(argv) > 2 else None)

if __name__ == '__main__':
    main()

#py task3.py log_file.txt error