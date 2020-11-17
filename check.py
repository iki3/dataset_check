import os,os.path
path='../datasets'
a=len([name for name in os.listdir('../datasets/.') if not(os.path.isfile(name))])
b=len([name for name in os.listdir('../datasets/.') if os.path.isdir(name)])

print(os.listdir('../datasets/.'))
print(a)
print(b)
dir_list=[]
for i in os.listdir('../datasets/.'):
    print(i)
    if(os.path.isdir(os.path.join(path,i))):
        dir_list.append(os.path.join(path,i))
        print('dir')
print(dir_list)

for i in dir_list:
    if(os.path.isdir(i)):
        print(i)
