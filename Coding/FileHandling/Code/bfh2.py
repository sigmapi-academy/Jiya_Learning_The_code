import pickle as P

print('the data stored in binary file: ')
fileName = input('Enter file name to read: ')
with open('./FileHandling/Files/'+fileName, 'rb') as fb:
    data = P.load(fb)
    print(data)