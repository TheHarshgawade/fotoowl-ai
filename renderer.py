from moviepy import ImageClip, concatenate_videoclips
import os

def render_video():
    IMAGE_FOLDER = "sample_images"
    OUTPUT_FILE = "output/final_video.mp4"

    # Get all images
    images = sorted([
        f for f in os.listdir(IMAGE_FOLDER)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ])

    if not images:
        print("No images found!")
        return

    clips = []

    for image in images:
        image_path = os.path.join(IMAGE_FOLDER, image)

        clip = (
            ImageClip(image_path)
            .with_duration(3)
            .resized(height=720)
        )

        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")

    os.makedirs("output", exist_ok=True)

    final_video.write_videofile(
        OUTPUT_FILE,
        fps=24,
        codec="libx264"
    )

    print(f"\n✅ Video saved successfully: {OUTPUT_FILE}")
    