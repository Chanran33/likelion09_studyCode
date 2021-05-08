#딕셔너리 실습
pairs = {'태연':'what do i call you','sokodomo':'지구멸망',
            '휘인':'whater color'}

#하나의 키-value 쌍을 더 추가하는 방법 : 딕셔너리 변수[키] = value
print(pairs)
pairs['선미'] = '꼬리'
print(pairs)

#특정키-value 쌍을 삭제하는 방법 : del 변수[키]
del pairs['태연'] 
print(pairs)

#key value값을 찾는 방법 : 딕셔너리 변수.get(키)
print(pairs.get('휘인'))