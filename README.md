# Tree Drive

A ride-hailing app backend built with Flask.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

## Deploy to Render
1. Push this repo to GitHub.
2. Connect your repo to Render.
3. Set build command: pip install -r requirements.txt
4. Set start command: gunicorn app:app
