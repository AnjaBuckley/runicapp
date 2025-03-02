import streamlit as st
import random
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64
from utils.data_loader import RunicData
from utils.image_recognition import analyze_drawing

st.set_page_config(page_title="Test Your Runic Knowledge", page_icon="✏️", layout="wide")

st.title("Test Your Runic Knowledge")


# Initialize data
@st.cache_resource
def get_runic_data():
    return RunicData()


runic_data = get_runic_data()

# Alphabet selection
selected_alphabet = st.radio(
    "Select Runic Alphabet to Test:", runic_data.get_all_alphabet_names()
)

# Get the selected alphabet data
alphabet_data = runic_data.get_alphabet(selected_alphabet)

# Initialize session state for tracking the current test
if "current_rune" not in st.session_state:
    st.session_state.current_rune = random.choice(list(alphabet_data.keys()))
    st.session_state.attempts = 0
    st.session_state.correct = 0

# Display the current Latin character to convert
st.subheader(f"Draw the runic equivalent of: {st.session_state.current_rune.upper()}")

# Optional: Show a hint
if st.checkbox("Show hint"):
    rune_data = alphabet_data[st.session_state.current_rune]
    st.write(
        f"This is the rune '{rune_data['name']}', meaning '{rune_data['meaning']}'"
    )

# Drawing canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",
    stroke_width=3,
    stroke_color="#000000",
    background_color="#ffffff",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Submit"):
        if canvas_result.image_data is not None:
            # Convert the drawing to an image
            img_data = canvas_result.image_data

            # Get the expected rune for comparison
            expected_rune = alphabet_data[st.session_state.current_rune]["name"]

            # Analyze the drawing using the image recognition function
            is_correct, feedback = analyze_drawing(img_data, expected_rune)

            st.session_state.attempts += 1
            if is_correct:
                st.session_state.correct += 1
                st.success(f"Correct! That is the rune for '{expected_rune}'")
            else:
                st.error(f"Not quite. {feedback}")

            # Show the correct rune
            st.image(
                alphabet_data[st.session_state.current_rune]["image_path"],
                caption=f"The correct rune: {expected_rune}",
                width=150,
            )

with col2:
    if st.button("Next Rune"):
        # Choose a new random rune
        st.session_state.current_rune = random.choice(list(alphabet_data.keys()))
        # Clear the canvas (this will be handled by the key change in the canvas)
        st.experimental_rerun()

# Display stats
st.write(f"Attempts: {st.session_state.attempts}, Correct: {st.session_state.correct}")
if st.session_state.attempts > 0:
    accuracy = (st.session_state.correct / st.session_state.attempts) * 100
    st.write(f"Accuracy: {accuracy:.1f}%")
