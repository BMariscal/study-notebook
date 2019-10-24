----
[x] Hash Table
-------------

| Algorithm      | Average	Worst case |
| ----------- | ----------- |
| Space	O(n)    | O(n)      |
| Search	O(1)  | O(n)      |
| Insert	O(1)     | O(n)      |
| Delete	O(1)   | O(n)      |


	□ Dictionary: Abstract Data Type (ADT)
		○ Maintain set of items, each with a key
			§ Insert(item)
			§ Delete(item)
			§ Search(key) 
	□ How to handle hash table collisions:
		○ Chaining = linked list.	
		○ Open Addressing= All entry records
		 are stored in the bucket array itself.

------------

[Understand Hash Functions](https://archive.org/details/0102WhatYouShouldKnow/06_02-understandingHashFunctions.mp4)

[Creating Hash Tables](https://archive.org/details/0102WhatYouShouldKnow/06_03-usingHashTables.mp4)

[Default Hash Behavior](https://archive.org/details/0102WhatYouShouldKnow/06_04-supportingHashing.mp4)

[Coursera](https://www.coursera.org/learn/data-structures/home/week/4)

[Coursera](https://www.coursera.org/learn/data-structures-optimizing-performance/home/week/6)

[Ransom Note](https://www.hackerrank.com/challenges/ctci-ransom-note/problem)

----
[X] Bitwise Operators
-------------
    2^0, 2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7  = 8 bits = 1 byte

     2^7  2^6 2^5 2^4  2^3 2^2 2^1 2^0
    | 128| 64 | 32| 16 | 8 | 4 | 2 | 1 |

Set Bit
------
``````
def set_bit(x, position):
  mask = 1 << position
  return x | mask

  x = 00000110
  position = 00000101
  mask = 00100000



calculation:
x 00000110
mask 00100000
output = 00100110

``````
Clear Bit
------
``````
sef clear_bit(x, position):
  mask = 1 << position
  return x & ~mask


x 00000110
position 00000010
mask 00000100
~mask 11111011


      x 00000110
& ~mask 11111011

         00000010

``````

Flip Bit
------
``````
def flip_bit(x, position):
  mask = 1 << position
  return x ^ mask


x 01100110
position 00000010
mask 00000100


x      01100110
^ mask 00000100

----------------
      01100010




``````

Left Shift
-------

Shift the binary digits by n, pad 0's on the right    


Each shift is a multiply by 2 (unless there's overflow)



Right Shift
--------

Shift the binary digits by n, pad 0's on the left

Each shift is a divide by 2 with round towards negative infinity




Is Bit Set
------

``````

def is_bit_set(x, position):
	shifted = x >> position
	return shifted & 1
	

X        01100110           00000011        shifted 
Position 00000101         & 00000001              1
Shifted   00000011          00000001    

``````
	
BIT TRICKS
--------
``````
Even: check the right-most bit

(x & 1) == 0


CHECK IF POWER OF TWO

                     1000
(x & x-1) == 0    &  0111
                     0000
``````
Exercise
---------
Write a function to count the number of
Bits that are different between two numbers
``````
def num_diff_bits(a, b): 
	count = 0 
	diff = a ^ b
	while diff != 0:
		 if diff & 1:
			 count += 1 
		diff = diff >> 1 
	return count

``````
http://bits.stephan-brumme.com/
http://h14s.p5r.org/2012/09/0x5f3759df.html

http://en.wikipedia.org/wiki/Fast_inverse_square_root


https://bits.stephan-brumme.com/


https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/

https://graphics.stanford.edu/~seander/bithacks.html

``````
>>> bin(0b1111 << 1)
'0b11110'
>>> bin(0b1111 << 2)
'0b111100'
>>> bin(0b1111 << 3)
'0b1111000'
>>> bin(0b1111 << 4)
'0b11110000'
``````

* https://wiki.python.org/moin/BitwiseOperators
* https://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer
* https://bits.stephan-brumme.com/swap.html
* https://bits.stephan-brumme.com/absInteger.html
* https://www.youtube.com/watch?v=Hzuzo9NJrlc&feature=youtu.be
-------------
[ ] Trees
-------------