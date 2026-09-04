import pickle

l = [1, 2, 3, 4, 5]
enc = pickle.dumps(l)

with open('sam1.txt', 'wb') as f:
    f.write(enc)

with open('sam1.txt', 'rb') as f:
    data = f.read()
    # print(data)
    og = pickle.loads(data)
    print(og)
