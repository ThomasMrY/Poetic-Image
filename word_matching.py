import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import sys
import json
import requests
import synonyms

def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        #'from': 'AUTO',
        #'to': 'Chinese',
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        return response.text
    else:
        #print("有道词典调用失败")
        return None

def get_reuslt(repsonse):
    result = json.loads(repsonse)
    return result['translateResult'][0][0]['tgt']

def main():
    start = time.clock()
    filename = './couplet_100k.txt'
    #input_tag_list = ['chair', 'moon','mountain']
    input_tag_list = ['moon']
    list_trans = []
    final_input_tag_list = []
    for i in range(len(input_tag_list)):
        list_trans.append(get_reuslt(translate(input_tag_list[i])))
    
    for i in range(len(list_trans)):
        synonyms_words = synonyms.nearby(list_trans[i])
        d=dict(zip(synonyms_words[0],synonyms_words[1]))
        synonyms_words = [k for k,v in d.items() if v >=0.7]
        final_input_tag_list += synonyms_words[:3]
    
    final_result_length = 5
    retrieval_results = []
    
    with open(filename, 'r', encoding='utf-8') as in_file:
        all_lines = in_file.readlines()
    ''' # much slower?
    pool = ThreadPool()
    func = partial(retrieve_tag, all_lines, -1)
    pool.map(func, input_tag_list)
    pool.close()
    pool.join()
    '''
    for i in range(len(final_input_tag_list)):
        tag = final_input_tag_list[i]
        #tag_retrieval_result = retrieve_tag(all_lines,result_length = retrieval_result_length, tag )
        tag_retrieval_result = retrieve_tag(all_lines,-1, tag)
        retrieval_results+=tag_retrieval_result
    #'''
    results = {}
    for i in retrieval_results:
        results[i] = results.get(i, 0) + 1 
    results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    output_results_index = [index[0] for index in results[:5]]
    results = [all_lines[i][:-1] for i in output_results_index] # ['一树桂花为月亮', '一鉴荒唐月亮猪', '云追月亮风吹柳', '今夜烟花同月亮', '今宵月亮真圆啊']
    #tic = time.clock()-start
    #print(tic)
    return results

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
    results = main()
    print(results)
