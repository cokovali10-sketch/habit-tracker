"""Build habit-tracker EXE with PyInstaller."""
import subprocess, sys, os
# --- константы вынесены FORGE refactor ---
CONST_1024 = 1024


def build():
    print("Building habit-tracker EXE...")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--name", "habit-tracker",
        "--console",
        "main.py"
    ]
    subprocess.run(cmd, check=True)
    os.makedirs("dist", exist_ok=True)
    if os.path.exists("dist/habit-tracker.exe"):
        size = os.path.getsize("dist/habit-tracker.exe") // (CONST_1024*CONST_1024)
        print(f"OK: dist/habit-tracker.exe ({size} MB)")
    else:
        print("FAILED")

if __name__ == "__main__":
    build()
