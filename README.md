# Medical-and-Book-Reading-Chatbots-using-CrewAI

Medical Chatbot-(branch-"Medbot")
The Medical Chatbot consists of multiple simple Agents with a Gemini-1.5-flash. These agents will sequentially come to a explanation about the given medical condition.

Rag Model(branch-"Book_Reading Bot")
The Book Reader Chatbot consists of a pair of Agentic Rag models that will read two pdf's of the same book (one less detailed, the other detailed), and answer the given question. This is to see how much the vastness of the vector database affects the agent's decision making.

The model uses the Gemini "Embedder-001" to chunk embed the provided pdf's into a chroma database, using these embeddings whenever more information is needed.
Since crewai internally uses "EmbedChain" as the embedding tool, hence even local embedding models such as Ollama can be used to locally embed the database.
