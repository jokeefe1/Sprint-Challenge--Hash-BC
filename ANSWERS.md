## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

The runtime is: 
O(1) to access and array with the index
O(n) to add or remove from the front
O(1) to add or remove from the back

* What is the worse case scenario if you try to extend the storage size of a dynamic array?

The worst case is that your computer will run out of memory (memory leak).

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

A blockchain consists of blocks of data connected together in a chain (linked list) where each subsequent block contains the cryptographic hash of the block before it. Each new block then makes a hash using the previous block's hash -- doing so makes it cryptographically impossible to insert fake data into the chain, thus allowing the chain of data to be trusted.
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Proof of work is a way to make it economically infeasible to create a fake chain long enough to be considered the trusted chain. This protects the chain from a 51% attack.