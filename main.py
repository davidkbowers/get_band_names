import psycopg2
from dotenv import load_dotenv
import os
import spacy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')

    conn = psycopg2.connect(
        'postgresql://uqncvrehjtrbtpjg:nokerbqermgsvnej@5.161.119.174:8004/cvuugpihdcqkhmnv')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM articles')
    rows = cursor.fetchall()

    for row in rows:
        headline = row[3]
        headline_str = str(headline)
        headline_str = headline_str.lower()
        sentence = headline_str
        # subject = find_subject(sentence)
        # print(f'Subject: {subject}')
        nlp.pipe_labels['ner']
        doc = nlp(sentence)
        for ent in doc.ents:
            print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_), "\n\n")
