from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# --- Pydantic Models for Request Body ---
class ChatRequest(BaseModel):
    message: str
    game_state: dict # Example: {"harmony_level": 50, "active_microbes": 5}

class GameAction(BaseModel):
    response: str
    action: str
    parameters: dict

@app.get("/")
def read_root():
    return {"message": "Chat Server is running."}

@app.post("/chat", response_model=GameAction)
async def handle_chat(chat_request: ChatRequest):
    """
    Placeholder endpoint for handling chat messages.
    In a real implementation, this would call the OpenAI API with the user's
    message and the game state, using function calling to generate an action.
    """
    logger.info(f"Received chat message: '{chat_request.message}'")
    logger.info(f"Current game state: {chat_request.game_state}")

    # Mock logic to simulate OpenAI's structured response (function calling)
    # This will randomly choose between a few predefined actions.
    possible_actions = [
        {
            "response": "The microbes seem to be responding positively! Their collective harmony has increased.",
            "action": "INCREASE_HARMONY",
            "parameters": {"amount": 10}
        },
        {
            "response": "A specific microbe appears to be agitated. Let's try to calm it down.",
            "action": "UPDATE_MICROBE_BEHAVIOR",
            "parameters": {"microbe_id": random.randint(1, 5), "new_behavior": "calm"}
        },
        {
            "response": "Just a simple chat message, no action taken.",
            "action": "NONE",
            "parameters": {}
        }
    ]

    mock_action = random.choice(possible_actions)

    logger.info(f"Returning mock action: {mock_action}")
    return mock_action

if __name__ == "__main__":
    import uvicorn
    # To run this server, use the command: uvicorn main:app --host 0.0.0.0 --port 8001 --reload
    uvicorn.run(app, host="0.0.0.0", port=8001)
