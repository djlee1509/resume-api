from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('resume.json5') as f:
    data = json.load(f)


@app.route('/profile')
def get_profile():
    return jsonify(data['profile'])


@app.route('/contact/<string:contact_detail>')
def get_contact(contact_detail):
    if contact_detail in ["email", "github", "phone"]:
        return jsonify(data['contact'][contact_detail])
    return jsonify({'Error': f"Parameter: {contact_detail} does not exist in contact."})


@app.route('/skills/<string:skill>')
def get_skills(skill):
    if skill in ["technical_skills", "languages"]:
        return jsonify(data["skills"][skill])
    return jsonify({'Error': f"Parameter: {skill} does not exist in skills."})


@app.route('/experience/<int:num>')
def get_experience(num):
    rank = num - 1
    exp = data['experience']

    if 0 < num <= len(exp):
        return jsonify(exp[rank])
    return jsonify({'Error': f"{num} is out of range in the list of my experiences. Range: 1 - {len(exp)}"})


@app.route('/projects/<int:num>')
def get_project(num):
    rank = num - 1
    projects = data['projects']

    if 0 < num <= len(projects):
        return jsonify(projects[rank])
    return jsonify({'Error': f"{num} is out of range in the list of my projects. Range: 1 - {len(projects)}"})


@app.route('/education/<int:num>')
def get_education(num):
    rank = num - 1
    education = data['education']

    if 0 < num <= len(education):
        return jsonify(education[rank])
    return jsonify({'Error': f"{num} is out of range in the list of my education. Range: 1 - {len(education)}"})


@app.route('/interests')
def get_interests():
    return jsonify(data['interests'])


if __name__ == "__main__":
    app.run(debug=True)