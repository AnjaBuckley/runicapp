import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(
    page_title="Runic Alphabet Learning App", page_icon="🪄", layout="wide"
)

st.title("Runic Alphabet Learning App")
st.write("""
Learn and test your knowledge of ancient runic alphabets:
- Elder Futhark (2nd–8th century CE)
- Younger Futhark (Viking Age)
- Anglo-Saxon Futhorc (Early Medieval England)
""")

st.write(
    "Navigate to the Learn page to study the alphabets, or the Test page to practice your knowledge."
)
