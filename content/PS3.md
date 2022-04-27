# q1
A relation R on a set A is antisymmetric if for any a, b in A, and (a,b) valid relation, that (b,a) not a valid relation. By definition, R^-1 takes all valid (a,b) in R and has all (b,a) valid instead. For an element to be in R cap R^-1, while R is symmetric, (a,b) must be in R and (b,a) must be in R^-1, which implies a=b, thus all lists in R cap R inv must be in the form (a,a) for some elem a, making it equal to the identity relation. 

A relation $R$ on a set $A$ is antisymmetric if for any distinct ($a,b$) in $A$ and ($a,b$) is a valid relation on $R$, then ($b,a$) is not a valid relation. 
# q2
To be equivalence relation, must be reflexive, symmetric, and transitive. 
Reflexive: for all x in A, we have x R x. For any a in Z9, a^2 - a^2 = 0, 9 divides into 0, so relation is reflexive

Symmetric: Let x,y in Z9 and x R y, then x^2 teq y^2 (mod 9), which means y^2 teq x^2 (mod 9), and that y R x, so R is symmetric

Transitive: Let x,y,z in Z9 and x R y and y R z. Then x^2 = y^2 (mod 9) and y^2 = z^2 (mod 9), so x^2 = y^2 = z^2 (mod 9), thus x R z and R is transitive. 

Equivalence classes:
[0] = {0, 3, 6}
[1] = {1, 8}
[2] = {2, 7}
[4] = {4, 5}

(b)
Reflexive: For any a in Z9, a^3 - a^3 = 9, 9 divides into 0, so reflexive.

Symmetric: let x,y in Z9 and x R y, then x^3 = y^3 (mod 3) which means y^3 = x^3 mod 9 so that y R x, so R is symmetric

Transitive: Let x,y,z in Z9 and x R y and y R z. then x^3=y^3 mod 9 and y^3 = z^3 mod 9 so x^3 = y^3 = z^3 mod 9, thus x R z and R is transitive.

[0] = {0, 3, 6}
[1] = {1, 4, 7}
[2] = {2, 5, 8}
# q3
(a) 11! / 1! 4! 4! 2!

(b) 10! / 2! 3! 3! 1! 1!

(c) 12! / 4! 1! 3! 1! 1! 1! 1!

# q4
40! / 5! ^ 8 x 8!
# q5
{1,2,3,4}
{1}{2,3,4}
{2}{1,3,4}
{3}{1,2,4}
{4}{1,2,3}
{1,2}{3,4}
{1,3}{2,4}
{1,4}{2,3}

For either set, choosing a pair of subsets whose union is a set, with 2^n possible subsets, we can choose 2^n - 2 (nonempty and not the entire set) sets for the first set, and 1 way to choose the second set (all the elements that weren't in the first set). Divide this by 2, because we don't care if some distinct set is the first set or the second set, giving 2^n-1 - 1

so (a) is 2^3 - 1 = 7
(b) 2^99 - 1
# q6
{1,2,3,4,5} 
Want a set with 3 elements, each of which are either 1 element from the original set or 2 of those elements. repeats are okay.
each element can be any 5 of the original set, or binom 5 2 = 10 choices for 2 element sets, so 15 total possible choices for any of the 3 elements. don't care about the order so 15^3 choices

If no repeat digits, there are 15 choices for the first element, then either
# q7
There are a number of equivalence relations equal to the number of partitions. 

```
R1 = 1,1 2,2 3,3
R2 = 1,1 2,2 3,3 1,2 2,1
R3 = 1,1 2,2 3,3 1,3 3,1
R4 = 1,1 2,2 3,3 2,3 3,2
R5 = 1,1 2,2 3,3 1,2 2,1 1,3 3,1 2,3 3,2
```

(b)
```
1,1 2,2 3,3 4,4
1,1 2,2 3,3 4,4 1,2 2,1
1,1 2,2 3,3 4,4 1,3 3,1
1,1 2,2 3,3 4,4 1,4 4,1
1,1 2,2 3,3 4,4 2,3 3,2
1,1 2,2 3,3 4,4 2,4 4,2
1,1 2,2 3,3 4,4 3,4 4,3
```

# q8
Assume there is integers $a$ and $b$ such that $21a+30b=1$. Then there exists some integer $k=7a+10b$, and $3k=1$. This implies that $k=1/3$. But because $a, b$ are integers, there is no way to multiply or add them with other integers to produce a ratio, contradicting the statement and proving it wrong.
# q9
Assume $a^2+b^2=1, a+b\leq1$. Square to get $a^2+2ab+b^2\leq 1$ Because $a^2+b^2=1$, can rewrite as $1+2ab\leq 1$. This implies $2ab\leq 0$. However, this isn't possible because $a,b>0$, so we disprove $a+b\leq 1$, meaning it must be $>1$. 
# q10
If for all positive integers $n$ the statement is true, for $n=1$, $1\cdot 1! = 2!-1$, which is true. 
Suppose FSOC the statement is false
Let $X\subseteq N$ be the set of counterexamples for the statement. $X$ contains a smallest element. We've shown the statement is true for $n=1$, so smallest element must be $>1$. 
Call the smallest element in $X, z$. since $z>1, z-1 \notin X$. 
$$\sum_{k=1}^{z-1}k\cdot k!= z!-1  $$
Add $z\cdot z!$ to both sides:
$$\sum_{k=1}^{z}k\cdot k!= (z+1)!-1  $$
Therefore, the original statement is true. 