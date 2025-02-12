import jieba

def tokenize_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield jieba.lcut(line)

for tokens in tokenize_text('news_list'):
    print(tokens)