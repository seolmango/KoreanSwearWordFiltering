"""
욕설 탐지 모듈의 메인입니다.
"""

from dataload import *
from tools import *

class filters():
    """
    필터링 클래스 입니다.
    """
    def __init__(self, badword_path : str, filter_path :str):
        """필터링 클래스 초기화함수입니다

        Args:
            badword_path (str): 욕설 데이터가 있는 경로입니다
            filter_path (str): 필터 데이터가 있는 경로입니다
        """
        raw_filter_data = load_filter_data(filter_path)
        self.BASE_FILTER = raw_filter_data['base_filter']
        self.FILTERS = raw_filter_data
        
class text_object():
    """
    텍스트 클래스 입니다.
    """
    
    def __init__(self, text : str ,filters_object : filters):
        self.BEFORE_MODIFY = text
        modifing_text = tokenization_word(text)
        modifing_text = remove_duplicate_token(modifing_text)
        modifing_text = detach_korean_word(modifing_text,False)
        self.AFTER_MODIFY = switch_token_num(modifing_text,filters_object,False)
        first_text = tokenization_word(text)
        first_text = remove_duplicate_token(first_text)
        first_text = detach_korean_word(first_text,True)
        self.FIRST_MODIFY = switch_token_num(first_text,filters_object,True)
        
        
        


if __name__ == '__main__':
    a = filters('KoreanSwaerWordFiltering\Data\BadWords.txt','KoreanSwaerWordFiltering\Data\BasicData.txt')
    print(a.BASE_FILTER)
    print(a.FILTERS)
    b = text_object("테스트입니다",a)
    print(b.BEFORE_MODIFY)
    print(b.AFTER_MODIFY)
    print(b.FIRST_MODIFY)