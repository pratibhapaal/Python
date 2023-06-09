# -*- coding: utf-8 -*-
"""Python_Intermediate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rd-LCLi9y4X2At2_0aEmm2sFI6mBIwy-

Problem: Given a sorted array A of size N. Find the number of elements that are less than or equal to B.

NOTE: Expected Time Complexity O(log N)
"""

def solve(self, A, B):
    result=0
    for i in A:
        if i<=B:
            result+=1
    return result

"""Problem: Given a sorted array A of size N and a target value B, return the index of the target in the list (0-based indexing) if the target is found.
If not found, return the index where it would be if it were inserted.

NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.
"""

def searchInsert(self,A, B):
  start=0
  end=len(A)-1
  for i in range(len(A)):
      mid=(start+end)//2
      if A[mid]==B:
          return mid
      elif A[mid]>B:
          end=mid-1
      elif A[mid]<B:
          start=mid+1
  return start

"""Problem: Given an unsorted list of integers. Return the sum of the first and last elements of the list after sorting the first k elements of the list using Bubble Sort."""

def bubbleSort(arr,k):
    res=0
    # no. of passes/round
    for i in range(k-1):
        # no. of iteration for swapping
        for j in range(k-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    res=arr[0]+arr[-1]
    return res

"""Problem: Given a list of strings, use selection sort to sort these strings in lexicographical order."""

def selectionSort(lis):
    n=len(lis)
    for i in range(n-1):
        min_val=i
        for j in range(i+1,n):
            if lis[min_val]>lis[j]:
                min_val=j
        if lis[min_val]!=i:
            lis[min_val],lis[i]=lis[i],lis[min_val]
    return lis

"""Problem: Given a list of numbers, perform k iterations of insertion sort on it and return the element present at the center.

Note:
For a list of length n, return the n//2th indexed element after applying k iterations of insertion sort.
"""

def insertionSort(arr,k):
    n=len(arr)
    for i in range(1,k+1):
        insert=i
        j=i-1
        while j>=0:
            if arr[j]>arr[insert]:
                arr[j],arr[insert]=arr[insert],arr[j]
            else:
                break
            insert=j
            j-=1
    return arr[n//2]

"""Problem: Write a recursive function that returns the number of occurrences of "hi" in the string passed as a parameter to the function."""

def countHi(s, count=0):
    if len(s)==0:
        return count
    if s[0:2]=="hi":
        count=count+1
        return countHi(s[2:],count)
    else:
        return countHi(s[1:],count)

"""Problem: Write a program to calculate the sum of the positive integers of the series n + (n-2) + (n-4)..... (until n-x ≥ 0)."""

def sum_series(n):
    if n<=0:
        return 0
    return n+sum_series(n-2)

"""Problem: Write a recursive program to calculate the harmonic sum of the first n numbers.

Note: The harmonic sum is the sum of reciprocals of the positive integers. (Round the sum to 3 decimal places)
"""

def harmonic_sum(n):
    if n<=0:
        return 0
    return round((n**-1)+harmonic_sum(n-1),3)

"""Problem: Write a recursive function to return the reverse of a given number passed as an argument."""

def rev(n, temp=''):
  if n==0:
      return temp
  rem=str(n%10)
  return rev(n//10,temp+rem)

"""Problem: Given the value of nPr and nCr for a certain n and r, find the value of r.
Note: In case no value of r exists return -1.
"""

import math
def valueOf(perm,com):
    R=perm//com
    i=1
    while i!=R:
        if math.factorial(i)==R:
            return i
        i=i+1
    return-1

"""Problem: Create a class Bill and initialize it with the details: previous and current meter readings. Create a function total_bill() inside the Bill class which returns the total bill based on the following criteria:

1. For the first 100 units consumed: 3.5 rs/unit

2. For the next 100 units consumed: 5 rs/unit

3. For remaining units consumed: 8 rs/unit

4. Meter Charges: 150 rs (It's included only once but is mandatory)
"""

class Bill():

    def __init__(self, prev_read, cur_read):
        self.prev_read=prev_read
        self.cur_read=cur_read
            
        
    def total_bill(self):
        total=150.0
        actual=self.cur_read-self.prev_read
        if actual<=100:
            total+=actual*3.5
            return total
        if actual>=100:
            total+=100*3.5
            actual-=100
        if actual>=100:
            total+=100*5
            actual-=100
        if actual>=0:
            total+=actual*8
            actual-=100
        
        return total

"""Create a class Student and initialize it with the following class variables:
marks in subject 1
credit of subject 1
marks in subject 2
credit of subject 2

Create a function gradepointaverage() for the Student class which computes the GPA rounded to two decimals, based on the following criteria of points in a subject :

1. If marks>=90:10 points
2. If 90>marks>=75: 9 points
3. If 75>marks>=60: 8 points
4. If 60>marks>=45: 7 points
5. If marks<45: 0 points

GPA =  
creditofsubject1+creditofsubject2
(pointsinsubject1∗creditofsubject1+pointsinsubject2∗creditofsubject2)
​

The points in a subject should be calculated according to the criteria mentioned in the question.
Also, implement a special zero case to handle when credits of both subjects are 0, return "Zero credits for both subjects".

"""

class Student():
    
    def __init__(self, marks1,marks2,credits1, credits2):
        self.marks1=marks1
        self.marks2=marks2
        self.credits1=credits1
        self.credits2=credits2
   
    def grade_point_average(self):

        if self.credits1==0 and self.credits2==0:
            return "Zero credits for both subjects"
        
        point1= None
        if self.marks1>90:
            point1=10
        elif self.marks1<=90 and self.marks1>=75:
            point1=9
        elif self.marks1<75 and self.marks1>=60:
            point1=8
        elif self.marks1<60 and self.marks1>=45:
            point1=7
        elif self.marks1<45:
            point1=0

        point2= None
        if self.marks2>90:
            point2=10
        elif self.marks2<=90 and self.marks2>=75:
            point2=9
        elif self.marks2<75 and self.marks2>=60:
            point2=8
        elif self.marks2<60 and self.marks2>=45:
            point2=7
        elif self.marks2<45:
            point2=0


        gpa=((point1*self.credits1)+(point2*self.credits2))/(self.credits1+self.credits2)
    
        return round (gpa,2)

"""Problem: Complete the classes Smaller and Larger.

Smaller class gets instantiated when the argument of the function (a:string) has a length smaller than 6 otherwise Larger is instantiated.
Both the classes have the same two methods, display() printing the type of a (class), and
evaluate() printing the number of vowels if the Name is Smaller otherwise it prints the number of consonants.
"""

class Smaller:
    def __init__(self,a):
        self.string=a
    
    def display(self):
        print("The type of Name is smaller")
    
    def evaluate(self):
        ans=0
        
        s=set('aeiou')
        for i in a.lower():
            if i in s:
                ans=ans+1
        print(ans)
        
class Larger:
    def __init__(self,a):
        self.string=a
    
    def display(self):
        print("The type of Name is larger")
    
    def evaluate(self):
        ans=0
        
        s=set('aeiou')
        for i in a.lower():
            if i not in s:
                ans=ans+1 
        print(ans)

def main(a):

    if len(a)<6:
        obj=Smaller(a)
        obj.display()
        obj.evaluate()
    else:
        obj=Larger(a)
        obj.display()
        obj.evaluate()

"""Problem: Complete the Python function second_lowest() to find the second-lowest grade of students from the given names and grades of each student using lists and lambda function. For the input, the number of students, names, and the grades of each student were given."""

def second_lowest(students, scores):
    '''
    input:
    students -> a list of students
    scores -> list of the scores, with each score being that of the ith student
    
    output:
    student_data -> 2d list of data, with each inner list having name of student as 1st and score of 2nd as second element respectively
    second_low_score -> the second lowest score
    second_names -> list of students with score same as second lowest score, in the same order as in the students list
    '''
    
    student_data, second_low_score, second_names = None, None, None
    student_data=list(map(list,zip(students,scores)))
    new=sorted(student_data,key=lambda x: x[1])
    scores=sorted(set(scores))
    second_low_score=scores[1]
    second_names=[]
    for x,y in student_data:
        if y==second_low_score:
            second_names.append(x)
    return student_data, second_low_score, second_names

"""Problem: Given a list of strings of varying lengths, complete the python function to sort the list of strings based on their lengths and return the sorted list.

Note: In case 2 strings have the same length, they are sorted in ascending order of their lexicographic index.
"""

def sort_strings(str_list):
  s=sorted(str_list)
  res=sorted(s,key=len)	
  return res

"""Problem: Given a list of email addresses, return a list containing only valid email addresses in lexicographical order. A Valid email address must follow the following rules:
1. It is of the form user@domain.com, user or domain can't be empty
2. It must have a single @ in the address.
3. The maximum length of the name before @ should be 20.
"""

def check(emails):    
    verified_lex = []
    new_emails=sorted(list(filter(lambda x:x.count('@')==1,emails)))
    l=[]
        
    for i in new_emails:
        l=i.split('@')
        if l[0]==0 or len(l[0])>20 or l[1]==0:
            continue
        verified_lex.append(i)

    return verified_lex