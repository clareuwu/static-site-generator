Clare Reinhart - pr1532
# TLB, page faults
1 TLB miss for 0x200000
1 page fault for 0x200000
1 TLB miss for 0x300000
1 page fault for 0x300000
See [[Test other page]]


In order

# Virtual memory
## 1.1
True sometimes. This can happen when a process tries to write to a non-write enable page, but the page is still in the TLB.
## 1.2
True sometimes. If the page isn't in the TLB, the CPU walks the page tables to check for a valid PTE. If one is found, and the PTE_U bit is set (allows user mode processes to access a page), there won't be a page fault raised. 
## 1.3 
True sometimes for the same reason as 1.2, but PTE_U bit not required to be set.
## 1.4
True always. If the PTE is valid and read enabled by user processes, then it should always be loadable.
## 1.5
True sometimes, the PTE_W bit controls whether processes are allowed to store into that page. Must be set to be true.