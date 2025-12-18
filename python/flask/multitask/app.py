from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get dropdown value
        dropdown_value = request.form.get("dropdown")
        
        # Get checkbox value (None if unchecked)
        checkbox_value = request.form.get("checkbox")
        
        # Get uploaded file
        uploaded_file = request.files.get("file")
        file_name = uploaded_file.filename if uploaded_file else None

        return f"""
        <h2>Form Submitted</h2>
        <p>Dropdown: {dropdown_value}</p>
        <p>Checkbox: {"Checked" if checkbox_value else "Not Checked"}</p>
        <p>Uploaded File: {file_name}</p>
        <br><a href="/">Go Back</a>
        """

    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(debug=True)
