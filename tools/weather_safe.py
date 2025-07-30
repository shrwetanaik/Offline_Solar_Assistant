from utils.kb_search import search_kb
from utils.ollama_api import *
def weather_advisory(query, lang="en"):
    kb_result = search_kb(query, lang)
    if kb_result and len(kb_result.strip()) > 10:
        return kb_result
    prompt = (
        "You are a solar weather safety advisor. "
        "Provide a detailed weather advisory for the following query:\n\n"
        f"{query}\n\n"
        "Respond in markdown with bold headings and clear advice."
    )
    if lang == "mr":
        query_en = to_english(query)
        response = ask_gemma(prompt.replace(query, query_en))
        return to_marathi(response)
    else:
        return ask_gemma(prompt)
