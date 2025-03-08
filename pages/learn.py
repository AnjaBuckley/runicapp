import streamlit as st
from utils.data_loader import RunicData
import os
import base64
from PIL import Image
import io

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

    # Define Elder Futhark runes directly
    elder_futhark_runes = [
        {
            "name": "fehu",
            "latin": "f",
            "meaning": "cattle, wealth",
            "image": "laguz.png",
        },
        {
            "name": "uruz",
            "latin": "u",
            "meaning": "aurochs (wild ox)",
            "image": "uruz.png",
        },
        {
            "name": "algiz",
            "latin": "z",
            "meaning": "protection, elk",
            "image": "algiz.png",
        },
        {
            "name": "thurisaz",
            "latin": "th",
            "meaning": "giant, thorn",
            "image": "thurisaz.png",
        },
        {"name": "ansuz", "latin": "a", "meaning": "god, mouth", "image": "ansuz.png"},
        {
            "name": "raido",
            "latin": "r",
            "meaning": "ride, journey",
            "image": "raido.png",
        },
        {
            "name": "kenaz",
            "latin": "k",
            "meaning": "torch, ulcer",
            "image": "kenaz.png",
        },
        {"name": "gebo", "latin": "g", "meaning": "gift", "image": "gebo.png"},
        {
            "name": "wunjo",
            "latin": "w",
            "meaning": "joy, pleasure",
            "image": "wunjo.png",
        },
        {
            "name": "hagalaz",
            "latin": "h",
            "meaning": "hail (precipitation)",
            "image": "hagalaz.png",
        },
        {
            "name": "naudhiz",
            "latin": "n",
            "meaning": "need, distress",
            "image": "naudiz.png",
        },
        {"name": "isaz", "latin": "i", "meaning": "ice", "image": "isaz.png"},
        {"name": "jera", "latin": "j", "meaning": "year, harvest", "image": "jera.png"},
        {"name": "eihwaz", "latin": "ei", "meaning": "yew tree", "image": "ehwaz.png"},
        {
            "name": "perthro",
            "latin": "p",
            "meaning": "dice cup, fate",
            "image": "perthro.png",
        },
        {"name": "sowilo", "latin": "s", "meaning": "sun", "image": "sowilo.png"},
        {
            "name": "tiwaz",
            "latin": "t",
            "meaning": "Tyr, sky god",
            "image": "tiwaz.png",
        },
        {"name": "berkanan", "latin": "b", "meaning": "birch", "image": "berkanan.png"},
        {"name": "ehwaz", "latin": "e", "meaning": "horse", "image": "ehwaz.png"},
        {
            "name": "mannaz",
            "latin": "m",
            "meaning": "man, human",
            "image": "mannaz.png",
        },
        {"name": "laguz", "latin": "l", "meaning": "water, lake", "image": "laguz.png"},
        {
            "name": "ingwaz",
            "latin": "ng",
            "meaning": "fertility god",
            "image": "inguz.png",
        },
        {"name": "dagaz", "latin": "d", "meaning": "day, dawn", "image": "dagaz.png"},
        {
            "name": "othala",
            "latin": "o",
            "meaning": "inheritance, estate",
            "image": "othila.png",
        },
    ]

    # Create a grid layout
    cols = st.columns(4)

    # Display all runes
    for i, rune in enumerate(elder_futhark_runes):
        with cols[i % 4]:
            image_path = f"static/images/Elder Futhark/{rune['image']}"
            if os.path.exists(image_path):
                st.image(image_path, width=100)
            else:
                st.write(f"Image not found: {image_path}")

            st.write(f"**Name:** {rune['name']}")
            st.write(f"**Latin:** {rune['latin']}")
            st.write(f"**Meaning:** {rune['meaning']}")

elif selected_alphabet == "Younger Futhark":
    st.write("16 runes used during the Viking Age")
    # Get the alphabet data from RunicData
    alphabet_data = runic_data.get_alphabet(selected_alphabet)

    # Create a grid layout
    cols = st.columns(4)
    col_index = 0

    for latin_char, rune_data in alphabet_data.items():
        with cols[col_index]:
            # Get the image filename from the data
            image_filename = os.path.basename(rune_data["image_path"])

            # Construct the path to the image
            image_path = f"static/images/{selected_alphabet}/{image_filename}"

            # Check if the file exists
            if os.path.exists(image_path):
                st.image(image_path, width=100)
            else:
                # If the exact path doesn't exist, try a case-insensitive search
                alphabet_dir = f"static/images/{selected_alphabet}"
                if os.path.exists(alphabet_dir):
                    found = False
                    for file in os.listdir(alphabet_dir):
                        if file.lower() == image_filename.lower():
                            st.image(f"{alphabet_dir}/{file}", width=100)
                            found = True
                            break
                    if not found:
                        st.write(f"Image not found: {rune_data['name']}")
                else:
                    st.write(f"Directory not found: {alphabet_dir}")

            st.write(f"**Name:** {rune_data['name']}")
            st.write(f"**Latin:** {rune_data['latin_equivalent']}")
            st.write(f"**Meaning:** {rune_data['meaning']}")

        col_index = (col_index + 1) % 4

else:  # Anglo-Saxon Futhorc
    st.write("28 runes used in Early Medieval England")
    # Get the alphabet data from RunicData
    alphabet_data = runic_data.get_alphabet(selected_alphabet)

    # Create a grid layout
    cols = st.columns(4)
    col_index = 0

    for latin_char, rune_data in alphabet_data.items():
        with cols[col_index]:
            # Get the image filename from the data
            image_filename = os.path.basename(rune_data["image_path"])

            # Construct the path to the image
            image_path = f"static/images/{selected_alphabet}/{image_filename}"

            # Check if the file exists
            if os.path.exists(image_path):
                st.image(image_path, width=100)
            else:
                # If the exact path doesn't exist, try a case-insensitive search
                alphabet_dir = f"static/images/{selected_alphabet}"
                if os.path.exists(alphabet_dir):
                    found = False
                    for file in os.listdir(alphabet_dir):
                        if file.lower() == image_filename.lower():
                            st.image(f"{alphabet_dir}/{file}", width=100)
                            found = True
                            break
                    if not found:
                        st.write(f"Image not found: {rune_data['name']}")
                else:
                    st.write(f"Directory not found: {alphabet_dir}")

            st.write(f"**Name:** {rune_data['name']}")
            st.write(f"**Latin:** {rune_data['latin_equivalent']}")
            st.write(f"**Meaning:** {rune_data['meaning']}")

        col_index = (col_index + 1) % 4
