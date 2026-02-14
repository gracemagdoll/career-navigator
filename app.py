from flask import Flask, render_template, request

app = Flask(__name__)

role_skills = {
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "Data Structures", "Git"],
    "Data Scientist": ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"]
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

        user_skills = [s.strip() for s in user_skills]

        missing_skills = [skill for skill in required if skill not in user_skills]

        matched = len(required) - len(missing_skills)
        readiness_score = int((matched / len(required)) * 100)

    return render_template("index.html",
                           roles=role_skills.keys(),
                           readiness_score=readiness_score,
                           missing_skills=missing_skills,
                           selected_role=selected_role)

if __name__ == "__main__":
    app.run(debug=True)
