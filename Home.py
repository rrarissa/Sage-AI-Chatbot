import streamlit as st
#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="AI Chat-Bot 🤖")

# remove hamburger button
st.markdown(
    """
    <style>
    .css-14xtw13.e8zbici0 {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# remove streamlit footer
st.markdown(
    """
    <style>
    .css-164nlkn.egzxvld1 {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)



#Contact
with st.sidebar.expander("📬 Contact Creator"):

    st.write("**👩🏻 LinkedIn**",
    "[linkedin/ruishucao](https://www.linkedin.com/in/ruishu-cao-709700197/)")
    st.write("**📪 Mail** : arissa0107@gmail.com")
    st.write("**Created by Ruishu**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Hi there! I am <span style='color: #d46a8f; text-shadow: 0 0 2px #9b59b6;'>Sage</span> 🦋, your AI-powered assistant.🤖 </h2>
    <h2 style='text-align: center;'>    It is great to meet you! ❤</h2>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

#Description
st.markdown(
    """ 
    <p style='text-align:center;font-size:18px;'>
I'm a smart chatbot using the best features of Langchain and Streamlit. 💻
 My aim is to help you quickly understand large documents and save you a ton of time. ⏰
 I support PDFs, TXT files, CSVs, and YouTube transcripts. 🧠

</p>
    """,
    unsafe_allow_html=True)
st.markdown("---")

# Pages 
st.subheader("🚀 Sage's Pages")
st.write("""
- **Robby-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Robby-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **Robby-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**The Sage Chatbot is under regular development. Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)



