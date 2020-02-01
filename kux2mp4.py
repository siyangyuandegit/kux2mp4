

import os 
import time


INPUT_DIR_PATH = 'F:\\download' #kux文件夹路径
OUTPUT_DIR_PATH = 'D:\\YoukuFiles\\output #输出文件夹路径

def kux2mp4(ffmpeg_path, input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        for file in files:
            # print(file)
            name = os.path.join(root,file)
            file = file.replace(' ', '')
            input_file = input_path + '\\' + str(file)
            print(input_file)
            if os.path.exists(input_file) != True:
                os.rename(name, input_file)
                time.sleep(1)
            output_file = output_path + '\\' + str(file)[:str(file).find('.kux')] + '.mp4'
            print(output_file)
            command = ffmpeg_path + ' -y -i ' + input_file + ' -c:v copy -c:a copy -threads 2 ' + output_file
            print(command)
            os.system(command)

def main():
    ffmpeg_path = os.getcwd() + '\\nplayer\\ffmpeg.exe'
    kux2mp4(ffmpeg_path, INPUT_DIR_PATH, OUTPUT_DIR_PATH)
    print(ffmpeg_path)

if __name__ == "__main__":
    # execute only if run as a script
    main()