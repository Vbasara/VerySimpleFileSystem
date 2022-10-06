#Vladimir Basarab VSFS Program Fall 2022

#Create a list that resembles the entire VerySimpleFileSystem
#-----------------------------------------------------
#block
#inode
#	Acess methods:
#	    open()
#	    read()
#	    write()
#superblock
#data region: 56/64 is data region
#metadata: data about data
#allocation structures.
#-----------------------------------------------------


from code import InteractiveConsole
from lib2to3.pgen2 import token


#creating 64 blocks for our filesystem
file_system = []


BLOCK_SIZE = 4096
INODE_BLOCKS = 5
DATA_BLOCKS = 56

#method that populates the virtual disk with blocks
def allocate_blocks(disk, num_of_blocks, block_size):
    for i in range(0, num_of_blocks):
        #create another list within the 'filesystem' to resemble blocks
        new_block = []                      
        #4096 is the number of bytes per block
        for i in range(0, block_size):
            #adding individual 
            new_block.append(0)
        #add this 'block' list to the filesystem
        #disk.append(bytes(new_block))
        disk.append(new_block)
 
# formating the disk while store metadata in the superblock
def format(disk, inode_blocks, data_blocks, block_size):
    #need total number of blocks
    total_blocks = 3 + inode_blocks + data_blocks
    allocate_blocks(disk,total_blocks, block_size)
    #implement superblock,its the first block on the disk
    superblock = disk[0]
    superblock[0] = inode_blocks
    superblock[1] = data_blocks

#iterates through the inodes to find the file specified
#otherwise it returns the index of an empty_inode
def open(disk,file_path):
    #remove the whitespaces from the filepath
    file_path = file_path.strip()
    superblock = disk[0]
    #get the number of inode blocks
    inode_blocks = superblock[0]
    empty_inode = -1
    #iterate through inodes
    for i in range(3, 3 + inode_blocks):
        inode = disk[i]
        ifp = inode[0:256]
        ifp_b = bytes(ifp)
        ifp_str = ifp_b.decode("UTF-8")
        #find the empty inodes
        if ifp_str == '':
            empty_inode = i
        if ifp_str == file_path:
            return i
    
    file_path_bytes = file_path.encode('UTF-8')
    inode = disk[empty_inode]
    for i in range(0,len(file_path_bytes)):
        inode[i] = file_path_bytes[i]
    return empty_inode


def read_to_buf(disk, file_path, buf):
    file_path = file_path.strip()
    superblock = disk[0]
    #get the number of inode blocks
    inode_blocks = superblock[0]
    empty_inode = -1
    #iterate through inodes
    for i in range(3, 3 + inode_blocks):
        inode = disk[i]
        ifp = inode[0:256]
        ifp_str = bytes(ifp).decode('UTF-8').strip()
        #find the empty inodes
        if ifp_str == file_path:
            inode_offset = 256
            for k in range(len(buf)):
                if inode_offset < BLOCK_SIZE:
                    buf[k] = inode[inode_offset]
                else:
                    break

def write(disk, inode, data):
    #check if the disk is full
    if inode == 0:
        raise

    data_length = len(data)
    data_length_bytes = data_length.to_bytes(1, 'little')

    #write to the inode
    for i in range(0,len(data_length_bytes)):
        inode[i + 256] = data_length_bytes[i]

    num_blocks_needed = int(data_length/BLOCK_SIZE + 1)

    # finding a empty data block /reference variable
    data_table = disk[2]
    blocks_found = []

    # loop to find empty data blocks to use. raise if not enough available blocks for files
    for i in range(BLOCK_SIZE):
        if data_table[i] == 0:
            blocks_found.append(i+8)
            data_table[i] = 1
        if len(blocks_found) >= num_blocks_needed:
            break
    if len(blocks_found) < num_blocks_needed:
        raise
    
    # Write to the Data block
    datablock_counter = 0
    block_offset = 0
    for i in data:
        if block_offset > BLOCK_SIZE:
            raise
        if block_offset == BLOCK_SIZE:
            datablock_counter += 1
            block_offset = 0

        if block_offset < BLOCK_SIZE:
            disk[blocks_found[datablock_counter]][block_offset] = i
            block_offset += 1


print("test")

format(file_system, INODE_BLOCKS, DATA_BLOCKS, BLOCK_SIZE)
inode = open(file_system, "test.vlad")
print(inode)
#inode = open(file_system, "test.vlad")
#print(inode)

write(file_system, file_system[3], [2,2,2,2,21])
write(file_system, file_system[4], [1,1,1,1,1,1])

buf = [0] * 256
read_to_buf(file_system, "test.vlad", buf)
print(str(buf))
print("another tester")

