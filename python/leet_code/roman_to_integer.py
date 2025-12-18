s='IX'
roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
s =s.replace("IV", "IIII").replace("XI", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX")#4,9,40,90
s=s.replace("CD", "CCCC").replace("CM", "DCCCC")#400.#900
print(s)
print(list(map(lambda x:roman_to_integer[x],s)))
print(sum(map(lambda x: roman_to_integer[x], s)))