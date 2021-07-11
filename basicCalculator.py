def calculate(s: str) -> int:
	stack = []
	operand, sign = 0, 1
	res = 0
	
	for ch in s:
		if ch.isdigit():
			operand = (operand * 10) + int(ch)
			
		elif ch == '+':
			res += operand * sign
			sign = 1
			operand = 0
			
		elif ch == '-':
			res += operand * sign
			sign = -1
			operand = 0
			
		elif ch == '(':
			stack.append(res)
			stack.append(sign)
			res = 0
			sign = 1
			
		elif ch == ')':
			res += operand * sign
			res *= stack.pop()
			res += stack.pop()
			operand = 0
			
	return res + operand * sign 


s="(1+(4+5+ +2)-3)+(6+ --8)"

print(calculate(s))
