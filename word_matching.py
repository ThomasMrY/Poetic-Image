import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import sys
import json
import requests

def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None

def get_reuslt(repsonse):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(repsonse)
    print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
    print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])


def main():
    filename = './couplet_100k.txt'
    input_tag_list = ['酒','月','水','风','山','云','一','眼']
    retrieval_result_length = 9
    final_result_length = 5
    with open(filename, 'r', encoding='utf-8') as in_file:
        all_lines = in_file.readlines()
    retrieval_results = []
    start = time.clock()
    #'''
    for i in range(len(input_tag_list)):
        tag = input_tag_list[i]
        #tag_retrieval_result = retrieve_tag(all_lines,result_length = retrieval_result_length, tag )
        tag_retrieval_result = retrieve_tag(all_lines,-1, tag)
        #retrieval_results.append(tag_retrieval_result)
        retrieval_results+=tag_retrieval_result
    ''' # much slower?
    pool = ThreadPool()
    func = partial(retrieve_tag, all_lines, -1)
    pool.map(func, input_tag_list)
    pool.close()
    pool.join()
    '''
    results = {}
    for i in retrieval_results:
        results[i] = results.get(i, 0) + 1 
        #results = sorted(results.items(), key=lambda item:item[0]) 
    results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    tic = time.clock()-start
    print(tic)
    print("本程序调用有道词典的API进行翻译，可达到以下效果：")
    print("外文-->中文")
    print("中文-->英文")
    word = input('请输入你想要翻译的词或句：')
    list_trans = translate(word)
    get_reuslt(list_trans)


def retrieve_tag(content, result_length, tag):
    tag_retrieval_index = []
    for j in range(int(len(content)/3)):
        data_sentence = content[j*3]
        if (data_sentence.find(tag))!= -1:
            tag_retrieval_index.append(j*3)
        if len(tag_retrieval_index)==result_length:
            break
    return tag_retrieval_index

if __name__ == "__main__":
    main()
