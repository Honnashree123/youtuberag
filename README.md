# AI Chat Applications Workshop

This repository contains two AI-powered chat applications built with Streamlit:

1. **YouTube RAG Assistant** (`VideoChatting_RAG.py`): Ask questions about YouTube videos using transcript-based retrieval-augmented generation (RAG).
2. **Vision QA** (`qavision/visionqapp.py`): Upload images and ask questions about them using multimodal AI.

## Features

### YouTube RAG Assistant
- Fetch transcripts from YouTube videos
- Process and chunk transcripts with timestamps
- Build vector embeddings for semantic search
- Answer questions with relevant video segments and timestamps
- Embed YouTube video segments in responses

### Vision QA
- Upload images (JPEG, PNG, WebP, GIF)
- Ask questions about uploaded images
- Maintain chat history for contextual conversations
- Powered by Groq's multimodal models

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd workshop
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage

### YouTube RAG Assistant
Run the YouTube RAG application:
```bash
streamlit run VideoChatting_RAG.py
```

1. Paste a YouTube video URL
2. Wait for the pipeline to process the transcript
3. Ask questions about the video content
4. View answers with relevant video timestamps

### Vision QA
Run the Vision QA application:
```bash
streamlit run qavision/visionqapp.py
```

1. Upload an image in the sidebar
2. Enter your Groq API key (or set it in environment)
3. Ask questions about the image
4. Continue the conversation with chat history

## Requirements

- Python 3.8+
- Groq API key (for both applications)
- Internet connection (for YouTube transcript fetching and API calls)

## Dependencies

- streamlit: Web app framework
- youtube-transcript-api: YouTube transcript fetching
- langchain: RAG pipeline components
- faiss-cpu: Vector database
- sentence-transformers: Text embeddings
- groq: AI model API client
- python-dotenv: Environment variable management

## Troubleshooting

- **Transcript not available**: Some YouTube videos don't have captions enabled.
- **API errors**: Ensure your Groq API key is valid and has sufficient credits.
- **Embedding model download**: First run may take longer due to downloading the sentence transformer model.
- **Port conflicts**: If Streamlit port 8501 is busy, it will use the next available port.
- **Transcript fetching fails in deployed apps**: YouTube blocks requests from cloud IPs (common on platforms like Streamlit Cloud). The app works best when run locally on your machine.

## License

This project is for educational purposes.