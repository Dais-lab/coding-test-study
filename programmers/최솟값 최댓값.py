"""
작성자 : donghyun Kim
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""

def solution(s):
    integer_list = list(map(int, s.split()))
    return "{} {}".format(min(integer_list), max(integer_list))
