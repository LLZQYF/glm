tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据公司名称获得该公司所有基本信息。输入：{'company_name': }, 输出['公司名称', '公司简称', '英文名称', '关联证券', '公司代码', '曾用简称', 所属市场', '所属行业', '上市日期', '法人代表', '总经理', '董秘', '邮政编码', '注册地址', '办公地址', '联系电话', '传真', '官方网址', '电子邮箱', '入选指数', '主营业务', '经营范围', '机构简介', '每股面值', '首发价格', '首发募资净额', '首发主承销商']等信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    }
                },
            "required": ["company_name"],
            },
        }
    },
    {  
    "type":"function",  
        "function":{  
            "name":"search_company_name_by_info",  
            "description": "根据公司基本信息某个字段是某个值来查询具体的公司名称。可以输入的字段有['上市日期', '主营业务', '传真', '入选指数', '公司代码', '公司简称', '关联证券', '办公地址', '官方网址', '总经理', '所属市场', '所属行业', '曾用简称', '机构简介', '每股面值', '法人代表', '注册地址', '电子邮箱', '经营范围', '联系电话', '英文名称', '董秘', '邮政编码', '首发主承销商', '首发价格', '首发募资净额',]。例子：输入：{'key':'所属行业','value':'批发业'} 输出：[{'公司名称': '国药集团药业股份有限公司'},{'公司名称': '苏美达股份有限公司'},{'公司名称': '深圳市英唐智能控制股份有限公司'}]",  
            "parameters": {  
                "type": "object",  
                "properties": {  
                    "key": {  
                        "type": "string",  
                        "description": "字段名",  
                    },  
                    "value": {  
                        "type": "string",  
                        "description": "字段值",  
                    }  
                },  
                "required": ["key", "value"],  
            },  
        }  
    },
    {
        "type":"function",
        "function":{
            "name":"get_company_register",
            "description": "根据公司名称获得该公司所有注册信息。输入：{'company_name': } 输出['公司名称', '登记状态', '统一社会信用代码', '注册资本', '成立日期', '省份', '城市', '区县', '注册号', '组织机构代码', '参保人数', '企业类型', '曾用名']等信息",
            "parameters": {
                "type": "object",
                "properties": {
                "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    }
                },
                "required": ["company_name"],
            },
        }
    },
    {  
    "type":"function",  
    "function":{  
        "name":"search_company_name_by_register",  
        "description": "根据公司注册信息某个字段是某个值来查询具体的公司名称。可以输入的字段有['企业类型', '区县', '参保人数', '城市', '成立日期', '曾用名', '注册号', '注册资本', '登记状态', '省份', '组织机构代码', '统一社会信用代码']。例子：输入：{'key':'注册号','value':'440101000196724'} 输出：[{'公司名称': '广州发展集团股份有限公司'}]",  
        "parameters": {  
            "type": "object",  
            "properties": {  
                    "key": {  
                        "type": "string",  
                        "description": "字段名",  
                    },  
                    "value": {  
                        "type": "string",  
                        "description": "字段值",  
                    }  
                },  
                "required": ["key", "value"],  
            },  
        }  
    },
    {  
        "type":"function",  
        "function":{  
            "name":"get_sub_company_info",  
            "description": "根据公司名称获得该公司所有关联子公司信息。输入：{'company_name': } 输出['关联上市公司股票代码', '关联上市公司股票简称', '关联上市公司全称', '上市公司关系', '上市公司参股比例', '上市公司投资金额', '公司名称']相关信息",  
            "parameters": {  
                "type": "object",  
                "properties": {  
                    "company_name": {  
                            "type": "string",  
                            "description": "公司名称",  
                        }  
                    },  
                "required": ["company_name"],  
            },  
        }  
    },
    {  
    "type":"function",  
    "function":{  
        "name":"search_company_name_by_sub_info",  
        "description": "根据关联子公司信息某个字段是某个值来查询具体的公司名称。可以输入的字段有['上市公司关系', '上市公司参股比例', '上市公司投资金额', '关联上市公司全称', '关联上市公司股票代码', '关联上市公司股票简称',]。例子：输入：{'key':'关联上市公司全称','value':'冠昊生物科技股份有限公司'} 输出：[{'公司名称': '北昊干细胞与再生医学研究院有限公司'},{'公司名称': '北京申佑医学研究有限公司'},{'公司名称': '北京文丰天济医药科技有限公司'},{'公司名称': '冠昊生命健康科技园有限公司'}]",  
        "parameters": {  
            "type": "object",  
            "properties": {  
                "key": {  
                        "type": "string",  
                        "description": "字段名",  
                    },  
                "value": {  
                        "type": "string",  
                        "description": "字段值",  
                    }  
                },  
            "required": ["key", "value"],  
            },  
        }  
    },
    {  
        "type":"function",  
        "function":{  
            "name":"get_legal_document",  
            "description": "根据法律文书案号获得该案所有基本信息。输入：{'case_num': } 输出['标题', '案号', '文书类型', '原告', '被告', '原告律师', '被告律师', '案由', '审理法条依据', '涉案金额', '判决结果', '胜诉方', '文件名']等相关信息",  
                "parameters": {  
                    "type": "object",  
                    "properties": {  
                        "case_num": {  
                            "type": "string",  
                            "description": "法律文书案号",  
                        }  
                    },  
                "required": ["case_num"],  
            },  
        }  
    },     
    {  
    "type":"function",  
    "function":{  
        "name":"search_case_num_by_legal_document",  
        "description": "根据法律文书某个字段是某个值来查询具体的案号。可以输入的字段有['判决结果', '原告', '原告律师', '审理法条依据', '文书类型', '文件名', '标题', '案由', '涉案金额', '胜诉方', '被告', '被告律师',]。例子：输入：{'key':'原告','value':'光明乳业股份有限公司'} 输出：[{'案号': '(2020)苏06民初861号'},{'案号': '(2021)沪0104民初6181号'},{'案号': '(2021)沪0104民初17782号'},{'案号': '(2019)湘0111民初3091号'}]",  
        "parameters": {  
            "type": "object",  
            "properties": {  
                "key": {  
                        "type": "string",  
                        "description": "字段名",  
                    },  
                "value": {  
                        "type": "string",  
                        "description": "字段值",  
                    }  
                },  
            "required": ["key", "value"],  
            },  
        }  
    },
]

tools_v2 = [
    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_COMPANY_INFO",
            "description": "根据公司名称获取公司信息，包括公司名称、公司简介、英文名称、关联证券、公司代码、曾用简称、所属市场、所属行业、上市日期、法人代表、总经理、董秘、邮政编码、注册地址、办公地址、联系电话、传真、官方网址、电子邮箱、主营业务、经营范围、机构简介",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名称",
                        "type": "string"
                    }
                },
                "required": ["company_name"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_SEARCH_COMPANY_NAME_BY_INFO",
            "description": "根据公司简介、英文名称、关联证券、公司代码、曾用简称、所属市场、所属行业、上市日期、法人代表、总经理、董秘、邮政编码、注册地址、办公地址、联系电话、传真、官方网址、电子邮箱、主营业务、经营范围、机构简介 查询出公司名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "参数名",
                        "type": "string"
                    },
                    "value": {
                        "description": "参数值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_COMPANY_REGISTER",
            "description": "根据公司名称查询注册信息，注册信息包含公司名称、登记状态、统一社会信用代码、注册资本、成立日期、省份、城市、区县、注册号、组织机构代码、参保人数、企业类型、曾用名",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名字",
                        "type": "string"
                    }
                },
                "required": ["company_name"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_SEARCH_COMPANY_NAME_BY_REGISTER",
            "description": "根据企业公司注册信息，公司名称、登记状态、统一社会信用代码、注册资本、成立日期、省份、城市、区县、注册号、组织机构代码、参保人数、企业类型、曾用名，查询公司名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "参数名",
                        "type": "string"
                    },
                    "value": {
                        "description": "参数值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_SUB_COMPANY_INFO",
            "description": "根据公司名称获得与子公司有关的所有关联上市公司信息, 对子公司的投资额 比如：[控股比例份额,子公司名称,投资],并且根据结果统计投资和控股",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名字",
                        "type": "string"
                    }
                },
                "required": ["company_name"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_SUB_COMPANY_NAME_FIND_COMPANY_INFO",
            "description": "根据子公司的名字找到它属于是哪一家企业集团公司下的子公司",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名字",
                        "type": "string"
                    }
                },
                "required": ["company_name"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_LEGAL_DOCUMENT",
            "description": "根据案号获得该案所有基本信息，返回的信息包含标题、案号、文书类型、原告、被告、原告律师、被告律师、案由、审理法条依据、依据的法律条文、涉案金额、判决结果、胜诉方、文件名",
            "parameters": {
                "type": "object",
                "properties": {
                    "case_num": {
                        "description": "案号",
                        "type": "string"
                    }
                },
                "required": ["case_num"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_SEARCH_CASE_NUM_BY_LEGAL_DOCUMENT",
            "description": "根据标题、案号、文书类型、原告、被告、原告律师、被告律师、案由、审理法条依据、涉案金额、判决结果、胜诉方、文件名 来查询案号",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "参数名",
                        "type": "string"
                    },
                    "value": {
                        "description": "参数值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        },
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_COMPANY_NAME_BY_INDUSTRY",
            "description": "根据所属行业查询行业下的所有公司的注册信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "参数名",
                        "type": "string"
                    },
                    "value": {
                        "description": "参数值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_LEGAL_INFO_BY_COMPANY_NAME",
            "description": "根据公司名称查询被告信息合作的律师事务所",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "description": "公司名字",
                        "type": "string"
                    }
                },
                "required": ["company_name"]
            },
        }
    },

    {
        "type": "function",
        "function": {
            "name": "FUN_CALL_NAME_GET_COMPANY_NAME_BY_INDUSTRY",
            "description": "根据所属行业查询行业下的所有公司",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "description": "参数名",
                        "type": "string"
                    },
                    "value": {
                        "description": "参数值",
                        "type": "string"
                    }
                },
                "required": ["key", "value"]
            },
        }
    }

]

toolsB = [

]