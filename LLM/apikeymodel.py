import gradio as gr
import openai
import os

# Set your OpenAI API key
openai.api_key = "AIzaSyDdj5Ud3l4qv3MknBbQvwgOO5bwpHbg9Pg"  # Or set it directly
openai.api_base="https://api.groq.com/openaiv1"

def travel_assistant(query):
    system_prompt = "You are a travel assistant that helps users plan trips, suggest destinations, and give travel tips."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

iface = gr.Interface(fn=travel_assistant, 
                     inputs="text", 
                     outputs="text",
                     title="AI Travel Assistant (OpenAI)",
                     description="Enter your travel questions, and I'll help!")

iface.launch()
