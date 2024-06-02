from flask import Flask, render_template,request
import requests
from io import BytesIO
import numpy as np 
from PIL import Image as im 
import base64
import requests
import json


app = Flask(__name__)


#text to image API 

API_URL_text_to_image = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers_text_to_image = {"Authorization": "Bearer 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"}

# API_URL_text_to_image = "https://api-inference.huggingface.co/models/stabilityai/stable-cascade"
# headers_text_to_image = {"Authorization": "Bearer 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"}

def query_text_to_image(payload):
	response = requests.post(API_URL_text_to_image, headers=headers_text_to_image, json=payload)
	return response.content







#talk to me(ttm) api 





#text summarization api


# API_URL_summarization = "https://api-inference.huggingface.co/models/pszemraj/led-large-book-summary"
# headers_summarization = {"Authorization": "Bearer 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"}

API_URL_summarization= "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers_summarization= {"Authorization": "Bearer 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"}


def query_summarization(payload):
	response = requests.post(API_URL_summarization , headers=headers_summarization, json=payload)
	# return response.content
	return response.content




@app.route("/")
def index():
    return render_template('index.html')



@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')




@app.route("/tools_page")
def tools_page():
    return render_template('tools_page.html')

#text to image 
# @app.route("/tool1")
# def tool1():
#     return render_template('tool1.html')

@app.route("/textTOimage", methods=["GET", "POST"])
def tool1():
    if request.method == "POST":
        data = request.form["data"] 
        data= query_text_to_image({"inputs":data})

        base64_data = base64.b64encode(data).decode('utf-8')
        return render_template("textTOimage.html", base64_data=base64_data)
    else:
        return render_template("textTOimage.html")
    


#ttm


# @app.route("/tool2")
# def tool2():
#     return render_template('tool2.html')


@app.route("/TTM", methods=["GET", "POST"])
def tool2():
    # if request.method == "POST":
    #     msgtext= request.form["ttm"] 
    #     msgtext= query_summarization({"inputs":msgtext})

    #     # msgtext= base64.b64encode(msgtext).decode('utf-8')
    #     return render_template("TTM.html", data=msgtext)
    # else:
        return render_template("TTM.html")



#text summarization

# @app.route("/tool3")
# def tool3():
#     return render_template('tool3.html')
@app.route("/textSummarization", methods=["GET", "POST"])
def tool3():
    if request.method == "POST":
        msgtext= request.form["msgtext"] 
        msgtext= query_summarization({"inputs":msgtext})
        json_data = json.loads(msgtext)
        msgtext = json_data[0]['summary_text']
        # msgtext= base64.b64encode(msgtext).decode('utf-8')
        # msgtext=msgtext.get("summary_text")
        return render_template("textSummarization.html", data=msgtext)
    else:
        return render_template("textSummarization.html")




@app.route("/imgTOimg")
def tool4():
    return render_template("imgTOimg.html")





if __name__ == "__main__":
    app.run(debug=True,port=8002)