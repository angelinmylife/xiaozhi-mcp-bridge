# XiaoZhi MCP Bridge | 小智 MCP 桥接聚合服务

> Service with Docker :  Aggregate multiple external MCP services and connect to the XiaoZhi MCP access point.
> 
> 一键部署docker服务：聚合多个外部MCP服务，接入小智MCP接入点

## Quick Start | 快速开始

### 1. vim config file `config.json` | 配置文件

```json
{
    "mcpServers": {
        "mcp-server-01": {
            "url": "https://example.com/mcp",
            "transport": "http"
        },
        "mcp-server-02": {
            "url": "http://127.0.0.1:8000/sse/",
            "transport": "sse"
        }
    }
}
```

### 2. Run with docker command | Docker 命令直接运行

```shell
docker run -itd -v "./config.json:/app/config.json:ro" -e "MCP_ENDPOINT=wss://api.xiaozhi.me/mcp/?token=eyJhbGcx..." angelinmylife/xiaozhi-mcp-bridge
```

* `-v` : set `config.json` path | 设置配置文件路径
* `-e` : set `MCP_ENDPOINT` url | 设置MCP接入点地址

### 3. Run with docker compose | Docker-Compose 运行

```shell
# write docker-compose.yaml
cat > docker-compose.yaml << 'EOF'
version: "3"
services:
  xiaozhi-mcp-bridge:
    image: "angelinmylife/xiaozhi-mcp-bridge:latest"
    container_name: "xiaozhi-mcp-bridge"
    network_mode: host
    volumes:
      - "./config.json:/app/config.json:ro"
    environment:
      MCP_ENDPOINT: "wss://api.xiaozhi.me/mcp/?token=eyJhbGcx..."
    restart: always
EOF

# run
docker compose -f docker-compose.yaml up -d
```


