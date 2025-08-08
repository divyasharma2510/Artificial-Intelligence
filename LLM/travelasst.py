import gradio as gr
import openai
import os

# Set your OpenAI API key
openai.api_key = "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"  # Or set it directly
openai.api_base="https://api.groq.com/openai/v1"

def travel_assistant(query):
    system_prompt = "You are a smart travel assistant. You help users plan trips, suggest the best tourist spots,offer itinerary ideas, local tips, transportation info, and food recommendations."
    
    response = openai.ChatCompletion.create (
        model= "llama3-8b-8192",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

'''iface = gr.Interface(fn=travel_assistant, 
                     inputs="text", 
                     outputs="text",
                     title="AI Travel Assistant (OpenAI)",
                     description="Enter your travel questions, and I'll help!")

iface.launch()'''

iface = gr.Interface(
    fn=travel_assistant,
    inputs=gr.Textbox(lines=2, placeholder="e.g. Plan a 2-day trip to Tokyo"),
    outputs="text",
    title="🌍 AI Travel Assistant",
    description="Ask travel questions and get detailed trip plans, places to visit, food to try, and more — powered by Groq + GPT!"
)

iface.launch()
