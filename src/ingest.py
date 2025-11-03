import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/rag")  # nosec
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def ingest_pdf():
    """
    Load PDF document from the specified path.
    
    Returns:
        List of Document objects from LangChain
        
    Raises:
        FileNotFoundError: If PDF file is not found
        Exception: For other PDF loading errors
    """
    try:
        # Check if file exists
        if not os.path.exists(PDF_PATH):
            raise FileNotFoundError(f"PDF file not found at path: {PDF_PATH}")
        
        # Load PDF using PyPDFLoader
        print(f"Loading PDF from: {PDF_PATH}")
        loader = PyPDFLoader(PDF_PATH)
        documents = loader.load()
        
        print(f"Successfully loaded {len(documents)} pages from PDF")
        return documents
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"Error loading PDF: {e}")
        raise


if __name__ == "__main__":
    ingest_pdf()