from stegano import lsb
import os

def create_payload():
    img_path = input("Enter mel.png: ").strip()
    if not os.path.exists(img_path):
        print(f"Error: {img_path} not found!")
        return

    command = input("Enter command 'shutdown': ").strip()
    
   
    try:
        secret_img = lsb.hide(img_path, command)
        output_name = "mel_secret.png"
        secret_img.save(output_name)
        print(f"File created: {output_name}")
        print(f"Hidden command: {command}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_payload()