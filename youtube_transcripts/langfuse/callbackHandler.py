import  os
from dotenv import load_dotenv
from langfuse.callback import CallbackHandler

load_dotenv()

langfuseHandler = CallbackHandler(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

__all__ = [langfuseHandler]