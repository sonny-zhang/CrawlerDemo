# @Time     : 2019/6/3 11:31
# @Author   : sonny-zhang
# @FileName : common.py
# @github   : @sonny-zhang
import hashlib


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ == "__main__":
    print(get_md5("hello".encode('utf-8')))
