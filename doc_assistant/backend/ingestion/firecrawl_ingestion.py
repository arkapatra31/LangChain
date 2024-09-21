import os
import asyncio
from dotenv import load_dotenv
from langchain_community.document_loaders import FireCrawlLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

INDEX_NAME = os.getenv('PINECONE_INDEX_FOR_FIRECRAWL')

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

urls_to_be_crawled = [
    "https://docs.commercetools.com/api/general-concepts",
    "https://docs.commercetools.com/api/predicates/query",
    "https://docs.commercetools.com/api/limits",
    "https://docs.commercetools.com/api/performance-tips",
    "https://docs.commercetools.com/api/graphql",
    "https://docs.commercetools.com/api/projects/product-tailoring",
    "https://docs.commercetools.com/api/projects/products-suggestions"
]


async def ingest_from_firecrawl():
    loader = FireCrawlLoader(
        url="https://docs.commercetools.com/api/projects/products-suggestions",
        params={
            'pageOptions': {"onlyMainContent": True},
            'limit': 15,
            'scrapeOptions': {'formats': ['markdown', 'html']},
            'wait_until_done': True
        },
    )

    docs = await loader.aload()

    print(f"{len(docs)} records to indexed into Pinecone from FireCrawl")

    await PineconeVectorStore.afrom_documents(docs, embeddings, index_name=INDEX_NAME)


if __name__ == '__main__':
    asyncio.run(ingest_from_firecrawl())
