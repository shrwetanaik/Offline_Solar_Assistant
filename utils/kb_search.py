import pandas as pd

kb = pd.read_csv("data/solar_kb.csv")

def search_kb(query, lang="en"):
    questions = kb['question_mr'] if lang == "mr" else kb['question_en']
    answers = kb['answer_mr'] if lang == "mr" else kb['answer_en']
    for q, a in zip(questions, answers):
        if q.strip().lower() in query.strip().lower():
            return a
    return None
