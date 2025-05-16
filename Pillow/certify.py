from flask import Flask, request, send_file, render_template_string
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head><title>Generate Certificate</title></head>
<body>
  <h2>Student Certificate Form</h2>
  <form action="/generate" method="post">
    Name: <input type="text" name="name"><br>
    Mother's Name: <input type="text" name="mother_name"><br>
    Father's Name: <input type="text" name="father_name"><br>
    DOB: <input type="text" name="dob"><br>
    Month/Year: <input type="text" name="month_year"><br>
    Register No: <input type="text" name="reg_no"><br><br>
    <input type="submit" value="Generate Certificate">
  </form>
</body>
</html>
'''

@app.route('/')
def form():
    return render_template_string(HTML_FORM)

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data
    name = request.form['name']
    mother = request.form['mother_name']
    father = request.form['father_name']
    dob = request.form['dob']
    month_year = request.form['month_year']
    reg_no = request.form['reg_no']

    # Load template image
    template_path = "210d0dbe-1984-4ef7-9f0e-8492b69b98e9.png"  # Make sure this file is present
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 24)

    # Draw text on the image
    draw.text((100, 220), f"Name: {name}", font=font, fill="black")
    draw.text((100, 260), f"Mother's Name: {mother}", font=font, fill="black")
    draw.text((100, 300), f"Father's Name: {father}", font=font, fill="black")
    draw.text((100, 340), f"Date of Birth: {dob}", font=font, fill="black")
    draw.text((100, 380), f"Month/Year: {month_year}", font=font, fill="black")
    draw.text((100, 420), f"Register No.: {reg_no}", font=font, fill="black")

    # Save to memory and return
    output = io.BytesIO()
    img.save(output, format="PNG")
    output.seek(0)
    return send_file(output, mimetype='image/png', download_name='certificate.png')

if __name__ == '__main__':
    app.run(debug=True)
