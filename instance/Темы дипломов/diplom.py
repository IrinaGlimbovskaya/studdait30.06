import os
import re
import sqlite3
from docx import Document

def parse_word_table(docx_file):
    doc = Document(docx_file)
    tables_data = []

    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
            tables_data.append(row_data)

    return tables_data

def extract_year_from_filename(filename):
    match = re.search(r'\d{4}', filename)
    if match:
        return match.group()
    else:
        return None

def save_to_database(data, db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS List_diploms 
                 (Id INTEGER PRIMARY KEY,
                 year TEXT,
                 name_student TEXT,
                 name_diplom TEXT,
                 name_teacher TEXT)''')

    for row in data:
        year = extract_year_from_filename(docx_file)
        name_student, name_diplom, name_teacher = row
        c.execute("INSERT INTO List_diploms (year, name_student, name_diplom, name_teacher) VALUES (?, ?, ?, ?)",
                  (year, name_student, name_diplom, name_teacher))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_file = "sait.db"

    for filename in os.listdir(current_directory):
        if filename.endswith(".docx"):
            docx_file = os.path.join(current_directory, filename)
            tables_data = parse_word_table(docx_file)
            save_to_database(tables_data, db_file)
