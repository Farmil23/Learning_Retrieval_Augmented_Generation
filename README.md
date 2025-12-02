# 🚀 My Journey to Mastering RAG (Retrieval-Augmented Generation)

Repository ini adalah dokumentasi perjalanan saya mempelajari **Retrieval-Augmented Generation (RAG)** dari nol. Tujuannya adalah membangun sistem AI yang tidak hanya pintar bicara, tapi juga *faktual* berdasarkan data yang saya berikan (PDF, Web, Teks).

## 🛠️ Tech Stack & Tools
Teknologi yang saya gunakan dalam eksperimen ini:
* **Language:** Python 3.10+
* **Orchestration:** [LangChain](https://python.langchain.com/) 🦜️🔗
* **LLM Provider:** Groq (Model: Llama3-8b) ⚡
* **Vector Database:** ChromaDB / FAISS 🗄️
* **Embeddings:** HuggingFace Embeddings 🤗
* **Frontend:** Streamlit 🎈

## 🗺️ Learning Roadmap & Progress
Checklist target pembelajaran saya:

### Phase 1: The Foundation
- [ ] Setup Environment (Python, `.env`, API Keys)
- [ ] Basic Call ke LLM (Groq + LangChain)
- [ ] Memahami konsep *Context Window* & *Prompts*

### Phase 2: Data Ingestion (ETL)
- [ ] **Loaders:** Membaca data dari PDF (`PyPDFLoader`) dan Teks
- [ ] **Chunking:** Memecah teks besar menjadi potongan kecil (`RecursiveCharacterTextSplitter`)
- [ ] Eksperimen dengan `chunk_size` dan `chunk_overlap`

### Phase 3: The Brain (Vector Store)
- [ ] Mengubah teks menjadi angka (Embeddings)
- [ ] Menyimpan vektor ke Database (ChromaDB/FAISS)
- [ ] Melakukan *Similarity Search* (Mencari teks yang mirip query)

### Phase 4: Building the RAG Chain
- [ ] Membuat Retriever (Pencari otomatis)
- [ ] Menggabungkan Retriever + Prompt + LLM (`RetrievalQA` Chain)
- [ ] **Milestone Project:** Chatbot "Tanya Dokumen PDF" Sederhana

### Phase 5: Advanced & UI
- [ ] Menambahkan Memory (Agar bot ingat chat sebelumnya)
- [ ] Membuat UI Web dengan Streamlit
- [ ] Evaluasi akurasi jawaban

## 📚 Key Concepts (Catatan Pribadi)

### 1. Apa itu RAG?
Teknik memberikan "buku referensi" kepada AI saat ujian. Alih-alih mengandalkan hafalan (training data), AI mencari jawaban di dokumen yang kita sediakan dulu, baru menjawab.

### 2. Chunking
Memotong dokumen panjang menjadi paragraf-paragraf kecil agar muat di memori AI dan pencarian lebih fokus.

### 3. Embeddings
Proses menerjemahkan teks menjadi deretan angka (vektor). Kalimat dengan makna mirip akan memiliki nilai angka yang "berdekatan".

## 📂 Struktur Folder
```bash
.
├── 📂 data/               # Tempat simpan file PDF/sumber data
├── 📂 notebooks/          # Eksperimen koding (Jupyter Notebook)
├── 📂 src/                # Script Python yang sudah jadi (app.py)
├── .env                   # API Keys (JANGAN DI-UPLOAD KE GITHUB)
├── requirements.txt       # Daftar library
└── README.md              # File ini|
