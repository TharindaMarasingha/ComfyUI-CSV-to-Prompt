# ComfyUI CSV to Prompt Node
### Created by Tharinda Marasingha

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Node-green.svg)

A lightweight and efficient custom node for **ComfyUI** that allows you to load prompts directly from CSV files. It is specifically designed for **Bulk/Batch Image Generation**, allowing you to automate the creation of hundreds of images using a pre-defined list of prompts.

## ✨ Features

* **📂 Auto-Scan:** Automatically detects CSV files placed in the `csv_files` directory.
* **🔄 Bulk Mode:** Uses the generic `Seed` number to iterate through your CSV rows automatically.
* **⚡ Lightweight:** No heavy dependencies (pandas not required—uses standard Python).
* **🛡️ Robust:** Handles missing columns and empty files gracefully.

---

## 📥 Installation

### Method 1: ComfyUI Manager (Recommended)
1.  Open **ComfyUI Manager**.
2.  Select **"Install via Git URL"**.
3.  Paste the link to this GitHub repository.
4.  Restart ComfyUI.

### Method 2: Manual Installation
Navigate to your ComfyUI `custom_nodes` folder and run the following command:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TharindaMarasingha/ComfyUI-CSV-to-Prompt.git


