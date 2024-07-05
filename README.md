# MediChat
MediChat is an advanced medical chatbot designed to assist with clinical queries and provide information based on medical literature. It leverages state-of-the-art models and embeddings to deliver accurate and reliable responses.

## Features
### Medical Expertise: 
Provides information based on extensive training on medical literature.
### Advanced Model: 
Utilizes the [Llama-2-7B-Chat](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML) model from Hugging Face.
### Vector Database: 
Incorporates Chroma DB for efficient data retrieval.
### High-Quality Embeddings: 
Uses [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) embeddings from Hugging Face.
## Model Details
### Llama-2-7B-Chat Model:
- Source: [Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin)
- Description: An open-source large language model optimized for chat-based interactions, capable of understanding and generating human-like text.
## Database and Embeddings
### Chroma DB: 
A vector database that allows for efficient storage and retrieval of embeddings.
### Embeddings Model:
- Source: [Link](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- Description: A small, fast, and high-quality embedding model that provides dense vector representations of text.
## Training Data
MediChat is trained on embeddings derived from the following medical books:

- Clinical Emergency Medicine (PDFDrive.com)
- Current Essentials of Medicine
- Gale Encyclopedia of Medicine Vol. 4 (N-S)
## Installation
To set up MediChat, follow these steps:

Clone the Repository:

- git clone https://github.com/Gyanbardhan/MediChat.git
- cd MediChat
## Install Dependencies:


- pip install -r requirements.txt
## Download the Model and Embeddings:

- Llama-2-7B-Chat model: Download from Hugging Face and place it in the models directory.
- Sentence-Transformers embeddings: Download from Hugging Face and place them in the embeddings directory.
- Set Up Chroma DB

#### Run the MediChat application with the following command:


- python app.py
#### Interact with MediChat via the provided interface, asking medical questions and receiving expert responses based on the embedded medical literature.
