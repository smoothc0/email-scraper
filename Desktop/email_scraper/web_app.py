from flask import Flask, render_template, request, send_from_directory
import os
from main import run_scraper  # ✅ Make sure you're importing the right function

app = Flask(__name__)

OUTPUT_DIR = 'output'

@app.route('/', methods=['GET', 'POST'])
def index():
    emails = None
    keyword = None
    file = None  # ✅ Add this

    if request.method == 'POST':
        keyword = request.form['keyword']
        result = run_scraper(keyword)  # ✅ Call the actual scraping function
        emails = result['emails']
        file = os.path.basename(result['file']) if result['file'] else None  # ✅ Extract just filename

    return render_template('index.html', emails=emails, keyword=keyword, file=file)  # ✅ Pass file to template

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
