# Indian-cultureBot
I built this chatbot on `indian culture and heritage` 

## Clone repo
`link:` https://github.com/Abhi4012/Indian-cultureBot.git

```git clone https://github.com/Abhi4012/Indian-cultureBot.git``` clone this repository using `git bash` or `command prompt` in you local system.


## some steps for using this project and run in locaL systems
## create an enviroment
`conda create --prefix ./env python=3.10 -y`

## activate enviroment
`conda activate ./env`

## Install requirements
`pip install -r requirements.txt`


## create .env file for keep your secret api key
PINECONE: Pinecone is a cloud-based vector database designed specifically to store, index, and retrieve high-dimensional vectors. 
```pinecone link for creating api key and environment:``` https://www.pinecone.io/
`PINECONE_API_KEY = "YOUR PINECONE API KEY"`
`PINECONE_API_ENV = "YOUR PINECONE ENV KEY"`

## Download the model
model name:
`llama-2-7b-chat.ggmlv3.q4_0.bin`
model link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main


## Run
`python app.py`