# 참고하면 도움이 되는 Tips👩🏻‍💻

### Recursion depth 관련 오류 해결
재귀함수 문제에는 꼭 이 코드를 써주자 !! 

```python 
import sys
sys.setrecursionlimit(10 ** 6)
```
-------

### 입력해야 할 값이 많을 때
`input()` 보다 더 빠르게 동작하는 `sys.std.realine()` 사용하기 !!
```python 
import sys
input = sys.stdin.readline         # input에 저장하면 input 함수와 동일하게 사용 가능 
a, b = map(int, input().split())      
```

------

### 무한을 의미하는 값
`int(1e9)` 라고 입력하면 10억을 나타내므로 이걸 사용하자 !!
```python 
INF = int(1e9)
```
