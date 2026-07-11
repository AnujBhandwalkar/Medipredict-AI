# 🏥 MediPredict AI

**MediPredict AI** is a Flask-based web application that predicts disease risk scores across five categories — **Diabetes, Heart Disease, Liver Disease, Kidney Disease, and Lung Disease** — using pre-trained machine learning models (scikit-learn / XGBoost).

> ⚠️ **Disclaimer:** This tool is for informational and educational purposes only. It is **not** a substitute for professional medical diagnosis. Always consult a qualified healthcare provider.

---

## ✨ Features

- 🔍 **Single or multi-disease prediction** — predict one condition at a time or all five at once
- 📊 **Interactive dashboard** with patient history (stored via localStorage)
- 📄 **PDF report generation** using ReportLab, with patient details, risk scores, and risk levels
- 📧 **Email delivery** of PDF reports directly to patients via SMTP
- 🎨 Clean, modern UI with custom theming per disease type

---

## 🧠 Machine Learning Models

All models are **pre-trained** and included as `.pkl` files in the `models/` folder — no retraining required to run the app.

| Disease | Files |
|---|---|
| Diabetes | `diabetes_model.pkl`, `diabetes_scaler.pkl` |
| Heart Disease | `heart_model.pkl`, `heart_scaler.pkl` |
| Liver Disease | `liver_model.pkl`, `liver_scaler.pkl` |
| Kidney Disease | `kidney_model.pkl`, `kidney_scaler.pkl` |
| Lung Disease | `lung_model.pkl`, `lung_scaler.pkl` |

Training datasets used are included in the `datasets/` folder for reference and reproducibility.

> **Note:** `heart_model.pkl` is ~69MB. If you plan to fork/clone this repo frequently, consider using [Git LFS](https://git-lfs.github.com/) for a smoother experience.

---

## 📁 Project Structure

```
medipredict-ai/
│
├── app.py                    # Flask backend (main entry point)
├── email_utils.py            # SMTP email sending logic
├── report_pdf.py             # PDF report generation (ReportLab)
│
├── templates/                # HTML templates
│   ├── landing.html
│   ├── index.html
│   ├── dashboard.html
│   ├── result.html
│   └── result_single.html
│
├── models/                   # Pre-trained ML models & scalers (.pkl)
│
├── datasets/                 # Training datasets (CSV/XLSX)
│
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/anujbhandwalkar/medipredict-ai.git
cd medipredict-ai
```

### 2. Install dependencies

```bash
pip install flask numpy scikit-learn xgboost reportlab python-dotenv
```

### 3. Configure email (optional)

To enable the "Send Report" email feature, create a `.env` file in the project root:

```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_SENDER=MediPredict AI <your_email@gmail.com>
```

> For Gmail: enable 2-Step Verification, then generate an **App Password** under Google Account → Security → App Passwords. Use that as `MAIL_PASSWORD`.

If `.env` is not configured, the app still works — email sending will simply be disabled.

### 4. Run the app

```bash
python app.py
```

Then open your browser to:

```
http://127.0.0.1:5000/
```

---

## 📄 Pages & Routes

| Page | Route | Description |
|---|---|---|
| Landing | `/landing` | Homepage |
| Predict Form | `/predict-form` | Input form for predictions |
| Dashboard | `/dashboard` | Patient history & stats |
| Predict (multi) | `POST /predict` | Predicts all 5 diseases at once |
| Predict (single) | `POST /predict_single` | Predicts one selected disease |
| Send Report | `POST /send_report` | Emails a PDF report to the patient |

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **ML:** scikit-learn, XGBoost
- **PDF Generation:** ReportLab
- **Frontend:** HTML, CSS, JavaScript (Jinja2 templating)
- **Storage:** Browser localStorage (patient/session data — no database required)

---

## 📜 License

This project is for academic/educational purposes.