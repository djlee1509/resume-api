from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

with open('resume.json5') as f:
    data = json.load(f)


@app.route('/resume')
def resume():
    return jsonify(data)


@app.route('/profile')
def get_profile():
    return jsonify(data['profile'])


@app.route('/contact/<string:contact_detail>')
@app.route('/contact/', defaults={'contact_detail': None})
def get_contact(contact_detail):
    if contact_detail is None:
        return jsonify(data['contact'])

    if contact_detail in ["email", "github", "phone"]:
        return jsonify(data['contact'][contact_detail])
    return jsonify({'Error': f"Parameter: {contact_detail} does not exist in contact."})


@app.route('/skills/', defaults={'skill': None})
@app.route('/skills/<string:skill>')
def get_skills(skill):
    if skill is None:
        return jsonify(data["skills"])

    if skill in ["technical_skills", "languages"]:
        return jsonify(data["skills"][skill])
    return jsonify({'Error': f"Parameter: {skill} does not exist in skills."})


@app.route('/<string:sec>/', defaults={'num': None})
@app.route('/<string:sec>/<int:num>')
def get_section(num, sec):
    if sec in ["experience", "projects", "education"]:
        section = data[sec]

        if num is None:
            return jsonify(section)

        if 0 < num <= len(section):
            rank = num - 1
            return jsonify(section[rank])
        return jsonify({'Error': f"{num} is out of range in the list of my {sec}. Range: 1 - {len(section)}"})
    return jsonify({'Error': f"Wrong Request! {sec} section is not in my CV."})


# @app.route('/projects/<int:num>')
# def get_project(num):
#     rank = num - 1
#     projects = data['projects']
#
#     if 0 < num <= len(projects):
#         return jsonify(projects[rank])
#     return jsonify({'Error': f"{num} is out of range in the list of my projects. Range: 1 - {len(projects)}"})
#
#
# @app.route('/education/<int:num>')
# def get_education(num):
#     rank = num - 1
#     education = data['education']
#
#     if 0 < num <= len(education):
#         return jsonify(education[rank])
#     return jsonify({'Error': f"{num} is out of range in the list of my education. Range: 1 - {len(education)}"})


@app.route('/interests')
def get_interests():
    return jsonify(data['interests'])


if __name__ == "__main__":
    app.run(debug=True)