from flask import Flask, render_template, jsonify, request
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings

import os
prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
app = Flask(__name__)


embeddings = embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb=Chroma(persist_directory='db',embedding_function=embeddings)


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",model_type="llama",config={'max_new_tokens':2048,'context_length' : 4096,'temperature':0.8})

qa=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=vectordb.as_retriever(search_kwargs={"k":2}),return_source_documents=True,chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)