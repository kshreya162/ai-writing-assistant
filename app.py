import streamlit as st
from llm import get_llm
from prompts import (blog_prompt,email_prompt,code_prompt,social_prompt)

st.set_page_config(
    page_title="AI Writing Assistant",
    layout="wide"
)

st.title("AI Writing Assistant")
st.write(
    "Generate blogs, emails, code explanations, "
    "and social media posts using Gemini."
)

st.sidebar.header("Settings")

mode = st.sidebar.selectbox(
    "Choose a writing mode",
    [
        "Blog Writer",
        "Email Drafter",
        "Code Explainer",
        "Social Media Post"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

if mode == "Blog Writer":

    topic = st.text_area(
        "What should the blog be about?"
    )

elif mode == "Email Drafter":

    content = st.text_area(
        "What should the email say?"
    )

    tone = st.selectbox(
        "Choose tone",
        ["Professional", "Friendly", "Formal", "Casual"]
    )

elif mode == "Code Explainer":

    code = st.text_area(
        "Paste your code here",
        height=300
    )

elif mode == "Social Media Post":

    topic = st.text_area(
        "What should the post be about?"
    )

if st.button("Generate"):

    llm = get_llm(temperature)

    if mode == "Blog Writer":

        chain = blog_prompt | llm

        response = chain.invoke({
            "topic": topic
        })

    elif mode == "Email Drafter":

        chain = email_prompt | llm

        response = chain.invoke({
            "content": content,
            "tone": tone
        })

    elif mode == "Code Explainer":

        chain = code_prompt | llm

        response = chain.invoke({
            "code": code
        })

    elif mode == "Social Media Post":

        chain = social_prompt | llm

        response = chain.invoke({
            "topic": topic
        })

    st.subheader("Generated Content")
    st.markdown(response.content[0])