import subprocess

repo_path = '/content/Shura'

codetorun = """
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui /content/Shura
!git clone https://huggingface.co/embed/negative /content/Shura/embeddings/negative
!git clone https://huggingface.co/embed/lora /content/Shura/models/Lora/positive
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/Shura/models/ESRGAN -o 4x-UltraSharp.pth
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/Shura/scripts/run_n_times.py
!git clone -b v2.1 https://github.com/camenduru/deforum-for-automatic1111-webui /content/Shura/extensions/deforum-for-automatic1111-webui
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-images-browser /content/Shura/extensions/stable-diffusion-webui-images-browser
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-huggingface /content/Shura/extensions/stable-diffusion-webui-huggingface
!git clone https://github.com/Iyashinouta/sd-model-downloader /content/Shura/extensions/sd-model-downloader
!git clone -b v2.1 https://github.com/camenduru/sd-civitai-browser /content/Shura/extensions/sd-civitai-browser
!git clone -b v2.1 https://github.com/camenduru/sd-webui-additional-networks /content/Shura/extensions/sd-webui-additional-networks
!git clone https://github.com/Mikubill/sd-webui-controlnet /content/Shura/extensions/sd-webui-controlnet
!git clone -b v2.1 https://github.com/camenduru/openpose-editor /content/Shura/extensions/openpose-editor
!git clone https://github.com/jexom/sd-webui-depth-lib /content/Shura/extensions/sd-webui-depth-lib
!git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /content/Shura/extensions/tag-autocomplete
!git clone https://github.com/hnmr293/posex /content/Shura/extensions/posex
!git clone https://github.com/dbolya/tomesd /content/Shura/extensions/tomesd
!git clone -b v2.1 https://github.com/camenduru/sd-webui-tunnels /content/Shura/extensions/sd-webui-tunnels
!git clone -b v2.1 https://github.com/camenduru/batchlinks-webui /content/Shura/extensions/batchlinks-webui
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-catppuccin /content/Shura/extensions/stable-diffusion-webui-catppuccin
!git clone -b v2.1 https://github.com/camenduru/a1111-sd-webui-locon /content/Shura/extensions/a1111-sd-webui-locon
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-rembg /content/Shura/stable-diffusion-webui-rembg
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-two-shot /content/Shura/extensions/stable-diffusion-webui-two-shot
!git clone -b v2.1 https://github.com/camenduru/sd_webui_stealth_pnginfo /content/Shura/extensions/sd_webui_stealth_pnginfo
"""

codetorun2 = """
!git reset --hard
!git -C /content/Shura/repositories/stable-diffusion-stability-ai reset --hard
"""

lines = codetorun.splitlines()

def rulesbroken(codetoexecute, cwd=''):
    for line in lines:
        line = line.strip()
        if line.startswith('!'):
            line = line[1:]
        if not line == '':
            try:
                if cwd:
                    subprocess.run(line, shell=True, check=True, cwd=repo_path)
                else:
                    subprocess.run(line, shell=True, check=True)
            except Exception as e:
                print("Exception: " + str(e))

rulesbroken(lines)

lines = codetorun2.splitlines()

rulesbroken(lines, repo_path)
