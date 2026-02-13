# Resume Job Matching System Level 1

Resume Analyzer - Level 1 Basic

Resume Skill Matching System

A Flask-Based ATS Simulation

Overview

This project is a Resume–Job Description Matching System built using Python and Flask.

It simulates how an Applicant Tracking System (ATS) evaluates resumes by:

Extracting predefined skills

Comparing them against job requirements

Calculating a match percentage

Displaying matched and missing skills visually

Problem Statement

Recruiters often receive hundreds of resumes for a single job posting.

Manual screening is:

Time-consuming

Error-prone

Inconsistent

This system automates skill comparison using structured keyword evaluation.

How the System Works
User Input (JD + Resume)
        ↓
Skill Extraction (Regex Engine)
        ↓
Overlap-safe Matching
        ↓
Score Calculation
        ↓
Visual Result Display

Project Architecture
resumechecker/
│
├── app1.py               # Flask controller
├── skills1.py            # Skill definitions
├── skill_extractor.py    # Regex-based extraction
├── score_calculator.py   # Matching engine
│
└── templates/
    └── index.html        # UI

Internal Working (Step-by-Step)
1️⃣ Skill Definition (skills1.py)

Defines evaluation criteria:

SKILLS = [
    "python",
    "java",
    "sql",
    "nlp",
    "c",
    "c++",
    "c#"
]


Only skills listed here are evaluated.

2️⃣ Skill Extraction (skill_extractor.py)

Converts text to lowercase

Sorts skills by length (longest first)

Uses regex word-boundary matching

Prevents overlapping matches

Handles special cases like:

C

C++

C#

Example:

pattern = r'\b' + escaped_skill + r'\b'


Prevents:

"c" matching inside "machine"

"java" matching inside "javascript"

3️⃣ Score Calculation (score_calculator.py)
match_percentage = (matched / total_required) * 100


Returns:

{
  "percentage": 66.67,
  "matched": [...],
  "missing": [...]
}

4️⃣ Flask Application (app1.py)

Handles:

Input validation

Whitespace-only protection

Skill extraction

Score calculation

Result rendering

Example
Job Description

Looking for Python developer with SQL and NLP skills.

Resume

Experienced in Python and SQL.

Output
Metric	Result
Match Percentage	66.67%
Matched Skills	python, sql
Missing Skills	nlp
UI Features

Gradient background

Animated progress bar

Matched skill badges

Missing skill badges

Clean modular design

How to Run
pip install flask
python app1.py


Open in browser:

http://127.0.0.1:5000/

Current Limitations

Keyword-based only

No synonym recognition (AI ≠ Artificial Intelligence)

No semantic similarity

No experience weighting

Roadmap
Level 1

Keyword-based matching (Completed)

Level 2

PDF Resume Upload

Level 3

Synonym & Semantic Matching

Level 4

Experience-weighted ranking

# Author
# BANDARU CHARAN
B.Tech Computer Science

This Version Includes

Code highlighting

Proper markdown structure

Clean formatting

Recruiter-friendly tone
