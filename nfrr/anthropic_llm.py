from dotenv import load_dotenv
from langchain_aws import ChatBedrockConverse
import boto3

load_dotenv()

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)


# Initialize Anthropic-Claude LLM
def anthropic_llm():
    return ChatBedrockConverse(
        client=bedrock_client,
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        temperature=0,
        max_tokens=None,
        verbose=True,
    )

__all__ = [anthropic_llm]