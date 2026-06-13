import requests
from datetime import date


def get_weather():
    city = "Kochi"

    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=10
        )

        response.raise_for_status()

        return response.text.strip()

    except Exception:
        return "Weather unavailable"


def get_quote():
    try:
        response = requests.get(
            "https://zenquotes.io/api/random",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        return f'"{quote}" — {author}'

    except Exception:
        return "Quote unavailable"


def build_summary():
    today = date.today().strftime("%A, %d %B %Y")

    weather = get_weather()
    quote = get_quote()

    summary = f"""
==========================
PULSE - Daily Summary
==========================

Date:
{today}

Weather:
{weather}

Today's Quote:
{quote}

==========================
"""

    return summary


def run():
    summary = build_summary()

    print(summary)

    with open(
        "daily_summary.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(summary)

    print("Pulse ran successfully.")


if __name__ == "__main__":
    run()