example = ['kitties', 'frogs', 'grey', 'nonce']

def comma(example):
    for i in range(len(example) - 2):
        print(example[i], end=", ")
    print(example[-2] + ', and ' + example[-1])

comma(example)