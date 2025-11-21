import os
from flask import Flask,render_template,request
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.2-3b-preview",temperature = 0)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask',methods=['GET','POST'])
def ask_questions():
    answers=''
    if request.method == "POST":
        try:
            questions = request.form.get('question').lower()
            if questions == "what is your name":
                answers = "I am GeNet. Your Ai assistant!"
            else:
                response = llm.invoke(questions)
                answers = response.content
        except Exception as e:
            print(f"Error: {e}")
            answers = "Unable to grab data..!.Please enter the query again."
    return render_template('ask.html',answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
    
