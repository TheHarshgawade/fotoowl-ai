# 🎬 FotoOwl AI – AI-Powered Wedding Video Generation Pipeline

##  Project Overview

This project was developed as part of the FotoOwl AI Engineering Internship Assignment.

The objective of this project is to automate the creation of a wedding highlight video using AI. The pipeline understands the user's video requirements, analyzes wedding images, generates a storyboard, creates a JSX video script, compiles it, and renders the final MP4 video.

---

## Features

- AI-based user intent parsing using Gemini
- AI-powered wedding image analysis
- Automatic image description generation
- Storyboard generation
- JSX video script generation
- Script compilation with retry mechanism
- Video rendering using MoviePy
- LangGraph-based workflow orchestration
- Modular agent-based architecture

---

##  Tech Stack

- Python 3.13
- Google Gemini API (`google.genai`)
- LangGraph
- MoviePy
- Pillow
- python-dotenv

---

##  Model Selection Rationale

The project uses different tools based on their strengths:

- **Gemini 2.5 Flash** was selected for user intent parsing and image analysis because it provides fast and accurate multimodal capabilities.
- **LangGraph** was used to orchestrate the workflow between multiple AI agents while maintaining a shared pipeline state.
- **MoviePy** was chosen for rendering the final slideshow video because it is lightweight and integrates well with Python.

---

##  RAG Design Decisions

A complete Retrieval-Augmented Generation (RAG) pipeline was planned but not fully implemented due to the assignment timeline.

The intended design includes:

- ChromaDB as the local vector database
- Separate collections for:
  - Video style references
  - Remotion API examples
- Storyboard generation retrieving relevant style documents
- Script generation retrieving Remotion examples before generating JSX
- Compiler retries retrieving relevant documentation based on compilation errors

---

## 📂 Project Structure

```text
fotoowl-ai/
│
├── agents/
│   ├── intent_parser.py
│   ├── image_analyzer.py
│   ├── storyboard_writer.py
│   ├── script_generator.py
│   ├── compiler_fixer.py
│   └── renderer.py
│
├── sample_images/
├── output/
│   ├── image_descriptions.json
│   ├── storyboard.json
│   ├── video_intent.json
│   ├── video_script.jsx
│   └── final_video.mp4
│
├── tests/
│   └── test_pipeline.py
│
├── graph.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Workflow

```text
                User Prompt
                     │
                     ▼
            Intent Parser Agent
                     │
                     ▼
           Image Analyzer Agent
                     │
                     ▼
         Storyboard Writer Agent
                     │
                     ▼
          Script Generator Agent
                     │
                     ▼
          Compiler & Fixer Agent
                     │
                     ▼
            Video Renderer Agent
                     │
                     ▼
               Final MP4 Video
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/TheHarshgawade/fotoowl-ai.git
```

Move into the project folder:

```bash
cd fotoowl-ai
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the project:

```bash
python main.py
```

---

## 📁 Output Files

The pipeline generates:

- `video_intent.json`
- `image_descriptions.json`
- `storyboard.json`
- `video_script.jsx`
- `final_video.mp4`

---

## Assignment Deliverables

This repository includes:

- LangGraph workflow implementation
- Shared pipeline state
- AI-powered intent parsing
- AI-powered image analysis
- Storyboard generation
- JSX video script generation
- Compiler retry mechanism
- Video rendering pipeline
- Sample output files
- Mock test suite
- `.env.example`
- `requirements.txt`

---

##  Known Limitations

- Uses a simplified storyboard generation approach.
- Video rendering is implemented as a slideshow and does not include advanced cinematic effects.
- The RAG architecture is documented but not fully implemented.
- Multi-model routing is planned as a future enhancement.
- Compiler retry logic is intentionally simple for this assignment.

---

##  Future Improvements

- Full RAG implementation using ChromaDB
- Multi-model routing
- AI-generated captions
- Background music recommendation
- Advanced cinematic transitions
- Automatic scene selection
- Better video effects and animations

---

##  Author

**Harshad Gawade**

B.Sc. Cyber & Digital Science Graduate

GitHub: https://github.com/TheHarshgawade

---

##  License

This project was developed for the **FotoOwl AI Engineering Internship Assignment** and is intended for educational and evaluation purposes.
