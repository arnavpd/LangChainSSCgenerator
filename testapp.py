# api imports
import os
from apikey import apikey

# web app
import streamlit as st 

# langchain imports 
from langchain.llms import AI21
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['AI21_API_KEY'] = apikey
st.title("LLM Chain generating tool")

# create instance of OpenAI service
llm = AI21(model="j2-jumbo-instruct")

# pass in prompt
promptNum = int(st.text_input('Enter how many prompts you want processed by the Large Language Model'))

# array of prompts
prompts = []

# store each prompt
for i in range(promptNum):
    prompt = st.text_input('Enter your prompt', key = i)
    prompts.append(prompt)

# print prompts
st.write(prompts)

# create script template for each prompt
script_templates = []

# create the other templates
for i in range(promptNum):
    template = PromptTemplate(
        input_variables = ['title'],
        template= prompts[i] + '{title}'
    )
    script_templates.append(template)
    
# print script templates
st.write(script_templates)

# link the templates together
chains = []
for i in range(promptNum):
    # handle last case
    if i == promptNum - 1:
        title_chain = LLMChain(llm=llm, prompt = script_templates[i], verbose=True)
        script_chain = LLMChain(llm=llm, prompt = script_templates[0], verbose=True)
        sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)
        chains.append(sequential_chain)
        break
    title_chain = LLMChain(llm=llm, prompt = script_templates[i], verbose=True)
    script_chain = LLMChain(llm=llm, prompt = script_templates[i+1], verbose=True)
    sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)
    chains.append(sequential_chain)


# print chains
st.write(chains)

# single prompt
final_prompt = st.text_input('Enter your final prompt', key = promptNum + 1)

if final_prompt:
    # run the chain where the prompt is now title template which has the updated topic as prompt
    response = chains[0].run(final_prompt)
    st.write(response)