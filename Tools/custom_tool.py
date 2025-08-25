from langchain_core.tools import tool

# step 1 - create a function

def multiply (a,b):
    """Multipy two numbers"""
    return a * b


#step 2 - Add type hints

def multiply (a:int, b:int) -> int:
    """Multiply two numbers"""
    return a * b

#Step 3 - Add tool decorator

@tool
def multiply(a:int , b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3, "b":4})



print(multiply.name)
print(multiply.description)
print(multiply.args)



## Using structured tool and pydantic

# A structure tool in langchain is a special type of tool where the input to the tool follow a structured shema, typically defined using a pydanticc model

from pydantic import BaseModel, Field
from langchain.tool import StructuredTool

class MultiplyInput(BaseModel):
    a: int = Field(required=True , description='The first number to add')
    b: int = Field(required=True, description='Second number to add')

def multiply_func(a,b) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func = multiply_func,
    name = 'multiply',
    description = "Multiply two numbers",
    args_schema = MultiplyInput
)

result = multiply_tool.invoke({"a":2, "b":4})

## Using BaseTool Class

# Base tool is the abstract base class for all tools in lanchain, it defines the core structure and interface that any tool must follow, whether it's a simple one liner or a fully customized function.

#All other tool types like @tool, structuredTool are built on top of BaseTool

from langchain.tools import BaseTool
from typing import Type

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema : Type[BaseModel] = MultiplyInput

    def _run(self, a:int, b:int) -> int:
        return a*b
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({"a":2, "b":4})

# Toolkit

@tool
def add(a:int,b:int)-> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a * b

class MathToolkit:
    def get_tools(self):
        return [add,multiply]
    

toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, tool.description)