# Exam 2 - Exercise: First Adjustment  

This project implements memory allocation using the **First Fit** strategy.  

## Description  

The program manages the available memory by allocating resources according to the first free block of memory that the process can accommodate. If a process occupies all available memory, it is completely freed.  

Notes: 

- The last used search index is returned.  
- The base and the limit of the new available space are updated:
    - If the process occupied all memory, it is removed from the list.  
- `new_base`: The base address where the process was hosted.  
- `new_limit`: The space limit occupied by the process.  

