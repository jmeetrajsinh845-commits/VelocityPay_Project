# Installation Guide

# Overview

This guide explains how to set up and run the VelocityPay Analytics Platform on a local machine.

The project includes Python scripts, SQL files, Power BI dashboards, and machine learning components.

---

# System Requirements

## Operating System

- Windows 10/11
- macOS
- Linux

---

## Python Version

Python 3.11 or later

Verify installation:

```bash
python --version
```

---

## Required Software

- Visual Studio Code
- Git
- Power BI Desktop
- Python 3.11+

---

# Clone Repository

```bash
git clone https://github.com/<your-username>/VelocityPay-Analytics-Platform.git
```

Move into the project directory:

```bash
cd VelocityPay-Analytics-Platform
```

---

# Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# Install Required Packages

```bash
pip install -r requirements.txt
```

---

# Project Structure

```
VelocityPay_Project/

│

├── dashboards/

├── data/

├──
