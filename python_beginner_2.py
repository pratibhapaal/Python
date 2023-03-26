# -*- coding: utf-8 -*-
"""Python_Beginner_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16mqxhsz5H3qtUazP5yvCcOmdgP2X8ytj

Problem: Write a program to find the difference between the sum of all even elements and the sum of all odd elements from the given list.
"""

def even_odd(lst):
    sum_odd=0
    sum_even=0
    for i in lst:
        if i%2==0:
            sum_even=sum_even+i
        else:
            sum_odd=sum_odd+i
    return sum_even-sum_odd

"""Problem: Write a function to check if the input list has consecutive duplicate elements or not.
Return True if there are consecutive duplicate elements in the list else return False.

Here by consecutive duplicates, we mean duplicates that are present at consecutive indices in the array
"""

def duplicate(ls,n):
    ans = False
    for i in range(1,n):
        if ls[i]==ls[i-1]:
            ans=True
    return ans

"""Problem: Write a program for a given integer x and a list ls to return the first multiple of x that occurs in the list, and if there isn’t any multiple of x in the list then return -1."""

def first_multiple(ls,x):
    ans = -1
    for i in ls:
        if i%x==0:
            ans=print(i)
        else:
            pass
    return ans

"""Problem: You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists."""

def solve(self, A):

    a=list(set(A))
    largest=max(a)
    a.remove(largest)
    res=-1
    if len(a)!=0:
        res=max(a)
    return res

"""Problem: Write a program that returns the list of elements that are present in the given list and are divisible by 5 and 7."""

def divisible(lst):
  elements=[]
  for i in lst:
      if i%5==0 and i%7==0:
          elements.append(i)
      else:
          pass
      
  return elements

"""Problem: Given a sorted integer array A, and an integer B. Find the first and last index of B in A.
It is guaranteed that B exists in A. Return an array C of size 2, where C[0] is the first index of B in A and C[1] is the last index of B in A.
"""

def solve(self, A, B):
    a=[]
    for i in range(len(A)):
        if A[i]==B:
            a.append(i)
    return [a[0],a[-1]]

"""Problem: You are given a sorted array of A and an integer B. Return an array of size 2, where the first element is the ceil of B and the second element is the floor of B.

Ceil is the largest number greater than or equal to B and is present in the array A.
Floor is the largest number smaller than or equal to B and is present in the array A.
"""

def solve(self, A, B):
        ceil=-1
        floor=-1
        for i in A:
            if i==B:
                ceil=i
                floor=i
                break
            elif i>B:
                ceil=i
                break
            elif i<B:
                floor=i

        return (ceil,floor)

"""Problme: Given an array A, check if it is sorted in ascending order or not. Return 1 if array is sorted else return 0."""

def solve(self, A):
    res=0
    n=len(A)
    for i in range(1,n):
        if A[i]<A[i-1]:
            return 0
    return 1

"""Problem: You are given two matrices A & B of equal dimensions and you have to check whether two matrices are equal or not.

NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j in the given range.
"""

def solve(self, A, B):
    a=len(A)
    b=len(A[0])
    s=0
    for i in range(a):
        for j in range(b):
            if A[i][j]!=B[i][j]:
                return 0
    return 1

"""Problem: You are given a 2D integer matrix A, return a 1D integer array containing row-wise sums of original matrix."""

def solve(self, A):
    s=0
    lst=[]
    for i in range(len(A)):
        s=sum(A[i])
        lst.append(s)

    return lst

"""Problem: You are given lowercase string (A) and you have to tell the count of vowels and consonants in it."""

def solve(self, A):
    vowels=0
    consonants=0
    for i in A:
        if i in "aeiou":
            vowels=vowels+1
        else:
            consonants=consonants+1
    return (vowels, consonants)

"""Problem: You are given lowercase string (A) and you have to return after reversing that."""

def solve(self, A):
    return(A[::-1])

"""Problem: You are given a character string A, having length N and an integer ASCII code B.

You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or report that it does not exist.
"""

def solve(self, A, B):
    res=-1
    for i in A:
        if ord(i)==B:
            res=A.index(i)
        else:
            res
    return res

"""Problem: You are given a character string A and two integer ASCII codes B and C.

You have to find and replace all the occurrences of the character having ASCII code equal to B with character having ASCII code equal to C and return the resultant string.
"""

def solve(self, A, B, C):
    for i in A:
        if ord(i)==B:
            A=A.replace(i,chr(C))
    return A

"""Problem: Given the input date in DD/MM/YYYY format as a string, write a function that returns the converted date in the string formats MM/DD/YYYY and YYYY/MM/DD and return the new date formats."""

def date_format(date):
    d=date.split('/')
    return d[1]+'/'+d[0]+'/'+d[2],d[2]+'/'+d[1]+'/'+d[0]

"""Problem: Write a program to divide a given tuple into two tuples that contain even and odd indexed elements of the original tuple. Print both these tuples in the given output format."""

def odd_even_split_tuple(tup):
    t=list(tup)
    n=len(t)
    odd=[]
    even=[]
    for i in range(n):
        if i%2==0:
            odd.append(t[i])
        else:
            even.append(t[i])
    print('Odd:',tuple(odd))
    print('Even:',tuple(even))

"""Problem: Write a function to print out the frequency of all the unique elements present in a given tuple."""

def unique_count(tup):
    lst=[]
    for i in tup:
        if i not in lst:
            lst.append(i)
            print(i,":",tup.count(i))

"""Problem: Given two sentences, write a program to return the sum of the total number of unique words from each sentence."""

def set_operation(sent1,sent2):
    a=len(set(sent1.split()))
    b=len(set(sent2.split()))
    return a+b

"""Problem: Write a program to return the number of days in a specific month in a non-leap year. You are given the index of the month. Assume that this indexing starts from 1. For eg: 1 for January, 2 for February, ....so on till 12 for December."""

def no_of_days(n):
    lst1=[1,3,5,7,8,10,12]
    lst2=[4,6,9,11]
    if n==2:
        ans=28
    elif n in lst1:
        ans=31
    elif n in lst2:
        ans=30   
    return ans

"""Problem: Write a function to check whether a given number n as an input to the function is a perfect number or not. If the given integer is a perfect number return 1 else return 0."""

def perfect_number(n):
    sum1=0
    res=0
    for i in range(1,n):
        if n>=0 and n%i==0:
            sum1=sum1+i
        if n==sum1:
            res=1
    return res

"""Problem: You are given an integer T (Number of test cases). For each test case, You are given a dictionary as input, reverse the dictionary (make the keys as values and values as keys), and return the inverted dictionary."""

def invert_dict(data):
    res = {}
    res={v:k for k,v in data.items()}
    return res

"""Problem: You are hired by a Malibu club and are given a task to determine who can enter the club. Filter the guests who are 18 plus age using the given information about each individual. The end product we want is a list of 'You can Enter' or 'No Entry for you'.

Note: 2022 should be considered the current year and it should be used for calculating the age of guests.

Sample string: 'M2004Sam' where M means male or female, 2004 is the date of birth and Sam is the name of the guest.
"""

def club_entry(input_list):
    answer = []
    for i in input_list:
        if int(i[1:5])<2004:
           ele='You can Enter'
        else:
            ele='No Entry for you'
        answer.append(ele)
    return answer