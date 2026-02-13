import re
from skills1 import SKILLS

def extract_skills(text):
    text = text.lower()
    extracted_skills = []

    sorted_skills = sorted(SKILLS, key=len, reverse=True)

    for skill in sorted_skills:

        escaped_skill = re.escape(skill.lower())

        # For normal word skills
        if skill.isalnum() or " " in skill:
            pattern = r'\b' + escaped_skill + r'\b'
        else:
            # For special symbol skills like C++, C#
            pattern = escaped_skill

        if re.search(pattern, text):
            extracted_skills.append(skill)
            text = re.sub(pattern, '', text)

    return extracted_skills
