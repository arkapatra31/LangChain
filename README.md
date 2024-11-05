<center>
<h1><font color="#bde356"><b>LangChain</b></font><br></h1>
<img src="/assets/langchain-repo.webp" width="600" title="LangSmith Tracing">
<br><br>
</center>
<body>
<header>Repo for maintaining code implementation related to LangChain</header>
<br>
Note:- 
<li>
      Install the dependencies from requirements.txt using the below command:- <br>
      <b><i>pip install -r requirements.txt</i></b><br>
      To know more about requirements.txt visit 
      <a href="https://medium.com/@sim30217/pip-freeze-requirements-txt-993eb433ab0b">
        <font size = "1" color="b3e1f5">pip freeze > requirements.txt</font>
      </a>
</li>
<li>
      To create venv execute <b><u>python -m venv .venv</u></b>
</li>

<div align="center">
    <h4>Table of Contents</h4>
    <table>
        <tr>
            <th><font size="4" color="b3e1f5">Release Version</font></th>
            <th><font size="4" color="b3e1f5">Feature Implementation</font></th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.0">1.0.0</a></th>
            <th>
                <li>Ollama Integration</li>
                <li>Groq Integration</li>
                <li>GPT4All Integration</li>
                <li>Prompt Engineering</li>
                <li>LinkedIn Scraping</li>
                <li>RAG Model</li>
                <li>Pinecone as Vector DB</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.3">1.0.3</a></th>
            <th>
                <li>ReAct Agents</li>
                <li>Tools</li>
                <li>Pydantic Output Parser</li>
                <li>Agent Executors</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.4">1.0.4</a></th>
            <th>
                <li>Flask Application</li>
                <li>Re-Using ReAct Agent</li>
                <li>API response from Agent Response</li>
                <li>Agent Executors</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.5">1.0.5</a></th>
            <th>
                <li>LangSmith Tracing</li>                
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.6">1.0.6</a></th>
            <th>
                <li>Build ReAct Agent Executor from Scratch</li>
                <li>Tools defining for Agent</li>
                <li>ReAct Prompting</li>
                <li>LLM Reasoning Engine</li>
                <li>Output Parsing</li>
                <li>Tool Execution</li>
                <li>Handling Agent Action</li>
                <li>Setting up Agent Finish</li>
                <li>LLM Callback</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.7">1.0.7</a></th>
            <th>
                <li>Uploading and Reading PDF Data</li>
                <li>Chunking of PDF Data to list of Documents / Text</li>
                <li>Implementation of both predefined and custom chat prompts</li>
                <li>Pinecone Vector Store integration</li>
                <li>FAISS Local Vector Store Integration</li>
                <li>FAISS Vector saving local copy</li>
                <li>Retrieval from saved local FAISS</li>
                <li>Retrieval Chain implementation</li>
                <li>Implementation of Runnable Passthrough</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.8">1.0.8</a></th>
            <th>
                <li>Beautiful Soup Integration to manually scrape doc URLs</li>
                <li>Using OpenAIEmbeddings for text-embedding-3-small model</li>
                <li>Using RecursiveUrlLoader lib from Langchain to read docs from URL</li>
                <li>Splitting and chunking data</li>
                <li>Initialising the vector store using split documents and embeddings</li>
                <li>Chat Retrieval QA Chain Creation</li>
                <li>Streamlit Chat Components in UI/li>
                <li>Chat History / Context Addition to ChatLLM</li>
                <li>Using Rephrase Prompt with History Aware Retriever to hold Chat History</li>
                <li>Using FireCrawl to scrape and crawl websites and index them to Pinecone index</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.0.9">1.0.9</a></th>
            <th>
                <li>Understanding of Langchain Experimental Tools PKG</li>
                <li>Using the PythonREPL tool from Langchain</li>
                <li>Using the tool to write Python code</li>
                <li>Saving the reponse generated from the code</li>
                <li>Creating a CSV Agent to answer questions related to CSV file</li>
                <li>Creating a router agent to switch out to different agents based on the input prompt</li>
                <li>Create a Tool Calling Agent</li>
                <li>Bind Tools directly to a LLM</li>
                <li>Create Tool Calling Agent on 2 LLM Providers - OpenAI and Groq</li>
            </th>
        </tr>
        <tr>
            <th><a href="https://github.com/arkapatra31/langchain/releases/tag/v1.1.0">1.1.0</a></th>
            <th>
                <li>Dynamic record config generation using LLM</li>
                <li>Ability to change column data type, remove and associate reference value</li>
                <li>Sanitize and convert raw order data to DataFrame</li>
                <li>Read raw order data from a string and load it into a pandas DataFrame.</li>
                <li>Strip leading/trailing whitespace from column names.</li>
                <li>Ensure data consistency and handle missing/malformed data.</li>
                <li>Convert column data types to the appropriate format.</li>
                <li>Generate and save config files in json</li>
                <li>Read config files and apply them to raw order data</li>
                <li>Generate and save generated dataframe into CSV file</li>
            </th>
        </tr>
    </table>
<br>
<font color="#bde356"><b>LangSmith Tracing</b></font><br>
<img src="/assets/LangSmith_Tracing.png" width="500" title="LangSmith Tracing">
<br><br>
<font color="#bde356"><b>Agent Workflow</b></font><br>
<img src="/assets/ReActAgentExecutionWorkflow.drawio.png" style='border:3px solid #f2d096' width="500px" title="Agent Workflow"/>
<br><br>
<br><br>
</div>
</body>
