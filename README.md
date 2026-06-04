# 🎓 RAG-Based AI Teaching Assistant

## 📌 Overview

RAG-Based AI Teaching Assistant is an intelligent educational assistant that helps students quickly find relevant learning content from course videos using Retrieval-Augmented Generation (RAG).

The system processes educational videos, converts them into searchable text chunks, generates vector embeddings, and retrieves the most relevant course segments based on a student's question. It then uses a Large Language Model (LLM) to generate contextual answers while also guiding students to the exact video and timestamp where the topic is taught.

This project demonstrates the practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Large Language Models (LLMs)
* Educational Content Retrieval
* AI-Powered Learning Assistants

---

## 🚀 Features

### 📹 Video-Based Learning Assistant

* Answers questions related to course content.
* Searches through lecture transcripts instead of entire videos.
* Identifies relevant learning materials instantly.

### 🔍 Semantic Search

* Uses vector embeddings instead of keyword matching.
* Retrieves contextually relevant content even when exact keywords are absent.

### 🧠 Retrieval-Augmented Generation (RAG)

* Retrieves the most relevant transcript chunks.
* Provides grounded responses based on course material.
* Reduces hallucinations by supplying factual context to the LLM.

### ⏱ Timestamp-Based Guidance

The assistant tells students:

* Which lecture contains the answer.
* Relevant video number.
* Timestamp where the topic is discussed.

### 🎯 Course-Focused Responses

The assistant only answers questions related to the uploaded course content and avoids responding to unrelated queries.

---

## 🏗️ System Architecture

```text
Course Videos
      │
      ▼
Video to Audio Conversion
      │
      ▼
Speech-to-Text Processing
      │
      ▼
Chunk Generation
      │
      ▼
Embedding Creation (BGE-M3)
      │
      ▼
Vector Storage (Joblib DataFrame)
      │
      ▼
User Query
      │
      ▼
Query Embedding
      │
      ▼
Cosine Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
LLM (GPT / Llama)
      │
      ▼
Final Educational Answer
```

---

## 📂 Project Structure

```text
RAG-based-AI-Teaching-Assistent/

├── Audios/
│   ├── Course lecture audio files
│
├── Videos/
│   ├── Original course videos
│
├── jsons/
│   ├── Transcript chunks in JSON format
│
├── embeddings.joblib
│   ├── Precomputed vector embeddings
│
├── videos_to_mp3(Process_videos).py
│   ├── Converts videos into audio files
│
├── mp3_to_json(create_chunks).py
│   ├── Converts audio transcripts into chunks
│
├── preprocess_json(read_chunks).py
│   ├── Creates embeddings for transcript chunks
│
├── process_incoming.py
│   ├── Handles user questions and retrieval
│
├── config.py
│   ├── API configuration
│
├── prompt.txt
│   ├── Generated LLM prompt
│
├── response.txt
│   ├── Generated AI response
│
└── README.md
```

---

## 🛠 Technologies Used

### Programming Language

* Python

### AI & Machine Learning

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Cosine Similarity

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Joblib
* Requests
* OpenAI SDK

### LLMs

* GPT Models (OpenAI)
* Llama 3.2 (via Ollama)

### Embedding Model

* BGE-M3

### Local AI Infrastructure

* Ollama

---

## ⚙️ How the System Works

### Step 1: Video Processing

Course videos are converted into audio format.

```bash
videos_to_mp3(Process_videos).py
```

---

### Step 2: Audio Transcription & Chunking

Audio files are converted into structured transcript chunks.

Each chunk contains:

* Video title
* Video number
* Start timestamp
* End timestamp
* Transcript text

Output format:

```json
{
  "title": "Introduction to CSS",
  "number": "14",
  "start": 120,
  "end": 180,
  "text": "CSS is used to style HTML elements..."
}
```

---

### Step 3: Embedding Generation

The BGE-M3 embedding model converts transcript chunks into high-dimensional vectors.

```python
create_embedding(text_list)
```

These embeddings capture semantic meaning and enable intelligent search.

---

### Step 4: Building Knowledge Base

All transcript chunks and embeddings are stored in:

```text
embeddings.joblib
```

This serves as the vector database for retrieval.

---

### Step 5: User Query Processing

Example:

```text
What are semantic tags in HTML?
```

The query is converted into an embedding vector using BGE-M3.

---

### Step 6: Similarity Search

Cosine Similarity is used to identify the most relevant transcript chunks.

```python
cosine_similarity()
```

The top matching chunks are selected.

---

### Step 7: Context Injection

Relevant transcript chunks are inserted into a prompt.

The LLM receives:

* User question
* Relevant course content
* Video information
* Timestamp information

---

### Step 8: AI Response Generation

The assistant generates:

* Answer to the question
* Related lecture number
* Relevant timestamp
* Learning guidance

Example:

```text
Semantic Tags are introduced in Video 11.

You can watch the section between 2:10 and 6:45 where the instructor explains semantic HTML elements such as header, main, section, article, and footer.
```

---

## 🔍 Retrieval Strategy

The project uses:

### Embedding-Based Retrieval

Instead of:

```text
Keyword Matching
```

It uses:

```text
Semantic Similarity Search
```

Benefits:

* Better understanding of user intent.
* Finds relevant content even with different wording.
* More accurate retrieval.

---

## 📊 Educational Use Cases

### Students

* Quickly find concepts from long lectures.
* Revise topics efficiently.
* Save learning time.

### Instructors

* Create searchable course assistants.
* Improve learner engagement.
* Provide instant doubt resolution.

### E-Learning Platforms

* AI-powered video search.
* Smart tutoring systems.
* Personalized learning support.

---

## 🎯 Example Queries

```text
What are semantic tags in HTML?

How do forms work in HTML?

Explain CSS selectors.

What is the box model in CSS?

How do IDs and classes differ?
```

---

## 🔮 Future Enhancements

* Streamlit Web Interface
* Chat-based UI
* FAISS Vector Database
* Multi-Course Support
* PDF Knowledge Integration
* Voice-Based Queries
* Real-Time Lecture Assistant
* Hybrid Retrieval (Keyword + Semantic Search)
* User Authentication
* Learning Progress Tracking

---

## 📚 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Vector Embeddings
* Semantic Search
* Educational AI Systems
* Prompt Engineering
* Information Retrieval
* Python Development
* AI Application Design

---

## 👩‍💻 Author

**Sakshi Srivastav**

Data Science & AI Enthusiast passionate about building intelligent educational and conversational AI systems.

---

## ⭐ Support

If you found this project useful, please consider giving it a star on GitHub and sharing it with others interested in AI-powered learning systems.
