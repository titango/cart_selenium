# Main executable file
from scripts import superstore_script

def main():
  print("Staring program in main.py")
  
  # Run superstore script
  superstore_script.run(10)

if __name__ == "__main__":
  main()