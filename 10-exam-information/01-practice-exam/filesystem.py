from itertools import islice
from abc import ABC, abstractmethod
import re
class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__block_size = block_size
        self.__used_blocks = set()
        self.__available_blocks = set(range(block_count))

    @property
    def block_count(self):
        return self.__block_count
    
    @property
    def block_size(self):
        return self.__block_size
    
    @property
    def used_blocks(self):
        return self.__used_blocks
    
    @property
    def available_blocks(self):
        return self.__available_blocks
    
    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return len(self.__available_blocks | self.__used_blocks)
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        if len(self.__available_blocks) < block_count:
            raise RuntimeError("Insufficient available blocks left.")
        
        allocated_blocks = set(list(self.__available_blocks)[:block_count])
        self.__available_blocks -= allocated_blocks
        self.__used_blocks |= allocated_blocks  #This is a special operator that performs a set union operation.
        
        return allocated_blocks
    
    # with itertools

    # def allocate(self, block_count):
    #     if len(self.__available_blocks) < block_count:
    #         raise RuntimeError("Insufficient available blocks left.")
        
    #     allocated_blocks = set(islice(self.__available_blocks, block_count))
    #     self.__available_blocks -= allocated_blocks
    #     self.__used_blocks |= allocated_blocks
        
    #     return allocated_blocks
        
    def free(self, blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError("Block isn't being used, cannot be freed.")
            self.__used_blocks.remove(block)
            self.__available_blocks.add(block)


    

class Entity(ABC):
    def __init__(self, storage, name):
        if Entity.is_valid_name(name):
            self.__name = name
        else:
            raise RuntimeError("Name is invalid.")
        self.__storage = storage

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not Entity.is_valid_name(new_name):
            raise RuntimeError("New name is invalid.")
        self.__name = new_name
    
    @staticmethod
    def is_valid_name(name):
        if re.fullmatch("^[a-zA-Z0-9.]{1,16}$", name):
            return True
        else:
            return False
    
    # @staticmethod
    # def is_valid_name(name):
    #     return bool(re.fullmatch("^[a-zA-Z0-9.]{1,16}$", name))

    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size

    @abstractmethod
    def clear(self):
        pass




class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__blocks = []

    def grow(self, block_count):
        self.__blocks += self.storage.allocate(block_count)

    @property
    def size_in_blocks(self):
        return len(self.__blocks)
    
    def clear(self):
        self.storage.free(self.__blocks)
        self.__blocks = []




class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__children = []
    
    def add(self, entity):
        self.__children.append(entity)

    @property
    def size_in_blocks(self):
        return sum(child.size_in_blocks for child in self.__children)
    
    def clear(self):
        for child in self.__children:
            child.clear()