#Leap Year

'''
Write a Python program to determine if a given year is a leap year or not using the ternary operator.
You are required to:
Read an integer representing the year from the user. Use a ternary operator to check whether the year is a leap year or not. Print YES if the year is a leap year; otherwise, print NO.
Input Format
A single integer Y representing the year.

Output Format
Print "YES" if the year is a leap year. Print "NO" if the year is not a leap year.

Input:2024
Output:Yes
'''

y=int(input())

leap="Yes" if(y%4==0 and y%100!=0 or y%400==0) else "No"
print(leap)

#Output: 2024
         #Yes
         