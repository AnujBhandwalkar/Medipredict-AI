# MediPredict AI – File Structure & Setup Guide

## 📁 Required Folder Structure

Create your project folder exactly like this:

```
your_project/
│
├── app.py                    ← Flask backend (main entry point)
│
├── templates/                ← ALL HTML files go HERE (Flask requires this name)
│   ├── index.html            ← Landing page (homepage)
│   ├── dashboard.html        ← Dashboard with stats and history
│   └── result.html           ← Prediction results page
│
└── models/                   ← Your trained .pkl files go HERE
    ├── diabetes_model.pkl
    ├── diabetes_scaler.pkl
    ├── heart_model.pkl
    ├── heart_scaler.pkl
    ├── liver_model.pkl
    ├── liver_scaler.pkl
    ├── kidney_model.pkl
    ├── kidney_scaler.pkl
    ├── lung_model.pkl
    └── lung_scaler.pkl
```

---

## 🚀 How to Run

1. **Install dependencies** (if not already installed):
   ```bash
   pip install flask numpy scikit-learn
   ```

2. **Place your .pkl model files** inside the `models/` folder.

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **Open in browser**:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📄 Pages & URLs

| Page        | URL           | File                       |
|-------------|---------------|----------------------------|
| Home        | `/`           | `templates/index.html`     |
| Dashboard   | `/dashboard`  | `templates/dashboard.html` |
| Results     | `/result`     | `templates/result.html`    |
| Predict     | POST `/predict`| handled in `app.py`       |

---

## 🎨 Design Notes

- **Font**: Cabinet Grotesk (headings) + Instrument Sans (body) — loaded from Google Fonts
- **Colors**: Cream/warm white background, dark sidebar, red accents
- **Style**: Inspired by PromptHealth dashboard — clean sidebar layout, stat cards, data tables
- **No extra CSS file needed** — all styles are embedded in each HTML file

---

## ⚠️ Important Notes

- The `templates/` folder name is **mandatory** for Flask — do not rename it.
- The `models/` folder name matches what's in `app.py` — keep it consistent.
- `app.py` must be in the **root** of your project, NOT inside `templates/`.
- The dashboard (`dashboard.html`) shows demo/static data — to show real prediction history, you would need a database (e.g. SQLite with Flask-SQLAlchemy).
