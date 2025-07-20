from fastmcp import FastMCP
from fastmcp.mcp_config import MCPConfig
from config import Config


mcp_config = MCPConfig.from_file(Config.config_path)
mcp = FastMCP.as_proxy(mcp_config, name=Config.server_name)


if __name__ == "__main__":
    mcp.run(transport="stdio")

