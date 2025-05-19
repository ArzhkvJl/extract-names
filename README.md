# Intelligent search for information about companies.
Extracting and enriching company-related information from unstructured text.

## Overview 
The goal of this project is to produce JSON with structured information about companies mentioned in raw text.

## Installation
 Clone this repository, install packages from requirements.txt and download spacy model for language support.
```bash
git clone https://github.com/ArzhkvJl/extract-names  <my-folder>
cd <my-folder>
pip install -r requirements.txt
python -m spacy download en_core_web_trf  
```

## Usage

To use this application you have to create some API Keys from next links:

https://console.groq.com/keys

https://app.tavily.com/home

Put these API keys into .env file.

The input file `input.json` contains example texts that may mention zero or more companies. Each text is stored under a numbered JSON key. Use the provided sample texts or add your own text entries to the file using the same format.
```bash
# Run the application
python app.py
```
After launching the application specify the number of the input text you'd like to analyze.
The system will extract company mentions and generate structured information.
The result will be saved to `output.json` as a JSON object containing details about each company.

##  Features

* Extracts company names from arbitrary English text using `spaCy` (transformer-based NER)
* Uses Tavily API to search the web for relevant and recent information
* Uses a LangGraph ReAct agent with Groq-hosted LLM (`llama-3.3-70b-instant`) to generate structured data
* Outputs JSON per company including:
  * Website
  * Sector
  * Headquarters location
  * Short description
  * Key people (e.g. CEO, founders)
  * Competitive analysis