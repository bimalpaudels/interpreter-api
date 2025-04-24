### Python Interpreter Backend (FastAPI)

## Overview

This backend is a demonstration of the `restricted` package in action — built using FastAPI.

It showcases the use of `restricted`'s default configuration to safely evaluate user-submitted Python code with custom import restrictions and structured error handling. 
The API provides an endpoint to submit code and receive output, making it ideal for quick browser-based coding.

## Demo 
The frontend of this demo is hosted in Vercel.

[![Demo](https://github.com/user-attachments/assets/9f679859-5afa-49dd-b771-048452a2d7e9)](https://dotpy.bimals.net)

## Features
- "Sandboxed" Python execution.
- Custom import restrictions with helpful error messages.
- Timeout protection to avoid infinite loops.

## Installation and Usage
1. Clone the repo
```bash
git clone https://github.com/bimalpaudels/interpreter-api.git
cd interpreter-api
```

2. Install dependencies **(uv recommended)**
```bash
pip install -r requirements.txt
```

3. Run the server
```bash
uvicorn main:app --reload
```
