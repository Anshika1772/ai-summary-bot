from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/summarize")
def summarize(data: InputText):
    text = data.text

    # Simple summarization logic
    words = text.split()
    summary = " ".join(words[:20])  # first 20 words

    return {
        "summary": summary
    }