from utils.kb_search import search_kb
from utils.ollama_api import *
def get_disaster_guide(scenario, lang="en"):
    kb_result = search_kb(scenario, lang)
    if kb_result and len(kb_result.strip()) > 10:
        return kb_result
    # Otherwise, call LLM
    if lang == "mr":
        scenario_en = to_english(scenario)
        response = ask_gemma(
            f"You are a solar disaster preparedness assistant. Give a clear step-by-step safety guide for this scenario:\n\n{scenario_en}\n\nRespond in markdown with bold headings and numbered steps."
        )
        return to_marathi(response)
    else:
        return ask_gemma(
            f"You are a solar disaster preparedness assistant. Give a clear step-by-step safety guide for this scenario:\n\n{scenario}\n\nRespond in markdown with bold headings and numbered steps."
        )


