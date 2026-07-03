import json
import os

def generate_script():

    # Read storyboard.json
    with open("output/storyboard.json", "r", encoding="utf-8") as f:
        storyboard = json.load(f)

    script = """import {Sequence, Img} from 'remotion';

export const WeddingVideo = () => (
<>
"""

    for scene in storyboard["scenes"]:

        image = scene["image"]

        script += f"""
<Sequence durationInFrames={{150}}>
    <Img src="sample_images/{image}" />
</Sequence>

"""

    script += """
</>
);
"""

    os.makedirs("output", exist_ok=True)

    with open("output/video_script.jsx", "w", encoding="utf-8") as f:
        f.write(script)

    print("Video Script Created Successfully!")

    return script
    