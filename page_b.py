import streamlit as st
import streamlit as st
import base64
def file_to_base64(file):
    # ファイルを読み込む
        with open(file.name, "rb") as f:
            bytes_data = f.read()

        # Base64エンコード
        encoded_string = base64.b64encode(bytes_data).decode("utf-8")

        return encoded_string

uploaded_file = st.file_uploader("Upload image")
if uploaded_file is not None:
    encoded_image = file_to_base64(uploaded_file)
    
    # Base64文字列を表示
    st.write(f"Base64エンコードされた画像:")
    # st.image(uploaded_file, width=300)
with st.container(height=400):
        st.markdown("This is inside the container")
        st.write("This is inside the container")

    
