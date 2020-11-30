#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 源文本
source_text_list = ['AB', 'AD', 'AC', 'BCD', 'ABE', 'F']
# 分词字典
text_cut_word = {}
# 词频字典
word_frequency = {}
# 词频倒排索引
word_text_relationship = {}
for text in source_text_list:
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
source_text_list = list(text_avg_score.values())
source_text_list.sort(reverse=True)
# 设置重要性阈值
top_threshold = 4
# 筛选重要性文本
useful_text_list = source_text_list[0:top_threshold]
