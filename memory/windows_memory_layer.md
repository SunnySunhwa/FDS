## physical memory
  - hardware reserved
  - in use
  - modified
  - standby
  - free
---
## physical memory
  - available
    - standby + free
  - cached
    - modified + standby
  - total
    - installed - hardware reserved
  - installed
---
## virtual memory
  - total virtual memory
  - available virtual memory
  - committed
    - total - available
  - page file in use
    - committed(virtual in use) - in use
---
## cached
  - modified
    - not in use
    - if needed, written to the page file on hard disk
    - then, turned into free 
  - standby
    - when a process finished, unmodified to standby
    - if requests, look up standby -> cache of recently used file 
    - if needed, released to free
---
