# XML
# XML도 JSON과 마찬가지로 데이터를 전달을 목적으로 만든 구조화된 텍스트 형식
# eXtensible Markup Language은 데이터 저장 및 전달을 위해 만든 다목적 마크업 언어 Markup Language.
# 마크업 언어는 일반적인 텍스트와 구분되는 테크 Tag를 이용해 문서나 데이터를 구조화 하는 언어.
# 대표적인 마크업 언어로는 앞에서 삺펴본 HTML HyperText Markup Language.

# HTML의 경우는 태그가 미리 정해져 있지만 XML은 자신이 태그를 정의해서 사용할 수 있음
# 단 XML 문서의 규칙을 따라야 함

# * 태그는 '<문자열>' 로 시작해서 '</문자열>'로 끝나야함
# 시작과 끝 태그의 문자열은 같아야 하며 대소문자를 구분. XML 문서에서는 시작 태그에서 끝 태그까지로 이루어진 것을 요소 element 라고 함.

# * 태그는 중첩해 여러 개를 이용할 수 있는데 이때 태그는 반드시 올바른 순서대로 이용해야 함
# 즉, '<abc><def> ~ </def></abc>' 와 같이 나중에 나온 시작 태그에 대응하는 끝 태그가 먼저 나와야 함

# * XML 문서에는 반드시 최상위 root 요소가 있어야 함. 최상위 요소는 시작과 끝 태그로 다른 모든 요소를 감싸야 함.

# * 주석은 '<!--' 와 '-->' 로 문자열을 감싸서 표시. 즉 '<!-- 이것은 주석입니다 -->' 와 같이 이용.

# xml을 지원하는 모듈은 내장 모듈로 xml이 있고, 외부 모듈의 경우 xmltodict가 편리
# XML 데이터를 파이썬의 딕셔너리 타입으로 바로 변환.
# http://pypi.org/project/xmltodict/

# xmltodict 라이브러리에서 XML 형식의 데이터를 파이썬의 딕셔너리 타입으로 변환하는 함수.
# xmltodict.parse(xml_input [, xml_attribs=True 혹은 False ])
# xml_input은 XML 타입의 데이터.
# xml_attribs은 기본 값은 True.
# False 이면 XML 형식의 데이터를 딕셔너리 타입으로 변환할 때 속성을 무시

import xmltodict
import pprint

with open('./input/data.xml', 'r', encoding='utf-8') as xml_file:
    dict_data = xmltodict.parse(xml_file.read(), xml_attribs=True)  # xml 데이터를 딕셔너리로 변경
    # print(dict_data)
    # print(dict_data['response']['body']['items'])
    datas = dict_data['response']['body']['items']
    pprint.pprint(datas)