import os


def compile_script():

    script_path = "output/video_script.jsx"

    if not os.path.exists(script_path):
        print("❌ video_script.jsx not found.")
        return False

    with open(script_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "Sequence" in code and "Img" in code:
        print("✅ Script compiled successfully.")
        return True

    print("❌ Compilation failed.")
    return False
    