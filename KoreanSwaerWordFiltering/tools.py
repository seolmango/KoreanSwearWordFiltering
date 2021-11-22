"""
한국어 욕설 탐지 모듈에 사용되는 도구들을 모아놓은 파일입니다.
"""

__all__ = ['tokenization_word','remove_duplicate_token','detach_korean_word','accuracy_improvement']

KOREAN_FIRST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ',
              'ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
KOREAN_SECOND = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ',
              'ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
KOREAN_THIRD = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ',
                'ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ',
                'ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
FREQUENT_HIGH = {1: 2.8848931924611136, 2: 2.558925411794167, 3: 2.3, 4: 2.0943282347242818,
                     5: 1.9309573444801933, 6: 1.8011872336272723, 7: 1.6981071705534974, 8: 1.616227766016838,
                     9: 1.551188643150958, 10: 1.499526231496888, 11: 1.4584893192461115, 12: 1.4258925411794168,
                     13: 1.4000000000000001, 14: 1.3794328234724282, 15: 1.3630957344480195}

def tokenization_word(word : str) -> list:
    """입력된 문장을 토큰화합니다

    Args:
        word (str): 토큰화될 문장입니다

    Returns:
        list: 토큰화가 완료된 리스트로 [(글자,번호),] 형태입니다.
    """
    result = []
    for i in range(len(word)):
        if not word[i] in [' ','.',',']:
            result.append((word[i],i))
        else:
            pass
    return result

def remove_duplicate_token(token_word : list) -> list:
    """토큰화가 된 문장에서 중복되는 문자를 제거합니다.

    Args:
        token_word (list): 토큰화가 된 문장입니다.

    Returns:
        list: 중복문자열이 제거된 리스트입니다.
    """
    result = []
    for i in range(len(token_word)-1):
        if token_word[i][0] == token_word[i+1][0]:
            pass
        else:
            result.append(token_word[i])
    result.append(token_word[-1])
    return result

def detach_korean_word(token_word : list) -> list:
    """입력된 한국어를 초성,중성,종성으로 쪼개어 반환합니다.

    Args:
        token_word (list): 토큰화가 완료된 문장의 리스트입니다.

    Returns:
        list: 초성,중성,종성으로 분리가 완료된 리스트입니다.
    """
    result = [(' ',-2),(' ',-1)]
    for i in range(len(token_word)):
        aski = ord(token_word[i][0]) - 44032
        if -1 < aski and aski < 11173:
            first = KOREAN_FIRST[aski // 588]
            second = KOREAN_SECOND[(aski // 28) % 21]
            third = KOREAN_THIRD[aski % 28]
            if first == 'ㅇ':
                if result[-1][0] in KOREAN_SECOND and second == result[-1][0]:
                    pass
                elif result[-2][0] in KOREAN_SECOND and second == result[-2][0]:
                    pass
                else:
                    result.append((first,token_word[i][1]))
                    result.append((second,token_word[i][1]))
            else:
                result.append((first,token_word[i][1]))
                result.append((second,token_word[i][1]))
            if third != '':
                result.append((third,token_word[i][1]))
        else:
            result.append(token_word[i])
    return result[2:]

def accuracy_improvement(x : int) -> int:
    """더 좋은 정확도를 제공하기위해 사용하는 함수입니다.

    Args:
        x (int): 문장의 길이입니다.

    Returns:
        int: 확률 개선 값입니다.
    """
    if x in FREQUENT_HIGH:
        return FREQUENT_HIGH[x]
    else:
        return 0.1**((x-3)/10)+1.3

if __name__ == '__main__':
    a = "테스트 문장입니다!!"
    b = tokenization_word(a)
    c = remove_duplicate_token(b)
    d = detach_korean_word(c)
    print('a :' , a)
    print('b :' , b)
    print('c :' , c)
    print('d :' , d)
        