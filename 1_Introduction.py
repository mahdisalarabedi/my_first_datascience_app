import streamlit as st 

st.markdown(
    "<h1 style='direction: rtl; text-align: right;'>معرفی برنامه</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    این برنامه تعدادی از گفتگو های بیماران مبتلا به سرطان پانکراس و مراقبان آن ها را به صورت تصادفی از یک گروه تلگرامی انتخاب می کند و با مدل زبانی شرکت OpenAI تحلیل موضوعی انجام میدهد</div>
    """,
    unsafe_allow_html=True
)