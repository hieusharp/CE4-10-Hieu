sizes=[5, 7, 300, 90, 24, 50, 75]
#2.1 
print("These are my sheep size:",sizes)

#2.2
print("Now the biggest sheep has size {0}. Let's shear it." .format(max(sizes))) #2.2
im = sizes.index(max(sizes)) # index of max size in sizes
sizes[im]=8
print ("After shearing, here is my flock: ")
print(sizes)

#2.3, 2.4 2.5
for m in range(1,3):
    print()
    print("A month has passed, now here is my flock: ")
    sizes=[size+50*m for size in sizes]
    print(sizes)
    print("Now the biggest sheep has size {0}. Let's shear it." .format(max(sizes)))
    sizes[im]=8
    print ("After shearing, here is my flock: ")
    print(sizes)
   
#2.6
print("My flock has a total size of {0}. I would get {0}*2$= " .format(sum(sizes)), sum(sizes)*2)

