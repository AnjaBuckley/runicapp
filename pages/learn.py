import streamlit as st
from utils.data_loader import RunicData

st.set_page_config(page_title="Learn Runic Alphabets", page_icon="📚", layout="wide")

st.title("Learn Runic Alphabets")


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

# Display runes in a grid
alphabet_data = runic_data.get_alphabet(selected_alphabet)

# Create a grid layout
cols = st.columns(4)
col_index = 0

for latin_char, rune_data in alphabet_data.items():
    with cols[col_index]:
        st.image(rune_data["image_path"], width=100)
        st.write(f"**Name:** {rune_data['name']}")
        st.write(f"**Latin:** {rune_data['latin_equivalent']}")
        st.write(f"**Meaning:** {rune_data['meaning']}")

    col_index = (col_index + 1) % 4
