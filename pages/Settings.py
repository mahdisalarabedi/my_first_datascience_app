import streamlit as st
from Extracting_Conversations import Conversation_extractor
from Main_code_JSON_data_type import Prompting
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    لطفا پارامترهای زیر را تنظیم کنید</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    تعداد گفتگوهایی که میخواهید لیبل زده شوند را مشخص کنید</div>
    """,
    unsafe_allow_html=True
)
st.session_state.number_of_conversations=st.number_input(label="", min_value=50)
if st.button(label="to run the programm, click!", icon="🎉"):
    Conversation_extractor(st.session_state.number_of_conversations)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    دو پارامتر زیر میزان خلاقیت مدل را مشخص میکنند.\n هرچه قدر بیشتر باشند مدل پاسخ‌های خلاقانه تری میدهد</div>
    """,
    unsafe_allow_html=True
)
st.session_state.outcomes={}
st.session_state.temperature=st.number_input(label="temperature",min_value=0.0, max_value=1.0, step=0.1)
st.session_state.top_p=st.number_input(label="top_p", min_value=0.0, max_value=1.0,step=0.1)
if st.button(label="Let's label conversations"):
    st.session_state.outcomes=Prompting(st.session_state.top_p,st.session_state.temperature, number_of_API_calls=10)
