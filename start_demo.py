#!/usr/bin/env python3
"""
ESGx.Africa Demo Startup Script
Quick start script for the ESGx.Africa platform demo
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version_info.major}.{sys.version_info.minor}")

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        sys.exit(1)

def setup_environment():
    """Set up environment variables"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        print("🔧 Creating .env file from template...")
        env_file.write_text(env_example.read_text())
        print("✅ .env file created. Please update with your API keys if needed.")

def start_streamlit_demo():
    """Start the Streamlit demo"""
    print("🚀 Starting ESGx.Africa Demo...")
    print("🌍 Visit: http://localhost:8501")
    print("📱 The demo will open in your browser automatically")
    print("\n" + "="*50)
    print("ESGx.Africa - Ubuntu ESG Platform")
    print("AI-Powered ESG Intelligence for Africa")
    print("="*50 + "\n")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "esgx_africa_demo.py",
            "--server.port=8501",
            "--server.address=0.0.0.0",
            "--browser.gatherUsageStats=false"
        ])
    except KeyboardInterrupt:
        print("\n👋 ESGx.Africa demo stopped. Thanks for trying our platform!")
    except FileNotFoundError:
        print("❌ Streamlit not found. Please install requirements first.")
        sys.exit(1)

def start_fastapi_backend():
    """Start the FastAPI backend (optional)"""
    print("🚀 Starting ESGx.Africa Backend API...")
    print("📡 API will be available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/api/docs")
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app",
            "--host=0.0.0.0",
            "--port=8000",
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 ESGx.Africa API stopped.")
    except FileNotFoundError:
        print("❌ Uvicorn not found. Please install requirements first.")
        sys.exit(1)

def main():
    """Main startup function"""
    print("🌍 ESGx.Africa Platform Startup")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Setup environment
    setup_environment()
    
    # Install requirements
    install_requirements()
    
    # Choose what to start
    print("\nWhat would you like to start?")
    print("1. 📱 Streamlit Demo (Recommended for first-time users)")
    print("2. 🔧 FastAPI Backend (For developers)")
    print("3. 🚀 Both Demo and Backend")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        start_streamlit_demo()
    elif choice == "2":
        start_fastapi_backend()
    elif choice == "3":
        print("Starting both services...")
        print("Note: Use Ctrl+C to stop services")
        # Start backend in background and demo in foreground
        try:
            import threading
            backend_thread = threading.Thread(target=start_fastapi_backend)
            backend_thread.daemon = True
            backend_thread.start()
            start_streamlit_demo()
        except Exception as e:
            print(f"❌ Error starting services: {e}")
    else:
        print("❌ Invalid choice. Starting Streamlit demo by default...")
        start_streamlit_demo()

if __name__ == "__main__":
    main()