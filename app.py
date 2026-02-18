from flask import Flask, render_template, request

app = Flask(__name__)

role_skills = {
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "Data Structures", "Git"],
    "Data Scientist": ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Cybersecurity Fundamentals", "Python", "Risk Assessment"],
    "Cloud Engineer": ["AWS", "Azure", "Docker", "Linux", "Networking"],
    "DevOps Engineer": ["Linux", "Docker", "Kubernetes", "CI/CD", "Git"],
    "Mobile App Developer": ["Java", "Kotlin", "Swift", "Flutter", "UI/UX"],
    "Software Engineer": ["Data Structures", "Algorithms", "OOP", "Git", "Problem Solving"],
    "UI/UX Designer": ["Figma", "Wireframing", "Prototyping", "User Research", "Design Principles"],
    "Blockchain Developer": ["Solidity", "Ethereum", "Smart Contracts", "Cryptography", "Web3"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    readiness_score = None
    missing_skills = []
    selected_role = None

  if request.method == "POST":
    user_skills = request.form["skills"].split(",")
    selected_role = request.form["role"]
    required = role_skills[selected_role]

    user_skills = [s.strip().lower() for s in user_skills]
    required_lower = [r.lower() for r in required]

    missing_skills = [required[i] for i in range(len(required))
                      if required_lower[i] not in user_skills]

    matched = len(required) - len(missing_skills)
    readiness_score = int((matched / len(required)) * 100)

    return render_template(
        "index.html",
        roles=role_skills.keys(),
        readiness_score=readiness_score,
        missing_skills=missing_skills,
        selected_role=selected_role
    )

if __name__ == "__main__":
    app.run(debug=True)
