#!/usr/bin/env python3
"""
Setup script for Down In A Hole game
Automatically installs dependencies and runs the game
"""

import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required!")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def install_requirements():
    """Install requirements from requirements.txt"""
    try:
        print("📦 Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_pygame():
    """Check if pygame is installed"""
    try:
        import pygame
        print(f"✅ Pygame version: {pygame.version.ver}")
        return True
    except ImportError:
        print("❌ Pygame not found!")
        return False

def run_game():
    """Run the main game"""
    try:
        print("🎮 Starting Down In A Hole...")
        subprocess.run([sys.executable, "jogo.py"])
    except KeyboardInterrupt:
        print("\n👋 Game stopped by user")
    except Exception as e:
        print(f"❌ Error running game: {e}")

def main():
    """Main setup function"""
    print("🎯 Down In A Hole - Setup")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Check if pygame is already installed
    if not check_pygame():
        # Install requirements
        if not install_requirements():
            print("❌ Setup failed! Please install dependencies manually:")
            print("   pip install -r requirements.txt")
            sys.exit(1)
    
    print("\n🚀 Setup complete! Starting game...")
    run_game()

if __name__ == "__main__":
    main()
