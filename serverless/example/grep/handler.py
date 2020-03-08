import gzip
import re

with gzip.open(TMP_DIR, mode='rt') as f:
    lines = f.readlines()
    print(lines)
    
    with open(TMP_EXPORT_DIR, mode='wt') as ef:
      for line in lines:
        if re.search(r'正規表現', line):
          print(line)
          ef.write(line)
          
# 出力ファイルへの出力の仕方は、ファイルによって変化するので適宜変更する