from pathlib import Path

LINES_PER_FILE = 500000
PATTERN_TEMPLATE = "HackathonDataHourly"
CSV_PATTERN = f"{PATTERN_TEMPLATE}*.csv"
ZIP_PATTERN = f"{PATTERN_TEMPLATE}*.zip"
OUTPUT_DIR = "DataHourly/"
SMALL_FILE_NAME = ""

ZIPPED_BIG_FILE_NAMES = Path(".").glob(ZIP_PATTERN)

from zipfile import ZipFile

for zipped_big_file_name in ZIPPED_BIG_FILE_NAMES:
    with ZipFile(zipped_big_file_name, "r") as zipObj:
        zipObj.extractall()


BIG_FILE_NAMES = Path(".").glob(CSV_PATTERN)
Path(OUTPUT_DIR).mkdir(exist_ok=True)


lineno = 0
small_file = None
small_file_index = 0
for big_file_name in BIG_FILE_NAMES:
    with open(big_file_name) as big_file:
        print(f"Opened {big_file_name}")
        for line in big_file:
            if lineno % LINES_PER_FILE == 0:
                if small_file:
                    small_file.close()
                    print(f"    Closed {small_file_name}")
                    small_file_index += 1
                small_file_name = f"{OUTPUT_DIR}{SMALL_FILE_NAME}{small_file_index}.csv"
                small_file = open(small_file_name, "w")
                print(f"    Opened {small_file_name}")
            small_file.write(line)
            lineno += 1
        print(f"Closed {big_file_name}")
if small_file:
    small_file.close()

