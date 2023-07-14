import zhipuai
import os

os.environ['API_KEY'] = "c2cfeacba2f25dd217f35dc5a0e20d97.rzI9Z3qL68a72ORR"
zhipuai.api_key = "c2cfeacba2f25dd217f35dc5a0e20d97.rzI9Z3qL68a72ORR"


def invoke_example():
    response = zhipuai.model_api.invoke(
        model="chatglm_lite",
        prompt=[{"role": "user", "content": "请根据如下问题，生成5条，类似的问题，假设你是一名汽车行业的{资深编辑}，请在{汽车之家}写一篇{吉利汽车}{帝豪LHIP}的{新闻稿} ，需要展示出车型的 {销量优势}、{口碑优势}、{用车成本优势}，同时植入本月一系列降价或者补贴相关的{优惠促销}活动，需要逻辑严谨，全文流畅。"}],
        top_p=0.7,
        temperature=0.9,
    )
    print(response)


def async_invoke_example():
    response = zhipuai.model_api.async_invoke(
        model="chatglm_lite",
        prompt=[{"role": "user", "content": "人工智能"}],
        top_p=0.7,
        temperature=0.9,
    )
    print(response)


'''
  说明：
  add: 事件流开启
  error: 平台服务或者模型异常，响应的异常事件
  interrupted: 中断事件，例如：触发敏感词
  finish: 数据接收完毕，关闭事件流
'''


def sse_invoke_example():
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_lite",
        prompt=[{"role": "user", "content": "人工智能"}],
        top_p=0.7,
        temperature=0.9,
    )

    for event in response.events():
        if event.event == "add":
            print(event.data)
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
        elif event.event == "finish":
            print(event.data)
            print(event.meta)
        else:
            print(event.data)


def query_async_invoke_result_example():
    response = zhipuai.model_api.query_async_invoke_result("your task_id")
    print(response)

invoke_example()