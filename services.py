import sqlite3 as sq
import matplotlib.pyplot as plt
import os
from datetime import datetime
DATABSE = 'results.db'


def add_results(code):
    try:
        os.mkdir(f'./result_images/{code}')
    except:
        pass
    with sq.connect(DATABSE) as con:
        cur = con.cursor()
        curr_iter = int(cur.execute(f'SELECT COUNT(*) FROM results WHERE code=\'{code}\'').fetchone()[0]) + 1
    os.mkdir(f'./result_images/{code}/{curr_iter}')
    plt.imsave(f'./result_images/{code}/{curr_iter}/liver.png', plt.imread('liver.png'))
    plt.imsave(f'./result_images/{code}/{curr_iter}/tumor.png', plt.imread('tumor.png'))

    with sq.connect(DATABSE) as con:
        cur = con.cursor()
        timestamp = datetime.now().strftime('%d.%m.%Y')
        cur.execute(f'INSERT INTO results(liver_path, tumor_path, code, timestamp) VALUES(\'./result_images/{code}/{curr_iter}/liver.png\', \'./result_images/{code}/{curr_iter}/tumor.png\', \'{code}\', \'{timestamp}\')')
        con.commit()

def get_results(code):
    with sq.connect(DATABSE) as con:
        cur = con.cursor()
        return cur.execute(f'SELECT liver_path, tumor_path, timestamp FROM results WHERE code=\'{code}\'').fetchall()

def is_code_in_db(code):
    with sq.connect(DATABSE) as con:
        cur = con.cursor()
        return cur.execute(f'SELECT EXISTS(SELECT * FROM results WHERE code=\'{code}\')').fetchone()[0] == 1

if __name__ == "__main__":
    print(is_code_in_db('p0OCv8ahUPd0wWF7dHGfZU7d7XDg7ZbmfPbEi0CT'))
    # add_results('TEST2')