def common_character_count(str1, str2):
    str1_set = set(str1)
    result = 0
    for letter in str1_set:
        str1_count = str1.count(letter)
        str2_count = str2.count(letter)
        result += min([str1_count, str2_count])
    print(result)
    return result

s1 = "aabcc"
s2 = "adcaa"
common_character_count(s1, s2)

s1 = "zzzz"
s2 = "zzzzzzz"
common_character_count(s1, s2)
