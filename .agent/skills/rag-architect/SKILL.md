---
name: rag-architect
description: Design of the RAG system for Property Lens. Handles vector DB management, DLD document chunking, and hybrid search implementation.
---
# RAG Architect Skill

## Retrieval Strategy
1. **Hybrid Search**: Keyword search (BM25) for building names + Vector search for semantic queries.
2. **Metadata Filtering**: Hard filter by District and Transaction Date BEFORE performing vector search.
3. **Re-ranking**: Utilize Cross-encoders to rank the top 5 most relevant transactions.

## Data Processing
- **Chunking**: 512-token chunks with 10% overlap for legal/DLD texts.
- **Embedding Model**: Utilize `text-embedding-3-small` or higher density models for financial data.

## Output Validation
- **Source Attribution**: Every AI-generated claim must include a reference to the source data point.