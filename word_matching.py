import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import sys
import json
import requests
import synonyms
from cognitive_service import call_cv_api

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

def find_shanglian(input_info, tag_mode=1, final_output_number=5):
    start = time.clock()
    filename = './couplet_100k.txt'
    #input_tag_list = ['chair', 'moon','mountain']
    input_tag_list = ['moon']
    input_tag_list = input_info['description']['tags']
    print(input_tag_list)
    list_trans = []
    final_input_tag_list = []
    for i in range(len(input_tag_list)):
        list_trans.append(get_reuslt(translate(input_tag_list[i])))
    print(list_trans)
    list_trans = list(set(list_trans))
    print(list_trans)
    for i in range(len(list_trans)):
        synonyms_words = synonyms.nearby(list_trans[i])
        d=dict(zip(synonyms_words[0],synonyms_words[1]))
        synonyms_words = [k for k,v in d.items() if v >=0.7]
        if tag_mode==1:
            final_input_tag_list += synonyms_words[:3]
        else:
            final_input_tag_list.append(synonyms_words[:3])
    retrieval_results = []
    print(final_input_tag_list)
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
        if tag_mode==1:
            tag = final_input_tag_list[i]
            #tag_retrieval_result = retrieve_tag(all_lines,result_length = retrieval_result_length, tag )
            tag_retrieval_result = retrieve_tag(all_lines,-1, tag)
            retrieval_results+=tag_retrieval_result
        else:
            tag = final_input_tag_list[i]
            tag_retrieval_result = retrieve_tag(all_lines,-1, tag, tag_mode=2)
            retrieval_results+=tag_retrieval_result
    #'''
    results = {}
    for i in retrieval_results:
        results[i] = results.get(i, 0) + 1 
    results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    output_results_index = [index[0] for index in results[:final_result_length]]
    print ([index[1] for index in results[:final_result_length]])
    results = [all_lines[i][:-1] for i in output_results_index]
    #tic = time.clock()-start
    #print(tic)
    return results

def retrieve_tag(content, result_length, tag, tag_mode=1):
    tag_retrieval_index = []
    if tag_mode==1:
        for j in range(int(len(content)/3)):
            data_sentence = content[j*3]
            if (data_sentence.find(tag))!= -1:
                tag_retrieval_index.append(j*3)
            if len(tag_retrieval_index)==result_length:
                break
        return tag_retrieval_index
    elif tag_mode==2:
        for i in range(len(tag)):
            result_index = []
            for j in range(int(len(content)/3)):
                data_sentence = content[j*3]
                if (data_sentence.find(tag[i]))!= -1:
                    result_index.append(j*3)
                    tag_retrieval_index.append(j*3)
                if len(tag_retrieval_index)==result_length:
                    break
        return list(set(tag_retrieval_index))

if __name__ == "__main__":
    with open('./download1.jpg', 'rb') as f:
        input_info = call_cv_api(f.read())
        results = find_shanglian(input_info, tag_mode=2, final_output_number=5) # tag_mode表示同义词是/否只进行一次匹配, 对应取值2/1
        print(results)# ['思潮如江河湖海水涌', '日落长河生丽水', '江河湖海四水归一', '江河湖海滔滔水', '江河湖海皆有水']
