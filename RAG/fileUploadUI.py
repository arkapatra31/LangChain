import streamlit as st
import PyPDF2


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


# Title of the Streamlit app
st.title("PDF Text Extractor and Question Input")

# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(uploaded_file)

    # Display extracted text
    st.subheader("Extracted Text")
    st.text_area("PDF Content", text, height=300)

    # Input widget for user question
    user_question = st.text_input("Enter your question about the PDF content")

    # Display user question
    if user_question:
        st.subheader("Your Question")
        st.write(user_question)
