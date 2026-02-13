
from flask import Flask,render_template,request
from skill_extractor1 import extract_skills
from score_calculator1 import calculate_score

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    result=None
    error = None
    
    if request.method=="POST":
        job_description=request.form.get("job_description")
        resume_text=request.form.get("resume_text")

         # -------- VALIDATION START --------
        if not job_description or not job_description.strip():
            error = "Job description cannot be empty or contain only spaces."
            return render_template("index.html", error=error)

        if not resume_text or not resume_text.strip():
            error = "Resume text cannot be empty or contain only spaces."
            return render_template("index.html", error=error)
        # -------- VALIDATION END --------

        job_skills=extract_skills(job_description)
        resume_skills=extract_skills(resume_text)

        result=calculate_score(job_skills,resume_skills)
    
    return render_template("index1.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
