import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "OPENAI_KEY"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        content = request.form['text']
        user_input = [({'role': 'user', 'content': content})]

        # Send user input to OpenAI API to generate response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=user_input
        )

        # Get the generated text from the API response
        generated_text = response.choices[0].message.content

        # Render the template with the generated text
        return render_template('home.html', output=generated_text, user_input=content)

    # Render the template with an empty output and no user input
    return render_template('home.html', output='', user_input='')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
