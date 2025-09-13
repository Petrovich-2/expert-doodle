import streamlit as st
from pathlib import Path
from datetime import datetime
from PIL import Image

images_folder = Path("done/compress")
image_files = sorted(images_folder.glob("*.*"))


@st.cache_resource
def load_image(path):
    return Image.open(path)


if not image_files:
    st.error("No images found in the 'done' folder.")
else:
    idx = st.slider("Select image", 0, len(image_files) - 1, 0)
    selected_image = image_files[idx]

    image = load_image(str(selected_image))
    st.image(image, use_container_width=True, caption=selected_image.name)

    try:
        dt_str = selected_image.stem
        dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S")
        st.write("Image datetime:", dt)
    except Exception:
        st.write("Image datetime:", datetime.now())
