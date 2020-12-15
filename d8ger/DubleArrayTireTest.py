#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import islice

# 源文本
source_text_score_list = ['AB', 'AD', 'AC', 'BCD', 'ABE', 'F']
# 分词字典
text_cut_word = {}
# 词频字典
word_frequency = {}
# 词频倒排索引
word_text_relationship = {}
for text in source_text_score_list:
    text_cut_word[text] = []
    for key in text:
        text_cut_word[text].append(key)
        word_frequency[key] = word_frequency.get(key, 0) + 1
        tmp = word_text_relationship.get(key, [])
        tmp.append(text)
        word_text_relationship[key] = tmp
# for k, v_list in text_cut_word.items():
#     print(k + ":" + "_".join(v_list))
# for k, v in word_frequency.items():
#     print(k + ":" + str(v))
# for k, v_list in word_text_relationship.items():
#     print(k + ":" + "; ".join(v_list))

# 源文本分词列表根据词频排序
for k, v_list in text_cut_word.items():
    v_list.sort(key=lambda x: word_frequency[x], reverse=True)
total_num = sum(word_frequency.values())
word_weight = {}
for k, v in word_frequency.items():
    word_weight[k] = round(float(v / total_num), 2)
    print(k + ":" + str(word_weight[k]))

# 计算文本重要性均分
text_avg_score = {}
for k, v_list in text_cut_word.items():
    score = sum([word_weight[key] for key in v_list])
    text_avg_score[k] = round(float(score / len(v_list)), 2)
    print(k + ":(分值)", str(text_avg_score[k]))
# 按照得分倒序排列, 结果为[(k, v)]
source_text_score_list = sorted(text_avg_score.items(), key=lambda x: x[1], reverse=True)
# 设置重要性阈值
top_threshold = 4
# 筛选重要性文本
count = 1
for k, v in source_text_score_list:
    if count <= top_threshold:
        print("第[{}]个, 得分[{}], 源文本[{}]".format(count, v, k))
    count += 1
word_rank_list = list(word_frequency.keys())
word_count = len(word_rank_list)
word_iterator = iter(word_rank_list)
delta = int(word_count * 0.4)
# 一共5级
rank_split_list = [delta, delta, delta, word_count - delta * 3]
out = [list(islice(word_iterator, size)) for size in rank_split_list]
print(out)

# ['AB', 'AD', 'AC', 'BCD', 'ABE', 'F']
# 11,
