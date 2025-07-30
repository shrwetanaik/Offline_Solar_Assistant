from tools.troubleshooter import troubleshooter
from tools.estimator import solar_estimator
from tools.disaster_guide import get_disaster_guide
from tools.weather_safe import weather_advisory
from tools.damage_reporter import report_damage
from tools.messenger import send_message

def detect_lang(text):
    return "mr" if any('\u0900' <= ch <= '\u097F' for ch in text) else "en"

def main():
    while True:
        print("\nModules:")
        print("1) Troubleshooter 2) Estimator 3) Disaster Guide 4) Weather Advisory 5) Damage Reporter 6) Messenger 7) Exit")
        choice = input("Choose module: ")
        if choice == "1":
            q = input("Describe your issue (Marathi/English): ")
            lang = detect_lang(q)
            print(troubleshooter(q, lang))
        elif choice == "2":
            kwh = float(input("Enter daily kWh requirement: "))
            print(solar_estimator(kwh))
        elif choice == "3":
            scenario = input("What is your emergency scenario?: ")
            lang = detect_lang(scenario)
            print(get_disaster_guide(scenario, lang))
        elif choice == "4":
            wa = input("Ask weather safety question: ")
            lang = detect_lang(wa)
            print(weather_advisory(wa, lang))
        elif choice == "5":
            desc = input("Describe the damage: ")
            print(report_damage(desc))
        elif choice == "6":
            status = input("Type message for status board: ")
            user = input("Your name/id: ")
            print(send_message(status, user))
        elif choice == "7":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
