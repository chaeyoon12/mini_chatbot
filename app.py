import streamlit as st

st.set_page_config(page_title="미니 챗봇", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF0F5;  
        color: #4B0082;             
        font-family: 'Comic Sans MS', sans-serif;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: #4B0082;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("귀여운 미니 챗봇 🤖")
st.write("친구들이 입력하면 내가 대답해줘요!")

user_input = st.text_input("여기에 메시지를 입력하세요")

def chatbot_response(message):
    message = message.lower()
    if "안녕" in message or "hi" in message:
        return "안녕! 만나서 반가워"
    elif "이름" in message:
        return "나는 미니 챗봇이야! 🐰"
    elif "잘 지내" in message:
        return "응, 오늘 하루 어때?"
    elif "고마워" in message:
        return "천만에~ 😄"
    else:
        return "음… 잘 모르겠어 ㅠㅠ 😅"

if st.button("전송"):
    if user_input:
        response = chatbot_response(user_input)
        st.write("🤖 챗봇:", response)
    else:
        st.write("메시지를 입력해줘!")
