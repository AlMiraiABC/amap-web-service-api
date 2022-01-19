# For more information, please refer to https://aka.ms/vscode-docker-python
FROM nmtsoft-docker.pkg.coding.net/images/python/python:3.8.12-alpine-git

# Install pip requirements
COPY requirements.txt .

# exeute shell commands
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
