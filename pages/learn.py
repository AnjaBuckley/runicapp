import streamlit as st
from utils.data_loader import RunicData
import os
import base64
from PIL import Image
import io

st.set_page_config(page_title="Learn Runic Alphabets", page_icon="📚", layout="wide")

st.title("Learn Runic Alphabets")

# Add this near the top of your file
import os


# Initialize data
@st.cache_resource
def get_runic_data():
    return RunicData()


runic_data = get_runic_data()

# Alphabet selection
selected_alphabet = st.radio(
    "Select Runic Alphabet:", runic_data.get_all_alphabet_names()
)

# Display alphabet info
st.subheader(f"{selected_alphabet} Alphabet")

if selected_alphabet == "Elder Futhark":
    st.write("24 runes used from 2nd to 8th century CE")
elif selected_alphabet == "Younger Futhark":
    st.write("16 runes used during the Viking Age")
else:  # Anglo-Saxon Futhorc
    st.write("28 runes used in Early Medieval England")

# Get the alphabet data
alphabet_data = runic_data.get_alphabet(selected_alphabet)
st.write("Paths from get_alphabet:")
for key, rune in list(alphabet_data.items())[:2]:  # Show first two for brevity
    st.write(f"{key}: {rune['image_path']}")

# Display runes in a grid
alphabet_data = runic_data.get_alphabet(selected_alphabet)

# Add this before your grid display code
st.write("Current working directory:", os.getcwd())
st.write("Files in static/images/Elder Futhark:")
try:
    files = os.listdir("static/images/Elder Futhark")
    st.write(files)
except Exception as e:
    st.write(f"Error listing directory: {str(e)}")

# Create a grid layout
cols = st.columns(4)
col_index = 0

for latin_char, rune_data in alphabet_data.items():
    with cols[col_index]:
        # Try to find the file regardless of case
        image_path = rune_data["image_path"]
        correct_case_path = None

        # Check if the directory exists with proper case
        dir_path = os.path.dirname(image_path)
        if not os.path.exists(dir_path):
            # Try to find the directory with the correct case
            parent_dir = os.path.dirname(dir_path)
            if os.path.exists(parent_dir):
                for item in os.listdir(parent_dir):
                    if item.lower() == os.path.basename(dir_path).lower():
                        correct_case_path = os.path.join(
                            parent_dir, item, os.path.basename(image_path)
                        )
                        break
        else:
            correct_case_path = image_path

        if correct_case_path and os.path.exists(correct_case_path):
            st.image(correct_case_path, width=100)
        else:
            st.write(f"Image not found: {rune_data['name']}")

        st.write(f"**Name:** {rune_data['name']}")
        st.write(f"**Latin:** {rune_data['latin_equivalent']}")
        st.write(f"**Meaning:** {rune_data['meaning']}")

    col_index = (col_index + 1) % 4
