import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import sys


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

    #print(results)

    print(type(results))
    tic = time.clock()-start
    #print(retrieval_results)
    print(tic)


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





    