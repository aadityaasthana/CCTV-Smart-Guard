# dashboard_streamlit.py
import streamlit as st
import os
from glob import glob

st.set_page_config(layout='wide')
st.title('CCTV Smart Guard - Alerts')
clip_dir = 'data/clips'
if not os.path.exists(clip_dir):
    st.write('No clips yet. Run app.py first.')
else:
    clips = sorted(glob(os.path.join(clip_dir, '*.mp4')), reverse=True)
    for c in clips[:20]:
        st.video(c)
        st.write('---')
