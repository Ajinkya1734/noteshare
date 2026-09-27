from app import app, notes_registry

def client():
    app.config["TESTING"] = True
    notes_registry.clear()
    return app.test_client()

def test_health_check_endpoint():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_material_addition_updates_registry():
    c = client()
    post_res = c.post("/share", data={
        "title": "DevOps Question Bank",
        "link": "https://google.com",
        "category": "Exam Prep",
        "contributor": "1032210000"
    })
    assert post_res.status_code == 302
    
    home_view = c.get("/").data
    assert b"DevOps Question Bank" in home_view
    assert b"Exam Prep Materials: 1" in home_view

def test_blank_field_submission_rejected():
    c = client()
    bad_submission = c.post("/share", data={
        "title": "",
        "link": "https://google.com",
        "category": "Lecture Notes",
        "contributor": ""
    })
    assert bad_submission.status_code == 400