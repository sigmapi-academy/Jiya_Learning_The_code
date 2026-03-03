import pickle as P

student = {'rollNum':1, 'name':'Jiya', 'section':'E', 'class':8}
fileName = input('Enter file name: ')
with open('./FileHandling/Files/'+fileName,'wb') as fo:
    P.dump(student, fo)
    
    