from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, ScoredPoint
import uuid

# Qdrant Cloud Connection
QDRANT_URL = "https://28a8eda3-d623-43a6-8952-abcfeead6841.us-east4-0.gcp.cloud.qdrant.io"
QDRANT_API_KEY = "YOUR_QDRANT_API_KEY_HERE"  # Replace with your actual API key
COLLECTION_NAME = "hackernews"

# Connect to Qdrant
client = QdrantClient(QDRANT_URL, api_key=QDRANT_API_KEY)

# Step 1: Check and Create Collection
def create_collection():
    try:
        if client.collection_exists(collection_name=COLLECTION_NAME):
            print(f" Collection '{COLLECTION_NAME}' already exists.")
        else:
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
            )
            print(f" Collection '{COLLECTION_NAME}' created successfully!")
    except Exception as e:
        print(f" Error creating collection: {e}")

# Step 2: Upload Data to Qdrant
def upload_sample_data():
    data = {
        "id": str(uuid.uuid4()),  # Unique ID
        "title": "Example news title",
        "url": "https://example.com/news",
        "vector": ([0.123, -0.456, 0.789] * 342)[:1024]  # Ensuring exactly 1024 values
    }

    print(f"🛠 Vector length before upload: {len(data['vector'])}")  # Debugging

    try:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=data["id"],
                    vector=data["vector"],
                    payload={"title": data["title"], "url": data["url"]}
                )
            ],
        )
        print(f" Data uploaded successfully: {data['title']}")
    except Exception as e:
        print(f" Error uploading data: {e}")

# Step 3: Retrieve Data from Qdrant
def fetch_uploaded_data():
    try:
        result = client.scroll(collection_name=COLLECTION_NAME, limit=5)
        print("\n Uploaded Data:")

        for point in result[0]:  # result[0] contains points, result[1] is the offset
            print(f" ID: {point.id}")
            print(f" Title: {point.payload['title']}")
            print(f" URL: {point.payload['url']}")
            print("-" * 30)
    except Exception as e:
        print(f" Error retrieving data: {e}")

# Run Functions
if __name__ == "__main__":
    create_collection()  
    upload_sample_data()  
    fetch_uploaded_data()  # Verify uploaded data
