"""
풀이 : Donghyun Kim
이메일 : rkdqus2006@naver.com
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""

def solution(s):
    l = list(map(int, s.split()))
    
    return "{} {}".format(min(l), max(l))