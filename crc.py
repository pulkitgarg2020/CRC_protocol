'''
@Author:	Pulkit Garg
'''

# to perform the XOR operation 
# between two bit strings 
def XOR_operation(num1, num2):
	
	ans = ''
	for i in range(1, len(num2)):
		if num1[i] == num2[i]:
			ans = ans + '0'
		else:
			ans = ans + '1'
	return ans

# to perform XOR division
def XOR_division(m_x, g_x):

	length_XOR = len(g_x)
	num_XOR = m_x[0: length_XOR]

	while (length_XOR < len(m_x)):
		if num_XOR[0] == '1':
			num_XOR = XOR_operation(g_x, num_XOR)
		else:
			num1 = '0'*length_XOR
			num_XOR = XOR_operation(num1, num_XOR)

		num_XOR = num_XOR + m_x[length_XOR]
		length_XOR += 1

	if num_XOR[0] == '1':
		num_XOR = XOR_operation(m_x, num_XOR)
	else:
		num1 = '0'*length_XOR
		num_XOR = XOR_operation(num1, num_XOR)

	return num_XOR

# method to create a message
def sender(m_x, g_x):
	
	m_x = bin(m_x)[2:]
	g_x = bin(g_x)[2:]
	append_m_x = m_x + '0'*(len(g_x) - 1)
	num_XOR = XOR_division(append_m_x, g_x)
	return m_x + num_XOR

# method to check for error in received message
def receiver(p_x, g_x):
	p_x = bin(p_x)[2:]
	g_x = bin(g_x)[2:]
	num_XOR = XOR_division(p_x, g_x)
	checkError = '0'*(len(g_x) - 1)
	if num_XOR != checkError:
		print('Error in transmission since remainder: ' + num_XOR)
	else:
		print('Message received without any errors')

def main():
	ans = ''
	while(ans != '3'):
		ans = input('Enter 1 to send a message, 2 to check error in a received message and 3 to exit ')

		if ans == '1':
			m_x = int(input('Enter the message M(x) bit string: '), 2)
			g_x = int(input('Enter the reference polynomaial G(x) bit string: '), 2)
			p_x = sender(m_x, g_x)
			print("Transmitted String:", p_x)
		elif ans == '2':
			p_x = int(input('Enter the received p(x) bit string: '), 2)
			g_x = int(input('Enter the reference polynomaial G(x) bit string: '), 2)
			receiver(p_x, g_x)

if __name__ == "__main__":
    main()