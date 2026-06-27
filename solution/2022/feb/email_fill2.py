from collections import deque

# The key observation: folders only move down; however emails may 'fall down' when its window is at the end
# So for given folder i, only move it out of folder window after the email window reaches the last email 
# associated with folder i. 

def solution(M, N, K, emails):
     m_index = [-1] * (M+1)
     for i in range(N): # get the last index of email_num
          email_num = emails[i]
          m_index[email_num] = i

     email_index = 0
     top_email_lst = list()
     dq = deque()
     for folder_top in range(1, M-K+1):
          # current folders window is [folder_top, folder_top+K)
          last_index = m_index[folder_top] # email index should reach last_index
          while (email_index <= last_index) or (email_index < N and len(dq) < K):
               email = emails[email_index]
               email_index += 1
               
               # the order is important, need to put email into dq first to update the window, 
               # then compare or remove it
               dq.append(email)
               if len(dq) > K: # reduce email window
                    top_email_lst.append(dq.popleft())                    
               
               if folder_top <= email < (folder_top + K): # put email in folder and remove it from dq window
                    dq.pop()                                  

          # if reaching the end, move emails from top_email_lst into dq window
          while (email_index >= N and len(top_email_lst) > 0 and len(dq) < K):
               item = top_email_lst.pop()
               if folder_top > item or (folder_top + K) <= item:
                    dq.appendleft(item)
               
          # move folders window down by 1: move emails in dq into (folder_top + K), if possible
          dq = deque(x for x in dq if x != (folder_top + K))

     # now the folders window is at the bottom [M-K, M-1], could not change anymore
     # check whether the emails in top_email_lst, dq, emails[email_index:] can be moved into folders window
     # print(f'{top_email_lst=} {list(dq)=} {emails[email_index:]=}')
     for x in (top_email_lst + emails[email_index:] + list(dq)):
          if x < (M - K + 1):
               return False     
     
     return True


T = int(input())
results = list()
for _ in range(T):
     M, N, K = [int(x) for x in input().split()]
     emails = [int(x) for x in input().split()]
     results.append(solution(M, N, K,emails))

for x in results:
     if x:
          print('YES')
     else:
          print('NO')
