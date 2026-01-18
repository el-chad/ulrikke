from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.models import ChatCompletionRequest
from clients import get_open_router_client
from services import IntentRouter

app = FastAPI()

# CRITICAL: Allow TypingMind to talk to your local machine
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change this to your UI's domain
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)


@app.post("/v1/completions")
async def root(request: ChatCompletionRequest):
    messages = request.messages
    open_router_client = get_open_router_client()

    print(f"I just received this from TypingMind: {request}")
    last_prompt = messages[len(messages) - 1].content
    intent_router = IntentRouter(open_router_client, last_prompt)
    prompt_intent = await intent_router.determine_prompt_intent()
    model_output = await intent_router.route_by_intent(prompt_intent.category)
    print(f"prompt_type {prompt_intent}")
    return model_output
