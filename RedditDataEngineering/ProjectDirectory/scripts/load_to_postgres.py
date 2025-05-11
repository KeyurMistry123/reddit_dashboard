import pandas as pd
import psycopg2
import os

def load_to_postgres():
    conn = psycopg2.connect(
        dbname='airflow', user='airflow', password='airflow', host='postgres', port=5432
    )
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS reddit_posts (
        id TEXT PRIMARY KEY,
        title TEXT,
        score INTEGER,
        created DOUBLE PRECISION
    );''')
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/reddit_posts.csv'))
    for _, row in df.iterrows():
        cur.execute('''INSERT INTO reddit_posts (id, title, score, created) VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;''',
            (row['id'], row['title'], int(row['score']), float(row['created'])))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    load_to_postgres() 