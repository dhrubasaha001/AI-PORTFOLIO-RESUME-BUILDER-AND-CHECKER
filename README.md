# AI-PORTFOLIO-RESUME-BUILDER-AND-CHECKER
---

# 🚀 CareerBot AI Pro: Advanced Resume Architect

**CareerBot AI Pro** is a high-performance, full-stack AI application designed to bridge the gap between technical expertise and professional presentation. Built with **Python Flask** and powered by the **Groq Llama-3 70B** engine, it generates recruiter-grade, ATS-optimized resumes in under 1.5 seconds.

## 🌟 Key Features

* **AI Resume Generation:** Transforms raw data into structured, professional resumes using the industry-standard **STAR method**.
* **ATS Optimization Checker:** Analyzes existing resume text to provide a compatibility score and actionable feedback.
* **Ultra-Fast Inference:** Leverages the Groq Cloud API for near-instant response times.
* **Resilient Architecture:** Implements **Exponential Backoff** logic to handle API rate limits (429 errors) seamlessly.
* **One-Click PDF Export:** Real-time Markdown-to-PDF generation for instant professional use.

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| **Backend** | Python, Flask, Groq SDK |
| **Frontend** | Tailwind CSS, JavaScript (ES6+), Marked.js |
| **AI Model** | Llama-3.3-70b-versatile |
| **DevOps** | Render (Deployment), Gunicorn (WSGI), GitHub (CI/CD) |
| **Utilities** | Tenacity (Retry Logic), python-dotenv, html2pdf.js |

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/dhrubasaha001/AI-PORTFOLIO-RESUME-BUILDER-AND-CHECKER
cd AI-PORTFOLIO-RESUME-BUILDER-AND-CHECKER

```


2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure environment variables:**
Create a `.env` file in the root directory:
```text
GROQ_API_KEY=your_actual_api_key_here
DEV_MODE=False

```


5. **Run the application:**
```bash
python app.py

```



---

## 🧠 Core Algorithm: Resilience & Scaling

As a Senior AI Engineer, I implemented **Exponential Backoff** using the `tenacity` library to ensure production-level stability.

```python
@retry(
    stop=stop_after_attempt(3), 
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((groq.RateLimitError, groq.InternalServerError)),
    reraise=True 
)
def get_groq_response(prompt):
    # API Call Logic

```

This ensures that if the free-tier API hits a burst limit, the application waits (2s, 4s, 8s) and retries before ever showing an error to the user.

---

## 🚀 Deployment on Render

This project is optimized for deployment on **Render**.

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `gunicorn app:app`
* **Env Vars:** Ensure `GROQ_API_KEY` is added to the Render dashboard.

---

## 📈 Future Roadmap

* [ ] **Multi-Design Templates:** Modern, Academic, and Creative layouts.
* [ ] **Job Matching:** Automated keyword tailoring based on specific job descriptions.
* [ ] **User History:** Database integration to store and edit previous resumes.

---


