from flask import Flask,render_template,request,session
from langchain_community.llms import Ollama
llm = Ollama(model="llama3.2")
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
                answers = llm.invoke(questions)
        except:
            answers = "Unable to grab data..!.Please enter the query again."
    return render_template('ask.html',answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
    
