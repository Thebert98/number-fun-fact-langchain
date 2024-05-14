import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import requests
from langchain.agents import tool
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor


# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
        "system",
        """
            You are an advanced assistant designed to provide users with a fun fact about a number included in their input, {input}. 
            Utilize the numbersapi.com API to retrieve these fun facts. Ensure that you only relay the fun facts obtained directly from the numbersapi.com API, without creating your own facts or altering the content. Do not provide any output other than the fun fact, and do not format the response in JSON. If the user's input does not contain a number, inform them that you can provide a fun fact if they specify a number. It is acceptable if the input includes additional text, as long as a number is present. If a number is included but it is not a positive integer or 0 (zero), notify the user that you only provide fun facts for positive integers.
            """,
        ),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Define a tool to get a fun fact about a number
@tool
def get_number_fun_fact(num:int)->str:
    """Calls numbersapi.com/{num}/math api using the inputted number and returns fun fact about that number"""
    response = requests.get(f"http://numbersapi.com/{num}/math") 
    if response.ok:
        return response.text
    else:
        return "Failed to retrieve fun fact."

# Define the main function
def main():
    # Load environment variables
    load_dotenv()
    llm =""
    # Set the page title and header
    st.set_page_config(page_title = "Number Random Fact Generator")
    
    st.header("Fun Fact About a Number LangChain Edition",divider="violet")
    
    # Allow the user to select the model to use
    model = st.selectbox(
            "Choose what llm to use",
            ("gpt-4-turbo-preview","gpt-3.5-turbo","gpt-4o"),
            index = None,
            placeholder = "Select OpenAI model.."
    )
    # If a model is selected, create a ChatOpenAI instance
    if(model is not None and model !=""):
        llm = ChatOpenAI(model = model, temperature = 0)
   
    # If a ChatOpenAI instance is created, bind the tool to it
    if(llm is not None and llm !=""):
        tools = [get_number_fun_fact]
        llm_with_tools = llm.bind_tools(tools)

        # Create an agent and an executor
        agent = create_tool_calling_agent(llm_with_tools, tools, prompt)
        agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True,return_intermediate_steps=True)
        
        # Get user input and invoke the executor
        user_input = st.text_input("Select a number to get a fun fact about:")
        if user_input is not None and user_input !="":
            response = agent_executor.invoke({"input":user_input})
            # Display the intermediate steps and the final output
            with st.expander("Intermediate steps"):
                st.write(response['intermediate_steps'])
            st.write(f"Your input: {response['input']}")
            st.write(response["output"])
        
# Run the main function if this script is the main entry point
if __name__ == "__main__":
    main()