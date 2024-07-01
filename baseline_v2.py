from openai import OpenAI
import httpx
import json
import requests
import datetime
from zhipuai import ZhipuAI
from config import constants, tools
from config.tool_functions import get_company_info, search_company_name_by_info, get_company_register, search_company_name_by_register, get_sub_company_info, search_company_name_by_sub_info, get_legal_document, search_case_num_by_legal_document
client = ZhipuAI(api_key=constants.zhipu_key)
# client = OpenAI(http_client=httpx.Client(proxies=constants.openai_proxy), api_key=constants.openai_key)

def parse_function_call(response, messages):
    tool_calls = response.choices[0].message.tool_calls
    messages.append(response.choices[0].message.model_dump())  # gpt-4o
    for tool_call in tool_calls:
        function = tool_call.function
        func_args = function.arguments
        func_args = func_args.replace('（', '(')
        func_args = func_args.replace('）', ')')
        func_name = function.name
        if func_name == "FUN_CALL_NAME_GET_COMPANY_INFO":
            function_result = get_company_info(**json.loads(func_args))
        
        if tool_call.function.name == "FUN_CALL_NAME_SEARCH_COMPANY_NAME_BY_INFO":
            function_result = search_company_name_by_info(**json.loads(func_args))
            # 模型抽的字段可能不对 用其他字段依次查询
            if len(function_result) == 0:
                param = json.loads(func_args)
                # 根据其他字段一次查询
                for company_info_property in constants.company_info_property_list:
                    key = company_info_property
                    value = param['value']
                    function_result = search_company_name_by_info(key, value)
                    if len(function_result) > 0:
                        break
        
        if tool_call.function.name == "FUN_CALL_NAME_GET_COMPANY_REGISTER":
            register_info = get_company_register(**json.loads(func_args))

            if len(register_info) == 0:
                function_result = search_company_name_by_register('注册号', json.loads(func_args)['company_name'])
            else:
                function_result = register_info

        if tool_call.function.name == "FUN_CALL_NAME_SEARCH_COMPANY_NAME_BY_REGISTER":
            function_result = search_company_name_by_register(**json.loads(func_args))
        
        if tool_call.function.name == "FUN_CALL_NAME_GET_SUB_COMPANY_INFO":
            # 传的是母公司的名称，需要从母公司找到子公司
            sub_company_list = []

            for sub_company_info_property in constants.sub_company_info_property_list:
                key = sub_company_info_property
                value = json.loads(func_args)['company_name']
                company_name_list = []
                company_name = search_company_name_by_sub_info(key, value)

                if len(company_name_list) == 0:
                    company_name_str = json.loads(func_args)['company_name']
                    search_company_name = search_company_name_by_info('英文名称', company_name_str)

                    if len(search_company_name) > 0:
                        company_name = search_company_name_by_sub_info(key, search_company_name['公司名称'])

                if isinstance(company_name, dict):
                    company_name_list.append(company_name)

                if isinstance(company_name, list):
                    company_name_list = company_name

                if len(company_name_list) > 0:

                    for company_name_dict in company_name_list:
                        sub_company_info = get_sub_company_info(company_name_dict['公司名称'])
                        # print(sub_company_info)
                        sub_company_info.pop('关联上市公司股票代码')
                        sub_company_info.pop('关联上市公司股票简称')
                        sub_company_info.pop('上市公司关系')
                        if sub_company_info.get('上市公司参股比例'):
                            pass
                        else:
                            sub_company_info['上市公司参股比例'] = "0"

                        if sub_company_info.get('上市公司投资金额'):
                            pass
                        else:
                            sub_company_info['上市公司投资金额'] = "0万"

                        sub_company_info['子公司名称'] = sub_company_info['公司名称']
                        sub_company_info['控股'] = sub_company_info['上市公司参股比例']
                        sub_company_info['投资'] = sub_company_info['上市公司投资金额']

                        sub_company_info.pop('关联上市公司全称')
                        sub_company_info.pop('公司名称')
                        sub_company_info.pop('上市公司参股比例')
                        sub_company_info.pop('上市公司投资金额')

                        sub_company_list.append(sub_company_info)
                    break
            # print(sub_company_list)
            content = sub_company_list.__str__() + " " + messages[0]['content']
            function_result = content
            # content = get_count_model(content)

            # # 小于30家公司 将数据给模型，大于30家公司直接给计算结果
            # if len(sub_company_list) < 30:
            #     # 合并
            #     sub_company_list.append({"统计", content})
            #     function_result = sub_company_list
            # else:
            #     function_result = content

        if tool_call.function.name == "FUN_CALL_NAME_GET_LEGAL_DOCUMENT":
            function_result = get_legal_document(**json.loads(func_args))
        
        if tool_call.function.name == "FUN_CALL_NAME_SEARCH_CASE_NUM_BY_LEGAL_DOCUMENT":
            case_num_info = search_case_num_by_legal_document(**json.loads(func_args))

            cas_num_list = []
            if isinstance(case_num_info, dict):
                cas_num_list.append(case_num_info)

            if isinstance(case_num_info, list):
                cas_num_list = case_num_info

            legal_info_list = []
            if len(case_num_info) != 0:
                for case_num in cas_num_list:
                    legal_info_list.append(get_legal_document(case_num['案号']))

            function_result = legal_info_list.__str__()

        if tool_call.function.name == "FUN_CALL_NAME_GET_COMPANY_NAME_BY_INDUSTRY":
            param = json.loads(func_args)
            key = '所属行业'
            value = param['value']
            company_name_list = search_company_name_by_info(key, value)
            if len(company_name_list) > 0:
                register_info_list = []
                for company_name in company_name_list:
                    register_info = get_company_register(company_name['公司名称'])
                    register_info_list.append(register_info)

                register_info_list.append({"公司数量", len(register_info_list)})
                function_result = register_info_list

        if tool_call.function.name == "FUN_CALL_NAME_GET_SUB_COMPANY_NAME_FIND_COMPANY_INFO":
            function_result = get_sub_company_info(**json.loads(func_args))

        if tool_call.function.name == "FUN_CALL_NAME_LEGAL_INFO_BY_COMPANY_NAME":
            company_name = json.loads(func_args)['company_name']
            cas_num_result = search_case_num_by_legal_document('被告', company_name)
            cas_num_list = []
            legal_info_list = []

            if isinstance(cas_num_result, dict):
                cas_num_list.append(cas_num_result)

            if isinstance(cas_num_result, list):
                cas_num_list = cas_num_result

            for case_num in cas_num_list:
                legal_info_list.append(get_legal_document(case_num['案号']))

            function_result = legal_info_list.__str__()
        messages.append({
            "role": "tool",
            "content": function_result.__str__(),
            "tool_call_id": tool_call.id
        })
    second_response = client.chat.completions.create(
        model=constants.model_name,
        messages=messages,
        tools=tools.tools_v2,
    )
    # print("second_response.choices[0].message = ", second_response.choices[0].message)
    # breakpoint()
    return second_response

if __name__ == '__main__':
    question_path = 'glm/data/question.json'
    result_path = 'glm/result/' + f'{constants.model_name}_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '_output.json'
    # result_path = 'glm/result/' + f'{constants.model_name}' + '_output_test.json'
    with open(question_path, 'r', encoding='utf-8') as file, open(result_path, 'w', encoding='utf-8') as output_file:
        for line in file:
            data = json.loads(line)
            print(data['question'])
            messages = []
            # messages.append(
            #     {
            #         "role": "system",
            #         "content": constants.prompt
            #     }
            # )
            messages.append(
                {
                    "role": "user",
                    "content": f"{data['question']}"
                }
            )
            response = client.chat.completions.create(
                model=constants.model_name,
                temperature=0.95,
                top_p=0.7,
                messages=messages,
                tools=tools.tools_v2,
                tool_choice="auto",
            )
            while response.choices[0].finish_reason == "tool_calls":  # 如果返回的是工具调用（多次）:response.choices[0].finish_reason == "tool_calls" or "stop"
                response = parse_function_call(response, messages)
            print(response.choices[0].message)
            data['answer'] = response.choices[0].message.content
            json.dump(data, output_file, ensure_ascii=False)
            output_file.write('\n')