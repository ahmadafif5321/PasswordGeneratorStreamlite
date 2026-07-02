# Password Generator (Streamlit)

A small web app that generates random passwords of a chosen length, built with [Streamlit](https://streamlit.io/).

## What and why

My company requires a password change every month, and coming up with a new one each time got old fast. I first wrote a [command-line version](https://github.com/ahmadafif5321/RandomPasswordGenerator), then turned it into this web app so it would be usable from any browser without touching a terminal.

I wrote up the full process of building and deploying it for free in this blog post: [Create and Publish a Python Random Password Generator Web App for Free](https://ahmadafif.com/blog/create-and-publish-a-python-random-password-generator-web-app-for-free/).

This is a learning/utility project, intentionally small: one Python file, one dependency.

## Quick start

```bash
pip install -r requirements.txt
streamlit run BasePassGen.py
```

Streamlit opens the app in your browser (by default at `http://localhost:8501`).

A `.devcontainer` config is included, so the repo can also be opened directly in GitHub Codespaces or any dev-container-aware editor.

## How it works

The whole app lives in `BasePassGen.py`:

- A slider selects the password length (8 to 30 characters, default 12).
- On "Generate Password", the app builds the password by picking random characters from `string.ascii_letters + string.digits + string.punctuation` using `random.choice`.
- The result is displayed on the page, followed by a short success message, balloons, and a random joke from a small list of quotes.

## Honest limitations

- Passwords are generated with Python's `random` module, which is not cryptographically secure. For anything sensitive, `secrets.choice` would be the right tool.
- There is no character-class guarantee (a generated password could, in theory, contain no digits or no symbols).
- No tests; it is a single-file utility.

## Tech stack

- Python
- Streamlit 1.37 (the only dependency)
- Python standard library: `random`, `string`

## Related

- [RandomPasswordGenerator](https://github.com/ahmadafif5321/RandomPasswordGenerator) — the original CLI script this app evolved from, plus Tkinter and Flask variants of the same idea.
