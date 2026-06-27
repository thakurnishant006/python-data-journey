## Things I understood clearly:
to open the file
f = open('file_name') -> if in same directory // default is reading (pass path instead of the file name)
f = open(test.txt,'r') -> another parameter to specify the action we want to do with the file

print(f.name) -> read the file

f.close() -> need to close the file , if we dont close the file it will cause leaks

// Open using the context manager: they allows us to work with the file within the block it allows us to automatically close the file 
 ------------ Read a file--------------
with open('test.txt' , 'r') as f:
    f_contents = f.read(100)-> size as argument to print total character [Print 100 char]
    print(f_contents) // suits for small file
    // read lines
    f_contents = f.readlines() // read all line
    f_contents = f.readline() // read 1st line
    // Read line from large file :
    for line in f:
        print(line , end ='') // will not get the memory isssue

size_to_read = 100
   if _contents = f.read(size_to_read) 
    while len(f_contents) > 0:
        print(f_contents, end = '')
        f_contents = f.read(size_to_read)
f.seek(0) -> it will tell where to begin
        print(f_contents, end = '')
        f_contents = f.read(size_to_read)

print(f.tell()) -> tell where we are how much char we read.

-------------Write a file----------------
we cannont write a file opened in a read mode
with open(test.txt) as f:  -> is a file is present it will overwrite if not it creates a new one.
    f.write('text) -> write it
    f.seek()-> set the position to the begining 
    f.write('test2') -> write where we left off


--------------------read and write a file --------
with open('test.txt','r') as rf: -> reading original file
    with open('testcpy.txt','w') as wf: -> writing to the copy file
    for line in rf:
        wf.write(line)

// Large a picture file
Open files in the binary mode: use b in parameter
with open('1.jpg','rb') as rf:
    with open('1_cpy.jpg','wf') as wf:
        for i in rf:
            wf.write(i)

// to do this in chunk size 
chunk_size = 4096
rf_chunk = rf.read(chunk_size)
while len(rf_chunk) > 0:
    wf.write(rf_chunk)
    rf_chunk = rf.read(chunk_size)




## Things that confused me:

## Things I want to try in code:

## New words I heard (write them even if you don't know them yet):

### New thinks i learnd form the corey video


# Things i missed -----