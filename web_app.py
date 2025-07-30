import gradio as gr
from tools.troubleshooter import troubleshooter
from tools.estimator import solar_estimator
from tools.disaster_guide import get_disaster_guide
from tools.weather_safe import weather_advisory
from tools.damage_reporter import report_damage

def detect_lang(text):
    return "mr" if any('\u0900' <= ch <= '\u097F' for ch in text) else "en"

def troubleshooter_fn(question):
    lang = detect_lang(question)
    return troubleshooter(question, lang)

def estimator_fn(daily_kwh):
    try:
        kwh = float(daily_kwh)
        return solar_estimator(kwh)
    except Exception:
        return "Please enter a valid number for kWh."

def disaster_guide_fn(scenario):
    lang = detect_lang(scenario)
    return get_disaster_guide(scenario, lang)

def weather_safe_fn(query):
    lang = detect_lang(query)
    return weather_advisory(query, lang)

def damage_report_fn(description):
    return report_damage(description)

with gr.Blocks(title="Offline Solar Assistant", theme=gr.themes.Default()) as demo:
    gr.Markdown(
        """
        # ☀️ Solar Assistant (Offline, English/Marathi)
        All modules run locally—no internet needed after setup!
        """
    )
    with gr.Tab("Solar Troubleshooter"):
        q = gr.Textbox(label="Describe your solar issue (Marathi or English)", lines=2)
        out = gr.Textbox(label="Response")
        btn = gr.Button("Submit")
        btn.click(troubleshooter_fn, inputs=q, outputs=out)
    with gr.Tab("Solar Estimator"):
        kwh_in = gr.Textbox(label="Enter daily required kWh", value="3")
        est_out = gr.Textbox(label="Estimation")
        est_btn = gr.Button("Estimate")
        est_btn.click(estimator_fn, inputs=kwh_in, outputs=est_out)
    with gr.Tab("Disaster Guide"):
        scen = gr.Textbox(label="Describe your disaster scenario", lines=2)
        guide_out = gr.Textbox(label="Guide")
        guide_btn = gr.Button("Get Guide")
        guide_btn.click(disaster_guide_fn, inputs=scen, outputs=guide_out)
    with gr.Tab("Weather Safety"):
        weather_in = gr.Textbox(label="Weather safety question (Marathi/English)", lines=2)
        weather_out = gr.Textbox(label="Advice")
        weather_btn = gr.Button("Get Advice")
        weather_btn.click(weather_safe_fn, inputs=weather_in, outputs=weather_out)
    with gr.Tab("Damage Reporter"):
        dmg_desc = gr.Textbox(label="Describe the damage", lines=2)
        dmg_btn = gr.Button("Report")
        dmg_res = gr.Textbox(label="Report Status")
        dmg_btn.click(damage_report_fn, inputs=dmg_desc, outputs=dmg_res)

demo.launch(server_name="0.0.0.0", server_port=7860, show_api=False)
