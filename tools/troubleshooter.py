from utils.kb_search import search_kb
from utils.ollama_api import ask_gemma
from utils.translation import to_english, to_marathi

def troubleshooter(user_input, lang="en"):
    kb_ans = search_kb(user_input, lang)
    print("[troubleshooter] KB answer:", kb_ans)
    if kb_ans:
        print("[troubleshooter] Returning KB answer")
        return kb_ans

    print("[troubleshooter] Querying LLM")
    eng_input = to_english(user_input) if lang == "mr" else user_input
    llm_ans = ask_gemma(eng_input)
    print("[troubleshooter] LLM answer:", llm_ans)
    return to_marathi(llm_ans) if lang == "mr" else llm_ans
