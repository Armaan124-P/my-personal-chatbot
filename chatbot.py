import streamlit as st

def query (user_query): 

    api_key = st.secrets["GEMINI_API_KEY"] 

    from google import  genai

    my_ai = genai.Client(api_key = api_key)

    responce = my_ai.models.generate_content(
        model = "gemini-1.5-flash-8b",
        contents = user_query
    )

    return responce.text

if "message" not in st.session_state:
    st.session_state.message = []



st.title("MY PERSONAL AI CHATBOT")

for i in st.session_state.message:
    with st.chat_message(i["role"]):
        st.markdown(i["msg"])

user_input = st.chat_input("enter you question")

if user_input :
    st.session_state.message.append({
        "role": "user",
        "msg" : user_input

    })
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("ai"):
        with st.spinner("wait"):
            result = query (user_input)    
            st.markdown(result)
    st.session_state.message.append({
        "role": "ai",
        "msg" : result

    })         
