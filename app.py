import subprocess
import sys

if __name__ == "__main__":
    print("Starting HermesFace Sync Wrapper...")
    
    # Enhanced error handling: don't crash if sync fails
    try:
        subprocess.run([sys.executable, "scripts/sync_hf.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Sync failed with exit code {e.returncode}, but continuing startup...")
        print(f"    Error: {e}")
        print("    → Hermes Agent will start without initial dataset sync")
    except Exception as e:
        print(f"⚠️  Unexpected sync error: {e}")
        print("    → Hermes Agent will start anyway")
