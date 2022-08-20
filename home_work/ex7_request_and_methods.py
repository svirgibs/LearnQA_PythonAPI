import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
method_types = ['GET', 'POST', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'PUT']


def print_text_and_status_code(obj):
    print(obj.text)
    print(obj.status_code)
    print('---------------------')


def do_all_req_types(method):
    res_get = requests.get(url, params={"method": f"{method}"})
    res_post = requests.post(url, data={"method": f"{method}"})
    res_delete = requests.delete(url, data={"method": f"{method}"})
    res_head = requests.head(url, data={"method": f"{method}"})
    res_options = requests.options(url, data={"method": f"{method}"})
    resp_patch = requests.patch(url, data={"method": f"{method}"})
    res_put = requests.put(url, data={"method": f"{method}"})
    return res_get, res_post, res_delete, res_head, res_options, resp_patch, res_put


if __name__ == '__main__':
    """
    # Вопрос №1
    response1 = requests.get(url)
    print_text_and_status_code(response1)

    # Вопрос №2
    response2 = requests.head(url)
    print_text_and_status_code(response2)

    # Вопрос №3
    response3 = requests.get(url, params={"method": "GET"})
    print_text_and_status_code(response3)
    print('////////////////////////////////////////')
    """
    # Вопрос №4
    for method_type in method_types:
        responses_by_method = do_all_req_types(method_type)
        for obj in responses_by_method:
            if obj.request.method != method_type and obj.text == '{"success":"!"}':
                print("Cочетание, когда реальный тип запроса не совпадает со значением параметра, "
                      "но сервер отвечает так, словно все ок:")
                print("Real method: %s, Param: %s " % (obj.request.method, method_type))
                print_text_and_status_code(obj)
            elif obj.request.method == method_type and obj.status_code != 200:
                print("Типы совпадают, но сервер считает, что это не так")
                print("Real method: %s, Param: %s " % (obj.request.method, method_type))
                print_text_and_status_code(obj)





