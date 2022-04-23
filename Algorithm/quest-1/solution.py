import sys
def solution(log_text):
    # TODO
    j =0
    str = []
    for i in range(0, len(log_text)):
        str0 = ''
        if log_text[i] == ">":
            j = j+1
            k = i
            if j % 2 == 1:
                while log_text[k+1] != '<':
                    k = k+1
                    str0 = str0+ log_text[k]
            if str0 != '':        
                str.append(str0)
    ans = {}        
    for s in range(0, len(str)):
        if s % 2 == 0:
            ans[str[s]] = str[s+1]
    return ans        
    
# 채점을 위해 아래 코드는 수정하지 마세요.
if __name__ == '__main__':
    input_DIR = sys.argv[1]
    with open(input_DIR, "r") as input_file:
        log_text = input_file.read()

    submission = solution(log_text)
    print(submission)
