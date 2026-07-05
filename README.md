# 🎬 FotoOwl AI – AI-Powered Wedding Video Generation Pipeline

## Project Overview

This project was developed as part of the FotoOwl AI Internship Assignment.

The goal of the project is to automate the process of creating a wedding highlight video using AI. The pipeline understands the user's video requirements, analyzes wedding images, generates a storyboard, creates a video script, and renders a final video.

---

## Features

- Parses user video requirements using Gemini AI
- Analyzes wedding images with AI
- Generates image descriptions
- Creates a storyboard automatically
- Generates a JSX video script
- Compiles the generated script
- Renders a final MP4 video using MoviePy
- LangGraph-based workflow
- Modular agent architecture

---

## Tech Stack

- Python 3.13
- Google Gemini API (`google.genai`)
- LangGraph
- MoviePy
- Pillow
- python-dotenv

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
├── tests/
│   └── test_pipeline.py
│
├── graph.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔄 Workflow

```text
User Prompt
      │
      ▼
Intent Parser
      │
      ▼
Image Analyzer
      │
      ▼
Storyboard Writer
      │
      ▼
Script Generator
      │
      ▼
Compiler Fixer
      │
      ▼
Video Renderer
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

The project generates:

- `video_intent.json`
- `image_descriptions.json`
- `storyboard.json`
- `video_script.jsx`
- `final_video.mp4`

---

##  Future Improvements

- RAG-based knowledge retrieval
- Multi-model routing
- Automatic caption generation
- Background music selection
- Advanced cinematic transitions

---

## Author

**Harshad Gawade**

B.Sc. Cyber & Digital Science Graduate

GitHub: https://github.com/TheHarshgawade
