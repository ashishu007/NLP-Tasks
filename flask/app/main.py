from app import app1
from flask import request, render_template, jsonify
from app import nlp_obj

@app1.route('/check', methods=['GET'])
def check():
    return jsonify({'status': 'ok'})

@app1.route("/")
def hello():
    return render_template("index.html")

@app1.route("/sentiment", methods=["POST", "GET"])
def classify_sentiment():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)

    query = form_r["query"][0]
    result = nlp_obj.return_sentiment(query)
    result[0]["query"] = query

    print(result)

    return render_template("results.html", result=result, task="Sentiment Analysis")

@app1.route("/squad", methods=["POST", "GET"])
def question_answering():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)

    question = form_r["question"][0]
    context = form_r["context"][0]

    result = nlp_obj.return_answer(context, question)
    
    result["question"] = question
    result["context"] = context

    return render_template("results.html", result=result, task="Question Answering")

@app1.route("/gpt2", methods=["POST", "GET"])
def generate_text():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)

    context = form_r["context"][0]
    result = nlp_obj.return_generated_text(context)
    
    result[0]["context"] = context
    print(result)

    return render_template("results.html", result=result, task="Text Generation")
