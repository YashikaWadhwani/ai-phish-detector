from flask import Flask, render_template, request
import google.generativeai as genai
import os
import PyPDF2

#app 
app = Flask(__name__)

#set up the google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDQ5jTmn6FRT_N-tV1pyKOUkz7HlwIpJtc"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

#initialize the gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


def predict_fake_or_real_email_content(text):
        prompt = f"""
        you are an expert in identifying scam emails in text, email etc , analyse the following text 

        -**Real/Legitimate** (Authentic, safe message)
        -**Scam/Fake** (Phishing, fraudulent message, or suspicious message)

        for the following text 
        {text}

        return a clear message indicating whether this content is real or fake 

        only return classification message and nothing else
        note: do not return empty or null response
        """


        response = model .generate_content(prompt)
        return response.text.strip() 

def url_detection(url):
        prompt = f"""
        you are an expert in identifying scam urls and phishing websites , analyse the following url 

        -**Legitimate** (Authentic, safe website)
        -**Phishing** (Fraudulent website, or suspicious website)
        -**Malware** (Malicious website, or harmful website)
        -**defacement** (Hacked website, or compromised website)
        -**spam** (Spammy website, or unwanted website)

        for eg
        -**Legitimate** : https://www.google.com , https://www.wikipedia.org
        -**Phishing** : http://secure-login-paypal.com , http://update-accounts.com     
        -**Malware** : http://malicious-site.com , http://dangerous-download.com , "http://free-gift-cards.com"
        -**defacement** : http://hacked-website.com , http://compromised-site.com
        -**spam** : http://spammy-site.com , http://unwanted-offers.com 

        etc

        for the following url 
        {url}

        return a clear message indicating whether this url is legitimate or phishing 

        only return classification message and nothing else
        note: do not return empty or null response
        """


        response = model .generate_content(prompt)
        return response.text.strip()

#routes 
@app.route("/")
def index():
          return render_template("index.html")
@app.route("/scam/", methods=["GET", "POST"])
def detect_scam():
        if "file" not in request.files:
                return render_template("index.html", message="No file part")
        file = request.files['file']
        
        extracted_text = ""
        if file.filename.endswith('.pdf'):
                pdf_reader = PyPDF2.PdfReader(file)
                extracted_text =" ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        elif file.filename.endswith('.txt'):
                extracted_text = file.read().decode('utf-8')
        else:
                return render_template("index.html", message="Unsupported file type. Please upload a PDF or TXT file.")             

           
        message = predict_fake_or_real_email_content((extracted_text))
        return render_template("index.html", message=message)


@app.route("/predict", methods=["POST"])
def predict_url():
        if request.method == "POST":
                url = request.form.get("url", "").strip()
                
                if not url.startswith(("http://", "https://")):
                        return render_template("index.html", message="Invalid URL. Please enter a valid URL starting with http:// or https://")
                
                classification = url_detection(url)
                return render_template("index.html", predicted_class=classification)
#python main

if __name__ == "__main__":
    app.run(debug=True)
