import json
import os
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    config_path = Path(os.environ.get("OPENCLAW_CONFIG_PATH", root / "openclaw.json"))
    api_key = os.environ.get("GEMINI_API_KEY")
    model = os.environ.get("GEMINI_MODEL", "google/gemini-2.5-flash")

    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY before running this script.")

    if not config_path.exists():
        raise SystemExit(
            f"Config not found: {config_path}. Copy openclaw.example.json to openclaw.json first."
        )

    with config_path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    config.setdefault("env", {})["GEMINI_API_KEY"] = api_key
    config.setdefault("agents", {}).setdefault("defaults", {}).setdefault("model", {})[
        "primary"
    ] = model

    with config_path.open("w", encoding="utf-8") as file:
        json.dump(config, file, indent=2, ensure_ascii=False)
        file.write("\n")

    print("Config updated successfully.")
    print(f"  - Config: {config_path}")
    print("  - API key: loaded from GEMINI_API_KEY")
    print(f"  - Model: {model}")


if __name__ == "__main__":
    main()
