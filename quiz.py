# quiz.py — Extended Fun + Serious Quiz based on DeepSeek vs ChatGPT Presentation

import streamlit as st

# --- Quiz Questions ---
quiz = [
    # Serious questions
    {"question": "Who were the founders of OpenAI?", "options": ["Elon Musk and Sam Altman", "Jeff Bezos and Sundar Pichai", "Bill Gates and Mark Zuckerberg"], "answer": "Elon Musk and Sam Altman"},
    {"question": "What year was OpenAI founded?", "options": ["2015", "2017", "2020"], "answer": "2015"},
    {"question": "Which company heavily partnered with OpenAI?", "options": ["Microsoft", "Apple", "Google"], "answer": "Microsoft"},
    {"question": "What is the architecture type used by ChatGPT models?", "options": ["Transformer", "CNN", "Recurrent Neural Network"], "answer": "Transformer"},
    {"question": "What architecture does DeepSeek-V2 use?", "options": ["Dense Transformer", "Mixture of Experts (MoE)", "Recursive Networks"], "answer": "Mixture of Experts (MoE)"},
    {"question": "What year was DeepSeek founded?", "options": ["2021", "2022", "2023"], "answer": "2023"},
    {"question": "What model introduced multimodal input (text, image, audio)?", "options": ["GPT-3.5", "GPT-4o", "DeepSeek-Coder"], "answer": "GPT-4o"},
    {"question": "Which DeepSeek model specializes in coding tasks?", "options": ["DeepSeek-V2", "DeepSeek-Coder", "DeepSeek LLM"], "answer": "DeepSeek-Coder"},
    {"question": "What type of license does DeepSeek use for its open models?", "options": ["MIT License", "GPL License", "Proprietary"], "answer": "MIT License"},
    {"question": "What training data types were used for ChatGPT?", "options": ["Only news articles", "Internet text, books, academic papers", "Only tweets"], "answer": "Internet text, books, academic papers"},
    {"question": "What is one major weakness of GPT-3.5?", "options": ["Slowness", "Weaker at complex reasoning", "Poor vocabulary"], "answer": "Weaker at complex reasoning"},
    {"question": "What country is DeepSeek based in?", "options": ["USA", "Germany", "China"], "answer": "China"},

    # Fun / Funny questions
    {"question": "What are we presenting today?", "options": ["A cooking class 🍳", "DeepSeek vs ChatGPT 🤖", "TikTok dance lessons 💃"], "answer": "DeepSeek vs ChatGPT 🤖"},
    {"question": "Who are the amazing members of this team?", "options": ["Lesalon, Salah, Alfred, Paschal", "Batman and Superman", "Tom and Jerry"], "answer": "Lesalon, Salah, Alfred, Paschal"},
    {"question": "DeepSeek sounds like the name of a...?", "options": ["Spy agency 🕵️", "New sports car 🚗", "AI company 🤖"], "answer": "AI company 🤖"},
    {"question": "Which model would be your best study buddy?", "options": ["GPT-4", "DeepSeek-Coder", "My cat 🐱"], "answer": "GPT-4"},
    {"question": "If you had to name your own AI company, what would you call it?", "options": ["SmartBrain 🤖", "LazyBot 😴", "CodeCrusher 💻"], "answer": "SmartBrain 🤖"},
    {"question": "OpenAI's main mission is to...?", "options": ["Conquer the world 🌎", "Benefit humanity 🤝", "Build flying cars 🚁"], "answer": "Benefit humanity 🤝"},
    {"question": "DeepSeek wants to make AI that is...?", "options": ["Hidden in caves 🧙", "Open-source and efficient 📖", "Only for robots 🤖"], "answer": "Open-source and efficient 📖"},
    {"question": "What's the best way to prepare for an AI presentation?", "options": ["Panic and eat pizza 🍕", "Study and practice 📚", "Hope for good luck 🍀"], "answer": "Study and practice 📚"},
]

# --- Streamlit Setup ---
st.set_page_config(page_title="🎉 DeepSeek vs ChatGPT Mega Quiz!", layout="centered")
st.title("🎉 DeepSeek vs ChatGPT — Fun & Serious Quiz!")

st.markdown("Test your memory and have fun based on our epic presentation! 🚀")

score = 0

# --- Display Quiz ---
for q in quiz:
    user_answer = st.radio(q["question"], q["options"], key=q["question"])
    if user_answer == q["answer"]:
        score += 1

# --- Submit and Show Results ---
if st.button("🎯 Submit Quiz"):
    st.success(f"You scored {score} out of {len(quiz)}!")

    if score == len(quiz):
        st.balloons()
        st.markdown("🏆 **Perfect score! You are officially an AI Mastermind!** 🧠🚀")
    elif score >= 15:
        st.markdown("🥳 **Awesome job! You're clearly paying attention!**")
    elif score >= 10:
        st.markdown("😄 **Good effort! Maybe one or two slides were missed... 😉**")
    else:
        st.markdown("😂 **Well... at least you now know DeepSeek isn't a car brand!**")

st.info("Thanks for playing! Stay smart, stay curious! 🚀")