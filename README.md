# Number Fun Fact Langchain

Welcome to the Number Fun Fact Langchain project! This project leverages OpenAI's GPT models to generate fun and interesting facts about numbers. Whether you're a math enthusiast, a curious learner, or just looking for some entertaining tidbits, this project is for you.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Set Up API Key**: Obtain an OpenAI API key and set it up as described below.

### Setting Up Your OpenAI API Key

1. Sign up for an OpenAI account and obtain an API key.
2. Copy the `.env.example` file to a new file named `.env`.
3. Replace the placeholder in the `.env` file with your actual OpenAI API key.

## Installation

Ensure you have Python installed on your system. Then, follow these steps to install the necessary dependencies:

1. Navigate to the project directory.
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command in the project directory:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser. You can then interact with the application to obtain fun facts about numbers.

## Input Handling

The application can handle both plain numbers and natural language inputs containing numbers. For example:

- Direct number input: `5`
- Natural language input: `Tell me something interesting about the number 5.`

The application will extract the number from the input and provide a fun fact about it. If the input does not contain a number or contains an invalid number, the user will be informed accordingly.

## Features

- **Interactive Input**: Enter a number to learn a fun fact about it.
- **Live API Interaction**: Utilizes the numbersapi.com API to fetch real-time data.
- **LLM Integration**: Employs LangChain and OpenAI GPT models for enhanced responses.
