from pprint import pprint
import re
import arabic_reshaper
import pandas as pd
import json


#letters only
patt = re.compile(r'\\u.{4}')
raw_text = r"this is a test. \u00d9 To demonstrate 2 regex expressions!!"
letters_only_text = re.sub(patt, " ", raw_text)
print(letters_only_text)
text = '''
ha_ haha  
'''
pattern = re.compile(r'\bha',)
 
matches = pattern.findall(text)
# if matches:
#     print(matches)
# else: 
#     print('hello')

#that workedd
s ="\u00d8\u00ad\u00d9\u0082\u00d9\u008a\u00d9\u0082\u00d8\u00a9 \u00d9\u0085\u00d8\u00b4 \u00d9\u0083\u00d8\u00af\u00d8\u00a8  \u00d9\u0084\u00d9\u0085\u00d8\u00af\u00d8\u00a9 39 \u00d8\u00af\u00d9\u0082\u00d9\u008a\u00d9\u0082\u00d8\u00a9 \u00d9\u0084\u00d9\u0088 \u00d8\u00a8\u00d8\u00b9\u00d8\u00aa\u00d8\u00aa \u00d8\u00a7\u00d9\u0084\u00d8\u00b1\u00d8\u00ad\u00d9\u0085\u00d9\u0086 \u00d8\u00a7\u00d9\u0084\u00d8\u00b1\u00d8\u00ad\u00d9\u008a\u00d9\u0085 \u00d8\u00a7\u00d9\u0084\u00d9\u0085\u00d9\u0084\u00d9\u0083 \u00d8\u00a7\u00d9\u0084\u00d9\u0082\u00d8\u00af\u00d9\u0088\u00d8\u00b3 \u00d9\u0084 29 \u00d8\u00b4\u00d8\u00ae\u00d8\u00b5 \u00d9\u0087 \u00d8\u00aa\u00d8\u00b3\u00d9\u0085\u00d8\u00b9 \u00d8\u00a8\u00d9\u0083\u00d8\u00b1\u00d8\u00a9 9\u00d8\u00a7\u00d8\u00ae\u00d8\u00a8\u00d8\u00a7\u00d8\u00b1 \u00d8\u00ad \u00d8\u00aa\u00d9\u0081\u00d8\u00b1\u00d8\u00ad\u00d9\u0083 \u00d9\u0088\u00d9\u0084\u00d9\u0088 \u00d8\u00a7\u00d9\u0087\u00d9\u0085\u00d9\u0084\u00d8\u00aa\u00d9\u0087\u00d8\u00a7 \u00d8\u00ad \u00d9\u008a\u00d8\u00b5\u00d9\u008a\u00d8\u00a8\u00d9\u0083 \u00d8\u00b3\u00d9\u0088\u00d8\u00a1 \u00d9\u0084\u00d9\u0085\u00d8\u00af\u00d8\u00a9 \u00d8\u00b3\u00d9\u0086\u00d8\u00a9"
out = s.encode('latin1').decode('utf-8')
reshaped_text = arabic_reshaper.reshape(out)
rev_text = reshaped_text[::-1]  # slice backwards 
#print(out)
#print(rev_text)

def valid_emojis (s):
    return str(s).encode('latin1').decode('utf8') 
def valid_time (timestamp):
    return pd.to_datetime(timestamp,unit='ms')
def get_year (date):
    return date.year
def get_month (date):
    return date.month


stri = 'Reacted \u00e2\u009d\u00a4 to your message'
print(valid_emojis(stri) )

with open('message_sample.json','r') as c:
    cnv = json.load(c)["messages"]
my_cnv = pd.DataFrame(cnv)
my_cnv.drop(["is_unsent","is_taken_down","bumped_message_metadata"],axis=1,inplace=True)
my_cnv['content'] = my_cnv['content'].apply(valid_emojis)
my_cnv['timestamp_ms'] = my_cnv['timestamp_ms'].apply(valid_time)
my_cnv['year'] = my_cnv['timestamp_ms'].apply(get_year)
my_cnv['month'] = my_cnv['timestamp_ms'].apply(get_month)
my_cnv['msg_count'] = 1
msg_count = my_cnv.groupby(["year","month"])['msg_count'].sum()

print(len(my_cnv['content']))
search_value = input('Type a word to search for : ')
my_cnv['has_value'] =my_cnv.apply(lambda row: row.astype(str).str.contains(search_value).any(), axis=1)
my_cnv['content'].where(my_cnv['has_value'] == True).to_csv('has_value.csv',index=False)
my_cnv.to_csv('my_cnv.csv',index=False)
msg_count.to_csv('test.csv')
