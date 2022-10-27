from datetime import datetime

with open('lifeguards.in') as f:
    lines = f.readlines()

N = int(lines[0])

cows = [ [int(x) for x in lines[i].split()] for i in range(1, N+1)]
max_covered = 0

s1= datetime.now()

events_1 = [ (cow[0], i, 1) for i, cow in enumerate(cows)]
events_2 = [ (cow[1], i, -1) for i, cow in enumerate(cows)]

events = events_1+events_2
events.sort()

e1= datetime.now()
print(f'time pass: {e1-s1}')

cows_set = set()
total_covered = 0
cow_unique_covered = [0] * N 

#print(f'{events}')

for e in events:
    event_time, cow_id = e[0], e[1]

    # some cows on duty, the time [last_event_time, event_time] is covered
    if cows_set:
        total_covered += (event_time - last_event_time)
       
    # only one cow cover the time [last_event_time, event_time]
    if len(cows_set) == 1:
        cows_id = list(cows_set)[0]
        cow_unique_covered[cows_id] += (event_time - last_event_time)
        
    if cow_id in cows_set:
        cows_set.remove(cow_id)
    else:
        cows_set.add(cow_id)
        
    last_event_time = event_time

e2= datetime.now()
print(f'time pass: {e2-s1}')

# process each cows, find how much time it uniquely cover
for i, cow in enumerate(cows):
    covered = cow[1]-cow[0]
    unique_covered = cow_unique_covered[i]
    max_covered = max(max_covered, total_covered-unique_covered)

print(f'{max_covered}')

with open('lifeguards.out', 'w') as f:
    f.write(f'{max_covered}\n')
