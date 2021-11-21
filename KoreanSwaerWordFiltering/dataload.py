"""
한국어 욕설 탐지 모듈의 데이터를 로드하는 모듈입니다.
"""

from os import name
import re
from errors import *

class filter():
    """욕설 필터링 모듈의 필터 클래스입니다.

    """
    def __init__(self, filter_name,filter_setting):
        self.name = filter_name
        self.setting = filter_setting
        self.data = {}
    
    def load_data(self, name : str, data : int):
        """데이터 파일에서 읽어온 데이터를 가공하여 저장합니다

        Args:
            name (str): 필터에서 잡아낼 문자입니다
            data (int): 문자와 치환할 숫자입니다
        """
        self.data[name] = data
    
    
    
    
    
    
    
    
def load_badword_data(source_path : str) -> list:
    """욕설 데이터를 불러옵니다.

    Args:
        source_path (str): 욕설 데이터 파일의 경로

    Returns:
        list: 욕설 데이터로 [일반적인욕설리스트,초성욕설리스트]의 구조
    """
    result = [[],[]]
    f = open(source_path, 'r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        elif line.startswith('#'):
            pass
        elif line.startswith('$'):
            result[1].append(line[1:].strip())
        else:
            result[0].append(line.strip())
    f.close()
    return result

def load_filter_data(source_path : str) -> dict:
    """한국어 욕설 필터링 모듈의 필터 데이터를 불러옵니다.

    Args:
        source_path (str): 필터 데이터 파일의 경로

    Returns:
        dict: 
    """
    result = {}
    f = open(source_path, 'r', encoding='utf-8')
    line = f.readline()
    while line != "//end file":
        line = line[0:-1]
        if line.startswith('#'):
            pass
        elif line.startswith('{') and line.endswith('}'):
            line = line[1:-1]
            if line == 'End':
                result[now.name] = now
            else:
                a = line.split(':')
                now = filter(a[0],a[1])
        elif line:
            if line.startswith('[') and line.endswith(']'):
                name = line[1:-1]
                if not name in result:raise FilterException(f"{name}은 존재하지 않는 필터입니다.")
                now.data = result[name].data
            else:
                res = []
                for cur in re.split('[<>]',line):
                    if cur:
                        res.append(cur)
                if len(res) == 2:
                    now.load_data(res[0],res[1])
                elif len(res) == 3:
                    now.load_data(res[0],res[1]+result['base_filter'].data[res[2]])
                else:
                    raise FilterException(f"{line}은 잘못된 필터 데이터 입력법입니다.")
        else:
            pass
        line = f.readline()
    return result
            

print(load_badword_data('KoreanSwaerWordFiltering\Data\BadWords.txt'))
print(load_filter_data('KoreanSwaerWordFiltering\Data\BasicData.txt'))