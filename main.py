import streamlit as st
from PIL import Image
import io
import os 

st.set_page_config(page_title="Image to PDF", page_icon="🖼️")

st.markdown(
    """
    <style>
    /* Background and padding */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
        padding: 2rem;
    }

    /* Title style */
    h1 {
        color: #003366;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Convert button style */
    div.stButton > button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s ease;
        margin-top: 10px;
        width: 100%;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        transform: scale(1.05);
    }

    /* Download button style */
    div.stDownloadButton > button {
        background: linear-gradient(90deg, #28a745, #218838);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s ease;
        margin-top: 10px;
        width: 100%;
    }

    div.stDownloadButton > button:hover {
        background: linear-gradient(90deg, #218838, #28a745);
        transform: scale(1.05);
    }

    /* Footer style */
    .footer {
        text-align: center;
        color: #666;
        font-size: 15px;
        margin-top: 3rem;
        border-top: 1px solid #ccc;
        padding-top: 10px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style='text-align: center; color: #003366; font-family: "Segoe UI", sans-serif;'>
        🖼️ Image to PDF Converter
    </h1>
    """,
    unsafe_allow_html=True,
)


uploaded_images = st.file_uploader(
    label="Choose your images", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

pdf_bytes = None
pdf_file_name = f"converted_images.pdf" 

if uploaded_images:
    images = []
    st.subheader("🖼️ Preview of Uploaded Images:")

    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        images.append(image)
        st.image(image, caption=uploaded_image.name, use_container_width=True)

    # Set PDF file name from first image
    first_image_name = uploaded_images[0].name
    base_name = os.path.splitext(first_image_name)[0]
    pdf_file_name = f"{base_name}.pdf"


    col1, col2 = st.columns(2)

    with col1:
        convert_clicked = st.button("🔄 Convert to PDF")

    if convert_clicked and images:
        pdf_bytes = io.BytesIO()
        images[0].save(pdf_bytes, format="PDF", save_all=True, append_images=images[1:])
        pdf_bytes.seek(0)
        file_size_kb = round(len(pdf_bytes.getvalue()) / 1024, 2)
        st.success(f"✅ PDF created successfully! File size: {file_size_kb} KB")

    with col2:
        if pdf_bytes:
            st.download_button(
                label = "📥 Download PDF",
                data = pdf_bytes,
                # file_name="converted_images.pdf",
                file_name = pdf_file_name,
                mime = "application/pdf"
            )

st.markdown("""
    <div class='footer'>
        Made with ❤️ by <b>Anum Kamal</b>
    </div>
""", unsafe_allow_html=True)
