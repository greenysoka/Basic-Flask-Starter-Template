# Basic Flask Starter Template

A minimal Flask project with HTML, CSS, and JavaScript ready to go.

## Project structure

```
flask_template/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Main page template
└── static/
    ├── style.css           # Styles
    └── script.js           # Client-side JavaScript
```

## Getting started

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the development server

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Customising the template

| What you want to change | File to edit |
|---|---|
| Page content / structure | `templates/index.html` |
| Styles | `static/style.css` |
| Client-side behaviour | `static/script.js` |
| Routes / backend logic | `app.py` |

### Adding a new page

1. Create a new template in `templates/`, e.g. `templates/about.html`.
2. Add a route in `app.py`:

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

### Passing data to templates

Flask uses [Jinja2](https://jinja.palletsprojects.com/) for templating. Pass variables from your route:

```python
@app.route('/')
def hello_world():
    return render_template('index.html', name='World')
```

Then use them in the HTML:

```html
<h1>Hello, {{ name }}!</h1>
```
