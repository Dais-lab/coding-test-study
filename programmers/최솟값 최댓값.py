"""
작성자 : donghyun Kim
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""

def solution(s):
    l = list(map(int, s.split()))
    return "{} {}".format(min(l), max(l))
