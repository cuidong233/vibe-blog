<div align="center">

<img width="256" src="./logo/banana-vibe-blog.png">

*Turn complex tech into stories everyone can understand.*

**[中文](README.md) | English**

<p>

[![Version](https://img.shields.io/badge/version-v0.1.0-4CAF50.svg)](https://github.com/Anionex/banana-vibe-blog)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)

</p>

<b>A multi-Agent AI-powered long-form blog generator with deep research, smart illustrations, and Mermaid diagrams,<br></b>
<b>transforming technical knowledge into easy-to-understand articles for everyone</b>

<b>🎯 Lower the barrier to technical writing, making knowledge sharing simpler</b>

<br>

*If this project is useful to you, please star🌟 & fork🍴*

<br>

</div>


## ✨ Project Origin

Have you ever been stuck in this situation: you want to write a technical blog, but don't know how to make it understandable for non-technical readers; you have lots of technical knowledge in mind, but struggle to explain it with vivid metaphors?

Traditional technical blog writing has the following pain points:

- 1️⃣ **Time-consuming**: A high-quality technical article takes hours or even days
- 2️⃣ **Illustration difficulties**: Hard to find suitable images, Mermaid syntax is complex
- 3️⃣ **Lack of depth**: No time for deep research, content tends to be superficial
- 4️⃣ **Single audience**: Difficult to adjust content depth for readers of different technical levels
- 5️⃣ **Tedious distribution**: Need to manually adapt to different platform format requirements

Banana Vibe Blog was born to solve these problems. Based on multi-Agent collaborative architecture, it automatically completes the entire process of research, planning, writing, and illustration, letting you focus on the knowledge itself.

## 👨‍💻 Use Cases

1. **Tech Bloggers**: Quickly generate high-quality technical articles, saving writing time
2. **Developer Advocates**: Transform complex technology into easy-to-understand content, expanding influence
3. **Educators**: Generate teaching materials, using life-like metaphors to help students understand
4. **Product Managers**: Quickly understand technical concepts, better communicate with development teams
5. **Tech Beginners**: Easily get started with new technologies through AI-generated articles


## 🖼️ Demo & Results

### Homepage - Clean and Elegant Input Interface

![Homepage](./backend/outputs/images/首页图.png)

*Input topic, select article type and length, generate with one click*

**Article Types**:
- 📚 **Tutorial**: Step-by-step teaching, master technology from zero to one
- 🔧 **Problem Solving**: Targeted solutions for specific problems
- 📊 **Comparative Analysis**: Multi-solution comparison to help with tech selection

**Article Length**:

| Length | Chapters | Reading Time | Depth | Use Case |
|:---:|:---:|:---:|:---:|:---|
| 📄 **Short** | 3-5 chapters | ~30 min | shallow | Quick introduction, fast start |
| 📑 **Medium** | 5-8 chapters | ~60 min | medium | Concrete examples + step-by-step, deep learning |
| 📚 **Long** | 8-12 chapters | ~90+ min | deep | Principle analysis + data support + edge cases, comprehensive mastery |

> 💡 **Questioning Depth**: The system automatically adjusts content review standards based on article length. Long articles trigger stricter depth checks to ensure each concept has data support and principle analysis.

### AI Workflow Status - Real-time Generation Progress Tracking

<div align="center">
<table>
<tr>
<td><img src="./backend/outputs/images/中间运行过程图-1.png" width="400"/></td>
<td><img src="./backend/outputs/images/中间运行过程图-2.png" width="400"/></td>
</tr>
<tr>
<td align="center"><b>Step 1: Material Collection</b><br>Intelligent web search for resources</td>
<td align="center"><b>Step 2-3: Outline Planning & Content Writing</b><br>Generate structured outline, write by chapter</td>
</tr>
<tr>
<td><img src="./backend/outputs/images/中间运行过程图-4.png" width="400"/></td>
<td><img src="./backend/outputs/images/中间运行过程图-5.png" width="400"/></td>
</tr>
<tr>
<td align="center"><b>Step 4: Depth Questioning</b><br>Check content depth, supplement details</td>
<td align="center"><b>Step 5: Code Generation</b><br>Generate runnable example code</td>
</tr>
<tr>
<td><img src="./backend/outputs/images/中间运行过程图-6.png" width="400"/></td>
<td><img src="./backend/outputs/images/中间运行过程图-7.png" width="400"/></td>
</tr>
<tr>
<td align="center"><b>Step 6: Image Generation</b><br>Mermaid diagrams + AI images</td>
<td align="center"><b>Step 7: Quality Review</b><br>Score and provide improvement suggestions</td>
</tr>
<tr>
<td><img src="./backend/outputs/images/中间运行过程图-8.png" width="400"/></td>
<td><img src="./backend/outputs/images/中间运行过程图-9.png" width="400"/></td>
</tr>
<tr>
<td align="center"><b>Step 8: Document Assembly</b><br>Assemble complete document, extract summary</td>
<td align="center"><b>🎉 Generation Complete</b><br>Auto-save Markdown file</td>
</tr>
</table>
</div>

### Blog Results - Professional Technical Articles

![Blog Results](./backend/outputs/images/技术博客结果图.png)

*Complete blog content preview, supports image export and Markdown download*

---

## 🎨 Blog Generation Examples

| Blog Title | Local Preview | CSDN |
|:---|:---:|:---:|
| **Triton Deployment Practical Guide: From Design Principles to Production** | [Markdown](./backend/outputs/Triton%20部署实战指南_从设计思想到生产落地_20251231_034839.md) | [View](https://blog.csdn.net/ll1042668699/article/details/156437086) |
| **vLLM Inference Engine Deep Dive: Core Acceleration Mechanisms and Component Principles** | [Markdown](./backend/outputs/vLLM推理引擎深度拆解_核心加速机制与组件原理实战指南_20251231_031953.md) | [View](https://blog.csdn.net/ll1042668699/article/details/156436798) |
| **Message Queue Getting Started: Building an Async Communication System from Scratch** | [Markdown](./backend/outputs/消息队列入门实战_从零搭建异步通信系统_20251230_045909.md) | [View](https://blog.csdn.net/ll1042668699/article/details/156406666) |
| **Distributed Lock Practical Guide: Master High-Concurrency Resource Synchronization in 30 Minutes** | [Markdown](./backend/outputs/分布式锁实战指南_30分钟掌握高并发下的资源同步控制_20251230_052151.md) | [View](https://blog.csdn.net/ll1042668699/article/details/156406394) |
| **RAG Evolution Illustrated: Traditional RAG vs Graph RAG Architecture Comparison** | [Markdown](./backend/outputs/图解RAG进化_传统RAG%20vs%20Graph%20RAG架构实战对比_20251231_042358.md) | [View](https://blog.csdn.net/ll1042668699/article/details/156437897) |
| **Redis Quick Start Tutorial: Building a High-Performance Cache System from Scratch** | [Markdown](./backend/outputs/Redis%20快速上手实战教程_从零搭建高性能缓存系统_20251230_043948.md) | [View](https://blog.csdn.net/ll1042668699/article/details/156438172) |


## 🎯 Feature Introduction

### 1. Multi-Agent Collaborative Architecture
Multi-Agent workflow built on LangGraph, each agent with specific responsibilities, collaborating efficiently.
- **Researcher Agent**: Deep research, searching the web for latest materials
- **Planner Agent**: Smart planning, generating well-structured article outlines
- **Writer Agent**: Content creation, writing easy-to-understand section content
- **Coder Agent**: Code generation, providing runnable example code
- **Artist Agent**: Smart illustration, generating Mermaid diagrams and AI images

### 2. Deep Research Capability
- **Zhipu Search Integration**: Automatically search the web for latest technical materials
- **Knowledge Extraction**: Extract key information from search results
- **Citation Annotation**: Automatically annotate information sources, ensuring credibility

### 3. Smart Illustration System
- **Mermaid Diagrams**: Automatically generate flowcharts, architecture diagrams, sequence diagrams
- **AI Cover Images**: Generate cartoon-style covers based on nano-banana-pro
- **Context-Aware**: Generate unique illustrations based on section content

### 4. Multi-Format Export
- **Markdown**: Standard Markdown format, ready for direct publishing
- **Image Export**: One-click export article as long image
- **Live Preview**: Real-time Markdown and Mermaid rendering in frontend


## 🤖 Multi-Agent Collaborative Architecture

<div align="center">

<img width="800" src="./logo/multi-agent-architecture.png">

</div>

Banana Vibe Blog adopts a multi-Agent collaborative architecture where each Agent has clear responsibilities and works efficiently together:

- **Orchestrator Agent** (Director): Coordinates the entire workflow
- **Researcher Agent** (Researcher): Deep search and knowledge extraction
- **Planner Agent** (Planner): Generate structured outlines
- **Writer Agent** (Writer): Write section content
- **Coder Agent** (Coder): Generate example code
- **Artist Agent** (Illustrator): Generate Mermaid diagrams and AI images
- **Reviewer Agent** (Reviewer): Quality check and optimization
- **Assembler Agent** (Assembler): Final document assembly

All Agents share unified state management and Prompt template library, ensuring efficient collaboration and consistent output quality.


## 🗺️ Development Roadmap

| Status | Milestone |
| --- | --- |
| ✅ Completed | Multi-Agent architecture (Researcher/Planner/Writer/Coder/Artist) |
| ✅ Completed | Zhipu search service integration |
| ✅ Completed | Mermaid diagram auto-generation |
| ✅ Completed | AI cover image generation (nano-banana-pro) |
| ✅ Completed | SSE real-time progress push |
| ✅ Completed | Markdown live preview rendering |
| ✅ Completed | Export article as image |
| 🧭 Planned | AI Smart Reading Guide (Mind Map + Interactive Reading) |
| 🧭 Planned | PDF knowledge parsing and deep research |
| 🧭 Planned | Podcast format output (TTS synthesis) |
| 🧭 Planned | Tutorial video generation |
| 🧭 Planned | Multi-audience adaptation (students/children/professionals) |
| 🧭 Planned | Comic format output |
| 🧭 Planned | One-click publish to social media platforms |


## 📦 Usage

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Anionex/banana-blog
cd banana-blog
```

2. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp .env.example .env
```

Edit the `.env` file to configure necessary environment variables:
```env
# AI Provider format configuration (openai)
AI_PROVIDER_FORMAT=openai

# OpenAI format configuration
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1
TEXT_MODEL=gpt-4o

# Zhipu Search API (optional, for deep research)
ZHIPU_API_KEY=your-zhipu-api-key

# Nano Banana Pro API (optional, for AI cover images)
NANO_BANANA_API_KEY=your-nano-banana-api-key
```

4. **Start the service**
```bash
python app.py
```

5. **Access the application**
- Frontend: http://localhost:5001
- API: http://localhost:5001/api


## 🛠️ Technical Architecture

### Backend Tech Stack
- **Language**: Python 3.10+
- **Framework**: Flask 3.0
- **AI Framework**: LangGraph (Multi-Agent orchestration)
- **Template Engine**: Jinja2 (Prompt management)
- **Real-time Communication**: Server-Sent Events (SSE)

### AI Models & Services
| Function | Provider | Model/API | Description |
|----------|----------|-----------|-------------|
| **Text Generation** | Alibaba Bailian | Qwen (Qianwen) | Used for Agent text generation and reasoning |
| **Web Search** | Zhipu | Web Search API | Used for Researcher Agent's deep research |
| **AI Image Generation** | Nano Banana | nano-banana-pro | Used for AI cover images and illustrations |

### API Endpoints
- **Text Model**: OpenAI-compatible API format
- **Search Service**: `https://open.bigmodel.cn/api/paas/v4/web_search`
- **Image Generation**: `https://api.grsai.com`

### Frontend Tech Stack
- **Rendering**: Native HTML + JavaScript
- **Markdown**: marked.js
- **Code Highlighting**: highlight.js
- **Diagram Rendering**: Mermaid.js
- **Image Export**: html2canvas


## 📁 Project Structure

```
banana-blog/
├── backend/                          # Flask backend application
│   ├── app.py                        # Flask application entry
│   ├── config.py                     # Configuration file
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # Environment variable example
│   ├── static/                       # Static files
│   │   └── index.html                # Frontend page
│   ├── outputs/                      # Generated article output directory
│   │   └── images/                   # Generated images directory
│   └── services/
│       ├── llm_service.py            # LLM service
│       ├── image_service.py          # Image generation service
│       ├── task_service.py           # Task management service
│       └── blog_generator/           # Blog generator core
│           ├── blog_service.py       # Blog generation service
│           ├── graph.py              # LangGraph workflow definition
│           ├── agents/               # Agent implementations
│           │   ├── researcher.py     # Research Agent
│           │   ├── planner.py        # Planning Agent
│           │   ├── writer.py         # Writing Agent
│           │   ├── coder.py          # Code Agent
│           │   ├── artist.py         # Illustration Agent
│           │   └── assembler.py      # Assembly Agent
│           ├── templates/            # Jinja2 Prompt templates
│           │   ├── researcher.j2
│           │   ├── planner.j2
│           │   ├── writer.j2
│           │   ├── coder.j2
│           │   └── artist.j2
│           └── services/
│               └── search_service.py # Search service
├── docs/                             # Documentation directory
└── README.md                         # This file
```


## 🔧 Environment Variables

| Variable | Description | Example Value |
|----------|-------------|--------|
| `FLASK_ENV` | Flask runtime environment | development |
| `SECRET_KEY` | Flask secret key | banana-blog-secret-key |
| `AI_PROVIDER_FORMAT` | AI Provider format (openai/gemini) | openai |
| `TEXT_MODEL` | Text generation model | qwen3-max-preview |
| `OPENAI_API_KEY` | OpenAI-compatible API Key | - |
| `OPENAI_API_BASE` | OpenAI-compatible API Base URL | https://dashscope.aliyuncs.com/compatible-mode/v1 |
| `LOG_LEVEL` | Log level | INFO |
| `CORS_ORIGINS` | CORS allowed origins | * |
| `NANO_BANANA_API_KEY` | Nano Banana image generation API Key (optional) | - |
| `NANO_BANANA_API_BASE` | Nano Banana API Base URL | https://api.grsai.com |
| `NANO_BANANA_MODEL` | Nano Banana model name | nano-banana-pro |
| `ZAI_SEARCH_API_KEY` | Zhipu Web Search API Key (optional) | - |
| `ZAI_SEARCH_API_BASE` | Zhipu search API Base URL | https://open.bigmodel.cn/api/paas/v4/web_search |
| `ZAI_SEARCH_ENGINE` | Zhipu search engine type | search_pro_quark |
| `ZAI_SEARCH_MAX_RESULTS` | Search max results | 5 |
| `ZAI_SEARCH_CONTENT_SIZE` | Search content size | medium |
| `ZAI_SEARCH_RECENCY_FILTER` | Search recency filter | noLimit |


## 🤝 Contributing

Welcome to contribute to this project through
[Issue](https://github.com/Anionex/banana-blog/issues)
and
[Pull Request](https://github.com/Anionex/banana-blog/pulls)!


## 📄 License

MIT License
