import os
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# In-memory database structure
notes_registry = []

# Reads the deployment unique hash provided by cloud servers
COMMIT_HASH = os.getenv("RENDER_GIT_COMMIT", "local")[:7]

@app.route("/")
def home():
    total_notes = len(notes_registry)
    exam_prep_count = sum(1 for note in notes_registry if note["category"] == "Exam Prep")
    
    return render_template(
        "index.html", 
        notes=notes_registry, 
        total=total_notes, 
        exam_count=exam_prep_count, 
        commit=COMMIT_HASH
    )

@app.route("/share", methods=["POST"])
def share_material():
    title = request.form.get("title", "").strip()
    link = request.form.get("link", "").strip()
    category = request.form.get("category", "Lecture Notes")
    contributor = request.form.get("contributor", "").strip()

    # Dynamic Validation Quality Gate
    if not title or not link or not contributor:
        return {"status": "error", "message": "All fields are mandatory."}, 400

    notes_registry.append({
        "title": title,
        "link": link,
        "category": category,
        "contributor": contributor
    })
    return redirect("/")

@app.route("/api/notes")
def api_notes():
    return jsonify(notes_registry)

@app.route("/health")
def health():
    return {"status": "ok", "commit": COMMIT_HASH}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
