# Movie Recommendation and AI Agent System

## Overview
This project predicts similar movies using machine learning and cosine similarity.  
It also includes an AI agent with web search capability to generate real time movie overviews.  
The system is designed with production style logic and controlled external access.

## Features
- Movie similarity prediction using cosine similarity  
- Feature based comparison using genres, keywords, cast, and metadata  
- AI agent with live web search support
- data validation through pydantic 
- Real time movie overview generation  
- Rate limiting for external APIs and web requests  
- Modular and clean Python codebase  

## How Movie Recommendation Works
Movies are converted into numerical feature vectors.  
Cosine similarity is used to measure closeness between movies.  
Higher similarity scores indicate more similar movies.

Workflow:
- Data cleaning and preprocessing  
- Feature extraction and vectorization  
- Similarity matrix computation  
- Retrieval of top N similar movies  

## AI Agent Overview
The AI agent fetches live movie data from the web.  
It generates concise and updated movie summaries.  
This avoids reliance on static or outdated datasets with limited data.

Agent capabilities:
- Web search for movie details  
- Data filtering and summarization  
- Rate limited requests to external sources  

## Rate Limiting
Rate limiting is applied to control request frequency.  
It prevents API abuse and ensures stable system behavior.  
Limits apply to all web search and external API calls.

## Tech Stack/Tool
- Python  
- Scikit-learn  
- Cosine Similarity  
- DuckDuckGO Web Search API
- Groq API 
- Agent Framework(Langchain)  
- Requests and Rate Limiting Utilities  

## Use Cases
- Movie recommendation platforms  
- AI powered movie assistants  
- Learning project for machine learning and AI agents  
- Portfolio project demonstrating end to end AI systems  

## How to Run
1. Clone the repository  
2. Install required dependencies  
3. Run the main module  



## Summary
This project demonstrates applied machine learning and agent based AI using real world constraints and live data.