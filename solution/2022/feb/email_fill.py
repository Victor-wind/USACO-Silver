'''      
1          2       3        4        5       6      7         8     9       10       11      12
10.6mb    10.6mb   10.6mb   10.6mb  10.6mb  10.6mb  10.8mb  10.7mb  10.7mb  11.6mb  10.9mb  11.9mb
69ms      71ms     68ms     69ms    73ms    78ms    94ms    113ms   119ms   134ms   175ms   189ms
'''

def file_emails(emails:list, M, N, K):
    # folder window is value, email window is index
    folder_win_l, folder_win_h = 1, K
    email_win_l, email_win_h = 0, 0
    last_email_index = [-1]*(M+1)
    cnt = 0
    for i, email in enumerate(emails):
       last_email_index[email] = i
    
    # folder window Low could not move down until no corresponding emails below email window High to move
    # folder window could not 'fall through', once it is moved down, it could not be reached again.
    # emails may 'fall through' into email window when it reaches the bottom.
    # for example: folder window Low is 5, the last email '5' is at index 27, email window High must reach 27
    # if email window High is 26, after folder window Low moves to 6, last email '5' (at index 27) could not be achieved.

    # put processed emails in a list; the emails in window (emails_in_window) should be retrieved from the bottom of processed_emails list
    # if its size < K, then add emails from emails list to emails_in_window
    processed_emails = list()
    while True:
        last_cnt = cnt
        
        # add K emails to the emails window from the bottom of processed_emails
        # note: not all K emails will be added to emails_in_window, if they can be filled into folders
        emails_in_window = list()
        emails_win_cnt = 0
        while len(processed_emails) > 0 and emails_win_cnt < K:
            x = processed_emails.pop()
            emails_win_cnt += 1
            if folder_win_l <= x <= folder_win_h:
                cnt += 1
            else:
                emails_in_window.append(x)
        
        emails_in_window.reverse()
        # if emails_in_window has < K emails, add emails from emails list
        # note: when emails is near the end, emails_in_window may not have full K emails 
        while email_win_h < N and len(emails_in_window) < K:
            x = emails[email_win_h]
            emails[email_win_h] = -1
            email_win_h += 1
            if folder_win_l <= x <= folder_win_h:
                cnt += 1
            else:
                emails_in_window.append(x)

        # now move the emails_in_window so all emails belonging to folder_win_l are processed
        last_index = last_email_index[folder_win_l]

        move_down = True if email_win_h <= last_index else False
        
        while email_win_h <= last_index:
            x = emails[email_win_h]
            emails[email_win_h] = -1
            email_win_h += 1
            if folder_win_l <= x <= folder_win_h:
                cnt += 1
            else:
                emails_in_window.append(x)

        if move_down and email_win_h < N:
            emails_in_window.append(emails[email_win_h])
            email_win_h += 1

        processed_emails += emails_in_window
        folder_win_l += 1
        folder_win_h += 1

        if folder_win_h > M:
            if last_cnt != cnt:
                folder_win_h = M
                folder_win_l = M-K+1
            else:
                break
            
    # print(f' debug2 {email_win_l=} {email_win_h=} {folder_win_l=} {folder_win_h=} {emails=} {cnt=}')
    if cnt == N:
        return 'YES'
    else:
        return 'NO'

T = int(input())
for i in range(T):
    M, N, K = [int(x) for x in input().split()]
    emails = [int(x) for x in input().split()]
    res = file_emails(emails, M, N, K)
    #print(f'{M=} {N=} {K=} {res=}')
    #print(f'{emails=}')
    print(res)
  
