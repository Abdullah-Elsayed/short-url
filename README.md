# short-url

A small URL shortener web app built with Django. Paste a long URL, get a short one back.

## Stack

- Python + Django 3.2
- [pyshorteners](https://pypi.org/project/pyshorteners/) for shortening
- SQLite (default Django database)

## Project layout

```
shorturl/      # Django project settings and root URLconf
shorturlapp/   # the app: models, forms, views, urls, templates
manage.py
```

## Run locally

```bash
git clone https://github.com/Abdullah-Elsayed/short-url.git
cd short-url

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirments.txt

python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/

## Notes

- The requirements file is named `requirments.txt`, kept as-is to avoid breaking existing clones.
- An early learning project — not hardened for production.

## License

MIT — see [LICENSE](LICENSE).
