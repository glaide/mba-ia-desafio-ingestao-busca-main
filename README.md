# Desafio MBA Engenharia de Software com IA - Full Cycle

### How to execute this project.

## pre-requisites 

- Python 3.8+
- Docker and Docker Compose
- API Key from OpenAI or Google

## how to install

### clone the repository
```bash
git clone git@github.com:glaide/mba-ia-desafio-ingestao-busca-main.git
cd mba-ia-desafio-ingestao-busca-main
```

### create and activate the virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### install the dependencies
```bash
pip install -r requirements.txt
```

### set the environment variables
```bash
cp .env.example .env
```

Edit the .env file with the correct values.

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Database Configuration
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag

# PDF Configuration
PDF_PATH=document.pdf

# Model Configuration
LLM_PROVIDER=openai
```