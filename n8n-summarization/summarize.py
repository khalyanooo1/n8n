import sys
import os
from pdfminer.high_level import extract_text
from docx import Document
import torch
from transformers import pipeline

# Check if GPU is available, else use CPU
device = 0 if torch.cuda.is_available() else -1

# Load Summarization Model
summarizer = pipeline("summarization", model="t5-small", device=device)

# Function to Extract Text from PDF or DOCX
def extract_text_from_file(file_path):
    if not os.path.exists(file_path):
        return "Error: File not found."

    try:
        if file_path.endswith('.pdf'):
            text = extract_text(file_path)
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            text = '\n'.join([para.text for para in doc.paragraphs])
        else:
            return "Error: Unsupported file format. Only PDF and DOCX are supported."
        
        text = text.strip()
        return text if text else "Error: The file is empty or unreadable."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to Summarize Text in Chunks (for Large Files)
def summarize_text(text, chunk_size=512):
    if len(text) < 100:
        return "Error: Text too short to summarize."

    # Split text into chunks while maintaining sentence structure
    sentences = text.split('. ')
    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(chunk) + len(sentence) < chunk_size:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "

    if chunk:
        chunks.append(chunk.strip())

    summaries = []
    for chunk in chunks:
        input_length = len(chunk.split())  # Count words
        max_length = min(150, max(50, input_length // 2))  # Dynamically set max_length

        try:
            summary = summarizer(chunk, max_length=max_length, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            summaries.append(f"Error summarizing chunk: {str(e)}")

    return "\n\n".join(summaries)

# Main Execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No file path provided.")
        sys.exit(1)

    file_path = sys.argv[1]
    text = extract_text_from_file(file_path)

    if text.startswith("Error"):
        print(text)
    else:
        summary = summarize_text(text)
        print("\n🔹 Fast Summary:\n", summary)



