class Solution(object):
    def evalRPN(self, tokens):
        st = []
        for i in tokens:
            if i not in '+-*/':
                st.append(int(i))
            else:
                b = st.pop()
                a = st.pop()
                if i == '+':
                    st.append(a + b)
                if i == '-':
                    st.append(a - b)
                if i == '*':
                    st.append(a * b)
                if i == '/':
                    st.append(int(float(a) / b)) 
        return st[-1]
