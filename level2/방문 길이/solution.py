def solution(dirs):
    answer = 0
    visited = set()
    x,y,mx,my = 0,0,0,0
    
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            my += 1
                   
        elif dirs[i] == 'L':
            mx -= 1
                     
        elif dirs[i] == 'R':
            mx += 1
        
        elif dirs[i] == 'D':
            my -= 1
            
        if abs(mx) > 5 or abs(my) > 5 :
            mx, my = x, y
            continue
            
        if (x,y,mx,my) not in visited:
            visited.add((x,y,mx,my))
            visited.add((mx,my,x,y))
            answer +=1
        x, y = mx, my

    return answer

