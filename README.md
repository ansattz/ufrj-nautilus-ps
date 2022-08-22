# :anchor: PS - UFRJ Nautilus :anchor:

## Basic Python
### 1 - List index
*Write a program that tells if the first and last items in a list are the same (it should work for any list, i.e, the number of items is not fixed)*

Applying a simple conditional the function is able to check if the first item is equal to the last one. The statement `l[0] == l[-1]` compares the first item in the list with the last. 

### 2 - Filtering dividers
*Write a program that says the greatest prime divisor of a number given as input*

The first function `primeCheck(n)` collects all divisors of the number given as input. If the number of elements in this list of divisors is different from 2 it is not prime, otherwise it is prime.

The second function `primeDivisor(m)` collects all divisors of the given number and checks which numbers in this list are prime using the (primeCheck) function. Returns a list of prime divisors of the number m.

The third function collects the largest number from the list returned by `primeDivisor(m)`

### 3 - Palindrome Number
*Tell if the given number is a palindrome*

If the given number is equal is equal to itself in reverse, then it is a palindrome. We will compare the number with itself starting from the last index to the first index.

### 4 - Sum of primes
*Give the sum of all prime numbers less than 1000*

With the `primeCheck()` function, the function will collect all prime numbers less than 1000 and return the sum of the list that contains all these primes.

## OOP Python
*Create a Model for the AUVs of UFRJ Nautilus. It must contain the attributes: number of thursters, list with sensors, year of construction, vehicle name, and at least 1 attribute of free choice It must contain methods for:*
- View all AUVs in table
- View robots individually
- Rank robots from newest to oldest
- Must contain another method of free choice
---
The fifth attribute for the Vehicle model was the hydrophone. The methods were thought to be used with a numpy array (to make tables, but the use was discarded and stayed in the main branch). The first method was used to create the table with all AUVs. The `tableOfAUVs()` function has a for loop to get the objects through the list index and use the `infoAUV()` method to create a list of each robot. Finally, the function returns a list with two lists (the two objects defined as v1 and v2).

To show only one robot, the `anAUV()` function receives a parameter to be able to choose which robot will return. This parameter was placed because it was not informed about the possibility of randomness of the function (present any robot, individually). The parameter is default to always show at least one robot.

The ranking in the `newer()` function was done with two for loops. With the birthInfo method, the sortedBirth list receives a list with 2 elements: the first element is the year the robot was created and the second element is the robot. The sortedBirth list is sorted (the smallest number takes the first index, in this case 0) and it is used in the second for loop, except that only the first element of the list will be removed (the year of creation of the robot). The list is returned reversed.

The method chosen was to collect the name and sensors of the robots. The `AUVsensor()` function returns a list with two elements: two lists with two elements each, name and sensor list.

## Basic ROS

The ps_pkg contains a publisher, a subscriber and two topics. The `Accel()` method used in the publisher provides linear and angular velocity vectors in free space. In this case, the x,y and z coordinate data were randomly given using a list with numbers from 0 to 999 and applying `random.choice()` on each coordinate. The subscriber listens to the published topic by the publisher, calculates the norm of both the linear and angular vectors, and publishes the results in two separate topics: Vlinear_norm and Vangular_norm.
