from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Engineering Skills Virtual Laboratory', page_icon='⚡', layout='wide')
st.markdown('<style>.block-container {padding-top:1rem;padding-bottom:0}</style>', unsafe_allow_html=True)
components.html(Path(__file__).with_name('lab.html').read_text(encoding='utf-8'), height=1800, scrolling=True)
