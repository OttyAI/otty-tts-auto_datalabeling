import os

a = 1
current_dir = os.getcwd()  # 相对于运行脚本的位置，获取当前目录
raw_audio_path = os.path.join(current_dir, "raw_audio")  # 'raw_audio' 文件夹在当前目录
print("您的工作目录是：", current_dir)
print("音频路径是：", raw_audio_path)

print("请输入说话人名，注意只支持纯字母数字组合")
name = input()

if not os.path.exists(raw_audio_path):
  print(f"文件夹 {raw_audio_path} 不存在。请检查你的路径。")
  exit()

print("文件夹下的所有文件：")
print(os.listdir(raw_audio_path))

# 获取目标文件夹下的所有.wav文件
wav_files = [file for file in os.listdir(raw_audio_path) if file.endswith('.wav')]
print("找到的 wav 文件：", wav_files)

for wav_file in wav_files:
  new_file_name = f'{name}_{a}.wav'
  src_path = os.path.join(raw_audio_path, wav_file)
  dest_path = os.path.join(raw_audio_path, new_file_name)

  if not os.path.exists(src_path):
    print(f"源文件 {src_path} 不存在。跳过此文件...")
    continue

  try:
    os.rename(src_path, dest_path)
    print(f'{src_path} -> {dest_path}')
    with open("文件对照表.txt", "a") as f:
      f.write(f"{src_path}->{dest_path}\n")
    a += 1
  except Exception as e:
    print(f"在重命名文件 {src_path} 到 {dest_path} 时出现错误。错误是 {str(e)}")

print("重命名完成")
