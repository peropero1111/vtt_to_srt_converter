import os
from tkinter import Tk, filedialog

# vtt stt 변환 (실잘적)
def convert_vtt_to_srt(vtt_file, output_dir): #실질적 변환 함수

    with open(vtt_file, 'r', encoding='utf-8') as file:                                     #vtt 파일 읽기
        lines = file.readlines()

    srt_lines = []                                                                         #여기서부터
    counter = 1

    for line in lines:
        line = line.strip()
        if line.startswith("WEBVTT") or line == "":
            continue
        if " --> " in line:
            srt_lines.append(f"{counter}\n")
            counter += 1
            line = line.replace('.', ',')
        srt_lines.append(line + "\n")                                                      #여기까지가 변환 과정        

    srt_file = os.path.join(output_dir, os.path.basename(vtt_file).replace('.vtt', '.srt'))
    with open(srt_file, 'w', encoding='utf-8') as file:
        file.writelines(srt_lines)

# 파일 선택&변환
def main():
    root = Tk()
    root.withdraw()  

  
    vtt_files = filedialog.askopenfilenames(title="Select VTT Files", filetypes=[("VTT files", "*.vtt")])
    #파일들 선택(vtt)

    if not vtt_files:
        print("No files selected.")
        return

   
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    #폴더선택(srt)

    if not output_dir:
        print("No output directory selected.") 
        return

    # VTT 파일을 SRT로 변환
    for vtt_file in vtt_files:
        convert_vtt_to_srt(vtt_file, output_dir)
        print(f"Converted: {vtt_file} -> {os.path.join(output_dir, os.path.basename(vtt_file).replace('.vtt', '.srt'))}")

if __name__ == "__main__":
    main()
