from typing import TypedDict

from langgraph.graph import StateGraph, END


class VideoState(TypedDict):
    intent: str
    images: list
    storyboard: str
    script: str
    compiled: bool
    rendered: bool


def parse_intent(state: VideoState):
    print("Step 1: Parsing Intent...")
    state["intent"] = "Intent Parsed"
    return state


def analyze_images(state: VideoState):
    print("Step 2: Analyzing Images...")
    state["images"] = ["16 wedding images analyzed"]
    return state


def create_storyboard(state: VideoState):
    print("Step 3: Creating Storyboard...")
    state["storyboard"] = "Storyboard Created"
    return state


def generate_script(state: VideoState):
    print("Step 4: Generating JSX Script...")
    state["script"] = "video_script.jsx"
    return state


def compile_script(state: VideoState):
    print("Step 5: Compiling Script...")
    state["compiled"] = True
    return state


def render_video(state: VideoState):
    print("Step 6: Rendering Video...")
    state["rendered"] = True
    return state


graph = StateGraph(VideoState)

graph.add_node("parse_intent", parse_intent)
graph.add_node("analyze_images", analyze_images)
graph.add_node("create_storyboard", create_storyboard)
graph.add_node("generate_script", generate_script)
graph.add_node("compile_script", compile_script)
graph.add_node("render_video", render_video)

graph.set_entry_point("parse_intent")

graph.add_edge("parse_intent", "analyze_images")
graph.add_edge("analyze_images", "create_storyboard")
graph.add_edge("create_storyboard", "generate_script")
graph.add_edge("generate_script", "compile_script")
graph.add_edge("compile_script", "render_video")
graph.add_edge("render_video", END)

app = graph.compile()


if __name__ == "__main__":
    result = app.invoke(
        {
            "intent": "",
            "images": [],
            "storyboard": "",
            "script": "",
            "compiled": False,
            "rendered": False,
        }
    )

    print("\nWorkflow Completed!")
    print(result)
    