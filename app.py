import streamlit as st
import os
from rag_engine import load_qa_chain, ask_question

st.set_page_config(page_title='Lux Grown Assistant', page_icon='💎', layout='centered')

st.markdown('''
<style>
.stApp { background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%); }
h1 { color: #d4af37 !important; font-family: Georgia, serif; }
.source-box { background: #1e1e2e; border-left: 3px solid #d4af37; padding: 8px 14px; border-radius: 4px; font-size: 13px; color: #9ca3af; margin-top: 8px; }
</style>
''', unsafe_allow_html=True)

st.markdown('# 💎 Lux Grown Assistant')
st.markdown('Ask me anything about our lab-grown diamond jewelry collection.')

if not os.path.exists('chroma_db'):
    st.error('No product data found. Please add PDFs to the docs folder and run: python ingest.py')
    st.stop()

@st.cache_resource(show_spinner='Loading Lux Grown knowledge base...')
def get_chain():
    return load_qa_chain()

qa_chain = get_chain()

if 'messages' not in st.session_state:
    st.session_state.messages = [{'role': 'assistant', 'content': 'Hello! I am the Lux Grown jewelry assistant. I can answer questions about our lab-grown diamond collection, styles, metals, pricing, and care. What would you like to know? 💎'}]

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])
        if 'sources' in msg and msg['sources']:
            st.markdown(f'<div class="source-box">Sources: {" | ".join(msg["sources"])}</div>', unsafe_allow_html=True)

if user_input := st.chat_input('Ask about our jewelry collection...'):
    st.session_state.messages.append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)
    with st.chat_message('assistant'):
        with st.spinner('Looking through our catalog...'):
            result = ask_question(qa_chain, user_input)
        st.markdown(result['answer'])
        if result['sources']:
            st.markdown(f'<div class="source-box">Sources: {" | ".join(result["sources"])}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({'role': 'assistant', 'content': result['answer'], 'sources': result['sources']})

with st.sidebar:
    st.markdown('### 💎 Lux Grown')
    st.markdown('*Lab-Grown Diamond Jewelry*')
    st.divider()
    st.markdown('**Try asking:**')
    for q in ['What ring styles do you carry?', 'Do you offer rose gold settings?', 'What is your return policy?', 'How do I care for my jewelry?', 'What certifications do your diamonds have?']:
        st.markdown(f'- {q}')
    st.divider()
    if st.button('Clear chat history'):
        st.session_state.messages = [{'role': 'assistant', 'content': 'Hello! What would you like to know about Lux Grown? 💎'}]
        st.rerun()
    st.caption('Powered by Llama 3.2 | ChromaDB | LangChain')
