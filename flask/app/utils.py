from transformers import pipeline

class NLPTasks:
    def __init__(self):
        self.qa_pipe = pipeline("question-answering")
        self.sentiment_pipe = pipeline("sentiment-analysis")
        self.text_gen_pipe = pipeline("text-generation")

    def return_answer(self, context, question):
        return self.qa_pipe(question=question, context=context)

    def return_sentiment(self, query):
        return self.sentiment_pipe(query)

    def return_generated_text(self, context):
        return self.text_gen_pipe(context, max_length=50)
