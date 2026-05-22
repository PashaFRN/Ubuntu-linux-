import os

import requests


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY before running this script.")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={api_key}"
    )
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "hello"}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("API key and model work.")
            data = response.json()
            candidates = data.get("candidates", [])
            if candidates:
                text = candidates[0]["content"]["parts"][0]["text"]
                print(text[:200])
        else:
            print(f"Error: {response.json()}")
    except Exception as exc:
        print(f"Exception: {exc}")


if __name__ == "__main__":
    main()
