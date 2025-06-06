# Horizon TV Example Code Skeleton

# --- Backend (Python FastAPI) ---
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use JSON file to store layout configuration
import json

CONFIG_PATH = "ui_config.json"

def load_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Default layout
        default_config = {
            "theme": "dark",
            "rows": [
                {"title": "Trending Now", "apps": ["YouTube", "Netflix", "Twitch"]},
                {"title": "Continue Watching", "apps": ["Hulu", "Disney+"]}
            ]
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(default_config, f, indent=2)
        return default_config

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

ui_layout_config = load_config()


class LayoutRequest(BaseModel):
    theme: str
    rows: List[dict]

@app.get("/config")
def get_ui_config():
    return ui_layout_config

@app.post("/config")
def update_ui_config(req: LayoutRequest):
    global ui_layout_config
    ui_layout_config = req.dict()
    return {"message": "UI configuration updated."}

