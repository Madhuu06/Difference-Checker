from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from xml_compare import parse_xml_from_string, flatten_elements, compare_xml

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/compare', methods=['POST'])
def compare_xmls():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return jsonify({"error": "Both XML files are required"}), 400

    xml1 = file1.read().decode('utf-8')
    xml2 = file2.read().decode('utf-8')

    root1, err1 = parse_xml_from_string(xml1)
    root2, err2 = parse_xml_from_string(xml2)

    if err1 or err2:
        return jsonify({"error": err1 or err2}), 400

    flat1 = flatten_elements(root1)
    flat2 = flatten_elements(root2)
    differences = compare_xml(flat1, flat2)

    return jsonify(differences)

if __name__ == '__main__':
    app.run(debug=True)
