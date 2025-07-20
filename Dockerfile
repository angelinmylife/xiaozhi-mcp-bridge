FROM python:3.11.0

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


CMD ["python", "mcp-pipe.py", "mcp-bridge.py"]

