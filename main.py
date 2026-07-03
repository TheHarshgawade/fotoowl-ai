import json
import os

from agents.storyboard_writer import create_storyboard
from agents.script_generator import generate_script
from agents.compiler_fixer import compile_script
from agents.renderer import render_video

OUTPUT_FOLDER = "output"

print("Loading previous image descriptions...")

with open(
    os.path.join(OUTPUT_FOLDER, "image_descriptions.json"),
    "r",
    encoding="utf-8"
) as f:
    results = json.load(f)

print(f"Loaded {len(results)} image descriptions.")

create_storyboard(
    results[0]["image"],
    results[0]["description"]
)

print("Storyboard created.")

generate_script()

print("Video script created.")

if compile_script():

    print("Compilation Successful!")

    render_video()

else:

    print("Compilation Failed!")

print("\nPipeline Completed Successfully!")
