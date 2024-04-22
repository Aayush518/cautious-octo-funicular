from langchain_core.prompts import PromptTemplate 
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain 

import os
from secret_key import secret_key
os.environ['HUGGINGFACEHUB_API_TOKEN']=secret_key

# create the best prompt for the task
prompt = PromptTemplate(
    input_variables= ['product_name'],
template="Write a detailed and creative  description for a product named {product_name}." 
)


chain = LLMChain(llm=HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={'temperature':0.2}),prompt = prompt)

def get_product_description(product_name):
    """Generates product description using Langchain model"""
    output = chain.run(product_name=product_name)
    return output