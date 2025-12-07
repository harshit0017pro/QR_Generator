import qrcode
import streamlit as st
from io import BytesIO
# Setting up the title 
st.title("QR Code Generator")
st.markdown("""
### How It Works:
1. Enter the URL or text you want to convert into a QR code in the input box below.
2. Wait for the app to generate the QR code automatically.
3. Once the QR code is generated:
   - You can view it directly on the page.
   - Use the "Download QR Code" button to save it as an image file.
4. Scan the QR code with your phone or device to access the link or text.
""")
website_link = st.text_input("Enter you link here:")
qr = qrcode.QRCode(version = 1, box_size =5 , border=5)
if website_link:
    qr.add_data(website_link)
    qr.make()
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    st.success("QR Generated")
    file_path = "generated_qr.png"
    generated = img.save(file_path)
    # Display the QR code
    st.image(file_path, caption="Your QR Code")
    
    # Add a download button for the saved file
    with open(file_path, "rb") as file:
        st.download_button(label="Download QR Code", data=file, file_name="qr_code.png", mime="image/png")