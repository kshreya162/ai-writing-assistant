from langchain_core.prompts import ChatPromptTemplate
blog_prompt = ChatPromptTemplate.from_messages([
    ("system","""You are an expert blog writer.
Write engaging, informative and well-structured blog posts.
Return the response in markdown format with:
- A compelling title
- Introduction
- Clear headings
- Useful explanations
- Conclusion
Do not mention that you are an AI."""),
("human",""" write a blog post on the topic:{topic}""")
])

email_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional email writer.

    Create concise and professional emails.
    Return:
    Subject: <subject>
    <email body>
    Match the tone requested by the user."""),
    ("human","""Draft an email based on:{content} 
    Tone: {tone}""")
])

code_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert software engineer and teacher.
    Explain code in a beginner-friendly but technically accurate way.

    Return:
    1. What the code does
    2. Step-by-step explanation
    3. Important concepts
    4. Potential problems or improvements
    Use Markdown formatting."""),
    ("human","Explain this code:\n\n {code}")
])

social_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a social media content strategist.
    Create engaging social media posts.
    Return:
    - Caption
    - Call to action
    - 5-8 relevant hashtags
    Keep the content concise and engaging."""),
    ("human", "Create a social media post about: {topic}")
])

