import os


a = 1
current_dir = os.path.dirname(__file__)
raw_audio_path = os.path.join(current_dir, "raw_audio")
print("请输入说话人名，请注意只支持纯字母数字组合")
name = input()

# 获取目标文件夹下所有.wav文件
wav_files = [file for file in os.listdir(
    raw_audio_path) if file.endswith('.wav')]

a = 1

for wav_file in wav_files:
    new_file_name = f'{name}_{a}.wav'
    src_path = os.path.join(current_dir, wav_file)
    dest_path = os.path.join(current_dir, new_file_name)
    os.rename(src_path, dest_path)
    print(f'{src_path} -> {dest_path}')
    with open("文件对照表.txt", "w") as f:
        f.write(f"{src_path}->{dest_path}\n")
    a += 1

print("重命名完成")
