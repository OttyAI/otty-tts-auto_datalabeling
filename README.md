# otty-tts-auto_datalabeling

## how to use

**注意**
开发环境必须安装有conda/miniconda

steps:

```shell
git clone https://github.com/OttyAI/otty-tts-auto_datalabeling.git
```

```shell
cd otty-tts-auto_datalabeling
```

下载依赖

```shell
python3 download_dependencies.py 
```

将处理过的原始数据（清洗过的音频文件放到raw_audio,重命名音频（方便分类

```shell
python3 rename.py
```

开始标注

```sh
python3 auto_DataLabeling_re.py

```

每次标注完成后，都要清理标注

```sh
python3 clean_list.py
```
