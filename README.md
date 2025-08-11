# Down In A Hole

A 2D platformer game built with Python and Pygame.

## Quick Start

### Option 1: Automatic Setup (Recommended)
**Windows:**
- Double-click `run_game.bat`

**All Platforms:**
```bash
python setup.py
```

### Option 2: Manual Installation
1. Install Python 3.6 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python jogo.py
   ```

## Controls
- **Movement**: WASD or Arrow Keys
- **Jump**: W, Space, or Up Arrow
- **Variable Jump**: Hold jump button for higher jumps
- **Restart after death**: R key

## Game Features
- 2D platformer physics
- Character animation
- Collision detection
- Death and restart system
- Variable jumping mechanics

## Requirements
- Python 3.6+
- Pygame 2.5.0+

## File Structure
```
down-in-a-hole/
├── jogo.py          # Main game file
├── player.py        # Player character and physics
├── mapa.py          # Background rendering
├── settings.py      # Game configuration
├── requirements.txt # Python dependencies
├── setup.py         # Automatic setup script
├── run_game.bat     # Windows launcher
├── images/          # Game graphics
├── rivem_ani/       # Character animations
└── font/            # Custom fonts
```

## Troubleshooting
If you encounter issues:
1. Make sure Python 3.6+ is installed
2. Try running `pip install pygame` manually
3. Check that all asset files are present in their respective folders
