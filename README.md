# 🏥 MediPredict AI — Multi-Disease Risk Prediction System

**MediPredict AI** is a Flask-based machine learning web application that predicts disease risk scores across five major conditions — **Diabetes, Heart Disease, Liver Disease, Kidney Disease, and Lung Disease** — using pre-trained models (scikit-learn / XGBoost).

The platform includes an interactive healthcare dashboard, a patient management interface, PDF report generation, and automated email delivery — giving it the feel of a real-world clinical screening tool.

> ⚠️ **Disclaimer:** This tool is for informational and educational purposes only. It is **not** a substitute for professional medical diagnosis. Always consult a qualified healthcare provider.

---

## 📸 Screenshots

### 1. Landing Page
<img width="1470" height="872" alt="Landing Page" src="https://github.com/user-attachments/assets/1992b44b-dfdc-4b8e-b506-8ceeb9b49ee4" />

### 2. Prediction Interface
<img width="1470" height="871" alt="Prediction Page" src="https://github.com/user-attachments/assets/dcc43a44-18f8-40dd-9aa5-f5050026c844" />

### 3. Result Page
<img width="1470" height="872" alt="Result Page" src="https://github.com/user-attachments/assets/4ce72c88-da08-418a-a8ae-ba52978e4b37" />

### 4. Dashboard
<img width="1470" height="871" alt="Dashboard" src="https://github.com/user-attachments/assets/444bbcc4-f879-4796-a03d-7ea862c66e74" />

### 5. Patient Management
<img width="1470" height="859" alt="Screenshot 2026-07-11 at 3 49 22 PM" src="https://github.com/user-attachments/assets/6689c53d-c0e8-42f8-b462-3aa4a299f392" />

### 6. Email Report
<img width="1091" height="764" alt="Email Report" src="https://github.com/user-attachments/assets/9017a841-f49c-46c1-bd45-a658dd5e6811" />

---


## 🚀 Features

| Feature | Description |
|---|---|
| ✅ Multi-disease prediction | Predict one condition at a time, or all five at once |
| ✅ Interactive dashboard | Patient history, stats, and risk breakdowns at a glance |
| ✅ AI-powered risk scoring | Probability-based scores from trained ML models |
| ✅ PDF report generation | Branded reports via ReportLab, with risk levels |
| ✅ Email delivery | Sends the PDF report straight to the patient via SMTP |
| ✅ Patient management | Tracks patient IDs, prediction history & records |
| ✅ Responsive UI | Clean design with disease-specific theming |

---

## 🧠 Supported Diseases

| Disease | Key Parameters Used |
|---|---|
| **Diabetes** | Glucose level, BMI, blood pressure, insulin, HbA1c, family history, physical activity |
| **Heart Disease** | Cholesterol, ECG results, chest pain type, heart rate, blood pressure, BMI, smoking history |
| **Liver Disease** | Bilirubin levels, albumin, total proteins, alkaline phosphotase, aminotransferase values |
| **Kidney Disease** | Creatinine, urea, blood pressure, albumin |
| **Lung Disease** | Lung capacity, smoking status, hospital visits, disease type, treatment type |

---

## 🛠️ Tech Stack

**Frontend:** HTML5, CSS3, JavaScript, Jinja2 templating
**Backend:** Python, Flask
**Machine Learning:** scikit-learn, XGBoost, NumPy
**PDF Generation:** ReportLab
**Model Storage:** Pickle (`.pkl` files)
**Storage:** Browser localStorage for patient/session data (no database required)

---

## 📂 Project Structure

```
medipredict-ai/
│
├── app.py                    # Flask backend (main entry point)
├── email_utils.py            # SMTP email sending logic
├── report_pdf.py             # PDF report generation (ReportLab)
│
├── templates/                 # HTML templates
│   ├── landing.html
│   ├── index.html
│   ├── dashboard.html
│   ├── result.html
│   └── result_single.html
│
├── models/                    # Pre-trained ML models & scalers (.pkl)
│   ├── diabetes_model.pkl / diabetes_scaler.pkl
│   ├── heart_model.pkl / heart_scaler.pkl
│   ├── liver_model.pkl / liver_scaler.pkl
│   ├── kidney_model.pkl / kidney_scaler.pkl
│   └── lung_model.pkl / lung_scaler.pkl
│
├── datasets/                  # Training datasets (CSV/XLSX)
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

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
> For Gmail: enable 2-Step Verification, then generate an **App Password** under Google Account → Security → App Passwords.

If `.env` is not configured, the app still runs — email sending is simply disabled.

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000/
```

---

## 🔄 Flask Routes

| Route | Method | Description |
|---|---|---|
| `/landing` | GET | Landing page |
| `/predict-form` | GET | Prediction input form |
| `/dashboard` | GET | Analytics dashboard |
| `/predict` | POST | Predicts all 5 diseases at once |
| `/predict_single` | POST | Predicts one selected disease |
| `/send_report` | POST | Emails a PDF report to the patient |

---

## 🧠 Machine Learning Models

All models are **pre-trained** and included as `.pkl` files in the `models/` folder — no retraining required to run the app. Each disease module has its own prediction model and feature scaler, loaded dynamically via Python's `pickle`:

```python
diabetes_model  = load_file("diabetes_model.pkl")
diabetes_scaler = load_file("diabetes_scaler.pkl")
```

> **Note:** `heart_model.pkl` is ~69MB. If you plan to fork/clone this repo frequently, consider using [Git LFS](https://git-lfs.github.com/) for a smoother experience.

---

## 🔮 Future Improvements

- Database integration (replacing localStorage)
- User authentication system
- Cloud deployment
- Deep learning model integration
- Real-time hospital API integration
- Mobile-responsive optimization

---

## 📚 Learning Outcomes

This project demonstrates:
- Flask web development and REST-style routing
- Machine learning model deployment with scikit-learn/XGBoost
- Healthcare data analysis and predictive analytics
- PDF generation and automated email workflows
- Frontend-backend integration with Jinja2 templating

---

## ⚠️ Disclaimer

This application is developed for **educational and research purposes only**. Prediction results are generated by machine learning models and should not be considered professional medical advice or diagnosis. Always consult a qualified healthcare professional for medical decisions.

---

## 📜 License

This project is intended for academic and educational purposes.
