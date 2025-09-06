# Text to Image (Streamlit + Hugging Face)

A minimal Streamlit app that generates an image from text using a Hugging Face Stable Diffusion model.

## Features

- Text-to-image generation via Hugging Face model hub
- Simple Streamlit UI
- Works on CPU (slow) or GPU (faster, if PyTorch with CUDA is installed)

## Quick Start

### Prerequisites

- Python 3.9+ recommended
- pip
- Optional: NVIDIA GPU with recent drivers + CUDA for faster inference

### Setup

```bash
cd /path/to/repo
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### (Optional) Enable GPU

Install a CUDA-enabled PyTorch build appropriate for your system. Example (CUDA 12.1):

```bash
pip install --index-url https://download.pytorch.org/whl/cu121 torch torchvision torchaudio
```

Verify with:

```python
python -c "import torch; print(torch.cuda.is_available())"
```

## Run the App

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually http://localhost:8501).

## Hugging Face Model Access

This app uses the Stable Diffusion model `CompVis/stable-diffusion-v1-4`. You may need to accept the model license and authenticate with a Hugging Face token for first-time downloads.

1) Create an account at: https://huggingface.co/
2) Visit the model page `CompVis/stable-diffusion-v1-4` and accept its terms.
3) Authenticate locally with either:

```bash
huggingface-cli login
# or set an environment variable for the session
export HUGGINGFACE_TOKEN=hf_...your_token...
```

If downloads fail with 403/401 errors, ensure you accepted the terms and are logged in.

## Project Structure

```
app.py           # Streamlit app entrypoint
requirements.txt # Python dependencies
LICENSE          # MIT License
README.md        # This file
```

## Notes and Tips

- First run will download the model weights; it may take several minutes and several GB of disk.
- CPU inference is slow. For reasonable speed, use a GPU build of PyTorch.
- If you have limited VRAM, try smaller prompts or reduce image sizes (the current script uses defaults from the pipeline).

## Troubleshooting

- Authentication/permission errors when downloading model:
  - Ensure you accepted the `CompVis/stable-diffusion-v1-4` license on Hugging Face
  - Run `huggingface-cli login` or set `HUGGINGFACE_TOKEN`

- CUDA not available / GPU not used:
  - Install a CUDA-enabled PyTorch build matching your driver/CUDA version
  - Verify with `python -c "import torch; print(torch.cuda.is_available())"`

- Out-of-memory (OOM):
  - Close other GPU apps, reduce concurrent workloads
  - Consider a smaller model variant or lower image sizes if you adapt the code

- Streamlit not starting:
  - Confirm the virtual environment is activated and dependencies are installed
  - Check port conflicts; run `streamlit run app.py --server.port 8502`

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgements

- Stable Diffusion by CompVis, Stability AI and LAION
- Hugging Face ecosystem (`transformers`, `diffusers`)
- Streamlit for the web UI framework
