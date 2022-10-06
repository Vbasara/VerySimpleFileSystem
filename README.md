# VerySimpleFileSystem 
### Course: CIS-321 Fall 2022

## Description
  This is a simplified version of a filesystem that merely mimics the performance of a filesystem.
  I created a list that resembles the filesystem of which 5 blocks are set for the inode table
  and the other 55 are for the data blocks or data-region. For simplicity sake, each inode and 
  datablock are both 4096 bytes in size. So there are no sub indexes for each inode block. I used loops
  to iterate through the filesystem to find empty spaces that would need to be filled just like in a real
  filesystem. This was done in the Write() function. There are no pointers in python so offsets needed to 
  be used for allocation of data. The Open() and read() functions were implemented as directed in the chapter.
  They were responsible for opening and reading the file from the disk. I chose to only work with 5 files. 
  
## The Task
  You are being tasked with building the ‘vsfs’ that is described in Chapter 40 of the online textbook Three Easy Pieces. 
  The idea is to mimic the description as accurately as possible, in Python. This should only live in the command-line (CLI), 
  or not graphically. To receive full credit, you need to implement at least 70% of the elements listed in the 
  chapter.
## List of things implemented into the VSFileSystem
   - superblock
   - blocks
   - inodes
   - data region
   - inode table
   - Access methods:
   --    open()
   --    read()
   --    write()   
   - metadata: data about data
   - allocation structures
   
