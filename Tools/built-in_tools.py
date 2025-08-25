from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke('IPL news')
print(result)


# Shell tool

from langchain_coommunity.tools import ShellTool

shell_tool = ShellTool()

result = shell_tool.invoke('whoami')

print(result)