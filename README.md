# FotoOwl AI

## About the Project

This project was developed as part of the FotoOwl AI Internship Assignment.

The goal of this project is to use AI to understand a user's video editing prompt, analyze wedding images, and generate a basic storyboard and video editing script automatically.

I used the Google Gemini API for understanding the prompt and analyzing the images. The project follows a simple pipeline where each step generates an output file that is used in the next step.

## Features

- Converts a user prompt into video editing instructions
- Analyzes wedding images using Gemini AI
- Generates image descriptions
- Creates a simple storyboard
- Generates a JSX video editing script
- Simulates the final video rendering process

## Technologies Used

- Python
- Google Gemini API
- Pillow
- python-dotenv
- JSON

## Project Structure


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
├── main.py
├── requirements.txt
└── README.md


## How to Run

1. Clone this repository.


git clone https://github.com/TheHarshgawade/fotoowl-ai.git

2. Move into the project folder.

cd fotoowl-ai

3. Install the required packages.


pip install -r requirements.txt


4. Create a `.env` file and add your Gemini API key.


GEMINI_API_KEY=YOUR_API_KEY


5. Run the project.


python main.py




## Output

After running the project, the following files are generated in the `output` folder:

- `video_intent.json`
- `image_descriptions.json`
- `storyboard.json`
- `video_script.jsx`
- `render_output.json`


## Challenges I Faced

While developing this project, I faced a few challenges such as API key configuration, migrating from the old Gemini SDK to the new `google-genai` package, and handling API quota limits. I resolved these issues by updating the code, testing each module separately, and improving the project structure.

## Future Improvements

If I continue working on this project, I would like to:

- Generate a real video instead of a simulated output
- Add background music automatically
- Generate captions using AI
- Build a simple web interface for users

## Author

**Harshad Gawade**

GitHub: https://github.com/TheHarshgawade

This project was created for learning purposes as part of the FotoOwl AI Internship Assignment.
