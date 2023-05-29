def waterArea(heights):
    # Write your code here.
    
    #integers where each represents the height of a pillar of width 1. awter is pored over all the pillers
    #write a functions that returns the surface are of the water trapped between the pillars viewed from the front
    #spilled water should be ignored
    #aaray of integer were each integer represents a eight of a pillar
    #return the total of surface area of these are seen from the front
    if len(heights)==0:
        return 0

    #initialize the variables
    leftIdx=0
    rigthIdx=len(heights)-1
    leftMax=heights[leftIdx]
    rightMax=heights[rigthIdx]
    surfaceArea=0

    while leftIdx<rigthIdx:
        if heights[leftIdx]<heights[rigthIdx]:
            leftIdx+=1
            leftMax=max(leftMax,heights[leftIdx])
            surfaceArea+=leftMax-heights[leftIdx]
        else:
            rigthIdx-=1
            rightMax=max(rightMax,heights[rigthIdx])
            surfaceArea+=rightMax-heights[rigthIdx]
    return surfaceArea

    
