# Setup Guide — SAARTHI AI

## Prerequisites

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **OS** | Windows 10 / macOS / Linux | Windows 11 |
| **Python** | 3.10+ | 3.12+ |
| **RAM** | 8 GB | 16 GB |
| **GPU** | Not required | NVIDIA GPU with 4GB+ VRAM |
| **Disk** | 6 GB free | 10 GB free |

---

## Step 1: Install Ollama

Ollama runs AI models locally on your machine.

### Windows
1. Go to [https://ollama.com/download](https://ollama.com/download)
2. Download and run the Windows installer
3. Ollama starts automatically as a background service

### macOS
```bash
brew install ollama
```

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Verify Installation
```bash
ollama --version
```

---

## Step 2: Pull the AI Model

```bash
ollama pull qwen2.5:7b
```

This downloads ~4.7 GB. Wait for it to complete.

### Alternative Models (if you have limited VRAM)

| Your VRAM | Recommended Model | Command |
|-----------|------------------|---------|
| 4GB+ | qwen2.5:7b | `ollama pull qwen2.5:7b` |
| 2-4GB | phi3:latest | `ollama pull phi3` |
| <2GB (CPU only) | qwen2.5:3b | `ollama pull qwen2.5:3b` |

If you use a different model, update the `MODEL_NAME` variable in `utils/ai_engine.py`.

---

## Step 3: Clone the Repository

```bash
git clone https://github.com/vanshdigitals/ai-assistant-bootcamp-projects.git
cd "ai-assistant-bootcamp-projects/SAARTHI AI PROJECT"
```

---

## Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit` — the web UI framework
- `ollama` — Python client for the Ollama API

---

## Step 5: Run the App

```bash
streamlit run app.py
```

The app opens in your browser at **http://localhost:8501**.

---

## Troubleshooting

### "Could not connect to Ollama"
Ollama isn't running. Start it:
- **Windows:** Search for "Ollama" in Start menu and open it
- **Terminal:** Run `ollama serve`

### "Model not found"
You haven't pulled the model yet:
```bash
ollama pull qwen2.5:7b
```

### "Slow responses"
- If using CPU only, responses take 15-30 seconds. This is normal.
- Close other GPU-heavy apps (games, video editors) to free VRAM.

### "Streamlit not found"
```bash
pip install streamlit
```

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

---

## Switching Models

To use a different Ollama model:

1. Pull it: `ollama pull <model-name>`
2. Open `utils/ai_engine.py`
3. Change `MODEL_NAME = "qwen2.5:7b"` to your model
4. Restart the app

---

## Reset User Data

To start fresh, delete the memory file:
```bash
# Windows
del "memory\user_data.json"

# macOS/Linux
rm memory/user_data.json
```

The app recreates it on next launch.
