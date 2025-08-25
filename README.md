# Langchain-Practice

There are 6 components in langchain
1. Models
2. Prompts
3. Chains
4. Memory
5. Indexes
6. Agents


## Models
In Lanchain, Models are core interfaces through which you interact with AI Models.

It is designed to interact with various language models and embedding models.

Embedding models helps in semantic search.


## Prompts

- Prompts are input instructions or queries given to guide a model towards the output.

a - Text base prompts
b - Multimodal prompts

## Tool

- A tool is just a python function(or API) that is packaged in a way the LLM can understandd and call when needed.

- LLMs are great at 
1. Reasoning
2. Language generation

- But they can't do things like
1. Access live data 
2. Do realiable math
3. Call APIs
4. Run code
5. Interact with database

# There are two types of tools
1. Built-in tools
2. Custom Tools


## An AI agent is an LLM powered system that can autonomously think,decide and take action using external tools or APIs to achieve a goal.

## Toolkit

- A toolkit is just a collection (bundle) of related tools that serves a common purpose-  packaged together for convenience and resuability.

