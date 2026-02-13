
def calculate_score(job_skills,resume_skills):
    job_set=set(job_skills)
    resume_set=set(resume_skills)

    matched_skills=list(job_set & resume_set)

    missing_skills=list(job_set-resume_set)

    if len(job_set)==0:
        match_percentage=0
    else:
        match_percentage=(len(matched_skills)/len(job_set))*100
    
    return {
        "percentage":round(match_percentage,2),
        "matched":matched_skills,
        "missing":missing_skills
    }