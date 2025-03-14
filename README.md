n8n Workflow: Web Scraping, Vector Database, and Document Processing  

 Overview  
This n8n workflow automates web scraping, vector database storage, document processing, and user interaction. It extracts news headlines from Hacker News, converts them into embeddings, stores them in Qdrant, and allows users to search for relevant articles. Additionally, it processes uploaded documents (PDF/DOCX), extracts insights, and retrieves relevant content based on user queries.  

Since OpenAI's API was not used due to billing constraints, we implemented local embedding models and open-source APIs to handle vector storage and summarization.  

Features  
- Scrapes news headlines from Hacker News and extracts titles, URLs, and descriptions.  
- Converts extracted headlines into embeddings using local embedding models instead of OpenAI.  
- Stores embeddings in Qdrant (Vector Database) for efficient retrieval.  
- Implements a search function to retrieve the most relevant headlines.  
- Accepts PDF & DOCX uploads via Webhook.  
- Processes uploaded documents, extracts key insights, and summarizes content.  
- Allows users to query both the scraped news articles and processed document contents.  
- Retrieves the most relevant results using vector search.  
- Optimized workflow for efficiency and fast data retrieval.  

 Technologies Used  
- n8n for workflow automation.  
- HTTP Request Node for scraping Hacker News.  
- Qdrant as the vector database for storing embeddings.  
- Local embedding models for vectorization.  
- PDFMiner & python-docx for extracting text from PDF and DOCX files.  
- n8n Webhook for handling user uploads and queries.  
- Vector Search & API Calls for retrieving relevant results.  

Installation  
 1️ Clone the Repository  
git clone https://github.com/khalyanooo1/n8n.git
cd n8n-summarization
  
2️ Install Dependencies  

pip install -r requirements.txt

 3️  Start n8n  

n8n start


Workflow Steps  
Web Scraping (Hacker News)  
- Fetches latest news headlines and URLs.  
- Uses HTTP Request Node to pull data from Hacker News.  

Vector Database (Qdrant)  
- Converts scraped headlines into embeddings using local models.  
- Stores embeddings in Qdrant for quick retrieval.  
- Implements a search function for finding relevant articles.  

Document Processing 
- Accepts document uploads in PDF & DOCX formats via Webhook.  
- Extracts text using PDFMiner and python-docx.  
- Summarizes content using the T5-small model.  
- Stores processed document data for later retrieval.  

User Queries
- Users can ask questions about:  
  - Scraped news articles  
  - Processed document content  
- Uses vector search to retrieve highly relevant results.  

 Deployment Options  
 1️ Run Locally  

n8n start

2️ Deploy to Cloud Server (Optional)  
- Use Docker for self-hosting.  
- Deploy on n8n Cloud or a VPS for continuous operation.  

How to Use  
1. Start n8n and activate the workflow.  
2. Upload a document (PDF/DOCX) via the Webhook.  
3. Search for Hacker News articles by entering a query.  
4. Search document contents for relevant insights.  
5. Retrieve the most accurate and relevant results from vector search.  

Additional Notes  
- OpenAI was not used due to billing limitations and loading web tokens are so high .  
- Instead, local embedding models were utilized for vectorization.  
- Qdrant was used to efficiently store and search embeddings.  

Contributors  
Khalyan Alangulam Meenatchisundharam  
 [GitHub Profile](https://github.com/khalyanooo1)  

This workflow provides a real-world automation use case in n8n, demonstrating scraping, data storage, document processing, and intelligent search capabilities.
