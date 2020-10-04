def palindrome_partition(str,itr, result,tmp):
    tmp_str=''
    cur = tmp[:]
    for i in range(itr, len(str)):
        tmp_str=tmp_str+str[i]
        if palindrome(tmp_str):
            tmp.append(tmp_str)
            if i+1<len(str):
                palindrome_partition(str, i+1, result,  tmp[:])
            else:
                result.append(tmp)
            tmp=cur


def palindrome(str):
    str_rev=str[:][::-1]
    if str==str_rev:
        return True
    else:
        return False


if __name__ == "__main__":
    str = str(input("Please enter the string you wish to check...").strip())
    str=str.lower()
    length=len(str)
    temp = []
    result = []
    palindrome_partition(str, 0, result,[])

    for i in result:
        word = ''.join(i)
        if len(word)==length:
            print(*i, sep=' ')
