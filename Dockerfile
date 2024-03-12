# 使用官方 Python 镜像作为基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 创建用于保存录音文件的目录
RUN mkdir recordings

# 复制当前目录下的所有文件到容器的 /app 目录下
COPY . /app

# 安装项目依赖
RUN pip install gradio

# 暴露端口 7860
EXPOSE 7860

# 在容器启动时运行应用
CMD ["python", "app.py"]
