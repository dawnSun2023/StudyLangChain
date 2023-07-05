#Prompt templates 提示模版
from langchain import PromptTemplate
template = """
你喜欢{city}这座城市嘛?
"""

prompt = PromptTemplate.from_template(template)
str = prompt.format(city="武汉")
print(str)