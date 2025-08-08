import requests
import json
import gradio as gr

#Ollama API setup
url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type':'application/json',
}
history = []

#Function to generate response from model
def generate_response(prompt):
    history.append(f"User: {prompt}")
    final_prompt = "\n".join(history)

    data = {
        "model":"AI-Avatar",
        "prompt":final_prompt,
        "stream":False
    }
    response = requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code == 200:
        response_data = json.loads(response.text)
        reply = response_data.get('response','')
        history.append(f"AI-Avatar: {reply}")
        return reply
    else :
        print("Error:",response.text)
        return "Oops! Something went wrong."
    
#create Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs =gr.Textbox(lines=2,placeholder="Ask anything to AI-Avatar...."),
    outputs = "text",
    title="Chat with AI-Avatar"
)
interface.launch(share=True)