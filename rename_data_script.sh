#!/bin/bash

clear

echo "//////////////////////////////////////////"
echo "VITS数据集批量重命名   by领航员未鸟"
echo "//////////////////////////////////////////"
echo

echo "请将这个脚本放入目标文件夹后再运行"
echo
echo "它将会自动重命名该文件夹下所有wav格式的文件为 “说话人名_数字.wav” 而不改变其排序"
echo
echo "如果不是在目标文件夹下，请立即关闭，防止出现误修改!"
echo
echo "如有需求恢复原名请保留   文件对照表.txt"
echo
echo "并在同一目录下运行 恢复原名.sh"
echo "//////////////////////////////////////////"
echo

echo
echo

a=1

echo "请输入说话人名，请注意只支持纯字母数字组合"
read name

for file in *.wav
do
  if [ -e "$file" ]; then
    new_name="${name}_${a}.wav"
    mv "$file" "$new_name"
    echo "$file->$new_name"
    echo "$file->$new_name" >> 文件对照表.txt
    a=$((a+1))
  fi
done

echo
echo
echo "Done^^!"
read u
