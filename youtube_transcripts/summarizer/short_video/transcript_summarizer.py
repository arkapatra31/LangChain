from typing import List
from langchain_core.documents import Document
from youtube_transcripts import llm, load_youtube_transcripts
from langchain.chains.summarize import load_summarize_chain

# Fetch the transcript of a YouTube video
summary = load_youtube_transcripts()

# Save the actual transcript in a text file
with open("transcript.txt", "w") as f:
    for doc in summary:
        f.write(doc.page_content)
    f.close()

# Summarize the transcript using the summarization chain
chain = load_summarize_chain(llm, chain_type="stuff", verbose=True)

response = chain.run(summary)

# Save the response in a text file
with open("summary.txt", "w") as f:
    f.write(response)
