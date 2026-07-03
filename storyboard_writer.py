import json
import os


def create_storyboard(image_name, description):
    """
    Creates a simple storyboard for one image.
    """

    storyboard = {
        "title": "Wedding Highlight Reel",
        "music": "Emotional Piano",
        "scenes": [
            {
                "scene": 1,
                "image": image_name,
                "duration": 5,
                "transition": "fade",
                "caption": "A Beautiful Beginning",
                "description": description
            }
        ]
    }

    os.makedirs("output", exist_ok=True)

    with open("output/storyboard.json", "w", encoding="utf-8") as f:
        json.dump(storyboard, f, indent=4)

    return storyboard
    