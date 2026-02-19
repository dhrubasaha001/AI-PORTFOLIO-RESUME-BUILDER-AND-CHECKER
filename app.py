import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import groq

load_dotenv()
app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.3-70b-versatile" 

@retry(
    stop=stop_after_attempt(3), 
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((groq.RateLimitError, groq.InternalServerError)),
    reraise=True 
)
def get_groq_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert Resume Architect specializing in ATS-friendly engineering resumes."},
            {"role": "user", "content": prompt}
        ],
        model=MODEL_NAME,
        temperature=0.5,
    )
    return chat_completion.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    data = request.json
    # Enhanced Prompt for high detail
    prompt = f"""
    Create a detailed, professional, and ATS-optimized resume for:
    Name: {data.get('name')}
    Email: {data.get('email')} | Phone: {data.get('phone')}
    LinkedIn: {data.get('linkedin')} | GitHub: {data.get('github')}
    
    Education: {data.get('education')}
    Skills: {data.get('skills')}
    Projects: {data.get('projects')}
    Experience: {data.get('experience', 'N/A')}

    Requirements:
    1. Start with a powerful Professional Summary.
    2. Format contact info as a single line under the name.
    3. For projects, use the STAR method (Situation, Task, Action, Result).
    4. Group skills into categories (e.g., Languages, Frameworks, Tools).
    5. Use clean Markdown (bold for headers).
    """
    
    try:
        result = get_groq_response(prompt)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/check', methods=['POST'])
def check_resume():
    data = request.json
    prompt = f"Analyze this resume text. Provide an ATS score (0-100), identify missing keywords, and suggest 3 high-impact improvements:\n\n{data.get('resume_text')}"
    try:
        result = get_groq_response(prompt)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)