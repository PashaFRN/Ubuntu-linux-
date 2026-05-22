# OpenClaw Workspace Template

Safe OpenClaw workspace template for GitHub. This repo keeps the useful parts of a local setup while excluding live tokens, session data, private keys, logs, and runtime databases.

## Included

- `workspace/` - base agent persona and memory files
- `canvas/index.html` - polished local UI action bridge demo
- `openclaw.example.json` - public config template without secrets
- `update_config.py` - updates local `openclaw.json` from environment variables
- `test_api.py` - quick Gemini API smoke test

## Intentionally Excluded From Git

- live `openclaw.json`
- tokens, keys, and pairing data
- device identity and private keys
- sqlite databases, sessions, logs, and local backup files

These are already covered by `.gitignore`.

## Quick Start

1. Copy `openclaw.example.json` to `openclaw.json`.
2. Fill in your tokens and identifiers locally.
3. Copy `.env.example` to `.env`, or export the variables manually.
4. Run `python update_config.py` if you want to patch your local config from env vars.
5. Run `python test_api.py` to verify Gemini API access.

## Environment Variables

- `GEMINI_API_KEY` - required for `update_config.py` and `test_api.py`
- `GEMINI_MODEL` - optional, defaults to `google/gemini-2.5-flash` in the config updater and `gemini-2.5-flash` in the API test
- `OPENCLAW_CONFIG_PATH` - path to the local `openclaw.json`

## Publishing Model

This repository works best as a template plus a personal local workspace:

- public: templates, docs, canvas, safe helper scripts
- local only: real tokens, device identity, and runtime state

## Before You Push

Check that:

- `git status` does not show `openclaw.json`, `credentials/`, `identity/device.json`, `logs/`, or `tasks/*.sqlite`
- there are no hard-coded API keys or bot tokens in tracked files
- there are no local paths, private chat IDs, or session dumps in new files

If you want to publish a reusable OpenClaw starter, this shape is already much safer than pushing a raw `.openclaw` dump.
