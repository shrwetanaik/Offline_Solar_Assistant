import requests

import json

import re

def ask_gemma(prompt):
    markdown_prompt = f"""
        You are a solar troubleshooting expert. For the following user question, respond with:

        - A bold heading (use markdown, e.g., **Solution for a Non-Operating Solar Inverter:**)
        - Numbered steps, each with a bold step title
        - Bullet points for details under each step
        - End with 'Additional Tips:' in bold and a few tips

        Here is the question:
        {prompt}

        Respond in markdown format.
        """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:7b", "prompt": markdown_prompt},
            stream=True,
            timeout=120
        )
        print(f"[ask_gemma] Status: {response.status_code}")
        if response.status_code != 200:
            return f"Error: Ollama returned status {response.status_code}"

        result_text = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line)
                    result_text += data.get("response", "")
                except Exception as e:
                    print(f"[ask_gemma] JSON parse error: {e} | line={line}")

        # Sanitize output: remove all asterisks (*) to avoid markdown
        sanitized_text = re.sub(r"\*", "", result_text).strip()

        return sanitized_text if sanitized_text else "LLM did not return any answer."
    except Exception as e:
        print(f"[ask_gemma] Exception: {e}")
        return f"Error contacting Ollama: {e}"

