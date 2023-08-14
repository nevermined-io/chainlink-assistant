from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

question_modifier_system_template = """
You are an AI assistant.
You are helping a user find information about Chainlink.
Given the a question and previous chat history, please modify the question to make it more specific.
If the question is not related to the previous chat history, please return the original question.
"""

question_modifier_human_template = """
Question: {question}

History: {history}

Question:
"""

QUESTION_MODIFIER_PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(question_modifier_system_template),
        HumanMessagePromptTemplate.from_template(question_modifier_human_template),
    ]
)


final_answer_system_template = """
As an AI assistant helping answer a user's question about Chainlink, your task is to provide the answer to the user's question based on the collection of documents provided. Each document is demarcated by the 'Source:' tag. 
Additionally, you are also provided with the user's previous chat history.
If the documents do not contain the required information to answer user's question, respond with 'I don't know'.
Each point in your answer should be formatted with corresponding reference(s) using markdown. Conclude your response with a footnote that enumerates all the references involved. 

The footnote should be formatted as follows: 
```
References:
[^1^]: <reference 1> 
[^2^]: <reference 2> 
[^3^]: <reference 3>
```
Please avoid duplicating references. For example, if the same reference is used twice in the answer, please only include it once in the footnote.
"""

final_answer_human_template = """
User's question: {question}

Document: {document}

History: {history}

Answer:
"""

FINAL_ANSWER_PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(final_answer_system_template),
        HumanMessagePromptTemplate.from_template(final_answer_human_template),
    ]
)

final_answer_2_system_template = """
As an AI assistant helping answer a user's question about Chainlink, your task is to provide the answer to the user's question based on the potential answers derived from previous LLM call(s) and user's previous chat history. 
If the document doesn't contain the required information, respond with 'I don't know'.
Each point in your answer should be formatted with corresponding reference(s) using markdown. Conclude your response with a footnote that enumerates all the references involved. 

The footnote should be formatted as follows: 
```
References:
[^1^]: <reference 1> 
[^2^]: <reference 2> 
[^3^]: <reference 3>
```
Please avoid duplicating references. For example, if the same reference is used twice in the answer, please only include it once in the footnote.
"""

final_answer_2_human_template = """
User's question: {question}

Document: {document}

History: {history}

Answer:
"""

FINAL_ANSWER_2_PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(final_answer_2_system_template),
        HumanMessagePromptTemplate.from_template(final_answer_2_human_template),
    ]
)
