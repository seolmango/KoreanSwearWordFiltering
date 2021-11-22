"""
한국어 욕설 필터링 모듈의 에러들입니다. 
"""

__all__ =['DataLoadException',
          'BadWordsException',
          'FilterException',
          'TextModifyException',
          'NoRelateFilterException'
          ]

class DataLoadException(Exception):
    """
    데이터를 불러오는 도중 에러가 발생하면 발생하는 에러입니다.
    """
    pass

class BadWordsException(DataLoadException):
    """
    욕설 데이터를 불러오는 도중 에러가 발생하면 발생하는 에러입니다.
    """
    pass

class FilterException(DataLoadException):
    """
    필터 설정 파일을 불러오던중 에러가 발생하면 발생하는 에러입니다.
    """
    pass

class TextModifyException(Exception):
    """
    텍스트 처리 중 에러가 발생하면 발생하는 에러입니다.
    """
    pass

class NoRelateFilterException(TextModifyException):
    """
    연관된 필터를 찾을 수 없는 경우 발생하는 에러입니다.
    """
    pass