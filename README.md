# Sample code and notebooks for PyJax Langchain Demo

In order to run the OpenAI examples, you will need an OpenAI API Key from OpenAI in order to run the examples. You can either replace the OPENAI_API_KEY in the code or set an environment variable for OPENAI_API_KEY.

## Virtual Environment

I recommend setting a virtual environment for running this project.

You can activate a virtual environment on a Mac or Linux with the following commands:

```sh
$ python -m venv .venv
$ source .venv/bin/activate
```

Once the environment is activated, you can install the following LangChain packages:

```sh
$ pip install langchain_core
$ pip install langchain_openai
```

You can also install the dependencies from this repo by running the following command:

```sh
$ pip install -r requirements.txt
```

# OpenAI example require API Key

All of the OpenAI example require the OpenAI API Key. You can obtain an OpenAI API Key by going to their [platform portal](https://platform.openai.com/api-keys).

# Running the ChatBot

To run the chatbot, run the following command:

```sh
streamlit run pyjaxchatbot.py
```
