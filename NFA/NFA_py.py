
# coding: utf-8

# In[1]:


import numpy as np


# ![title](NFA_png.png)

# In[2]:


class NFA():
    def __init__(self, Q, sigma, delta, start_state, F):
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.start_state = start_state
        self.F = F
        self.current_state = start_state
        self.string = ''
        self.current_state_set = [start_state]
        self.ans=''
        
    def input_string(self, string, ans=''):
        for current_state in self.current_state_set:
            self.current_state = current_state
            self.string = string
            self.ans = ans

            if(len(self.string) == 0):
                if(self.current_state in self.F):
                    #print('接受！！！！')
                    print(self.ans+self.current_state)
                    return 1
                    continue
                else:
                    #print('该字符串遍历完成未被接受')
                    continue
            try:
                delta[Q.index(self.current_state)][sigma.index(string[0])]
            except Exception:
                #print('不存在该字符')
                continue
            
            if(delta[Q.index(self.current_state)][sigma.index(self.string[0])] != ['null']):
               # print(self.current_state,self.string[0],self.string,delta[Q.index(self.current_state)][sigma.index(string[0])])
                self.current_state_set = delta[Q.index(self.current_state)][sigma.index(self.string[0])]
                self.ans += self.current_state + ' '+ self.string[0] + ' '
                self.string = self.string[1:]
                self.input_string(self.string,self.ans)
                self.current_state = current_state
                self.string = string
                self.ans = ans
            
            if(delta[Q.index(self.current_state)][sigma.index('null')] !=  ['null']):
                #print(self.current_state,'null',self.string,delta[Q.index(self.current_state)][sigma.index('null')])
                self.current_state_set = delta[Q.index(self.current_state)][sigma.index('null')]
                self.ans += self.current_state +' null '
                self.input_string(self.string,self.ans)
                self.current_state = current_state
                self.string = string
                self.ans = ans


# In[17]:


Q = ['q1', 'q2', 'q3', 'q4']
sigma = ['0','1','null']
delta = [[['q1'], ['q1','q2'], ['null']],
 [['q3'], ['null'], ['q3']],
 [['null'], ['q4'], ['null']],
 [['q4'], ['q4'], ['null']]]
start_state = 'q1'
F = ['q4']
N1 = NFA(Q,sigma,delta,start_state,F)
print('所有可能的状态转移情况')
N1.input_string('1111')

