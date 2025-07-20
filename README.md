# XiaoZhi MCP Bridge

> 一键部署docker服务：聚合多个外部MCP服务，接入小智MCP接入点

## Quick Start

### vim config file `config.json`

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

### Run with docker command

```shell
docker run -itd -v "./config.json:/app/config.json:ro" -e "MCP_ENDPOINT=wss://api.xiaozhi.me/mcp/?token=eyJhbGcx..." angelinmylife/xiaozhi-mcp-bridge
```

### Run with docker compose

```shell
docker compose -f docker-compose.yaml up -d
```


