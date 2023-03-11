import pygame
pygame.init()
from pygame.locals import *
class bishopw(object):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            while jk==False:

                yposition=1+yposition
                xposition=1+xposition
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            
            while jk==True:

                yposition=yposition-1
                xposition=xposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  :
                    
                    
                    self.coords.append([xposition2,yposition2])

                else:
                    if yposition>-1 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                

                xposition=1+xposition
                yposition=yposition-1

                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if xposition<8 and yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and yposition>-1  and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:

                xposition=xposition-1
                yposition=yposition+1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if xposition>-1 and yposition<8  and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    
                else:
                    if xposition>-1 and yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])    
    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=""
                    fv=1
                    tg=1
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30

                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                                piece=""
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                if fv==0:
                    tg=3
                    return tg

                if fv==1:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                elif fv==2:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                
        else:
            return tg
                    
class rookw(bishopw):

    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:        
            while jk==False:

                yposition=1+yposition
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                
                if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            
            while jk==True:

                yposition=yposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and yposition>-1:
                    
                    
                    self.coords.append([xposition2,yposition2])

                else:
                    if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                

                xposition=1+xposition
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:

                xposition=xposition-1
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    
                else:
                    if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
class knightw(bishopw):
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        
        if xposition!=9:
            yposition=2+yposition
            xposition=1+xposition
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=2+yposition
            xposition=xposition-1
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-2
            xposition=1+xposition
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-2
            xposition=xposition-1
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-1
            xposition=xposition-2
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition+1
            xposition=xposition-2
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)


            yposition=yposition+1
            xposition=xposition+2
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)


            yposition=yposition-1
            xposition=xposition+2
            
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            if white_check==True :
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
class queenw(bishopw):

    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            while jk==False:

                yposition=1+yposition
                xposition=1+xposition
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            
            while jk==True:

                yposition=yposition-1
                xposition=xposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if yposition>-1 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  :
                    
                    
                    self.coords.append([xposition2,yposition2])

                else:
                    if yposition>-1 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                

                xposition=1+xposition
                yposition=yposition-1

                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and yposition>-1  and xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:

                xposition=xposition-1
                yposition=yposition+1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if xposition>-1 and yposition<8  and  xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    
                else:
                    if xposition>-1 and yposition<8 and xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            
            while jk==False:

                yposition=1+yposition
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                
                if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
                    
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:

                yposition=yposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if  yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    
                    self.coords.append([xposition2,yposition2])

                else:
                    if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                

                xposition=1+xposition
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==True:

                xposition=xposition-1
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    
                else:
                    if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition2,yposition2])
                    jk=False
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition]) 
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
class kingw(bishopw):
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        if vc=="k1b":
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            if xposition!=9:

                yposition=1+yposition
                xposition=1+xposition
                
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                
                xposition2=xposition2+30
                yposition2=yposition2+30
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])
                        
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                


                yposition=yposition-1
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True  :
                    
                    
                    self.coords.append([xposition2,yposition2])

                else:
                    if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition=1+xposition
                yposition=yposition-1

                
                xposition2=xposition*60
                yposition2=yposition*60

                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition<8 and yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and yposition>-1  and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                self.coords2.append([xposition4,yposition4])
                
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                xposition=xposition-1
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition>-1 and yposition<8  and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                    
                else:
                    if xposition>-1 and yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])


                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                

                yposition=1+yposition
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False        
                xposition2=xposition2+30
                yposition2=yposition2+30        
                if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  and fc==True:
                    
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                        
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                
                if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and yposition>-1 and fc==True:
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition=1+xposition
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                

                xposition=xposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                if moves2kb==0 and moves2r1b==0:
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    xposition=xposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_white)):
                        if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                            fc=False
                    if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==7 and yposition==7 and xposition==3:
                        xposition=list_searchx(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition-2
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_white)):
                            if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and Board[yposition][xposition-1][0]=="":
                            xposition=list_searchx(Board,"r1b")
                            yposition=list_searchy(Board,"r1b")
                            if xposition==0 and yposition==7:
                                xposition2=xposition2+30
                                yposition2=yposition2+30
                                self.coords.append([xposition2,yposition2])
                if  moves2kb==0 and moves2r2b==0:          
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    xposition=xposition+1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_white)):
                        if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                            fc=False
                    if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==7 and yposition==7 and xposition==5:
                        xposition=list_searchx(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition+2
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_white)):
                            if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                            xposition=list_searchx(Board,"r2b")
                            yposition=list_searchy(Board,"r2b")

                            if xposition==7 and yposition==7:
                                xposition2=xposition2+30
                                yposition2=yposition2+30
                                self.coords.append([xposition2,yposition2])


                        
        if vc=="k1w":
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            if xposition!=9:
                    yposition=1+yposition
                    xposition=1+xposition
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])
                            
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)

                    


                    yposition=yposition-1
                    xposition=xposition-1
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True  :
                        
                        
                        self.coords.append([xposition2,yposition2])

                    else:
                        if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    
                    xposition=1+xposition
                    yposition=yposition-1

                    
                    xposition2=xposition*60
                    yposition2=yposition*60

                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition<8 and yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if xposition<8 and yposition>-1  and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    
                    xposition4=xposition*60+30
                    yposition4=yposition*60+30
                    self.coords2.append([xposition4,yposition4])
                    
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)

                    xposition=xposition-1
                    yposition=yposition+1
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition>-1 and yposition<8  and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                        
                    else:
                        if xposition>-1 and yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])


                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)

                    

                    yposition=1+yposition
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False        
                    xposition2=xposition2+30
                    yposition2=yposition2+30        
                    if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  and fc==True:
                        
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                            
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)

                    yposition=yposition-1
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    
                    if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and yposition>-1 and fc==True:
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    
                    xposition=1+xposition
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    

                    xposition=xposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])
                    if  moves2kw==0 and moves2r1w==0: 
                        yposition=list_searchy(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition-1
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_black)):
                            if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==0 and xposition==3:
                            xposition=list_searchx(Board,vc)
                            xposition=list_searchx(Board,vc)
                            xposition=xposition-2
                            xposition2=xposition*60
                            yposition2=yposition*60
                            fc=True
                            for i in range (0,len(all_black)):
                                if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                    fc=False
                            if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and fc==True and Board[yposition][xposition-1][0]=="":
                                xposition=list_searchx(Board,"r1w")
                                yposition=list_searchy(Board,"r1w")
                                if xposition==0 and yposition==0:
                                    xposition2=xposition2+30
                                    yposition2=yposition2+30
                                    self.coords.append([xposition2,yposition2])

                    if moves2kw==0 and moves2r2w==0:             
                        yposition=list_searchy(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition+1
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_black)):
                            if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==0 and xposition==5:
                            xposition=list_searchx(Board,vc)
                            xposition=list_searchx(Board,vc)
                            xposition=xposition+2
                            xposition2=xposition*60
                            yposition2=yposition*60
                            fc=True
                            for i in range (0,len(all_black)):
                                if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                    fc=False
                            if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                                xposition=list_searchx(Board,"r2w")
                                yposition=list_searchy(Board,"r2w")
                                if xposition==7 and yposition==0:
                                    xposition2=xposition2+30
                                    yposition2=yposition2+30
                                    self.coords.append([xposition2,yposition2])


    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30

                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                                if self.coords[k1][0]==150 and self.coords[k1][1]==450 and moves2kb==0 and moves2r1b==0:
                                    Board[7][0][0]=""
                                    Board[7][0][1]=""
                                    Board[7][3][0]="r1b"
                                    Board[7][3][1]="b"
                                if self.coords[k1][0]==390 and self.coords[k1][1]==450 and moves2kb==0 and moves2r2b==0:
                                    Board[7][7][0]=""
                                    Board[7][7][1]=""
                                    Board[7][5][0]="r2b"
                                    Board[7][5][1]="b"
                                if self.coords[k1][0]==150 and self.coords[k1][1]==30 and moves2kw==0 and moves2r1w==0:
                                    Board[0][0][0]=""
                                    Board[0][0][1]=""
                                    Board[0][3][0]="r1w"
                                    Board[0][3][1]="w"
                                if self.coords[k1][0]==390 and self.coords[k1][1]==30 and moves2kw==0 and moves2r2w==0:
                                    Board[0][7][0]=""
                                    Board[0][7][1]=""
                                    Board[0][5][0]="r2w"
                                    Board[0][5][1]="w"
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                if fv==0:
                    tg=3
                    return tg

                if fv==1:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                elif fv==2:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                
        else:
            return tg

                    
class pawnw(bishopw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour,moves2):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
        self.moves2=moves2
        
    def possible_moves(self,coords,coords2,colour,moves2):
        self.colour=colour
        self.moves2=moves2
        
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=1+yposition
            xposition=xposition-1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="b":
                
                
                self.coords.append([xposition2,yposition2])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            yposition=1+yposition
            xposition=xposition+1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="b" :
                
                
                self.coords.append([xposition2,yposition2])
            if self.moves2==0:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                
                self.coords2.append([xposition4,yposition4])
                
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition+1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=2+yposition
                    xposition2=xposition*60+30
                    yposition2=yposition*60+30
                    
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                        
                        self.coords.append([xposition2,yposition2])


            else:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                self.coords2.append([xposition4,yposition4])
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=1+yposition
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    
                    self.coords.append([xposition2,yposition2])
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])


            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
                            
    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        global rookw_moves
        global bishopw_moves
        global queenw_moves
        global knightw_moves
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                    if fv==0:
                        tg=3
                        return tg

                    if fv==1:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                    elif fv==2:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30
                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                            if roomy==450:
                                event2=wait()
                                if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
                                    if queenw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q2w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                    elif queenw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                    elif queenw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
                                    if rookw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                    elif rookw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                    elif rookw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
                                    if bishopw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                    elif bishopw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                    elif bishopw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
                                    if knightw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                    elif knightw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                    elif knightw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                        
                            else:
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                            if fv==0:
                                tg=3
                                return tg

                            if fv==1:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                            elif fv==2:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                    
        else:
            return tg

class pawnb(bishopw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour,moves2):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
        self.moves2=moves2
        
    def possible_moves(self,coords,coords2,colour,moves2):
        self.colour=colour
        self.moves2=moves2
       
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9: 
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-1
            xposition=xposition-1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="w" :
                
                
                coords.append([xposition2,yposition2])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            yposition=yposition-1
            xposition=xposition+1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            
            
            
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="w" :
                
                
                coords.append([xposition2,yposition2])
            if self.moves2==0:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                coords2.append([xposition4,yposition4])
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=yposition-2
                    xposition2=xposition*60+30
                    yposition2=yposition*60+30
                    
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                        
                        self.coords.append([xposition2,yposition2])

            else:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                coords2.append([xposition4,yposition4])
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                
                
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
           
                    coords.append([xposition2,yposition2])
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    yposition=list_searchy(Board,attack[0][0])
                    xposition=list_searchx(Board,attack[0][0])
                    xposition=xposition*60+30
                    yposition=yposition*60+30
                    attack_positions2=[]

                    for a in range (0,len(attack_positions)):
                        zx=attack_positions[a][0]
                        zx=zx+30
                        zy=attack_positions[a][1]
                        zy=zy+30
                        attack_positions2.append([zx,zy])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==xposition and coords3[i][1]==yposition:
                            self.coords.append([xposition,yposition])
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])

    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        global rookb_moves
        global bishopb_moves
        global queenb_moves
        global knightb_moves
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                    if fv==0:
                        tg=3
                        return tg

                    if fv==1:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                    elif fv==2:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30
                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                            if roomy==30:
                                event2=wait()
                                if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
                                    if queenb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q2b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                    elif queenb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                    elif queenb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
                                    if rookb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                    elif rookb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                    elif rookb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
                                    if bishopb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                    elif bishopb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                    elif bishopb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
                                    if knightb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="n"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                                    elif knightb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                                    elif knightb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                            else:
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                            if fv==0:
                                tg=3
                                return tg

                            if fv==1:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                            elif fv==2:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                    
        else:
            return tg
def wait():
    fgh=False
    pygame.event.clear()
    while fgh==False:
        event2=pygame.event.wait()
        if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
            fgh=True
        elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
            fgh=True
        elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
            fgh=True
        elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
            fgh=True
    return event2
def wait2():
    fgh=False
    pygame.event.clear()
    while fgh==False:
        event3=pygame.event.wait()
        if event3.type==pygame.MOUSEBUTTONDOWN:
            fgh=True
    return event3
class bishop1(object):
    def __init__(self,b11,b12,b13,b14,black_protector,vc,king,colour,colour2):
        self.b11=b11
        self.b12=b12
        self.b13=b13
        self.b14=b14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,b11,b12,b13,b14,black_protector,vc,king,colour,colour2):
        self.b11=b11
        self.b12=b12
        self.b13=b13
        self.b14=b14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        global two_protectors
        pos_spaces=[]
        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=1+yposition
                xposition=1+xposition
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.b11.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b11.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            
                            yposition=1+yposition
                            xposition=1+xposition
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True
                                    
                                     
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b11.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition-1
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.b12.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b12.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:
                            
                            yposition=yposition-1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                 
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b12.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])

                xposition=1+xposition
                yposition=yposition-1

                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.b13.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b13.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            
                            xposition=1+xposition
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                 
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b13.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.b14.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b14.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition+1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                 
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b14.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False

class queen1(object):
    def __init__(self,q11,q12,q13,q14,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        self.q11=q11
        self.q12=q12
        self.q13=q13
        self.q14=q14
        self.q15=q15
        self.q16=q16
        self.q17=q17
        self.q18=q18
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,q11,q12,q13,q14,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        self.q11=q11
        self.q12=q12
        self.q13=q13
        self.q14=q14
        self.q15=q15
        self.q16=q16
        self.q17=q17
        self.q18=q18
        self.vc=vc
        global two_protectors
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=1+yposition
                xposition=1+xposition
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q11.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q11.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            
                            yposition=1+yposition
                            xposition=1+xposition
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True
                                    
                                     
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q11.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                yposition=yposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q12.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q12.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition-1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q12.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=1+xposition
                yposition=yposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q13.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q13.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            
                            xposition=1+xposition
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q13.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q14.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q14.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition+1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q14.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q15.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q15.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:                                
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=False                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q15.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
                    
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q16.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q16.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q16.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q17.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q17.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                    
                            xposition=xposition+1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q17.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q18.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q18.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q18.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            

class knight1(object):
    def __init__(self,kn1,black_protector,vc,king,colour,colour2):
        self.kn1=kn1
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,kn1,black_protector,vc,king,colour,colour2):
        self.kn1=kn1
        self.vc=vc
        self.king=king
        global two_protectors
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector

        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:

            yposition=2+yposition
            xposition=1+xposition
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=2+yposition
            xposition=xposition-1
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition-2
            xposition=1+xposition
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition-2
            xposition=xposition-1
            
            xposition2=xposition*60
            yposition2=yposition*60
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])

                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition-1
            xposition=xposition-2
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition+1
            xposition=xposition-2
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)


            yposition=yposition+1
            xposition=xposition+2
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)


            yposition=yposition-1
            xposition=xposition+2
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                
                
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

class rook1(object):
    def __init__(self,r11,r12,r13,r14,black_protector,vc,king,colour,colour2):
        self.r11=r11
        self.r12=r12
        self.r13=r13
        self.r14=r14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,r11,r12,r13,r14,black_protector,vc,king,colour,colour2):
        self.r11=r11
        self.r12=r12
        self.r13=r13
        global two_protectors
        self.r14=r14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if yposition!=9 or xposition!=9:
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r11.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r11.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                    
                            yposition=yposition+1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r11.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r12.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r12.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r12.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r13.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r13.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                    
                            xposition=xposition+1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r13.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r14.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r14.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r14.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False


class king1(object):
    def __init__(self,k1w,vc,colour,colour2):
        self.k1w=k1w
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
    def check(self,k1w,vc,colour,colour2):
        self.k1w=k1w
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        global two_protectors
        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:

            yposition=1+yposition
            xposition=1+xposition
            
            xposition2=xposition*60
            yposition2=yposition*60
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.k1w.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            


            yposition=yposition-1
            xposition=xposition-1
            
            xposition2=xposition*60
            yposition2=yposition*60
            
            if yposition>-1 and xposition>-1 and  Board[yposition][xposition][0]==""  :
                
               
                self.k1w.append([xposition2,yposition2])

            else:
                if yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            xposition=1+xposition
            yposition=yposition-1

            
            xposition2=xposition*60
            yposition2=yposition*60
            if xposition<8 and yposition>-1 and Board[yposition][xposition][0]=="" :
               
                self.k1w.append([xposition2,yposition2])
            else:
                if xposition<8 and yposition>-1  and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            xposition=xposition-1
            yposition=yposition+1
            
            xposition2=xposition*60
            yposition2=yposition*60
            
            if xposition>-1 and yposition<8  and Board[yposition][xposition][0]=="" :
               
                self.k1w.append([xposition2,yposition2])
                
            else:
                if xposition>-1 and yposition<8 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            

            yposition=1+yposition
            
            xposition2=xposition*60
            yposition2=yposition*60
            
           
            
            if yposition<8 and Board[yposition][xposition][0]=="" :
                
                
                self.k1w.append([xposition2,yposition2])
            else:
                if yposition<8 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
                    
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition-1
            
            xposition2=xposition*60
            yposition2=yposition*60
            
            if Board[yposition][xposition][0]=="" and yposition>-1:
                
               
                self.k1w.append([xposition2,yposition2])

            else:
                if yposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            xposition=1+xposition
            xposition2=xposition*60
            yposition2=yposition*60
            if xposition<8 and Board[yposition][xposition][0]=="" :
               
                self.k1w.append([xposition2,yposition2])
            else:
                if xposition<8 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            

            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            
            if xposition>-1 and Board[yposition][xposition][0]=="" :
               
                self.k1w.append([xposition2,yposition2])
                
            else:
                if xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])

class pawn1w(object):
    def __init__(self,p1,vc,colour,colour2):
        self.p1=p1
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
    def check(self,p1,vc,colour,colour2):
        self.p1=p1
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        global two_protectors
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=1+yposition
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1.append([xposition2,yposition2])
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1.append([xposition2,yposition2])
        
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)                
        if yposition!=9 or xposition!=9:
            yposition=1+yposition
            xposition=xposition+1
            xposition2=xposition*60
            yposition2=yposition*60
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1.append([xposition2,yposition2])
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1.append([xposition2,yposition2])

class pawn1b(object):
    def __init__(self,p1b,vc,colour,colour2):
        self.p1b=p1b
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
    def check(self,p1,vc,colour,colour2):
        self.p1b=p1b
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        global two_protectors
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)

        if yposition!=9 or xposition!=9:
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition-1
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1b.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1b.append([xposition2,yposition2])
                
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1b.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition=xposition+1
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1b.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1b.append([xposition2,yposition2])
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1b.append([xposition2,yposition2])
        
def convertx(piecex):
    d=piecex%60
    piecex=piecex-d
    return piecex

def converty(piecey):
    d=piecey%60
    piecey=piecey-d
    return piecey

def board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy):
    r1wmx=convertx(r1wmx)
    r1wmy=converty(r1wmy)
    
    r2wmx=convertx(r2wmx)
    r2wmy=converty(r2wmy)

    r3wmx=convertx(r3wmx)
    r3wmy=converty(r3wmy)

    r4wmx=convertx(r4wmx)
    r4wmy=converty(r4wmy)

    r5wmx=convertx(r5wmx)
    r5wmy=converty(r5wmy)
    
    r2bmx=convertx(r2bmx)
    r2bmy=converty(r2bmy)

    r3bmx=convertx(r3bmx)
    r3bmy=converty(r3bmy)

    r4bmx=convertx(r4bmx)
    r4bmy=converty(r4bmy)

    r5bmx=convertx(r5bmx)
    r5bmy=converty(r5bmy)
    
    r1bmx=convertx(r1bmx)
    r1bmy=converty(r1bmy)
    
    b1wmx=convertx(b1wmx)
    b1wmy=converty(b1wmy)
    
    b2wmx=convertx(b2wmx)
    b2wmy=converty(b2wmy)

    b3wmx=convertx(b3wmx)
    b3wmy=converty(b3wmy)

    b4wmx=convertx(b4wmx)
    b4wmy=converty(b4wmy)

    b5wmx=convertx(b5wmx)
    b5wmy=converty(b5wmy)
    
    b1bmx=convertx(b1bmx)
    b1bmy=converty(b1bmy)

    b2bmx=convertx(b2bmx)
    b2bmy=converty(b2bmy)

    b3bmx=convertx(b3bmx)
    b3bmy=converty(b3bmy)

    b4bmx=convertx(b4bmx)
    b4bmy=converty(b4bmy)

    b5bmx=convertx(b5bmx)
    b5bmy=converty(b5bmy)
    
    kn1wmx=convertx(kn1wmx)
    kn1wmy=converty(kn1wmy)

    kn2wmx=convertx(kn2wmx)
    kn2wmy=converty(kn2wmy)

    kn3wmx=convertx(kn3wmx)
    kn3wmy=converty(kn3wmy)

    kn4wmx=convertx(kn4wmx)
    kn4wmy=converty(kn4wmy)

    kn5wmx=convertx(kn5wmx)
    kn5wmy=converty(kn5wmy)
    
    kn1bmx=convertx(kn1bmx)
    kn1bmy=converty(kn1bmy)

    kn2bmx=convertx(kn2bmx)
    kn2bmy=converty(kn2bmy)

    kn3bmx=convertx(kn3bmx)
    kn3bmy=converty(kn3bmy)

    kn4bmx=convertx(kn4bmx)
    kn4bmy=converty(kn4bmy)

    kn5bmx=convertx(kn5bmx)
    kn5bmy=converty(kn5bmy)
    
    q1wmx=convertx(q1wmx)
    q1wmy=converty(q1wmy)

    q2wmx=convertx(q2wmx)
    q2wmy=converty(q2wmy)

    q3wmx=convertx(q3wmx)
    q3wmy=converty(q3wmy)

    q4wmx=convertx(q4wmx)
    q4wmy=converty(q4wmy)
    
    q1bmx=convertx(q1bmx)
    q1bmy=converty(q1bmy)

    q2bmx=convertx(q2bmx)
    q2bmy=converty(q2bmy)

    q3bmx=convertx(q3bmx)
    q3bmy=converty(q3bmy)

    q4bmx=convertx(q4bmx)
    q4bmy=converty(q4bmy)
    
    k1wmx=convertx(k1wmx)
    k1wmy=converty(k1wmy)

    k1bmx=convertx(k1bmx)
    k1bmy=converty(k1bmy)

    p8wmx=convertx(p8wmx)
    p8wmy=converty(p8wmy)

    p7wmx=convertx(p7wmx)
    p7wmy=converty(p7wmy)

    p6wmx=convertx(p6wmx)
    p6wmy=converty(p6wmy)

    p5wmx=convertx(p5wmx)
    p5wmy=converty(p5wmy)

    p4wmx=convertx(p4wmx)
    p4wmy=converty(p4wmy)

    p3wmx=convertx(p3wmx)
    p3wmy=converty(p3wmy)

    p2wmx=convertx(p2wmx)
    p2wmy=converty(p2wmy)

    p1wmx=convertx(p1wmx)
    p1wmy=converty(p1wmy)

    p1bmx=convertx(p1bmx)
    p1bmy=converty(p1bmy)

    p2bmx=convertx(p2bmx)
    p2bmy=converty(p2bmy)

    p3bmx=convertx(p3bmx)
    p3bmy=converty(p3bmy)

    p4bmx=convertx(p4bmx)
    p4bmy=converty(p4bmy)

    p5bmx=convertx(p5bmx)
    p5bmy=converty(p5bmy)

    p6bmx=convertx(p6bmx)
    p6bmy=converty(p6bmy)

    p7bmx=convertx(p7bmx)
    p7bmy=converty(p7bmy)

    p8bmx=convertx(p8bmx)
    p8bmy=converty(p8bmy)
    
    win.blit(bg,(0,0))
    if king_black_status=="alive":
        gameDisplay.blit(king_black,(k1bmx,k1bmy))
    else:
        gameDisplay.blit(king_black,(481,481))
    if king_white_status=="alive":
        gameDisplay.blit(king_white,(k1wmx,k1wmy))
    else:
        gameDisplay.blit(king_white,(481,481))

    if queen_black_status=="alive":
        gameDisplay.blit(queen_black,(q1bmx,q1bmy))
    else:
        gameDisplay.blit(queen_black,(480,60))

    if queen_black2_status=="alive":
        gameDisplay.blit(queen_black2,(q2bmx,q2bmy))
    else:
        gameDisplay.blit(queen_black2,(481,481))

    if queen_black3_status=="alive":
        gameDisplay.blit(queen_black3,(q3bmx,q3bmy))
    else:
        gameDisplay.blit(queen_black3,(481,481))

    if queen_black4_status=="alive":
        gameDisplay.blit(queen_black4,(q4bmx,q4bmy))
    else:
        gameDisplay.blit(queen_black4,(481,481))
        
    if queen_white_status=="alive":
        gameDisplay.blit(queen_white,(q1wmx,q1wmy))
    else:
        gameDisplay.blit(queen_white,(480,300))

    if queen_white2_status=="alive":
        gameDisplay.blit(queen_white2,(q2wmx,q2wmy))
    else:
        gameDisplay.blit(queen_white2,(481,481))

    if queen_white3_status=="alive":
        gameDisplay.blit(queen_white3,(q3wmx,q3wmy))
    else:
        gameDisplay.blit(queen_white3,(481,481))

    if queen_white4_status=="alive":
        gameDisplay.blit(queen_white4,(q4wmx,q4wmy))
    else:
        gameDisplay.blit(queen_white4,(481,481))
        
    if rook_black1_status=="alive":
        gameDisplay.blit(rook_black1,(r1bmx,r1bmy))
    else:
        gameDisplay.blit(rook_black1,(540,60))

    if rook_black2_status=="alive":
        gameDisplay.blit(rook_black2,(r2bmx,r2bmy))
    else:
        gameDisplay.blit(rook_black2,(600,60))

    if rook_black3_status=="alive":
        gameDisplay.blit(rook_black3,(r3bmx,r3bmy))
    else:
        gameDisplay.blit(rook_black3,(481,481))

    if rook_black4_status=="alive":
        gameDisplay.blit(rook_black4,(r4bmx,r4bmy))
    else:
        gameDisplay.blit(rook_black4,(481,481))

    if rook_black5_status=="alive":
        gameDisplay.blit(rook_black5,(r5bmx,r5bmy))
    else:
        gameDisplay.blit(rook_black5,(481,481))
                         
    if rook_white1_status=="alive":
        gameDisplay.blit(rook_white1,(r1wmx,r1wmy))
    else:
        gameDisplay.blit(rook_black1,(481,481))
        
    if rook_white2_status=="alive":
        gameDisplay.blit(rook_white2,(r2wmx,r2wmy))
    else:
        gameDisplay.blit(rook_white2,(481,481))

    if rook_white3_status=="alive":
        gameDisplay.blit(rook_white3,(r3wmx,r3wmy))
    else:
        gameDisplay.blit(rook_white3,(481,481))

    if rook_white4_status=="alive":
        gameDisplay.blit(rook_white4,(r4wmx,r4wmy))
    else:
        gameDisplay.blit(rook_white4,(481,481))

    if rook_white5_status=="alive":
        gameDisplay.blit(rook_white5,(r5wmx,r5wmy))
    else:
        gameDisplay.blit(rook_white5,(481,481))
        

    if knight_black1_status=="alive":
        gameDisplay.blit(knight_black1,(kn1bmx,kn1bmy))
    else:
        gameDisplay.blit(knight_black1,(660,60))

    if knight_black2_status=="alive":   
        gameDisplay.blit(knight_black2,(kn2bmx,kn2bmy))
    else:
        gameDisplay.blit(knight_black2,(720,60))

    if knight_black3_status=="alive":   
        gameDisplay.blit(knight_black3,(kn3bmx,kn3bmy))
    else:
        gameDisplay.blit(knight_black3,(481,481))

    if knight_black4_status=="alive":   
        gameDisplay.blit(knight_black4,(kn4bmx,kn4bmy))
    else:
        gameDisplay.blit(knight_black4,(481,481))
        
    if knight_black5_status=="alive":   
        gameDisplay.blit(knight_black5,(kn5bmx,kn5bmy))
    else:
        gameDisplay.blit(knight_black5,(481,481))


    if knight_white1_status=="alive":
        gameDisplay.blit(knight_white1,(kn1wmx,kn1wmy))
    else:
        gameDisplay.blit(knight_white1,(481,481))


    if knight_white2_status=="alive":
        gameDisplay.blit(knight_white2,(kn2wmx,kn2wmy))
    else:
        gameDisplay.blit(knight_white2,(481,481))

    if knight_white3_status=="alive":
        gameDisplay.blit(knight_white3,(kn3wmx,kn3wmy))
    else:
        gameDisplay.blit(knight_white3,(481,481))

    if knight_white4_status=="alive":
        gameDisplay.blit(knight_white4,(kn4wmx,kn4wmy))
    else:
        gameDisplay.blit(knight_white4,(481,481))

    if knight_white5_status=="alive":
        gameDisplay.blit(knight_white5,(kn5wmx,kn5wmy))
    else:
        gameDisplay.blit(knight_white5,(481,481))

    if bishop_black1_status=="alive":
        gameDisplay.blit(bishop_black1,(b1bmx,b1bmy))
    else:
        gameDisplay.blit(bishop_black1,(780,60))

    if bishop_black2_status=="alive":  
        gameDisplay.blit(bishop_black2,(b2bmx,b2bmy))
    else:
        gameDisplay.blit(bishop_black2,(840,60))

    if bishop_black3_status=="alive":  
        gameDisplay.blit(bishop_black3,(b3bmx,b3bmy))
    else:
        gameDisplay.blit(bishop_black3,(481,481))

    if bishop_black4_status=="alive":  
        gameDisplay.blit(bishop_black4,(b4bmx,b4bmy))
    else:
        gameDisplay.blit(bishop_black4,(481,481))

    if bishop_black5_status=="alive":  
        gameDisplay.blit(bishop_black5,(b5bmx,b5bmy))
    else:
        gameDisplay.blit(bishop_black5,(481,481))

    if bishop_white1_status=="alive":   
        gameDisplay.blit(bishop_white1,(b1wmx,b1wmy))
    else:
        gameDisplay.blit(bishop_white1,(481,481))

    if bishop_white2_status=="alive":     
        gameDisplay.blit(bishop_white2,(b2wmx,b2wmy))
    else:
        gameDisplay.blit(bishop_white2,(481,481))

    if bishop_white3_status=="alive":     
        gameDisplay.blit(bishop_white3,(b3wmx,b3wmy))
    else:
        gameDisplay.blit(bishop_white3,(481,481))

    if bishop_white4_status=="alive":     
        gameDisplay.blit(bishop_white4,(b4wmx,b4wmy))
    else:
        gameDisplay.blit(bishop_white4,(481,481))

    if bishop_white5_status=="alive":     
        gameDisplay.blit(bishop_white5,(b5wmx,b5wmy))
    else:
        gameDisplay.blit(bishop_white5,(481,481))


    if pawn_white1_status=="alive":   
        gameDisplay.blit(pawn_white1,(p1wmx,p1wmy))
    else:
        gameDisplay.blit(pawn_white1,(481,481))

    if pawn_white2_status=="alive":
        gameDisplay.blit(pawn_white2,(p2wmx,p2wmy))
    else:
        gameDisplay.blit(pawn_white2,(481,481))

    if pawn_white3_status=="alive":   
        gameDisplay.blit(pawn_white3,(p3wmx,p3wmy))
    else:
        gameDisplay.blit(pawn_white3,(481,481))

    if pawn_white4_status=="alive":    
        gameDisplay.blit(pawn_white4,(p4wmx,p4wmy))
    else:
        gameDisplay.blit(pawn_white4,(481,481))
    if pawn_white5_status=="alive":
        gameDisplay.blit(pawn_white5,(p5wmx,p5wmy))
    else:
        gameDisplay.blit(pawn_white5,(481,481))

    if pawn_white6_status=="alive":   
        gameDisplay.blit(pawn_white6,(p6wmx,p6wmy))
    else:
        gameDisplay.blit(pawn_white6,(481,481))

    if pawn_white7_status=="alive":  
        gameDisplay.blit(pawn_white7,(p7wmx,p7wmy))
    else:
        gameDisplay.blit(pawn_white7,(481,481))
    if pawn_white8_status=="alive": 
        gameDisplay.blit(pawn_white8,(p8wmx,p8wmy))
    else:
        gameDisplay.blit(pawn_white8,(481,481))
    if pawn_black1_status=="alive":
        gameDisplay.blit(pawn_black1,(p1bmx,p1bmy))
    else:
        gameDisplay.blit(pawn_black1,(900,60))

    if pawn_black2_status=="alive":    
        gameDisplay.blit(pawn_black2,(p2bmx,p2bmy))
    else:
        gameDisplay.blit(pawn_black2,(480,120))


    if pawn_black3_status=="alive":   
        gameDisplay.blit(pawn_black3,(p3bmx,p3bmy))
    else:
        gameDisplay.blit(pawn_black3,(481,481))

    if pawn_black4_status=="alive":
        gameDisplay.blit(pawn_black4,(p4bmx,p4bmy))
    else:
        gameDisplay.blit(pawn_black4,(481,481))

    if pawn_black5_status == "alive":
        gameDisplay.blit(pawn_black5,(p5bmx,p5bmy))
    else:
        gameDisplay.blit(pawn_black5,(481,481))
                         
    if pawn_black6_status== "alive" :                      
        gameDisplay.blit(pawn_black6,(p6bmx,p6bmy))
    else:
        gameDisplay.blit(pawn_black6,(481,481))

    if pawn_black7_status=="alive":                     
        gameDisplay.blit(pawn_black7,(p7bmx,p7bmy))
    else:
        gameDisplay.blit(pawn_black7,(481,481))

    if pawn_black8_status=="alive":
        gameDisplay.blit(pawn_black8,(p8bmx,p8bmy))
    else:
        gameDisplay.blit(pawn_black8,(481,481))
    
def list_searchy(Board, piece):
    f=9
    for i in range (0,8):
        for a in range (0,8):
            if Board[i][a][0]==piece:
                f=i
                return f
    return f
            
def list_searchx(Board, piece):
    f=9
    for i in range (0,8):
        for a in range (0,8):
            if Board[i][a][0]==piece:
                f=a
                return f
    return f





    
blength=480

win =pygame.display.set_mode((480,blength))
pygame.display.set_caption("Chess")
gameDisplay=pygame.display.set_mode((480,blength))
rook_white1=pygame.image.load("rook_white.png")
rook_white2=pygame.image.load("rook_white.png")

rook_white3=pygame.image.load("rook_white.png")
rook_white4=pygame.image.load("rook_white.png")
rook_white5=pygame.image.load("rook_white.png")

rook_black1=pygame.image.load("rook_black.png")
rook_black2=pygame.image.load("rook_black.png")

rook_black3=pygame.image.load("rook_black.png")
rook_black4=pygame.image.load("rook_black.png")
rook_black5=pygame.image.load("rook_black.png")

knight_white1=pygame.image.load("knight_white.png")
knight_white2=pygame.image.load("knight_white.png")

knight_white3=pygame.image.load("knight_white.png")
knight_white4=pygame.image.load("knight_white.png")
knight_white5=pygame.image.load("knight_white.png")

knight_black1=pygame.image.load("knight_black.png")
knight_black2=pygame.image.load("knight_black.png")
knight_black3=pygame.image.load("knight_black.png")
knight_black4=pygame.image.load("knight_black.png")
knight_black5=pygame.image.load("knight_black.png")

pawn_white1=pygame.image.load("pawn_white.png")
pawn_white2=pygame.image.load("pawn_white.png")
pawn_white3=pygame.image.load("pawn_white.png")
pawn_white4=pygame.image.load("pawn_white.png")
pawn_white5=pygame.image.load("pawn_white.png")
pawn_white6=pygame.image.load("pawn_white.png")
pawn_white7=pygame.image.load("pawn_white.png")
pawn_white8=pygame.image.load("pawn_white.png")

pawn_black1=pygame.image.load("pawn_black.png")
pawn_black2=pygame.image.load("pawn_black.png")
pawn_black3=pygame.image.load("pawn_black.png")
pawn_black4=pygame.image.load("pawn_black.png")
pawn_black5=pygame.image.load("pawn_black.png")
pawn_black6=pygame.image.load("pawn_black.png")
pawn_black7=pygame.image.load("pawn_black.png")
pawn_black8=pygame.image.load("pawn_black.png")

queen_white=pygame.image.load("queen_white.png")
queen_black=pygame.image.load("queen_black.png")
queen_white2=pygame.image.load("queen_white.png")
queen_black2=pygame.image.load("queen_black.png")
queen_white3=pygame.image.load("queen_white.png")
queen_black3=pygame.image.load("queen_black.png")
queen_white4=pygame.image.load("queen_white.png")
queen_black4=pygame.image.load("queen_black.png")
king_white=pygame.image.load("king_white.png")
king_black=pygame.image.load("king_black.png")

bishop_white1=pygame.image.load("bishop_white.png")
bishop_white2=pygame.image.load("bishop_white.png")
bishop_white3=pygame.image.load("bishop_white.png")
bishop_white4=pygame.image.load("bishop_white.png")
bishop_white5=pygame.image.load("bishop_white.png")

bishop_black1=pygame.image.load("bishop_black.png")
bishop_black2=pygame.image.load("bishop_black.png")
bishop_black3=pygame.image.load("bishop_black.png")
bishop_black4=pygame.image.load("bishop_black.png")
bishop_black5=pygame.image.load("bishop_black.png")

checkmate=pygame.image.load("checkmate.png")
stalemate=pygame.image.load("stalemate.png")
bg=pygame.image.load("ChessBoard.png")

global rook_white1_status
rook_white1_status="alive"
global rook_white2_status
rook_white2_status="alive"
global rook_white3_status
rook_white3_status="alive"
global rook_white4_status
rook_white4_status="alive"
global rook_white5_status
rook_white5_status="alive"

global knight_white1_status
knight_white1_status="alive"
global knight_white2_status
knight_white2_status="alive"
global knight_white3_status
knight_white3_status="alive"
global knight_white4_status
knight_white4_status="alive"
global knight_white5_status
knight_white5_status="alive"


global bishop_white1_status
bishop_white1_status="alive"
global bishop_white2_status
bishop_white2_status="alive"
global bishop_white3_status
bishop_white3_status="alive"
global bishop_white4_status
bishop_white4_status="alive"
global bishop_white5_status
bishop_white5_status="alive"

global king_white_status
king_white_status="alive"
global queen_white_status
queen_white_status="alive"

global queen_white2_status
queen_white2_status="alive"
global queen_white3_status
queen_white3_status="alive"
global queen_white4_status
queen_white4_status="alive"

global pawn_white1_status
pawn_white1_status="alive"

global pawn_white2_status
pawn_white2_status="alive"

global pawn_white3_status
pawn_white3_status="alive"

global pawn_white4_status
pawn_white4_status="alive"

global pawn_white5_status
pawn_white5_status="alive"

global pawn_white6_status
pawn_white6_status="alive"

global pawn_white7_status
pawn_white7_status="alive"

global pawn_white8_status
pawn_white8_status="alive"




global pawn_black1_status
pawn_black1_status="alive"

global pawn_black2_status
pawn_black2_status="alive"

global pawn_black3_status
pawn_black3_status="alive"

global pawn_black4_status
pawn_black4_status="alive"

global pawn_black5_status
pawn_black5_status="alive"

global pawn_black6_status
pawn_black6_status="alive"

global pawn_black7_status
pawn_black7_status="alive"

global pawn_black8_status
pawn_black8_status="alive"

global rook_black1_status
rook_black1_status="alive"
global rook_black2_status
rook_black2_status="alive"
global rook_black3_status
rook_black3_status="alive"
global rook_black4_status
rook_black4_status="alive"
global rook_black5_status
rook_black5_status="alive"


global knight_black1_status
knight_black1_status="alive"
global knight_black2_status
knight_black2_status="alive"
global knight_black3_status
knight_black3_status="alive"
global knight_black4_status
knight_black4_status="alive"
global knight_black5_status
knight_black5_status="alive"

global bishop_black1_status
bishop_black1_status="alive"
global bishop_black2_status
bishop_black2_status="alive"
global bishop_black3_status
bishop_black3_status="alive"
global bishop_black4_status
bishop_black4_status="alive"
global bishop_black5_status
bishop_black5_status="alive"


global king_black_status
king_black_status="alive"
global queen_black_status
queen_black_status="alive"

global queen_black2_status
queen_black2_status="alive"
global queen_black3_status
queen_black3_status="alive"
global queen_black4_status
queen_black4_status="alive"

rookb_moves=0
bishopb_moves=0
queenb_moves=0
knightb_moves=0

rookw_moves=0
bishopw_moves=0
queenw_moves=0
knightw_moves=0

Board=[[["r1w","w"],["kn1w","w"],["b1w","w"],["q1w", "w"],["k1w", "w"],["b2w","w"],["kn2w","w"],["r2w","w"]],
       [["p1w","w"],["p2w", "w"],["p3w","w"],["p4w","w"],["p5w","w"],["p6w","w"],["p7w", "w"],["p8w","w"]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["p1b","b"],["p2b", "b"],["p3b","b"],["p4b","b"],["p5b","b"],["p6b","b"],["p7b", "b"],["p8b","b"]],
       [["r1b","b"],["kn1b","b"],["b1b","b"],["q1b", "b"],["k1b", "b"],["b2b","b"],["kn2b","b"],["r2b","b"]]]

attack=[]
r1wmx=0
r1wmy=0

r2wmx=420
r2wmy=0

r3wmx=481
r3wmy=481

r4wmx=481
r4wmy=481

r5wmx=481
r5wmy=481

r2bmx=420
r2bmy=420

r1bmx=0
r1bmy=420

r3bmx=481
r3bmy=481

r4bmx=481
r4bmy=481

r5bmx=481
r5bmy=481

b1wmx=120
b1wmy=0

b3wmx=481
b3wmy=481

b4wmx=481
b4wmy=481

b5wmx=481
b5wmy=481

b2wmx=300
b2wmy=0

b1bmx=120
b1bmy=420

b2bmx=300
b2bmy=420

b3bmx=481
b3bmy=481

b4bmx=481
b4bmy=481

b5bmx=481
b5bmy=481

kn1wmx=60
kn1wmy=0

kn2wmx=360
kn2wmy=0

kn3wmx=481
kn3wmy=481

kn4wmx=481
kn4wmy=481

kn5wmx=481
kn5wmy=481

kn1bmx=60
kn1bmy=420

kn2bmx=360
kn2bmy=420

kn3bmx=481
kn3bmy=481

kn4bmx=481
kn4bmy=481

kn5bmx=481
kn5bmy=481

q1wmx=180
q1wmy=0

q2wmx=481
q2wmy=481

q3wmx=481
q3wmy=481

q4wmx=481
q4wmy=481

q1bmx=180
q1bmy=420

q2bmx=481
q2bmy=481

q3bmx=481
q3bmy=481

q4bmx=481
q4bmy=481

q5bmx=481
q5bmy=481

k1wmx=240
k1wmy=0

k1bmx=240
k1bmy=420

p1wmx=0
p1wmy=60

p2wmx=60
p2wmy=60

p3wmx=120
p3wmy=60

p4wmx=180
p4wmy=60

p5wmx=240
p5wmy=60

p6wmx=300
p6wmy=60

p7wmx=360
p7wmy=60

p8wmx=420
p8wmy=60


p1bmx=0
p1bmy=360

p2bmx=60
p2bmy=360

p3bmx=120
p3bmy=360

p4bmx=180
p4bmy=360

p5bmx=240
p5bmy=360

p6bmx=300
p6bmy=360

p7bmx=360
p7bmy=360

p8bmx=420
p8bmy=360

moves=0
hb=0
hw=0
black=(255,0,0)
run=True
piece=""
board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
pygame.display.update()
coords=[]
coords2=[]
rook1change=True
rook2change=True
rook3change=True
rook4change=True
rook5change=True

rook1bchange=True
rook2bchange=True
rook3bchange=True
rook4bchange=True
rook5bchange=True

bishop1change=True
bishop2change=True
bishop3change=True
bishop4change=True
bishop5change=True

bishop1bchange=True
bishop2bchange=True
bishop3bchange=True
bishop4bchange=True
bishop5bchange=True

knight1change=True
knight2change=True
knight3change=True
knight4change=True
knight5change=True

knight1bchange=True
knight2bchange=True
knight3bchange=True
knight4bchange=True
knight5bchange=True

queen1change=True
queen3change=True
queen4change=True

queen1bchange=True
queen2change=True
queen2bchange=True
queen3bchange=True
queen4bchange=True
king1change=True
king1bchange=True

pawn1change=True
pawn2change=True
pawn3change=True
pawn4change=True
pawn5change=True
pawn6change=True
pawn7change=True
pawn8change=True

pawn1bchange=True
pawn2bchange=True
pawn3bchange=True
pawn4bchange=True
pawn5bchange=True
pawn6bchange=True
pawn7bchange=True
pawn8bchange=True

moves28=0
moves27=0
moves26=0
moves25=0
moves24=0
moves23=0
moves22=0
moves21=0

moves28b=0
moves27b=0
moves26b=0
moves25b=0
moves24b=0
moves23b=0
moves22b=0
moves21b=0

moves2kw=0
moves2kb=0
moves2r1w=0
moves2r2w=0
moves2r1b=0
moves2r2b=0

pos_spaces=[]

two_protectors=False


b11=[]
b12=[]
b13=[]
b14=[]

b21=[]
b22=[]
b23=[]
b24=[]

b31=[]
b32=[]
b33=[]
b34=[]

b41=[]
b42=[]
b43=[]
b44=[]

b51=[]
b52=[]
b53=[]
b54=[]

r11=[]
r12=[]
r13=[]
r14=[]

r21=[]
r22=[]
r23=[]
r24=[]

r31=[]
r32=[]
r33=[]
r34=[]

r41=[]
r42=[]
r43=[]
r44=[]

r51=[]
r52=[]
r53=[]
r54=[]


kn1=[]
kn2=[]

q11=[]
q12=[]
q13=[]
q14=[]
q15=[]
q16=[]
q17=[]
q18=[]

q21=[]
q22=[]
q23=[]
q24=[]
q25=[]
q26=[]
q27=[]
q28=[]

q31=[]
q32=[]
q33=[]
q34=[]
q35=[]
q36=[]
q37=[]
q38=[]

q41=[]
q42=[]
q43=[]
q44=[]
q45=[]
q46=[]
q47=[]
q48=[]

k1w=[]

p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
p6=[]
p7=[]
p8=[]

b11b=[]
b12b=[]
b13b=[]
b14b=[]

b21b=[]
b22b=[]
b23b=[]
b24b=[]

b31b=[]
b32b=[]
b33b=[]
b34b=[]

b41b=[]
b42b=[]
b43b=[]
b44b=[]

b51b=[]
b52b=[]
b53b=[]
b54b=[]

r11b=[]
r12b=[]
r13b=[]
r14b=[]

r21b=[]
r22b=[]
r23b=[]
r24b=[]

r31b=[]
r32b=[]
r33b=[]
r34b=[]

r41b=[]
r42b=[]
r43b=[]
r44b=[]

r51b=[]
r52b=[]
r53b=[]
r54b=[]

kn1b=[]
kn2b=[]
kn3b=[]
kn4b=[]
kn5b=[]

q11b=[]
q12b=[]
q13b=[]
q14b=[]
q15b=[]
q16b=[]
q17b=[]
q18b=[]

q21b=[]
q22b=[]
q23b=[]
q24b=[]
q25b=[]
q26b=[]
q27b=[]
q28b=[]

q31b=[]
q32b=[]
q33b=[]
q34b=[]
q35b=[]
q36b=[]
q37b=[]
q38b=[]

q41b=[]
q42b=[]
q43b=[]
q44b=[]
q45b=[]
q46b=[]
q47b=[]
q48b=[]


k1b=[]

p1b=[]
p2b=[]
p3b=[]
p4b=[]
p5b=[]
p6b=[]
p7b=[]
p8b=[]

jkl=0
jkb=0
view=False

attack_positions=[]
black_check=False
white_check=False

black_protector=[]
white_protector=[]

queen2w_spawn=0
queen3w_spawn=0
queen4w_spawn=0

queen2b_spawn=0
queen3b_spawn=0
queen4b_spawn=0

bishop3b_spawn=0
bishop4b_spawn=0
bishop5b_spawn=0

bishop3w_spawn=0
bishop4w_spawn=0
bishop5w_spawn=0

rook3w_spawn=0
rook4w_spawn=0
rook5w_spawn=0

rook3b_spawn=0
rook4b_spawn=0
rook5b_spawn=0

knight3w_spawn=0
knight4w_spawn=0
knight5w_spawn=0

knight3b_spawn=0
knight4b_spawn=0
knight5b_spawn=0

counter=0
event3=wait2()
rfv=0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
            
        yposition=list_searchy(Board,"p1b")
        xposition=list_searchx(Board,"p1b")
        
        if xposition==9:
            pawn_black1_status="dead"

        yposition=list_searchy(Board,"p2b")
        xposition=list_searchx(Board,"p2b")
        if xposition==9:
            pawn_black2_status="dead"

            
        yposition=list_searchy(Board,"p3b")
        xposition=list_searchx(Board,"p3b")
        if xposition==9:
            pawn_black3_status="dead"


        yposition=list_searchy(Board,"p4b")
        xposition=list_searchx(Board,"p4b")
        if xposition==9:
            pawn_black4_status="dead"

            
        yposition=list_searchy(Board,"p5b")
        xposition=list_searchx(Board,"p5b")
        if xposition==9:
            pawn_black5_status="dead"


            
        yposition=list_searchy(Board,"p6b")
        xposition=list_searchx(Board,"p6b")
        if xposition==9:
            pawn_black6_status="dead"


        yposition=list_searchy(Board,"p7b")
        xposition=list_searchx(Board,"p7b")
        if xposition==9:
            pawn_black7_status="dead"



        yposition=list_searchy(Board,"p8b")
        xposition=list_searchx(Board,"p8b")
        if xposition==9:
            pawn_black8_status="dead"
            


        yposition=list_searchy(Board,"p1w")
        xposition=list_searchx(Board,"p1w")
        if xposition==9:
            pawn_white1_status="dead"


        yposition=list_searchy(Board,"p2w")
        xposition=list_searchx(Board,"p2w")
        if xposition==9:
            pawn_white2_status="dead"

            
        yposition=list_searchy(Board,"p3w")
        xposition=list_searchx(Board,"p3w")
        if xposition==9:
            pawn_white3_status="dead"


        yposition=list_searchy(Board,"p4w")
        xposition=list_searchx(Board,"p4w")
        if xposition==9:
            pawn_white4_status="dead"

            
        yposition=list_searchy(Board,"p5w")
        xposition=list_searchx(Board,"p5w")
        if xposition==9:
            pawn_white5_status="dead"


            
        yposition=list_searchy(Board,"p6w")
        xposition=list_searchx(Board,"p6w")
        if xposition==9:
            pawn_white6_status="dead"


        yposition=list_searchy(Board,"p7w")
        xposition=list_searchx(Board,"p7w")
        if xposition==9:
            pawn_white7_status="dead"



        yposition=list_searchy(Board,"p8w")
        xposition=list_searchx(Board,"p8w")
        if xposition==9:
            pawn_white8_status="dead"

        yposition=list_searchy(Board,"r1w")
        xposition=list_searchx(Board,"r1w")
        if xposition==9:
            rook_white1_status="dead"

    
        yposition=list_searchy(Board,"r2w")
        xposition=list_searchx(Board,"r2w")
        if xposition==9:
            rook_white2_status="dead"

        yposition=list_searchy(Board,"r3w")
        xposition=list_searchx(Board,"r3w")
        if xposition==9:
            rook_white3_status="dead"

        yposition=list_searchy(Board,"r3w")
        xposition=list_searchx(Board,"r3w")
        if xposition==9:
            rook_white3_status="alive"

        yposition=list_searchy(Board,"r4w")
        xposition=list_searchx(Board,"r4w")
        if xposition==9:
            rook_white4_status="dead"

        yposition=list_searchy(Board,"r4w")
        xposition=list_searchx(Board,"r4w")
        if xposition==9:
            rook_white4_status="alive"

        yposition=list_searchy(Board,"r5w")
        xposition=list_searchx(Board,"r5w")
        if xposition==9:
            rook_white5_status="dead"

        yposition=list_searchy(Board,"r5w")
        xposition=list_searchx(Board,"r5w")
        if xposition==9:
            rook_white5_status="alive"
            
        yposition=list_searchy(Board,"kn1w")
        xposition=list_searchx(Board,"kn1w")
        if xposition==9:
            knight_white1_status="dead"

        yposition=list_searchy(Board,"kn2w")
        xposition=list_searchx(Board,"kn2w")
        if xposition==9:
            knight_white2_status="dead"

        yposition=list_searchy(Board,"kn3w")
        xposition=list_searchx(Board,"kn3w")
        if xposition==9:
            knight_white3_status="dead"

        yposition=list_searchy(Board,"kn3w")
        xposition=list_searchx(Board,"kn3w")
        if xposition==9:
            knight_white3_status="alive"

        yposition=list_searchy(Board,"kn4w")
        xposition=list_searchx(Board,"kn4w")
        if xposition==9:
            knight_white4_status="dead"

        yposition=list_searchy(Board,"kn4w")
        xposition=list_searchx(Board,"kn4w")
        if xposition==9:
            knight_white4_status="alive"

        yposition=list_searchy(Board,"kn5w")
        xposition=list_searchx(Board,"kn5w")
        if xposition==9:
            knight_white5_status="dead"

        yposition=list_searchy(Board,"kn5w")
        xposition=list_searchx(Board,"kn5w")
        if xposition==9:
            knight_white5_status="alive"
            
        yposition=list_searchy(Board,"b1w")
        xposition=list_searchx(Board,"b1w")
        if xposition==9:
            bishop_white1_status="dead"

            
        yposition=list_searchy(Board,"b2w")
        xposition=list_searchx(Board,"b2w")
        if xposition==9:
            bishop_white2_status="dead"

        yposition=list_searchy(Board,"b2w")
        xposition=list_searchx(Board,"b2w")
        if xposition==9:
            bishop_white2_status="dead"

        yposition=list_searchy(Board,"b3w")
        xposition=list_searchx(Board,"b3w")
        if xposition==9:
            bishop_white3_status="dead"
            
        yposition=list_searchy(Board,"b3w")
        xposition=list_searchx(Board,"b3w")
        if xposition==9:
            bishop_white3_status="alive"

        yposition=list_searchy(Board,"b4w")
        xposition=list_searchx(Board,"b4w")
        if xposition==9:
            bishop_white4_status="dead"
            
        yposition=list_searchy(Board,"b4w")
        xposition=list_searchx(Board,"b4w")
        if xposition==9:
            bishop_white4_status="alive"

        yposition=list_searchy(Board,"b5w")
        xposition=list_searchx(Board,"b5w")
        if xposition==9:
            bishop_white5_status="dead"
            
        yposition=list_searchy(Board,"b5w")
        xposition=list_searchx(Board,"b5w")
        if xposition==9:
            bishop_white5_status="alive"
            
        yposition=list_searchy(Board,"k1w")
        xposition=list_searchx(Board,"k1w")
        if xposition==9:
            king_white_status="dead"

            
        yposition=list_searchy(Board,"q1w")
        xposition=list_searchx(Board,"q1w")
        if xposition==9:
            queen_white_status="dead"

        yposition=list_searchy(Board,"q2w")
        xposition=list_searchx(Board,"q2w")
        if xposition==9:
            queen_white2_status="dead"

        yposition=list_searchy(Board,"q2w")
        xposition=list_searchx(Board,"q2w")
        if xposition!=9:
            queen_white2_status="alive"

        yposition=list_searchy(Board,"q3w")
        xposition=list_searchx(Board,"q3w")
        if xposition==9:
            queen_white3_status="dead"

        yposition=list_searchy(Board,"q3w")
        xposition=list_searchx(Board,"q3w")
        if xposition!=9:
            queen_white3_status="alive"

        yposition=list_searchy(Board,"q4w")
        xposition=list_searchx(Board,"q4w")
        if xposition==9:
            queen_white4_status="dead"

        yposition=list_searchy(Board,"q4w")
        xposition=list_searchx(Board,"q4w")
        if xposition!=9:
            queen_white4_status="alive"
            
        yposition=list_searchy(Board,"r1b")
        xposition=list_searchx(Board,"r1b")
        if xposition==9:
            rook_black1_status="dead"

        yposition=list_searchy(Board,"r2b")
        xposition=list_searchx(Board,"r2b")
        if xposition==9:
            rook_black2_status="dead"

        yposition=list_searchy(Board,"r3b")
        xposition=list_searchx(Board,"r3b")
        if xposition==9:
            rook_black3_status="dead"
        yposition=list_searchy(Board,"r3b")
        xposition=list_searchx(Board,"r3b")
        if xposition==9:
            rook_black3_status="alive"

        yposition=list_searchy(Board,"r4b")
        xposition=list_searchx(Board,"r4b")
        if xposition==9:
            rook_black4_status="dead"
        yposition=list_searchy(Board,"r4b")
        xposition=list_searchx(Board,"r4b")
        if xposition==9:
            rook_black4_status="alive"

        yposition=list_searchy(Board,"r5b")
        xposition=list_searchx(Board,"r5b")
        if xposition==9:
            rook_black5_status="dead"
        yposition=list_searchy(Board,"r5b")
        xposition=list_searchx(Board,"r5b")
        if xposition==9:
            rook_black5_status="alive"
            
        yposition=list_searchy(Board,"kn1b")
        xposition=list_searchx(Board,"kn1b")
        if xposition==9:
            knight_black1_status="dead"

        yposition=list_searchy(Board,"kn2b")
        xposition=list_searchx(Board,"kn2b")
        if xposition==9:
            knight_black2_status="dead"

        yposition=list_searchy(Board,"kn3b")
        xposition=list_searchx(Board,"kn3b")
        if xposition==9:
            knight_black3_status="dead"
        yposition=list_searchy(Board,"kn3b")
        xposition=list_searchx(Board,"kn3b")
        if xposition==9:
            knight_black3_status="alive"

        yposition=list_searchy(Board,"kn4b")
        xposition=list_searchx(Board,"kn4b")
        if xposition==9:
            knight_black4_status="dead"
        yposition=list_searchy(Board,"kn4b")
        xposition=list_searchx(Board,"kn4b")
        if xposition==9:
            knight_black4_status="alive"

        yposition=list_searchy(Board,"kn5b")
        xposition=list_searchx(Board,"kn5b")
        if xposition==9:
            knight_black5_status="dead"
        yposition=list_searchy(Board,"kn5b")
        xposition=list_searchx(Board,"kn5b")
        if xposition==9:
            knight_black5_status="alive"
            
        yposition=list_searchy(Board,"b1b")
        xposition=list_searchx(Board,"b1b")
        if xposition==9:
            bishop_black1_status="dead"

            
        yposition=list_searchy(Board,"b2b")
        xposition=list_searchx(Board,"b2b")
        if xposition==9:
            bishop_black2_status="dead"

        yposition=list_searchy(Board,"b3b")
        xposition=list_searchx(Board,"b3b")
        if xposition==9:
            bishop_black3_status="dead"
        yposition=list_searchy(Board,"b3b")
        xposition=list_searchx(Board,"b3b")
        if xposition==9:
            bishop_black3_status="alive"

        yposition=list_searchy(Board,"b4b")
        xposition=list_searchx(Board,"b4b")
        if xposition==9:
            bishop_black4_status="dead"
        yposition=list_searchy(Board,"b4b")
        xposition=list_searchx(Board,"b4b")
        if xposition==9:
            bishop_black4_status="alive"

        yposition=list_searchy(Board,"b5b")
        xposition=list_searchx(Board,"b5b")
        if xposition==9:
            bishop_black5_status="dead"
        yposition=list_searchy(Board,"b5b")
        xposition=list_searchx(Board,"b5b")
        if xposition==9:
            bishop_black5_status="alive"
            
        yposition=list_searchy(Board,"k1b")
        xposition=list_searchx(Board,"k1b")
        if xposition==9:
            king_black_status="dead"

            
        yposition=list_searchy(Board,"q1b")
        xposition=list_searchx(Board,"q1b")
        if xposition==9:
            queen_black_status="dead"

        yposition=list_searchy(Board,"q2b")
        xposition=list_searchx(Board,"q2b")
        if xposition==9:
            queen_black2_status="dead"

        yposition=list_searchy(Board,"q2b")
        xposition=list_searchx(Board,"q2b")
        if xposition!=9:
            queen_black2_status="alive"

        yposition=list_searchy(Board,"q3b")
        xposition=list_searchx(Board,"q3b")
        if xposition==9:
            queen_black3_status="dead"

        yposition=list_searchy(Board,"q3b")
        xposition=list_searchx(Board,"q3b")
        if xposition!=9:
            queen_black3_status="alive"

        yposition=list_searchy(Board,"q4b")
        xposition=list_searchx(Board,"q4b")
        if xposition==9:
            queen_black4_status="dead"

        yposition=list_searchy(Board,"q4b")
        xposition=list_searchx(Board,"q4b")
        if xposition!=9:
            queen_black4_status="alive"
            
        b11=[]
        b12=[]
        b13=[]
        b14=[]

        b21=[]
        b22=[]
        b23=[]
        b24=[]

        b41=[]
        b42=[]
        b43=[]
        b44=[]

        b31=[]
        b32=[]
        b33=[]
        b34=[]

        b51=[]
        b52=[]
        b53=[]
        b54=[]
        
        r11=[]
        r12=[]
        r13=[]
        r14=[]

        r21=[]
        r22=[]
        r23=[]
        r24=[]

        r31=[]
        r32=[]
        r33=[]
        r34=[]

        r41=[]
        r42=[]
        r43=[]
        r44=[]

        r51=[]
        r52=[]
        r53=[]
        r54=[]
        
        kn1=[]
        kn2=[]
        kn3=[]
        kn4=[]
        kn5=[]
        
        q11=[]
        q12=[]
        q13=[]
        q14=[]
        q15=[]
        q16=[]
        q17=[]
        q18=[]

        q21=[]
        q22=[]
        q23=[]
        q24=[]
        q25=[]
        q26=[]
        q27=[]
        q28=[]

        q31=[]
        q32=[]
        q33=[]
        q34=[]
        q35=[]
        q36=[]
        q37=[]
        q38=[]

        q41=[]
        q42=[]
        q43=[]
        q44=[]
        q45=[]
        q46=[]
        q47=[]
        q48=[]
        
        k1w=[]

        p1=[]
        p2=[]
        p3=[]
        p4=[]
        p5=[]
        p6=[]
        p7=[]
        p8=[]

        b11b=[]
        b12b=[]
        b13b=[]
        b14b=[]

        b31b=[]
        b32b=[]
        b33b=[]
        b34b=[]

        b41b=[]
        b42b=[]
        b43b=[]
        b44b=[]

        b51b=[]
        b52b=[]
        b53b=[]
        b54b=[]
        
        b21b=[]
        b22b=[]
        b23b=[]
        b24b=[]

        r11b=[]
        r12b=[]
        r13b=[]
        r14b=[]

        r21b=[]
        r22b=[]
        r23b=[]
        r24b=[]

        r31b=[]
        r32b=[]
        r33b=[]
        r34b=[]

        r41b=[]
        r42b=[]
        r43b=[]
        r44b=[]

        r51b=[]
        r52b=[]
        r53b=[]
        r54b=[]
        
        kn1b=[]
        kn2b=[]
        kn3b=[]
        kn4b=[]
        kn5b=[]
        
        q11b=[]
        q12b=[]
        q13b=[]
        q14b=[]
        q15b=[]
        q16b=[]
        q17b=[]
        q18b=[]
        
        q21b=[]
        q22b=[]
        q23b=[]
        q24b=[]
        q25b=[]
        q26b=[]
        q27b=[]
        q28b=[]

        q31b=[]
        q32b=[]
        q33b=[]
        q34b=[]
        q35b=[]
        q36b=[]
        q37b=[]
        q38b=[]

        q41b=[]
        q42b=[]
        q43b=[]
        q44b=[]
        q45b=[]
        q46b=[]
        q47b=[]
        q48b=[]
        
        k1b=[]

        p1b=[]
        p2b=[]
        p3b=[]
        p4b=[]
        p5b=[]
        p6b=[]
        p7b=[]
        p8b=[]
        
        if hb==0:
            two_protectors=False
            black_protector=[]
            pos_spaces=[]
            Bishop1w2=bishop1(b11,b12,b13,b14,black_protector,"b1w","k1b","b","w")
            Bishop1w2.check(b11,b12,b13,b14,black_protector,"b1w","k1b","b","w")
######################################################################################                
            Bishop2w2=bishop1(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")
            Bishop2w2.check(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")
#########################################################################################
            Bishop3w3=bishop1(b31,b32,b33,b34,black_protector,"b3w","k1b","b","w")
            Bishop3w3.check(b31,b32,b33,b34,black_protector,"b3w","k1b","b","w")
#########################################################################################
            Bishop4w4=bishop1(b41,b42,b43,b44,black_protector,"b4w","k1b","b","w")
            Bishop4w4.check(b41,b42,b43,b44,black_protector,"b4w","k1b","b","w")
#########################################################################################
            Bishop5w5=bishop1(b51,b52,b53,b54,black_protector,"b5w","k1b","b","w")
            Bishop5w5.check(b51,b52,b53,b54,black_protector,"b5w","k1b","b","w")
#########################################################################################
            Queen1w2=queen1(q11,q12,q13,q14,q15,q16,q17,q18,black_protector,"q1w","k1b","b","w")
            Queen1w2.check(q11,q12,q13,q14,q15,q16,q17,q18,black_protector,"q1w","k1b","b","w")
#############################################################################
            Queen2w2=queen1(q21,q22,q23,q24,q25,q26,q27,q28,black_protector,"q2w","k1b","b","w")
            Queen2w2.check(q21,q22,q23,q24,q25,q26,q27,q28,black_protector,"q2w","k1b","b","w")
#############################################################################
            Queen4w4=queen1(q41,q42,q43,q44,q45,q46,q47,q48,black_protector,"q4w","k1b","b","w")
            Queen4w4.check(q41,q42,q43,q44,q45,q46,q47,q48,black_protector,"q4w","k1b","b","w")
#############################################################################
            Queen3w3=queen1(q31,q32,q33,q34,q35,q36,q37,q38,black_protector,"q3w","k1b","b","w")
            Queen3w3.check(q31,q32,q33,q34,q35,q36,q37,q38,black_protector,"q3w","k1b","b","w")
#####################################################################################
            knight1w2=knight1(kn1,black_protector,"kn1w","k1b","b","w")
            knight1w2.check(kn1,black_protector,"kn1w","k1b","b","w")            
##################################################################################
            knight2w2=knight1(kn1,black_protector,"kn2w","k1b","b","w")
            knight2w2.check(kn1,black_protector,"kn2w","k1b","b","w")
##################################################################################
            knight3w3=knight1(kn3,black_protector,"kn3w","k1b","b","w")
            knight3w3.check(kn3,black_protector,"kn3w","k1b","b","w")
##################################################################################
            knight4w4=knight1(kn4,black_protector,"kn4w","k1b","b","w")
            knight4w4.check(kn4,black_protector,"kn4w","k1b","b","w")
##################################################################################
            knight5w2=knight1(kn5,black_protector,"kn5w","k1b","b","w")
            knight5w2.check(kn5,black_protector,"kn5w","k1b","b","w") 
#######################################################################################
            Rook1w2=rook1(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")
            Rook1w2.check(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")
###############################################################################################
            Rook2w2=rook1(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")
            Rook2w2.check(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")
###############################################################################################
            Rook3w2=rook1(r31,r32,r33,r34,black_protector,"r3w","k1b","b","w")
            Rook3w2.check(r31,r32,r33,r34,black_protector,"r3w","k1b","b","w")
###############################################################################################
            Rook4w2=rook1(r41,r42,r43,r44,black_protector,"r4w","k1b","b","w")
            Rook4w2.check(r41,r42,r43,r44,black_protector,"r4w","k1b","b","w")
###############################################################################################
            Rook5w2=rook1(r51,r52,r53,r54,black_protector,"r5w","k1b","b","w")
            Rook5w2.check(r51,r52,r53,r54,black_protector,"r5w","k1b","b","w")
########################################################################################
            King1w2=king1(k1w,"k1w","b","w")
            King1w2.check(k1w,"k1w","b","w")
#####################################################################################
            Pawn1w2=pawn1w(p1,"p1w","b","w")
            Pawn1w2.check(p1,"p1w","b","w")
####################################################################
            Pawn2w2=pawn1w(p2,"p2w","b","w")
            Pawn2w2.check(p2,"p2w","b","w")
####################################################################
            Pawn3w2=pawn1w(p3,"p3w","b","w")
            Pawn3w2.check(p3,"p3w","b","w")
####################################################################
            Pawn4w2=pawn1w(p4,"p4w","b","w")
            Pawn4w2.check(p4,"p4w","b","w")
####################################################################
            Pawn5w2=pawn1w(p5,"p5w","b","w")
            Pawn5w2.check(p5,"p5w","b","w")
####################################################################
            Pawn6w2=pawn1w(p6,"p6w","b","w")
            Pawn6w2.check(p6,"p6w","b","w")
####################################################################
            Pawn7w2=pawn1w(p7,"p7w","b","w")
            Pawn7w2.check(p7,"p7w","b","w")
####################################################################
            Pawn8w2=pawn1w(p8,"p8w","b","w")
            Pawn8w2.check(p8,"p8w","b","w")
####################################################################
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition
            attack_positions=[]
            attack=[]
            
            for ju in range (0,len(r11)):
                if xposition==r11[ju][0] and yposition==r11[ju][1]:
                    black_check=True
                    attack.append(["r1w"])
                    attack_positions=r11
            for ju in range (0,len(r12)):
                if xposition==r12[ju][0] and yposition==r12[ju][1]:
                    black_check=True
                    attack.append(["r1w"])
                    attack_positions=r12
            for ju in range (0,len(r13)):
                if xposition==r13[ju][0] and yposition==r13[ju][1]:
                    black_check=True
                    attack.append(["r1w"])
                    attack_positions=r13
            for ju in range (0,len(r14)):
                if xposition==r14[ju][0] and yposition==r14[ju][1]:
                    black_check=True
                    attack.append(["r1w"])
                    attack_positions=r14
                    
            for ju in range (0,len(r21)):
                if xposition==r21[ju][0] and yposition==r21[ju][1]:
                    black_check=True
                    attack.append(["r2w"])
                    attack_positions=r21
            for ju in range (0,len(r22)):
                if xposition==r22[ju][0] and yposition==r22[ju][1]:
                    black_check=True
                    attack.append(["r2w"])
                    attack_positions=r22
            for ju in range (0,len(r23)):
                if xposition==r23[ju][0] and yposition==r23[ju][1]:
                    black_check=True
                    attack.append(["r2w"])
                    attack_positions=r23
            for ju in range (0,len(r24)):
                if xposition==r24[ju][0] and yposition==r24[ju][1]:
                    black_check=True
                    attack.append(["r2w"])
                    attack_positions=r24

            for ju in range (0,len(r31)):
                if xposition==r31[ju][0] and yposition==r31[ju][1]:
                    black_check=True
                    attack.append(["r3w"])
                    attack_positions=r31
            for ju in range (0,len(r32)):
                if xposition==r32[ju][0] and yposition==r32[ju][1]:
                    black_check=True
                    attack.append(["r3w"])
                    attack_positions=r32
            for ju in range (0,len(r33)):
                if xposition==r33[ju][0] and yposition==r33[ju][1]:
                    black_check=True
                    attack.append(["r3w"])
                    attack_positions=r33
            for ju in range (0,len(r34)):
                if xposition==r34[ju][0] and yposition==r34[ju][1]:
                    black_check=True
                    attack.append(["r3w"])
                    attack_positions=r34

            for ju in range (0,len(r41)):
                if xposition==r41[ju][0] and yposition==r41[ju][1]:
                    black_check=True
                    attack.append(["r4w"])
                    attack_positions=r41
            for ju in range (0,len(r42)):
                if xposition==r42[ju][0] and yposition==r42[ju][1]:
                    black_check=True
                    attack.append(["r4w"])
                    attack_positions=r42
            for ju in range (0,len(r43)):
                if xposition==r43[ju][0] and yposition==r43[ju][1]:
                    black_check=True
                    attack.append(["r4w"])
                    attack_positions=r43
            for ju in range (0,len(r44)):
                if xposition==r44[ju][0] and yposition==r44[ju][1]:
                    black_check=True
                    attack.append(["r4w"])
                    attack_positions=r44

            for ju in range (0,len(r51)):
                if xposition==r51[ju][0] and yposition==r51[ju][1]:
                    black_check=True
                    attack.append(["r5w"])
                    attack_positions=r51
            for ju in range (0,len(r52)):
                if xposition==r52[ju][0] and yposition==r52[ju][1]:
                    black_check=True
                    attack.append(["r5w"])
                    attack_positions=r52
            for ju in range (0,len(r53)):
                if xposition==r53[ju][0] and yposition==r53[ju][1]:
                    black_check=True
                    attack.append(["r5w"])
                    attack_positions=r53
            for ju in range (0,len(r54)):
                if xposition==r54[ju][0] and yposition==r54[ju][1]:
                    black_check=True
                    attack.append(["r5w"])
                    attack_positions=r54
                    
            for ju in range (0,len(b11)):
                if xposition==b11[ju][0] and yposition==b11[ju][1]:
                    black_check=True
                    attack.append(["b1w"])
                    attack_positions=b11
            for ju in range (0,len(b12)):
                if xposition==b12[ju][0] and yposition==b12[ju][1]:
                    black_check=True
                    attack_positions=b12
                    attack.append(["b1w"])
            for ju in range (0,len(b13)):
                if xposition==b13[ju][0] and yposition==b13[ju][1]:
                    black_check=True
                    attack.append(["b1w"])
                    attack_positions=b13
            for ju in range (0,len(b14)):
                if xposition==b14[ju][0] and yposition==b14[ju][1]:
                    black_check=True
                    attack.append(["b1w"])
                    attack_positions=b14

                    
            for ju in range (0,len(b21)):
                if xposition==b21[ju][0] and yposition==b21[ju][1]:
                    black_check=True
                    attack.append(["b2w"])
                    attack_positions=b21
            for ju in range (0,len(b22)):
                if xposition==b22[ju][0] and yposition==b22[ju][1]:
                    black_check=True
                    attack.append(["b2w"])
                    attack_positions=b22
            for ju in range (0,len(b23)):
                if xposition==b23[ju][0] and yposition==b23[ju][1]:
                    black_check=True
                    attack.append(["b2w"])
                    attack_positions=b23
            for ju in range (0,len(b24)):
                if xposition==b24[ju][0] and yposition==b24[ju][1]:
                    black_check=True
                    attack.append(["b2w"])
                    attack_positions=b24

            for ju in range (0,len(b31)):
                if xposition==b31[ju][0] and yposition==b31[ju][1]:
                    black_check=True
                    attack.append(["b3w"])
                    attack_positions=b31
            for ju in range (0,len(b32)):
                if xposition==b32[ju][0] and yposition==b32[ju][1]:
                    black_check=True
                    attack.append(["b3w"])
                    attack_positions=b32
            for ju in range (0,len(b33)):
                if xposition==b33[ju][0] and yposition==b33[ju][1]:
                    black_check=True
                    attack.append(["b3w"])
                    attack_positions=b33
            for ju in range (0,len(b34)):
                if xposition==b34[ju][0] and yposition==b34[ju][1]:
                    black_check=True
                    attack.append(["b3w"])
                    attack_positions=b34

            for ju in range (0,len(b41)):
                if xposition==b41[ju][0] and yposition==b41[ju][1]:
                    black_check=True
                    attack.append(["b4w"])
                    attack_positions=b41
            for ju in range (0,len(b42)):
                if xposition==b42[ju][0] and yposition==b42[ju][1]:
                    black_check=True
                    attack.append(["b4w"])
                    attack_positions=b42
            for ju in range (0,len(b43)):
                if xposition==b43[ju][0] and yposition==b43[ju][1]:
                    black_check=True
                    attack.append(["b4w"])
                    attack_positions=b43
            for ju in range (0,len(b44)):
                if xposition==b44[ju][0] and yposition==b44[ju][1]:
                    black_check=True
                    attack.append(["b4w"])
                    attack_positions=b44

            for ju in range (0,len(b51)):
                if xposition==b51[ju][0] and yposition==b51[ju][1]:
                    black_check=True
                    attack.append(["b5w"])
                    attack_positions=b51
            for ju in range (0,len(b52)):
                if xposition==b52[ju][0] and yposition==b52[ju][1]:
                    black_check=True
                    attack.append(["b5w"])
                    attack_positions=b52
            for ju in range (0,len(b53)):
                if xposition==b53[ju][0] and yposition==b53[ju][1]:
                    black_check=True
                    attack.append(["b5w"])
                    attack_positions=b53
            for ju in range (0,len(b54)):
                if xposition==b54[ju][0] and yposition==b54[ju][1]:
                    black_check=True
                    attack.append(["b5w"])
                    attack_positions=b54
                    
            for ju in range (0,len(kn1)):
                if xposition==kn1[ju][0] and yposition==kn1[ju][1]:
                    black_check=True
                    attack.append(["kn1w"])

            for ju in range (0,len(kn2)):
                if xposition==kn2[ju][0] and yposition==kn2[ju][1]:
                    black_check=True
                    attack.append(["kn2w"])

            for ju in range (0,len(kn3)):
                if xposition==kn3[ju][0] and yposition==kn3[ju][1]:
                    black_check=True
                    attack.append(["kn3w"])

            for ju in range (0,len(kn4)):
                if xposition==kn4[ju][0] and yposition==kn4[ju][1]:
                    black_check=True
                    attack.append(["kn4w"])

            for ju in range (0,len(kn5)):
                if xposition==kn5[ju][0] and yposition==kn5[ju][1]:
                    black_check=True
                    attack.append(["kn5w"])
                    
            for ju in range (0,len(k1w)):
                if xposition==k1w[ju][0] and yposition==k1w[ju][1]:
                    black_check=True
                    attack.append(["k1w"])
                    attack_positions=k1w

                    
            for ju in range (0,len(q11)):
                if xposition==q11[ju][0] and yposition==q11[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q11
            for ju in range (0,len(q12)):
                if xposition==q12[ju][0] and yposition==q12[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q12
            for ju in range (0,len(q13)):
                if xposition==q13[ju][0] and yposition==q13[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q13
            for ju in range (0,len(q14)):
                if xposition==q14[ju][0] and yposition==q14[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q14
            for ju in range (0,len(q15)):
                if xposition==q15[ju][0] and yposition==q15[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q15
            for ju in range (0,len(q16)):
                if xposition==q16[ju][0] and yposition==q16[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q16
            for ju in range (0,len(q17)):
                if xposition==q17[ju][0] and yposition==q17[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q17
            for ju in range (0,len(q18)):
                if xposition==q18[ju][0] and yposition==q18[ju][1]:
                    black_check=True
                    attack.append(["q1w"])
                    attack_positions=q18

            for ju in range (0,len(q21)):
                if xposition==q21[ju][0] and yposition==q21[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q21
            for ju in range (0,len(q22)):
                if xposition==q22[ju][0] and yposition==q22[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q22
            for ju in range (0,len(q23)):
                if xposition==q23[ju][0] and yposition==q23[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q23
            for ju in range (0,len(q24)):
                if xposition==q24[ju][0] and yposition==q24[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q24
            for ju in range (0,len(q25)):
                if xposition==q25[ju][0] and yposition==q25[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q25
            for ju in range (0,len(q26)):
                if xposition==q26[ju][0] and yposition==q26[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q26
            for ju in range (0,len(q27)):
                if xposition==q27[ju][0] and yposition==q27[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q27
            for ju in range (0,len(q28)):
                if xposition==q28[ju][0] and yposition==q28[ju][1]:
                    black_check=True
                    attack.append(["q2w"])
                    attack_positions=q28

            for ju in range (0,len(q31)):
                if xposition==q31[ju][0] and yposition==q31[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q31
            for ju in range (0,len(q32)):
                if xposition==q32[ju][0] and yposition==q32[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q32
            for ju in range (0,len(q33)):
                if xposition==q33[ju][0] and yposition==q33[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q33
            for ju in range (0,len(q34)):
                if xposition==q34[ju][0] and yposition==q34[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q34
            for ju in range (0,len(q35)):
                if xposition==q35[ju][0] and yposition==q35[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q35
            for ju in range (0,len(q36)):
                if xposition==q36[ju][0] and yposition==q36[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q36
            for ju in range (0,len(q37)):
                if xposition==q37[ju][0] and yposition==q37[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q37
            for ju in range (0,len(q38)):
                if xposition==q38[ju][0] and yposition==q38[ju][1]:
                    black_check=True
                    attack.append(["q3w"])
                    attack_positions=q38

            for ju in range (0,len(q41)):
                if xposition==q41[ju][0] and yposition==q41[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q41
            for ju in range (0,len(q42)):
                if xposition==q42[ju][0] and yposition==q42[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q42
            for ju in range (0,len(q43)):
                if xposition==q43[ju][0] and yposition==q43[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q43
            for ju in range (0,len(q44)):
                if xposition==q44[ju][0] and yposition==q44[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q44
            for ju in range (0,len(q45)):
                if xposition==q45[ju][0] and yposition==q45[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q45
            for ju in range (0,len(q46)):
                if xposition==q46[ju][0] and yposition==q46[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q46
            for ju in range (0,len(q47)):
                if xposition==q47[ju][0] and yposition==q47[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q47
            for ju in range (0,len(q48)):
                if xposition==q48[ju][0] and yposition==q48[ju][1]:
                    black_check=True
                    attack.append(["q4w"])
                    attack_positions=q48
                    
            for ju in range (0,len(p1)):
                if xposition==p1[ju][0] and yposition==p1[ju][1]:
                    black_check=True
                    attack.append(["p1w"])
                    
            for ju in range (0,len(p2)):
                if xposition==p2[ju][0] and yposition==p2[ju][1]:
                    black_check=True
                    attack.append(["p2w"])
                    
            for ju in range (0,len(p3)):
                if xposition==p3[ju][0] and yposition==p3[ju][1]:
                    black_check=True
                    attack.append(["p3w"])
                    
            for ju in range (0,len(p4)):
                if xposition==p4[ju][0] and yposition==p4[ju][1]:
                    black_check=True
                    attack.append(["p4w"])
                    
            for ju in range (0,len(p5)):
                if xposition==p5[ju][0] and yposition==p5[ju][1]:
                    black_check=True
                    attack.append(["p5w"])
                    
            for ju in range (0,len(p6)):
                if xposition==p6[ju][0] and yposition==p6[ju][1]:
                    black_check=True
                    attack.append(["p6w"])
                    
            for ju in range (0,len(p7)):
                if xposition==p7[ju][0] and yposition==p7[ju][1]:
                    black_check=True
                    attack.append(["p7w"])
                    
            for ju in range (0,len(p8)):               
                if xposition==p8[ju][0] and yposition==p8[ju][1]:
                    black_check=True
                    attack.append(["p8w"])
                    
            all_white=[]
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition
            for i in range (0,len(r11)):
                if r11!=[]:
                    all_white.append(r11[i])
                    if r11[len(r11)-1][0]==xposition and r11[len(r11)-1][1]==yposition:
                        r112=(r11[(len(r11))-1][0])
                        r113=(r11[(len(r11))-1][1])                
                        r111=[r112,r113+60]
                        all_white.append(r111)
                
            for i in range (0,len(r12)):
                if r12!=[]:
                    all_white.append(r12[i])
                    if r12[len(r12)-1][0]==xposition and r12[len(r12)-1][1]==yposition:
                        r122=(r12[(len(r12))-1][0])
                        r123=(r12[(len(r12))-1][1])                
                        r121=[r122,r123-60]
                        all_white.append(r121)
                
            for i in range (0,len(r13)):
                if r13!=[]:
                    all_white.append(r13[i])
                    if r13[len(r13)-1][0]==xposition and r13[len(r13)-1][1]==yposition:
                        r132=(r13[(len(r13))-1][0])
                        r133=(r13[(len(r13))-1][1])                
                        r131=[r132+60,r133]
                        all_white.append(r131)
                
            for i in range (0,len(r14)):
                if r14!=[]:
                    all_white.append(r14[i])
                    if r14[len(r14)-1][0]==xposition and r14[len(r14)-1][1]==yposition:
                        r142=(r14[(len(r14))-1][0])
                        r143=(r14[(len(r14))-1][1])                
                        r141=[r142-60,r143]
                        all_white.append(r141)
                        
            for i in range (0,len(r21)):
                if r21!=[]:
                    all_white.append(r21[i])
                    if r21[len(r21)-1][0]==xposition and r21[len(r21)-1][1]==yposition:
                        r212=(r21[(len(r21))-1][0])
                        r213=(r21[(len(r21))-1][1])                
                        r211=[r212,r213+60]
                        all_white.append(r211)
                
            for i in range (0,len(r22)):
                if r22!=[]:
                    all_white.append(r22[i])
                    if r22[len(r22)-1][0]==xposition and r22[len(r22)-1][1]==yposition:
                        r222=(r22[(len(r22))-1][0])
                        r223=(r22[(len(r22))-1][1])                
                        r221=[r222,r223-60]
                        all_white.append(r221)
                
            for i in range (0,len(r23)):
                if r23!=[]:
                    all_white.append(r23[i])
                    if r23[len(r23)-1][0]==xposition and r23[len(r23)-1][1]==yposition:
                        r232=(r23[(len(r23))-1][0])
                        r233=(r23[(len(r23))-1][1])                
                        r231=[r232+60,r233]
                        all_white.append(r231)
                
            for i in range (0,len(r24)):
                if r24!=[]:
                    all_white.append(r24[i])
                    if r24[len(r24)-1][0]==xposition and r24[len(r24)-1][1]==yposition:
                        r242=(r24[(len(r24))-1][0])
                        r243=(r24[(len(r24))-1][1])                
                        r241=[r242-60,r243]
                        all_white.append(r241)
            for i in range (0,len(r31)):
                if r31!=[]:
                    all_white.append(r31[i])
                    if r31[len(r31)-1][0]==xposition and r31[len(r31)-1][1]==yposition:
                        r312=(r31[(len(r31))-1][0])
                        r313=(r31[(len(r31))-1][1])                
                        r311=[r312,r313+60]
                        all_white.append(r311)
                
            for i in range (0,len(r32)):
                if r32!=[]:
                    all_white.append(r32[i])
                    if r32[len(r32)-1][0]==xposition and r32[len(r32)-1][1]==yposition:
                        r322=(r32[(len(r32))-1][0])
                        r323=(r32[(len(r32))-1][1])                
                        r321=[r322,r323-60]
                        all_white.append(r321)
                
            for i in range (0,len(r33)):
                if r33!=[]:
                    all_white.append(r33[i])
                    if r33[len(r33)-1][0]==xposition and r33[len(r33)-1][1]==yposition:
                        r332=(r33[(len(r33))-1][0])
                        r333=(r33[(len(r33))-1][1])                
                        r331=[r332+60,r333]
                        all_white.append(r331)
                
            for i in range (0,len(r34)):
                if r34!=[]:
                    all_white.append(r34[i])
                    if r34[len(r34)-1][0]==xposition and r34[len(r34)-1][1]==yposition:
                        r342=(r34[(len(r34))-1][0])
                        r343=(r34[(len(r34))-1][1])                
                        r341=[r342-60,r343]
                        all_white.append(r341)

            for i in range (0,len(r41)):
                if r41!=[]:
                    all_white.append(r41[i])
                    if r41[len(r41)-1][0]==xposition and r41[len(r41)-1][1]==yposition:
                        r412=(r41[(len(r41))-1][0])
                        r413=(r41[(len(r41))-1][1])                
                        r411=[r412,r413+60]
                        all_white.append(r411)
                
            for i in range (0,len(r42)):
                if r42!=[]:
                    all_white.append(r42[i])
                    if r42[len(r42)-1][0]==xposition and r42[len(r42)-1][1]==yposition:
                        r422=(r42[(len(r42))-1][0])
                        r423=(r42[(len(r42))-1][1])                
                        r421=[r422,r423-60]
                        all_white.append(r421)
                
            for i in range (0,len(r43)):
                if r43!=[]:
                    all_white.append(r43[i])
                    if r43[len(r43)-1][0]==xposition and r43[len(r43)-1][1]==yposition:
                        r432=(r43[(len(r43))-1][0])
                        r433=(r43[(len(r43))-1][1])                
                        r431=[r432+60,r433]
                        all_white.append(r431)
                
            for i in range (0,len(r44)):
                if r44!=[]:
                    all_white.append(r44[i])
                    if r44[len(r44)-1][0]==xposition and r44[len(r44)-1][1]==yposition:
                        r442=(r44[(len(r44))-1][0])
                        r443=(r44[(len(r44))-1][1])                
                        r441=[r442-60,r443]
                        all_white.append(r441)

                        
            for i in range (0,len(r51)):
                if r51!=[]:
                    all_white.append(r51[i])
                    if r51[len(r51)-1][0]==xposition and r51[len(r51)-1][1]==yposition:
                        r512=(r51[(len(r51))-1][0])
                        r513=(r51[(len(r51))-1][1])                
                        r511=[r512,r513+60]
                        all_white.append(r511)
                
            for i in range (0,len(r52)):
                if r52!=[]:
                    all_white.append(r52[i])
                    if r52[len(r52)-1][0]==xposition and r52[len(r52)-1][1]==yposition:
                        r522=(r52[(len(r52))-1][0])
                        r523=(r52[(len(r52))-1][1])                
                        r521=[r522,r523-60]
                        all_white.append(r521)
                
            for i in range (0,len(r53)):
                if r53!=[]:
                    all_white.append(r53[i])
                    if r53[len(r53)-1][0]==xposition and r53[len(r53)-1][1]==yposition:
                        r532=(r53[(len(r53))-1][0])
                        r533=(r53[(len(r53))-1][1])                
                        r531=[r532+60,r533]
                        all_white.append(r531)
                
            for i in range (0,len(r54)):
                if r54!=[]:
                    all_white.append(r54[i])
                    if r54[len(r54)-1][0]==xposition and r54[len(r54)-1][1]==yposition:
                        r542=(r54[(len(r54))-1][0])
                        r543=(r54[(len(r54))-1][1])                
                        r541=[r542-60,r543]
                        all_white.append(r541)

            for i in range (0,len(b11)):
                if b11!=[]:
                    all_white.append(b11[i])
                    if b11[len(b11)-1][0]==xposition and b11[len(b11)-1][1]==yposition:
                        b112=(b11[(len(b11))-1][0])
                        b113=(b11[(len(b11))-1][1])                
                        b111=[b112+60,b113+60]
                        all_white.append(b111)
                
            for i in range (0,len(b12)):
                if b12!=[]:
                    all_white.append(b12[i])
                    if b12[len(b12)-1][0]==xposition and b12[len(b12)-1][1]==yposition:
                        b122=(b12[(len(b12))-1][0])
                        b123=(b12[(len(b12))-1][1])                
                        b121=[b122-60,b123-60]
                        all_white.append(b121)
                
            for i in range (0,len(b13)):
                if b13!=[]:
                    all_white.append(b13[i])
                    if b13[len(b13)-1][0]==xposition and b13[len(b13)-1][1]==yposition:
                        b132=(b13[(len(b13))-1][0])
                        b133=(b13[(len(b13))-1][1])                
                        b131=[b132+60,b133-60]
                        all_white.append(b131)
                
            for i in range (0,len(b14)):
                if b14!=[]:
                    all_white.append(b14[i])
                    if b14[len(b14)-1][0]==xposition and b14[len(b14)-1][1]==yposition:
                        b142=(b14[(len(b14))-1][0])
                        b143=(b14[(len(b14))-1][1])                
                        b141=[b142-60,b143+60]
                        all_white.append(b141)
                        
            for i in range (0,len(b21)):
                if b21!=[]:
                    all_white.append(b21[i])
                    if b21[len(b21)-1][0]==xposition and b21[len(b21)-1][1]==yposition:
                        b212=(b21[(len(b21))-1][0])
                        b213=(b21[(len(b21))-1][1])                
                        b211=[b212+60,b213+60]
                        all_white.append(b211)
                
            for i in range (0,len(b22)):
                if b22!=[]:
                    all_white.append(b22[i])
                    if b22[len(b22)-1][0]==xposition and b22[len(b22)-1][1]==yposition:
                        b222=(b22[(len(b22))-1][0])
                        b223=(b22[(len(b22))-1][1])                
                        b221=[b222-60,b223-60]
                        all_white.append(b221)
                
            for i in range (0,len(b23)):
                if b23!=[]:
                    all_white.append(b23[i])
                    if b23[len(b23)-1][0]==xposition and b23[len(b23)-1][1]==yposition:
                        b232=(b23[(len(b23))-1][0])
                        b233=(b23[(len(b23))-1][1])                
                        b231=[b232+60,b233-60]
                        all_white.append(b231)
                
            for i in range (0,len(b24)):
                if b24!=[]:
                    all_white.append(b24[i])
                    if b24[len(b24)-1][0]==xposition and b24[len(b24)-1][1]==yposition:
                        b242=(b24[(len(b24))-1][0])
                        b243=(b24[(len(b24))-1][1])                
                        b241=[b242-60,b243+60]
                        all_white.append(b241)
                        
            for i in range (0,len(b31)):
                if b31!=[]:
                    all_white.append(b31[i])
                    if b31[len(b31)-1][0]==xposition and b31[len(b31)-1][1]==yposition:
                        b312=(b31[(len(b31))-1][0])
                        b313=(b31[(len(b31))-1][1])                
                        b311=[b312+60,b313+60]
                        all_white.append(b311)
                
            for i in range (0,len(b32)):
                if b32!=[]:
                    all_white.append(b32[i])
                    if b32[len(b32)-1][0]==xposition and b32[len(b32)-1][1]==yposition:
                        b322=(b32[(len(b32))-1][0])
                        b323=(b32[(len(b32))-1][1])                
                        b321=[b322-60,b323-60]
                        all_white.append(b321)
                
            for i in range (0,len(b33)):
                if b33!=[]:
                    all_white.append(b33[i])
                    if b33[len(b33)-1][0]==xposition and b33[len(b33)-1][1]==yposition:
                        b332=(b33[(len(b33))-1][0])
                        b333=(b33[(len(b33))-1][1])                
                        b331=[b332+60,b333-60]
                        all_white.append(b331)
                
            for i in range (0,len(b34)):
                if b34!=[]:
                    all_white.append(b34[i])
                    if b34[len(b34)-1][0]==xposition and b34[len(b34)-1][1]==yposition:
                        b342=(b34[(len(b34))-1][0])
                        b343=(b34[(len(b34))-1][1])                
                        b341=[b342-60,b343+60]
                        all_white.append(b341)
                        

            for i in range (0,len(b41)):
                if b41!=[]:
                    all_white.append(b41[i])
                    if b41[len(b41)-1][0]==xposition and b41[len(b41)-1][1]==yposition:
                        b412=(b41[(len(b41))-1][0])
                        b413=(b41[(len(b41))-1][1])                
                        b411=[b412+60,b413+60]
                        all_white.append(b411)
                
            for i in range (0,len(b42)):
                if b42!=[]:
                    all_white.append(b42[i])
                    if b42[len(b42)-1][0]==xposition and b42[len(b42)-1][1]==yposition:
                        b422=(b42[(len(b42))-1][0])
                        b423=(b42[(len(b42))-1][1])                
                        b421=[b422-60,b423-60]
                        all_white.append(b421)
                
            for i in range (0,len(b43)):
                if b43!=[]:
                    all_white.append(b43[i])
                    if b43[len(b43)-1][0]==xposition and b43[len(b43)-1][1]==yposition:
                        b432=(b43[(len(b43))-1][0])
                        b433=(b43[(len(b43))-1][1])                
                        b431=[b432+60,b433-60]
                        all_white.append(b431)
                
            for i in range (0,len(b44)):
                if b44!=[]:
                    all_white.append(b44[i])
                    if b44[len(b44)-1][0]==xposition and b44[len(b44)-1][1]==yposition:
                        b442=(b44[(len(b44))-1][0])
                        b443=(b44[(len(b44))-1][1])                
                        b441=[b442-60,b443+60]
                        all_white.append(b441)
                        
            for i in range (0,len(b51)):
                if b51!=[]:
                    all_white.append(b51[i])
                    if b51[len(b51)-1][0]==xposition and b51[len(b51)-1][1]==yposition:
                        b512=(b51[(len(b51))-1][0])
                        b513=(b51[(len(b51))-1][1])                
                        b511=[b512+60,b513+60]
                        all_white.append(b511)
                
            for i in range (0,len(b52)):
                if b52!=[]:
                    all_white.append(b52[i])
                    if b52[len(b52)-1][0]==xposition and b52[len(b52)-1][1]==yposition:
                        b522=(b52[(len(b52))-1][0])
                        b523=(b52[(len(b52))-1][1])                
                        b521=[b522-60,b523-60]
                        all_white.append(b521)
                
            for i in range (0,len(b53)):
                if b53!=[]:
                    all_white.append(b53[i])
                    if b53[len(b53)-1][0]==xposition and b53[len(b53)-1][1]==yposition:
                        b532=(b53[(len(b53))-1][0])
                        b533=(b53[(len(b53))-1][1])                
                        b531=[b532+60,b533-60]
                        all_white.append(b531)
                
            for i in range (0,len(b54)):
                if b54!=[]:
                    all_white.append(b54[i])
                    if b54[len(b54)-1][0]==xposition and b54[len(b54)-1][1]==yposition:
                        b542=(b54[(len(b54))-1][0])
                        b543=(b54[(len(b54))-1][1])                
                        b541=[b542-60,b543+60]
                        all_white.append(b541)
                        
                    
            for i in range (0,len(kn1)):
                if kn1!=[]:
                    all_white.append(kn1[i])
                    
            for i in range (0,len(kn2)):
                if kn2!=[]:
                    all_white.append(kn2[i])

            for i in range (0,len(kn3)):
                if kn3!=[]:
                    all_white.append(kn3[i])

            for i in range (0,len(kn4)):
                if kn4!=[]:
                    all_white.append(kn4[i])

            for i in range (0,len(kn5)):
                if kn5!=[]:
                    all_white.append(kn5[i])
                    
            for i in range (0,len(q11)):
                if q11!=[]:
                    all_white.append(q11[i])
                    if q11[len(q11)-1][0]==xposition and q11[len(q11)-1][1]==yposition:
                        q112=(q11[(len(q11))-1][0])
                        q113=(q11[(len(q11))-1][1])                
                        q111=[q112+60,q113+60]
                        all_white.append(q111)
                
            for i in range (0,len(q12)):
                if q12!=[]:
                    all_white.append(q12[i])
                    if q12[len(q12)-1][0]==xposition and q12[len(q12)-1][1]==yposition:
                        q122=(q12[(len(q12))-1][0])
                        q123=(q12[(len(q12))-1][1])                
                        q121=[q122-60,q123-60]
                        all_white.append(q121)
                
            for i in range (0,len(q13)):
                if q13!=[]:
                    all_white.append(q13[i])
                    if q13[len(q13)-1][0]==xposition and q13[len(q13)-1][1]==yposition:
                        q132=(q13[(len(q13))-1][0])
                        q133=(q13[(len(q13))-1][1])                
                        q131=[q132+60,q133-60]
                        all_white.append(q131)
                
            for i in range (0,len(q14)):
                if q14!=[]:
                    all_white.append(q14[i])
                    if q14[len(q14)-1][0]==xposition and q14[len(q14)-1][1]==yposition:
                        q142=(q14[(len(q14))-1][0])
                        q143=(q14[(len(q14))-1][1])                
                        q141=[q142-60,q143+60]
                        all_white.append(q141)
            for i in range (0,len(q15)):
                if q15!=[]:
                    all_white.append(q15[i])
                    if q15[len(q15)-1][0]==xposition and q15[len(q15)-1][1]==yposition:
                        q152=(q15[(len(q15))-1][0])
                        q153=(q15[(len(q15))-1][1])                
                        q151=[q152,q153+60]
                        all_white.append(q151)
                
            for i in range (0,len(q16)):
                if q16!=[]:
                    all_white.append(q16[i])
                    if q16[len(q16)-1][0]==xposition and q16[len(q16)-1][1]==yposition:
                        q162=(q16[(len(q16))-1][0])
                        q163=(q16[(len(q16))-1][1])                
                        q161=[q162,q163-60]
                        all_white.append(q161)
                
            for i in range (0,len(q17)):
                if q17!=[]:
                    all_white.append(q17[i])
                    if q17[len(q17)-1][0]==xposition and q17[len(q17)-1][1]==yposition:
                        q172=(q17[(len(q17))-1][0])
                        q173=(q17[(len(q17))-1][1])                
                        q171=[q172+60,q173]
                        all_white.append(q171)
                
            for i in range (0,len(q18)):
                if q18!=[]:
                    all_white.append(q18[i])
                    if q18[len(q18)-1][0]==xposition and q18[len(q18)-1][1]==yposition:
                        q182=(q18[(len(q18))-1][0])
                        q183=(q18[(len(q18))-1][1])                
                        q181=[q182-60,q183]
                        all_white.append(q181)

            for i in range (0,len(q21)):
                if q21!=[]:
                    all_white.append(q21[i])
                    if q21[len(q21)-1][0]==xposition and q21[len(q21)-1][1]==yposition:
                        q212=(q21[(len(q21))-1][0])
                        q213=(q21[(len(q21))-1][1])                
                        q211=[q212+60,q213+60]
                        all_white.append(q211)
                
            for i in range (0,len(q22)):
                if q22!=[]:
                    all_white.append(q22[i])
                    if q22[len(q22)-1][0]==xposition and q22[len(q22)-1][1]==yposition:
                        q222=(q22[(len(q22))-1][0])
                        q223=(q22[(len(q22))-1][1])                
                        q221=[q222-60,q223-60]
                        all_white.append(q221)
                
            for i in range (0,len(q23)):
                if q23!=[]:
                    all_white.append(q23[i])
                    if q23[len(q23)-1][0]==xposition and q23[len(q23)-1][1]==yposition:
                        q232=(q23[(len(q23))-1][0])
                        q233=(q23[(len(q23))-1][1])                
                        q231=[q232+60,q233-60]
                        all_white.append(q231)
                
            for i in range (0,len(q24)):
                if q24!=[]:
                    all_white.append(q24[i])
                    if q24[len(q24)-1][0]==xposition and q24[len(q24)-1][1]==yposition:
                        q242=(q24[(len(q24))-1][0])
                        q243=(q24[(len(q24))-1][1])                
                        q241=[q242-60,q243+60]
                        all_white.append(q241)
            for i in range (0,len(q25)):
                if q25!=[]:
                    all_white.append(q25[i])
                    if q25[len(q25)-1][0]==xposition and q25[len(q25)-1][1]==yposition:
                        q252=(q25[(len(q25))-1][0])
                        q253=(q25[(len(q25))-1][1])                
                        q251=[q252,q253+60]
                        all_white.append(q251)
                
            for i in range (0,len(q26)):
                if q26!=[]:
                    all_white.append(q26[i])
                    if q26[len(q26)-1][0]==xposition and q26[len(q26)-1][1]==yposition:
                        q262=(q26[(len(q26))-1][0])
                        q263=(q26[(len(q26))-1][1])                
                        q261=[q262,q263-60]
                        all_white.append(q261)
                
            for i in range (0,len(q27)):
                if q27!=[]:
                    all_white.append(q27[i])
                    if q27[len(q27)-1][0]==xposition and q27[len(q27)-1][1]==yposition:
                        q272=(q27[(len(q27))-1][0])
                        q273=(q27[(len(q27))-1][1])                
                        q271=[q272+60,q273]
                        all_white.append(q271)
                
            for i in range (0,len(q28)):
                if q28!=[]:
                    all_white.append(q28[i])
                    if q28[len(q28)-1][0]==xposition and q28[len(q28)-1][1]==yposition:
                        q282=(q28[(len(q28))-1][0])
                        q283=(q28[(len(q28))-1][1])                
                        q281=[q282-60,q283]
                        all_white.append(q281)

            for i in range (0,len(q31)):
                if q31!=[]:
                    all_white.append(q31[i])
                    if q31[len(q31)-1][0]==xposition and q31[len(q31)-1][1]==yposition:
                        q312=(q31[(len(q31))-1][0])
                        q313=(q31[(len(q31))-1][1])                
                        q311=[q312+60,q313+60]
                        all_white.append(q311)
                
            for i in range (0,len(q32)):
                if q32!=[]:
                    all_white.append(q32[i])
                    if q32[len(q32)-1][0]==xposition and q32[len(q32)-1][1]==yposition:
                        q322=(q32[(len(q32))-1][0])
                        q323=(q32[(len(q32))-1][1])                
                        q321=[q322-60,q323-60]
                        all_white.append(q321)
                
            for i in range (0,len(q33)):
                if q33!=[]:
                    all_white.append(q33[i])
                    if q33[len(q33)-1][0]==xposition and q33[len(q33)-1][1]==yposition:
                        q332=(q33[(len(q33))-1][0])
                        q333=(q33[(len(q33))-1][1])                
                        q331=[q332+60,q333-60]
                        all_white.append(q331)
                
            for i in range (0,len(q34)):
                if q34!=[]:
                    all_white.append(q34[i])
                    if q34[len(q34)-1][0]==xposition and q34[len(q34)-1][1]==yposition:
                        q342=(q34[(len(q34))-1][0])
                        q343=(q34[(len(q34))-1][1])                
                        q341=[q342-60,q343+60]
                        all_white.append(q341)
            for i in range (0,len(q35)):
                if q35!=[]:
                    all_white.append(q35[i])
                    if q35[len(q35)-1][0]==xposition and q35[len(q35)-1][1]==yposition:
                        q352=(q35[(len(q35))-1][0])
                        q353=(q35[(len(q35))-1][1])                
                        q351=[q352,q353+60]
                        all_white.append(q351)
                
            for i in range (0,len(q36)):
                if q36!=[]:
                    all_white.append(q36[i])
                    if q36[len(q36)-1][0]==xposition and q36[len(q36)-1][1]==yposition:
                        q362=(q36[(len(q36))-1][0])
                        q363=(q36[(len(q36))-1][1])                
                        q361=[q362,q363-60]
                        all_white.append(q361)
                
            for i in range (0,len(q37)):
                if q37!=[]:
                    all_white.append(q37[i])
                    if q37[len(q37)-1][0]==xposition and q37[len(q37)-1][1]==yposition:
                        q372=(q37[(len(q37))-1][0])
                        q373=(q37[(len(q37))-1][1])                
                        q371=[q372+60,q373]
                        all_white.append(q371)
                
            for i in range (0,len(q38)):
                if q38!=[]:
                    all_white.append(q38[i])
                    if q38[len(q38)-1][0]==xposition and q38[len(q38)-1][1]==yposition:
                        q382=(q38[(len(q38))-1][0])
                        q383=(q38[(len(q38))-1][1])                
                        q381=[q382-60,q383]
                        all_white.append(q381)


            for i in range (0,len(q41)):
                if q41!=[]:
                    all_white.append(q41[i])
                    if q41[len(q41)-1][0]==xposition and q41[len(q41)-1][1]==yposition:
                        q412=(q41[(len(q41))-1][0])
                        q413=(q41[(len(q41))-1][1])                
                        q411=[q412+60,q413+60]
                        all_white.append(q411)
                
            for i in range (0,len(q42)):
                if q42!=[]:
                    all_white.append(q42[i])
                    if q42[len(q42)-1][0]==xposition and q42[len(q42)-1][1]==yposition:
                        q422=(q42[(len(q42))-1][0])
                        q423=(q42[(len(q42))-1][1])                
                        q421=[q422-60,q423-60]
                        all_white.append(q421)
                
            for i in range (0,len(q43)):
                if q43!=[]:
                    all_white.append(q43[i])
                    if q43[len(q43)-1][0]==xposition and q43[len(q43)-1][1]==yposition:
                        q432=(q43[(len(q43))-1][0])
                        q433=(q43[(len(q43))-1][1])                
                        q431=[q432+60,q433-60]
                        all_white.append(q431)
                
            for i in range (0,len(q44)):
                if q44!=[]:
                    all_white.append(q44[i])
                    if q44[len(q44)-1][0]==xposition and q44[len(q44)-1][1]==yposition:
                        q442=(q44[(len(q44))-1][0])
                        q443=(q44[(len(q44))-1][1])                
                        q441=[q442-60,q443+60]
                        all_white.append(q441)
            for i in range (0,len(q45)):
                if q45!=[]:
                    all_white.append(q45[i])
                    if q45[len(q45)-1][0]==xposition and q45[len(q45)-1][1]==yposition:
                        q452=(q45[(len(q45))-1][0])
                        q453=(q45[(len(q45))-1][1])                
                        q451=[q452,q453+60]
                        all_white.append(q451)
                
            for i in range (0,len(q46)):
                if q46!=[]:
                    all_white.append(q46[i])
                    if q46[len(q46)-1][0]==xposition and q46[len(q46)-1][1]==yposition:
                        q462=(q46[(len(q46))-1][0])
                        q463=(q46[(len(q46))-1][1])                
                        q461=[q462,q463-60]
                        all_white.append(q461)
                
            for i in range (0,len(q47)):
                if q47!=[]:
                    all_white.append(q47[i])
                    if q47[len(q47)-1][0]==xposition and q47[len(q47)-1][1]==yposition:
                        q472=(q47[(len(q47))-1][0])
                        q473=(q47[(len(q47))-1][1])                
                        q471=[q472+60,q473]
                        all_white.append(q471)
                
            for i in range (0,len(q48)):
                if q48!=[]:
                    all_white.append(q48[i])
                    if q48[len(q48)-1][0]==xposition and q48[len(q48)-1][1]==yposition:
                        q482=(q48[(len(q48))-1][0])
                        q483=(q48[(len(q48))-1][1])                
                        q481=[q482-60,q483]
                        all_white.append(q481)
                    
            for i in range (0,len(k1w)):
                if k1w!=[]:
                    all_white.append(k1w[i])
            for i in range (0,len(p1)):
                if p1!=[]:
                    all_white.append(p1[i])
            for i in range (0,len(p2)):
                if p2!=[]:
                    all_white.append(p2[i])
            for i in range (0,len(p3)):
                if p3!=[]:
                    all_white.append(p3[i])
            for i in range (0,len(p4)):
                if p4!=[]:
                    all_white.append(p4[i])
            for i in range (0,len(p5)):
                if p5!=[]:
                    all_white.append(p5[i])
            for i in range (0,len(p6)):
                if p6!=[]:
                    all_white.append(p6[i])
            for i in range (0,len(p7)):
                if p7!=[]:
                    all_white.append(p7[i])
            for i in range (0,len(p8)):
                if p8!=[]:
                    all_white.append(p8[i])
            hb=1


        if hw==0:
            two_protectors=False
            white_protector=[]
            pos_spaces=[]
            Bishop1b2=bishop1(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
            Bishop1b2.check(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
######################################################################################                
            Bishop2b2=bishop1(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")
            Bishop2b2.check(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")
#########################################################################################
            Queen1b2=queen1(q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b,white_protector,"q1b","k1w","w","b")
            Queen1b2.check(q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b,white_protector,"q1b","k1w","w","b")
#############################################################################
            Queen2b2=queen1(q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b,white_protector,"q2b","k1w","w","b")
            Queen2b2.check(q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b,white_protector,"q2b","k1w","w","b")
#####################################################################################
            knight1b2=knight1(kn1b,white_protector,"kn1b","k1w","w","b")
            knight1b2.check(kn1b,white_protector,"kn1b","k1w","w","b")            
##################################################################################
            knight2b2=knight1(kn1b,white_protector,"kn2b","k1w","w","b")
            knight2b2.check(kn1b,white_protector,"kn2b","k1w","w","b") 
#######################################################################################
            Rook1b2=rook1(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")
            Rook1b2.check(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")
###############################################################################################
            Rook2b2=rook1(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")
            Rook2b2.check(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")
########################################################################################
            King1b2=king1(k1b,"k1b","w","b")
            King1b2.check(k1b,"k1b","w","b")
#####################################################################################
            Pawn1b2=pawn1b(p1b,"p1b","w","b")
            Pawn1b2.check(p1b,"p1b","w","b")
####################################################################
            Pawn2b2=pawn1b(p2b,"p2b","w","b")
            Pawn2b2.check(p2b,"p2b","w","b")
####################################################################
            Pawn3b2=pawn1b(p3b,"p3b","w","b")
            Pawn3b2.check(p3b,"p3b","w","b")
####################################################################
            Pawn4b2=pawn1b(p4b,"p4b","w","b")
            Pawn4b2.check(p4b,"p4b","w","b")
####################################################################
            Pawn5b2=pawn1b(p5b,"p5b","w","b")
            Pawn5b2.check(p5b,"p5b","w","b")
####################################################################
            Pawn6b2=pawn1b(p6b,"p6b","w","b")
            Pawn6b2.check(p6b,"p6b","w","b")
####################################################################
            Pawn7b2=pawn1b(p7b,"p7b","w","b")
            Pawn7b2.check(p7b,"p7b","w","b")
####################################################################
            Pawn8b2=pawn1b(p8b,"p8b","w","b")
            Pawn8b2.check(p8b,"p8b","w","b")
####################################################################
    ####################################################################
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition

            
            for ju in range (0,len(r11b)):
                if xposition==r11b[ju][0] and yposition==r11b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r1b"])
                    attack_positions=r11b
            for ju in range (0,len(r12b)):
                if xposition==r12b[ju][0] and yposition==r12b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r1b"])
                    attack_positions=r12b
            for ju in range (0,len(r13b)):
                if xposition==r13b[ju][0] and yposition==r13b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r1b"])
                    attack_positions=r13b
            for ju in range (0,len(r14b)):
                if xposition==r14b[ju][0] and yposition==r14b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r1b"])
                    attack_positions=r14b
                    
            for ju in range (0,len(r21b)):
                if xposition==r21b[ju][0] and yposition==r21b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r2b"])
                    attack_positions=r21b
            for ju in range (0,len(r22b)):
                if xposition==r22b[ju][0] and yposition==r22b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r2b"])
                    attack_positions=r22b
            for ju in range (0,len(r23b)):
                if xposition==r23b[ju][0] and yposition==r23b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r2b"])
                    attack_positions=r23b
            for ju in range (0,len(r24b)):
                if xposition==r24b[ju][0] and yposition==r24b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r2b"])
                    attack_positions=r24b

            for ju in range (0,len(r31b)):
                if xposition==r31b[ju][0] and yposition==r31b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r3b"])
                    attack_positions=r31b
            for ju in range (0,len(r32b)):
                if xposition==r32b[ju][0] and yposition==r32b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r3b"])
                    attack_positions=r32b
            for ju in range (0,len(r33b)):
                if xposition==r33b[ju][0] and yposition==r33b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r3b"])
                    attack_positions=r33b
            for ju in range (0,len(r34b)):
                if xposition==r34b[ju][0] and yposition==r34b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r3b"])
                    attack_positions=r34b

            for ju in range (0,len(r41b)):
                if xposition==r41b[ju][0] and yposition==r41b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r4b"])
                    attack_positions=r41b
            for ju in range (0,len(r42b)):
                if xposition==r42b[ju][0] and yposition==r42b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r4b"])
                    attack_positions=r42b
            for ju in range (0,len(r43b)):
                if xposition==r43b[ju][0] and yposition==r43b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r4b"])
                    attack_positions=r43b
            for ju in range (0,len(r44b)):
                if xposition==r44b[ju][0] and yposition==r44b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r4b"])
                    attack_positions=r44b

            for ju in range (0,len(r51b)):
                if xposition==r51b[ju][0] and yposition==r51b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r5b"])
                    attack_positions=r51b
            for ju in range (0,len(r52b)):
                if xposition==r52b[ju][0] and yposition==r52b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r5b"])
                    attack_positions=r52b
            for ju in range (0,len(r53b)):
                if xposition==r53b[ju][0] and yposition==r53b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r5b"])
                    attack_positions=r53b
            for ju in range (0,len(r54b)):
                if xposition==r54b[ju][0] and yposition==r54b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["r5b"])
                    attack_positions=r54b
                    
            for ju in range (0,len(b11b)):
                if xposition==b11b[ju][0] and yposition==b11b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b1b"])
                    attack_positions=b11b
            for ju in range (0,len(b12b)):
                if xposition==b12b[ju][0] and yposition==b12b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=b12b
                    attack.append(["b1b"])
            for ju in range (0,len(b13b)):
                if xposition==b13b[ju][0] and yposition==b13b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b1b"])
                    attack_positions=b13b
            for ju in range (0,len(b14b)):
                if xposition==b14b[ju][0] and yposition==b14b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b1b"])
                    attack_positions=b14b


                    
            for ju in range (0,len(b21b)):
                if xposition==b21b[ju][0] and yposition==b21b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b2b"])
                    attack_positions=b21b
            for ju in range (0,len(b22b)):
                if xposition==b22b[ju][0] and yposition==b22b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b2b"])
                    attack_positions=b22b
            for ju in range (0,len(b23b)):
                if xposition==b23b[ju][0] and yposition==b23b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b2b"])
                    attack_positions=b23b
            for ju in range (0,len(b24b)):
                if xposition==b24b[ju][0] and yposition==b24b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b2b"])
                    attack_positions=b24b

            for ju in range (0,len(b31b)):
                if xposition==b31b[ju][0] and yposition==b31b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b3b"])
                    attack_positions=b31b
            for ju in range (0,len(b32b)):
                if xposition==b32b[ju][0] and yposition==b32b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b3b"])
                    attack_positions=b32b
            for ju in range (0,len(b33b)):
                if xposition==b33b[ju][0] and yposition==b33b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b3b"])
                    attack_positions=b33b
            for ju in range (0,len(b34b)):
                if xposition==b34b[ju][0] and yposition==b34b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b3b"])
                    attack_positions=b34b

            for ju in range (0,len(b41b)):
                if xposition==b41b[ju][0] and yposition==b41b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b4b"])
                    attack_positions=b41b
            for ju in range (0,len(b42b)):
                if xposition==b42b[ju][0] and yposition==b42b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b4b"])
                    attack_positions=b42b
            for ju in range (0,len(b43b)):
                if xposition==b43b[ju][0] and yposition==b43b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b4b"])
                    attack_positions=b43b
            for ju in range (0,len(b44b)):
                if xposition==b44b[ju][0] and yposition==b44b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b4b"])
                    attack_positions=b44b

            for ju in range (0,len(b51b)):
                if xposition==b51b[ju][0] and yposition==b51b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b5b"])
                    attack_positions=b51b
            for ju in range (0,len(b52b)):
                if xposition==b52b[ju][0] and yposition==b52b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b5b"])
                    attack_positions=b52b
            for ju in range (0,len(b53b)):
                if xposition==b53b[ju][0] and yposition==b53b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b5b"])
                    attack_positions=b53b
            for ju in range (0,len(b54b)):
                if xposition==b54b[ju][0] and yposition==b54b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["b5b"])
                    attack_positions=b54b
                    
            for ju in range (0,len(kn1b)):
                if xposition==kn1b[ju][0] and yposition==kn1b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["kn1b"])

            for ju in range (0,len(kn2b)):
                if xposition==kn2b[ju][0] and yposition==kn2b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["kn2b"])

            for ju in range (0,len(kn3b)):
                if xposition==kn3b[ju][0] and yposition==kn3b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["kn3b"])

            for ju in range (0,len(kn3b)):
                if xposition==kn3b[ju][0] and yposition==kn3b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["kn3b"])

            for ju in range (0,len(kn4b)):
                if xposition==kn4b[ju][0] and yposition==kn4b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["kn4b"])
                    
            for ju in range (0,len(kn5b)):
                if xposition==kn5b[ju][0] and yposition==kn5b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["kn5b"])

                    
            for ju in range (0,len(q11b)):
                if xposition==q11b[ju][0] and yposition==q11b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q11b
                    attack.append(["q1b"])
                    attack_positions=q11b
            for ju in range (0,len(q12b)):
                if xposition==q12b[ju][0] and yposition==q12b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q12b
                    attack.append(["q1b"])
                    attack_positions=q12b
            for ju in range (0,len(q13b)):
                if xposition==q13b[ju][0] and yposition==q13b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q13b
                    attack.append(["q1b"])
                    attack_positions=q13b
            for ju in range (0,len(q14b)):
                if xposition==q14b[ju][0] and yposition==q14b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q14b
                    attack.append(["q1b"])
                    attack_positions=q14b
            for ju in range (0,len(q15b)):
                if xposition==q15b[ju][0] and yposition==q15b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q15b
                    attack.append(["q1b"])
                    attack_positions=q15b
            for ju in range (0,len(q16b)):
                if xposition==q16b[ju][0] and yposition==q16b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q16b
                    attack.append(["q1b"])
                    attack_positions=q16b
            for ju in range (0,len(q17b)):
                if xposition==q17b[ju][0] and yposition==q17b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q17b
                    attack.append(["q1b"])
                    attack_positions=q17b
            for ju in range (0,len(q18b)):
                if xposition==q18b[ju][0] and yposition==q18b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q18b
                    attack.append(["q1b"])
                    attack_positions=q18b

            for ju in range (0,len(q21b)):
                if xposition==q21b[ju][0] and yposition==q21b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q21b
                    attack.append(["q2b"])
                    attack_positions=q21b
            for ju in range (0,len(q22b)):
                if xposition==q22b[ju][0] and yposition==q22b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q22b
                    attack.append(["q2b"])
                    attack_positions=q22b
            for ju in range (0,len(q23b)):
                if xposition==q23b[ju][0] and yposition==q23b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q23b
                    attack.append(["q2b"])
                    attack_positions=q23b
            for ju in range (0,len(q24b)):
                if xposition==q24b[ju][0] and yposition==q24b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q24b
                    attack.append(["q2b"])
                    attack_positions=q24b
            for ju in range (0,len(q25b)):
                if xposition==q25b[ju][0] and yposition==q25b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q25b
                    attack.append(["q2b"])
                    attack_positions=q25b
            for ju in range (0,len(q26b)):
                if xposition==q26b[ju][0] and yposition==q26b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q26b
                    attack.append(["q2b"])
                    attack_positions=q26b
            for ju in range (0,len(q27b)):
                if xposition==q27b[ju][0] and yposition==q27b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q27b
                    attack.append(["q2b"])
                    attack_positions=q27b
            for ju in range (0,len(q28b)):
                if xposition==q28b[ju][0] and yposition==q28b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q28b
                    attack.append(["q2b"])
                    attack_positions=q28b

            for ju in range (0,len(q31b)):
                if xposition==q31b[ju][0] and yposition==q31b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q31b
                    attack.append(["q3b"])
                    attack_positions=q31b
            for ju in range (0,len(q32b)):
                if xposition==q32b[ju][0] and yposition==q32b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q32b
                    attack.append(["q3b"])
                    attack_positions=q32b
            for ju in range (0,len(q33b)):
                if xposition==q33b[ju][0] and yposition==q33b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q33b
                    attack.append(["q3b"])
                    attack_positions=q33b
            for ju in range (0,len(q34b)):
                if xposition==q34b[ju][0] and yposition==q34b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q34b
                    attack.append(["q3b"])
                    attack_positions=q34b
            for ju in range (0,len(q35b)):
                if xposition==q35b[ju][0] and yposition==q35b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q35b
                    attack.append(["q3b"])
                    attack_positions=q35b
            for ju in range (0,len(q36b)):
                if xposition==q36b[ju][0] and yposition==q36b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q36b
                    attack.append(["q3b"])
                    attack_positions=q36b
            for ju in range (0,len(q37b)):
                if xposition==q37b[ju][0] and yposition==q37b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q37b
                    attack.append(["q3b"])
                    attack_positions=q37b
            for ju in range (0,len(q38b)):
                if xposition==q38b[ju][0] and yposition==q38b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q38b
                    attack.append(["q3b"])
                    attack_positions=q38b

            for ju in range (0,len(q41b)):
                if xposition==q41b[ju][0] and yposition==q41b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q41b
                    attack.append(["q4b"])
                    attack_positions=q41b
            for ju in range (0,len(q42b)):
                if xposition==q42b[ju][0] and yposition==q42b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q42b
                    attack.append(["q4b"])
                    attack_positions=q42b
            for ju in range (0,len(q43b)):
                if xposition==q43b[ju][0] and yposition==q43b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q43b
                    attack.append(["q4b"])
                    attack_positions=q43b
            for ju in range (0,len(q44b)):
                if xposition==q44b[ju][0] and yposition==q44b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q44b
                    attack.append(["q4b"])
                    attack_positions=q44b
            for ju in range (0,len(q45b)):
                if xposition==q45b[ju][0] and yposition==q45b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q45b
                    attack.append(["q4b"])
                    attack_positions=q45b
            for ju in range (0,len(q46b)):
                if xposition==q46b[ju][0] and yposition==q46b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q46b
                    attack.append(["q4b"])
                    attack_positions=q46b
            for ju in range (0,len(q47b)):
                if xposition==q47b[ju][0] and yposition==q47b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q47b
                    attack.append(["q4b"])
                    attack_positions=q47b
            for ju in range (0,len(q48b)):
                if xposition==q48b[ju][0] and yposition==q48b[ju][1]:
                    white_check=True
                    attack=[]
                    attack_positions=q48b
                    attack.append(["q4b"])
                    attack_positions=q48b
                    
            for ju in range (0,len(p1b)):
                if xposition==p1b[ju][0] and yposition==p1b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p1b"])
            for ju in range (0,len(p2b)):
                if xposition==p2b[ju][0] and yposition==p2b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p2b"])
            for ju in range (0,len(p3b)):
                if xposition==p3b[ju][0] and yposition==p3b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p3b"])
            for ju in range (0,len(p4b)):
                if xposition==p4b[ju][0] and yposition==p4b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p4b"])
            for ju in range (0,len(p5b)):
                if xposition==p5b[ju][0] and yposition==p5b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p5b"])
            for ju in range (0,len(p6b)):
                if xposition==p6b[ju][0] and yposition==p6b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p6b"])
            for ju in range (0,len(p7b)):
                if xposition==p7b[ju][0] and yposition==p7b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p7b"])
            for ju in range (0,len(p8b)):
                if xposition==p8b[ju][0] and yposition==p8b[ju][1]:
                    white_check=True
                    attack=[]
                    attack.append(["p8b"])
            all_black=[]
            all_white=[]
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition            

            for i in range (0,len(r11b)):
                if r11b!=[]:
                    all_black.append(r11b[i])
                    if r11b[len(r11b)-1][0]==xposition and r11b[len(r11b)-1][1]==yposition:
                        r11b2=(r11b[(len(r11b))-1][0])
                        r11b3=(r11b[(len(r11b))-1][1])                
                        r11b1=[r11b2,r11b3+60]
                        all_black.append(r11b1)
                
            for i in range (0,len(r12b)):
                if r12b!=[]:
                    all_black.append(r12b[i])
                    if r12b[len(r12b)-1][0]==xposition and r12b[len(r12b)-1][1]==yposition:
                        r12b2=(r12b[(len(r12b))-1][0])
                        r12b3=(r12b[(len(r12b))-1][1])                
                        r12b1=[r12b2,r12b3-60]
                        all_black.append(r12b1)
                
            for i in range (0,len(r13b)):
                if r13b!=[]:
                    all_black.append(r13b[i])
                    if r13b[len(r13b)-1][0]==xposition and r13b[len(r13b)-1][1]==yposition:
                        r13b2=(r13b[(len(r13b))-1][0])
                        r13b3=(r13b[(len(r13b))-1][1])                
                        r13b1=[r13b2+60,r13b3]
                        all_black.append(r13b1)
                
            for i in range (0,len(r14b)):
                if r14b!=[]:
                    all_black.append(r14b[i])
                    if r14b[len(r14b)-1][0]==xposition and r14b[len(r14b)-1][1]==yposition:
                        r14b2=(r14b[(len(r14b))-1][0])
                        r14b3=(r14b[(len(r14b))-1][1])                
                        r14b1=[r14b2-60,r14b3]
                        all_black.append(r14b1)
                        
            for i in range (0,len(r21b)):
                if r21b!=[]:
                    all_black.append(r21b[i])
                    if r21b[len(r21b)-1][0]==xposition and r21b[len(r21b)-1][1]==yposition:
                        r21b2=(r21b[(len(r21b))-1][0])
                        r21b3=(r21b[(len(r21b))-1][1])                
                        r21b1=[r21b2,r21b3+60]
                        all_black.append(r21b1)
                
            for i in range (0,len(r22b)):
                if r22b!=[]:
                    all_black.append(r22b[i])
                    if r22b[len(r22b)-1][0]==xposition and r22b[len(r22b)-1][1]==yposition:
                        r22b2=(r22b[(len(r22b))-1][0])
                        r22b3=(r22b[(len(r22b))-1][1])                
                        r22b1=[r22b2,r22b3-60]
                        all_black.append(r22b1)
                
            for i in range (0,len(r23b)):
                if r23b!=[]:
                    all_black.append(r23b[i])
                    if r23b[len(r23b)-1][0]==xposition and r23b[len(r23b)-1][1]==yposition:
                        r23b2=(r23b[(len(r23b))-1][0])
                        r23b3=(r23b[(len(r23b))-1][1])                
                        r23b1=[r23b2+60,r23b3]
                        all_black.append(r23b1)
                
            for i in range (0,len(r24b)):
                if r24b!=[]:
                    all_black.append(r24b[i])
                    if r24b[len(r24b)-1][0]==xposition and r24b[len(r24b)-1][1]==yposition:
                        r24b2=(r24b[(len(r24b))-1][0])
                        r24b3=(r24b[(len(r24b))-1][1])                
                        r24b1=[r24b2-60,r24b3]
                        all_black.append(r24b1)
            for i in range (0,len(r31b)):
                if r31b!=[]:
                    all_black.append(r31b[i])
                    if r31b[len(r31b)-1][0]==xposition and r31b[len(r31b)-1][1]==yposition:
                        r31b2=(r31b[(len(r31b))-1][0])
                        r31b3=(r31b[(len(r31b))-1][1])                
                        r31b1=[r31b2,r31b3+60]
                        all_black.append(r31b1)
                
            for i in range (0,len(r32b)):
                if r32b!=[]:
                    all_black.append(r32b[i])
                    if r32b[len(r32b)-1][0]==xposition and r32b[len(r32b)-1][1]==yposition:
                        r32b2=(r32b[(len(r32b))-1][0])
                        r32b3=(r32b[(len(r32b))-1][1])                
                        r32b1=[r32b2,r32b3-60]
                        all_black.append(r32b1)
                
            for i in range (0,len(r33b)):
                if r33b!=[]:
                    all_black.append(r33b[i])
                    if r33b[len(r33b)-1][0]==xposition and r33b[len(r33b)-1][1]==yposition:
                        r33b2=(r33b[(len(r33b))-1][0])
                        r33b3=(r33b[(len(r33b))-1][1])                
                        r33b1=[r33b2+60,r33b3]
                        all_black.append(r33b1)
                
            for i in range (0,len(r34b)):
                if r34b!=[]:
                    all_black.append(r34b[i])
                    if r34b[len(r34b)-1][0]==xposition and r34b[len(r34b)-1][1]==yposition:
                        r34b2=(r34b[(len(r34b))-1][0])
                        r34b3=(r34b[(len(r34b))-1][1])                
                        r34b1=[r34b2-60,r34b3]
                        all_black.append(r34b1)

            for i in range (0,len(r41b)):
                if r41b!=[]:
                    all_black.append(r41b[i])
                    if r41b[len(r41b)-1][0]==xposition and r41b[len(r41b)-1][1]==yposition:
                        r41b2=(r41b[(len(r41b))-1][0])
                        r41b3=(r41b[(len(r41b))-1][1])                
                        r41b1=[r41b2,r41b3+60]
                        all_black.append(r41b1)
                
            for i in range (0,len(r42b)):
                if r42b!=[]:
                    all_black.append(r42b[i])
                    if r42b[len(r42b)-1][0]==xposition and r42b[len(r42b)-1][1]==yposition:
                        r42b2=(r42b[(len(r42b))-1][0])
                        r42b3=(r42b[(len(r42b))-1][1])                
                        r42b1=[r42b2,r42b3-60]
                        all_black.append(r42b1)
                
            for i in range (0,len(r43b)):
                if r43b!=[]:
                    all_black.append(r43b[i])
                    if r43b[len(r43b)-1][0]==xposition and r43b[len(r43b)-1][1]==yposition:
                        r43b2=(r43b[(len(r43b))-1][0])
                        r43b3=(r43b[(len(r43b))-1][1])                
                        r43b1=[r43b2+60,r43b3]
                        all_black.append(r43b1)
                
            for i in range (0,len(r44b)):
                if r44b!=[]:
                    all_black.append(r44b[i])
                    if r44b[len(r44b)-1][0]==xposition and r44b[len(r44b)-1][1]==yposition:
                        r44b2=(r44b[(len(r44b))-1][0])
                        r44b3=(r44b[(len(r44b))-1][1])                
                        r44b1=[r44b2-60,r44b3]
                        all_black.append(r44b1)

                        
            for i in range (0,len(r51b)):
                if r51b!=[]:
                    all_black.append(r51b[i])
                    if r51b[len(r51b)-1][0]==xposition and r51b[len(r51b)-1][1]==yposition:
                        r51b2=(r51b[(len(r51b))-1][0])
                        r51b3=(r51b[(len(r51b))-1][1])                
                        r51b1=[r51b2,r51b3+60]
                        all_black.append(r51b1)
                
            for i in range (0,len(r52b)):
                if r52b!=[]:
                    all_black.append(r52b[i])
                    if r52b[len(r52b)-1][0]==xposition and r52b[len(r52b)-1][1]==yposition:
                        r52b2=(r52b[(len(r52b))-1][0])
                        r52b3=(r52b[(len(r52b))-1][1])                
                        r52b1=[r52b2,r52b3-60]
                        all_black.append(r52b1)
                
            for i in range (0,len(r53b)):
                if r53b!=[]:
                    all_black.append(r53b[i])
                    if r53b[len(r53b)-1][0]==xposition and r53b[len(r53b)-1][1]==yposition:
                        r53b2=(r53b[(len(r53b))-1][0])
                        r53b3=(r53b[(len(r53b))-1][1])                
                        r53b1=[r53b2+60,r53b3]
                        all_black.append(r53b1)
                
            for i in range (0,len(r54b)):
                if r54b!=[]:
                    all_black.append(r54b[i])
                    if r54b[len(r54b)-1][0]==xposition and r54b[len(r54b)-1][1]==yposition:
                        r54b2=(r54b[(len(r54b))-1][0])
                        r54b3=(r54b[(len(r54b))-1][1])                
                        r54b1=[r54b2-60,r54b3]
                        all_black.append(r54b1)

            for i in range (0,len(b11b)):
                if b11b!=[]:
                    all_black.append(b11b[i])
                    if b11b[len(b11b)-1][0]==xposition and b11b[len(b11b)-1][1]==yposition:
                        b11b2=(b11b[(len(b11b))-1][0])
                        b11b3=(b11b[(len(b11b))-1][1])                
                        b11b1=[b11b2+60,b11b3+60]
                        all_black.append(b11b1)
                
            for i in range (0,len(b12b)):
                if b12b!=[]:
                    all_black.append(b12b[i])
                    if b12b[len(b12b)-1][0]==xposition and b12b[len(b12b)-1][1]==yposition:
                        b12b2=(b12b[(len(b12b))-1][0])
                        b12b3=(b12b[(len(b12b))-1][1])                
                        b12b1=[b12b2-60,b12b3-60]
                        all_black.append(b12b1)
                
            for i in range (0,len(b13b)):
                if b13b!=[]:
                    all_black.append(b13b[i])
                    if b13b[len(b13b)-1][0]==xposition and b13b[len(b13b)-1][1]==yposition:
                        b13b2=(b13b[(len(b13b))-1][0])
                        b13b3=(b13b[(len(b13b))-1][1])                
                        b13b1=[b13b2+60,b13b3-60]
                        all_black.append(b13b1)
                
            for i in range (0,len(b14b)):
                if b14b!=[]:
                    all_black.append(b14b[i])
                    if b14b[len(b14b)-1][0]==xposition and b14b[len(b14b)-1][1]==yposition:
                        b14b2=(b14b[(len(b14b))-1][0])
                        b14b3=(b14b[(len(b14b))-1][1])                
                        b14b1=[b14b2-60,b14b3+60]
                        all_black.append(b14b1)
                        
            for i in range (0,len(b21b)):
                if b21b!=[]:
                    all_black.append(b21b[i])
                    if b21b[len(b21b)-1][0]==xposition and b21b[len(b21b)-1][1]==yposition:
                        b21b2=(b21b[(len(b21b))-1][0])
                        b21b3=(b21b[(len(b21b))-1][1])                
                        b21b1=[b21b2+60,b21b3+60]
                        all_black.append(b21b1)
                
            for i in range (0,len(b22b)):
                if b22b!=[]:
                    all_black.append(b22b[i])
                    if b22b[len(b22b)-1][0]==xposition and b22b[len(b22b)-1][1]==yposition:
                        b22b2=(b22b[(len(b22b))-1][0])
                        b22b3=(b22b[(len(b22b))-1][1])                
                        b22b1=[b22b2-60,b22b3-60]
                        all_black.append(b22b1)
                
            for i in range (0,len(b23b)):
                if b23b!=[]:
                    all_black.append(b23b[i])
                    if b23b[len(b23b)-1][0]==xposition and b23b[len(b23b)-1][1]==yposition:
                        b23b2=(b23b[(len(b23b))-1][0])
                        b23b3=(b23b[(len(b23b))-1][1])                
                        b23b1=[b23b2+60,b23b3-60]
                        all_black.append(b23b1)
                
            for i in range (0,len(b24b)):
                if b24b!=[]:
                    all_black.append(b24b[i])
                    if b24b[len(b24b)-1][0]==xposition and b24b[len(b24b)-1][1]==yposition:
                        b24b2=(b24b[(len(b24b))-1][0])
                        b24b3=(b24b[(len(b24b))-1][1])                
                        b24b1=[b24b2-60,b24b3+60]
                        all_black.append(b24b1)
                        
            for i in range (0,len(b31b)):
                if b31b!=[]:
                    all_black.append(b31b[i])
                    if b31b[len(b31b)-1][0]==xposition and b31b[len(b31b)-1][1]==yposition:
                        b31b2=(b31b[(len(b31b))-1][0])
                        b31b3=(b31b[(len(b31b))-1][1])                
                        b31b1=[b31b2+60,b31b3+60]
                        all_black.append(b31b1)
                
            for i in range (0,len(b32b)):
                if b32b!=[]:
                    all_black.append(b32b[i])
                    if b32b[len(b32b)-1][0]==xposition and b32b[len(b32b)-1][1]==yposition:
                        b32b2=(b32b[(len(b32b))-1][0])
                        b32b3=(b32b[(len(b32b))-1][1])                
                        b32b1=[b32b2-60,b32b3-60]
                        all_black.append(b32b1)
                
            for i in range (0,len(b33b)):
                if b33b!=[]:
                    all_black.append(b33b[i])
                    if b33b[len(b33b)-1][0]==xposition and b33b[len(b33b)-1][1]==yposition:
                        b33b2=(b33b[(len(b33b))-1][0])
                        b33b3=(b33b[(len(b33b))-1][1])                
                        b33b1=[b33b2+60,b33b3-60]
                        all_black.append(b33b1)
                
            for i in range (0,len(b34b)):
                if b34b!=[]:
                    all_black.append(b34b[i])
                    if b34b[len(b34b)-1][0]==xposition and b34b[len(b34b)-1][1]==yposition:
                        b34b2=(b34b[(len(b34b))-1][0])
                        b34b3=(b34b[(len(b34b))-1][1])                
                        b34b1=[b34b2-60,b34b3+60]
                        all_black.append(b34b1)
                        

            for i in range (0,len(b41b)):
                if b41b!=[]:
                    all_black.append(b41b[i])
                    if b41b[len(b41b)-1][0]==xposition and b41b[len(b41b)-1][1]==yposition:
                        b41b2=(b41b[(len(b41b))-1][0])
                        b41b3=(b41b[(len(b41b))-1][1])                
                        b41b1=[b41b2+60,b41b3+60]
                        all_black.append(b41b1)
                
            for i in range (0,len(b42b)):
                if b42b!=[]:
                    all_black.append(b42b[i])
                    if b42b[len(b42b)-1][0]==xposition and b42b[len(b42b)-1][1]==yposition:
                        b42b2=(b42b[(len(b42b))-1][0])
                        b42b3=(b42b[(len(b42b))-1][1])                
                        b42b1=[b42b2-60,b42b3-60]
                        all_black.append(b42b1)
                
            for i in range (0,len(b43b)):
                if b43b!=[]:
                    all_black.append(b43b[i])
                    if b43b[len(b43b)-1][0]==xposition and b43b[len(b43b)-1][1]==yposition:
                        b43b2=(b43b[(len(b43b))-1][0])
                        b43b3=(b43b[(len(b43b))-1][1])                
                        b43b1=[b43b2+60,b43b3-60]
                        all_black.append(b43b1)
                
            for i in range (0,len(b44b)):
                if b44b!=[]:
                    all_black.append(b44b[i])
                    if b44b[len(b44b)-1][0]==xposition and b44b[len(b44b)-1][1]==yposition:
                        b44b2=(b44b[(len(b44b))-1][0])
                        b44b3=(b44b[(len(b44b))-1][1])                
                        b44b1=[b44b2-60,b44b3+60]
                        all_black.append(b44b1)
                        
            for i in range (0,len(b51b)):
                if b51b!=[]:
                    all_black.append(b51b[i])
                    if b51b[len(b51b)-1][0]==xposition and b51b[len(b51b)-1][1]==yposition:
                        b51b2=(b51b[(len(b51b))-1][0])
                        b51b3=(b51b[(len(b51b))-1][1])                
                        b51b1=[b51b2+60,b51b3+60]
                        all_black.append(b51b1)
                
            for i in range (0,len(b52b)):
                if b52b!=[]:
                    all_black.append(b52b[i])
                    if b52b[len(b52b)-1][0]==xposition and b52b[len(b52b)-1][1]==yposition:
                        b52b2=(b52b[(len(b52b))-1][0])
                        b52b3=(b52b[(len(b52b))-1][1])                
                        b52b1=[b52b2-60,b52b3-60]
                        all_black.append(b52b1)
                
            for i in range (0,len(b53b)):
                if b53b!=[]:
                    all_black.append(b53b[i])
                    if b53b[len(b53b)-1][0]==xposition and b53b[len(b53b)-1][1]==yposition:
                        b53b2=(b53b[(len(b53b))-1][0])
                        b53b3=(b53b[(len(b53b))-1][1])                
                        b53b1=[b53b2+60,b53b3-60]
                        all_black.append(b53b1)
                
            for i in range (0,len(b54b)):
                if b54b!=[]:
                    all_black.append(b54b[i])
                    if b54b[len(b54b)-1][0]==xposition and b54b[len(b54b)-1][1]==yposition:
                        b54b2=(b54b[(len(b54b))-1][0])
                        b54b3=(b54b[(len(b54b))-1][1])                
                        b54b1=[b54b2-60,b54b3+60]
                        all_black.append(b54b1)
                        
                    
            for i in range (0,len(kn1b)):
                if kn1b!=[]:
                    all_black.append(kn1b[i])
                    
            for i in range (0,len(kn2b)):
                if kn2b!=[]:
                    all_black.append(kn2b[i])

            for i in range (0,len(kn3b)):
                if kn3b!=[]:
                    all_black.append(kn3b[i])

            for i in range (0,len(kn4b)):
                if kn4b!=[]:
                    all_black.append(kn4b[i])

            for i in range (0,len(kn5b)):
                if kn5b!=[]:
                    all_black.append(kn5b[i])
                    
            for i in range (0,len(q11b)):
                if q11b!=[]:
                    all_black.append(q11b[i])
                    if q11b[len(q11b)-1][0]==xposition and q11b[len(q11b)-1][1]==yposition:
                        q11b2=(q11b[(len(q11b))-1][0])
                        q11b3=(q11b[(len(q11b))-1][1])                
                        q11b1=[q11b2+60,q11b3+60]
                        all_black.append(q11b1)
                
            for i in range (0,len(q12b)):
                if q12b!=[]:
                    all_black.append(q12b[i])
                    if q12b[len(q12b)-1][0]==xposition and q12b[len(q12b)-1][1]==yposition:
                        q12b2=(q12b[(len(q12b))-1][0])
                        q12b3=(q12b[(len(q12b))-1][1])                
                        q12b1=[q12b2-60,q12b3-60]
                        all_black.append(q12b1)
                
            for i in range (0,len(q13b)):
                if q13b!=[]:
                    all_black.append(q13b[i])
                    if q13b[len(q13b)-1][0]==xposition and q13b[len(q13b)-1][1]==yposition:
                        q13b2=(q13b[(len(q13b))-1][0])
                        q13b3=(q13b[(len(q13b))-1][1])                
                        q13b1=[q13b2+60,q13b3-60]
                        all_black.append(q13b1)
                
            for i in range (0,len(q14b)):
                if q14b!=[]:
                    all_black.append(q14b[i])
                    if q14b[len(q14b)-1][0]==xposition and q14b[len(q14b)-1][1]==yposition:
                        q14b2=(q14b[(len(q14b))-1][0])
                        q14b3=(q14b[(len(q14b))-1][1])                
                        q14b1=[q14b2-60,q14b3+60]
                        all_black.append(q14b1)
            for i in range (0,len(q15b)):
                if q15b!=[]:
                    all_black.append(q15b[i])
                    if q15b[len(q15b)-1][0]==xposition and q15b[len(q15b)-1][1]==yposition:
                        q15b2=(q15b[(len(q15b))-1][0])
                        q15b3=(q15b[(len(q15b))-1][1])                
                        q15b1=[q15b2,q15b3+60]
                        all_black.append(q15b1)
                
            for i in range (0,len(q16b)):
                if q16b!=[]:
                    all_black.append(q16b[i])
                    if q16b[len(q16b)-1][0]==xposition and q16b[len(q16b)-1][1]==yposition:
                        q16b2=(q16b[(len(q16b))-1][0])
                        q16b3=(q16b[(len(q16b))-1][1])                
                        q16b1=[q16b2,q16b3-60]
                        all_black.append(q16b1)
                
            for i in range (0,len(q17b)):
                if q17b!=[]:
                    all_black.append(q17b[i])
                    if q17b[len(q17b)-1][0]==xposition and q17b[len(q17b)-1][1]==yposition:
                        q17b2=(q17b[(len(q17b))-1][0])
                        q17b3=(q17b[(len(q17b))-1][1])                
                        q17b1=[q17b2+60,q17b3]
                        all_black.append(q17b1)
                
            for i in range (0,len(q18b)):
                if q18b!=[]:
                    all_black.append(q18b[i])
                    if q18b[len(q18b)-1][0]==xposition and q18b[len(q18b)-1][1]==yposition:
                        q18b2=(q18b[(len(q18b))-1][0])
                        q18b3=(q18b[(len(q18b))-1][1])                
                        q18b1=[q18b2-60,q18b3]
                        all_black.append(q18b1)

            for i in range (0,len(q12b)):
                if q12b!=[]:
                    all_black.append(q12b[i])
                    if q12b[len(q12b)-1][0]==xposition and q12b[len(q12b)-1][1]==yposition:
                        q12b2=(q12b[(len(q12b))-1][0])
                        q12b3=(q12b[(len(q12b))-1][1])                
                        q12b1=[q12b2+60,q12b3+60]
                        all_black.append(q12b1)
                
            for i in range (0,len(q22b)):
                if q22b!=[]:
                    all_black.append(q22b[i])
                    if q22b[len(q22b)-1][0]==xposition and q22b[len(q22b)-1][1]==yposition:
                        q22b2=(q22b[(len(q22b))-1][0])
                        q22b3=(q22b[(len(q22b))-1][1])                
                        q22b1=[q22b2-60,q22b3-60]
                        all_black.append(q22b1)
                
            for i in range (0,len(q23b)):
                if q23b!=[]:
                    all_black.append(q23b[i])
                    if q23b[len(q23b)-1][0]==xposition and q23b[len(q23b)-1][1]==yposition:
                        q23b2=(q23b[(len(q23b))-1][0])
                        q23b3=(q23b[(len(q23b))-1][1])                
                        q23b1=[q23b2+60,q23b3-60]
                        all_black.append(q23b1)
                
            for i in range (0,len(q24b)):
                if q24b!=[]:
                    all_black.append(q24b[i])
                    if q24b[len(q24b)-1][0]==xposition and q24b[len(q24b)-1][1]==yposition:
                        q24b2=(q24b[(len(q24b))-1][0])
                        q24b3=(q24b[(len(q24b))-1][1])                
                        q24b1=[q24b2-60,q24b3+60]
                        all_black.append(q24b1)
            for i in range (0,len(q25b)):
                if q25b!=[]:
                    all_black.append(q25b[i])
                    if q25b[len(q25b)-1][0]==xposition and q25b[len(q25b)-1][1]==yposition:
                        q25b2=(q25b[(len(q25b))-1][0])
                        q25b3=(q25b[(len(q25b))-1][1])                
                        q25b1=[q25b2,q25b3+60]
                        all_black.append(q25b1)
                
            for i in range (0,len(q26b)):
                if q26b!=[]:
                    all_black.append(q26b[i])
                    if q26b[len(q26b)-1][0]==xposition and q26b[len(q26b)-1][1]==yposition:
                        q26b2=(q26b[(len(q26b))-1][0])
                        q26b3=(q26b[(len(q26b))-1][1])                
                        q26b1=[q26b2,q26b3-60]
                        all_black.append(q26b1)
                
            for i in range (0,len(q27b)):
                if q27b!=[]:
                    all_black.append(q27b[i])
                    if q27b[len(q27b)-1][0]==xposition and q27b[len(q27b)-1][1]==yposition:
                        q27b2=(q27b[(len(q27b))-1][0])
                        q27b3=(q27b[(len(q27b))-1][1])                
                        q27b1=[q27b2+60,q27b3]
                        all_black.append(q27b1)
                
            for i in range (0,len(q28b)):
                if q28b!=[]:
                    all_black.append(q28b[i])
                    if q28b[len(q28b)-1][0]==xposition and q28b[len(q28b)-1][1]==yposition:
                        q28b2=(q28b[(len(q28b))-1][0])
                        q28b3=(q28b[(len(q28b))-1][1])                
                        q28b1=[q28b2-60,q28b3]
                        all_black.append(q28b1)

            for i in range (0,len(q31b)):
                if q31b!=[]:
                    all_black.append(q31b[i])
                    if q31b[len(q31b)-1][0]==xposition and q31b[len(q31b)-1][1]==yposition:
                        q31b2=(q31b[(len(q31b))-1][0])
                        q31b3=(q31b[(len(q31b))-1][1])                
                        q31b1=[q31b2+60,q31b3+60]
                        all_black.append(q31b1)
                
            for i in range (0,len(q32b)):
                if q32b!=[]:
                    all_black.append(q32b[i])
                    if q32b[len(q32b)-1][0]==xposition and q32b[len(q32b)-1][1]==yposition:
                        q32b2=(q32b[(len(q32b))-1][0])
                        q32b3=(q32b[(len(q32b))-1][1])                
                        q32b1=[q32b2-60,q32b3-60]
                        all_black.append(q32b1)
                
            for i in range (0,len(q33b)):
                if q33b!=[]:
                    all_black.append(q33b[i])
                    if q33b[len(q33b)-1][0]==xposition and q33b[len(q33b)-1][1]==yposition:
                        q33b2=(q33b[(len(q33b))-1][0])
                        q33b3=(q33b[(len(q33b))-1][1])                
                        q33b1=[q33b2+60,q33b3-60]
                        all_black.append(q33b1)
                
            for i in range (0,len(q34b)):
                if q34b!=[]:
                    all_black.append(q34b[i])
                    if q34b[len(q34b)-1][0]==xposition and q34b[len(q34b)-1][1]==yposition:
                        q34b2=(q34b[(len(q34b))-1][0])
                        q34b3=(q34b[(len(q34b))-1][1])                
                        q34b1=[q34b2-60,q34b3+60]
                        all_black.append(q34b1)
            for i in range (0,len(q35b)):
                if q35b!=[]:
                    all_black.append(q35b[i])
                    if q35b[len(q35b)-1][0]==xposition and q35b[len(q35b)-1][1]==yposition:
                        q35b2=(q35b[(len(q35b))-1][0])
                        q35b3=(q35b[(len(q35b))-1][1])                
                        q35b1=[q35b2,q35b3+60]
                        all_black.append(q35b1)
                
            for i in range (0,len(q36b)):
                if q36b!=[]:
                    all_black.append(q36b[i])
                    if q36b[len(q36b)-1][0]==xposition and q36b[len(q36b)-1][1]==yposition:
                        q36b2=(q36b[(len(q36b))-1][0])
                        q36b3=(q36b[(len(q36b))-1][1])                
                        q36b1=[q36b2,q36b3-60]
                        all_black.append(q36b1)
                
            for i in range (0,len(q37b)):
                if q37b!=[]:
                    all_black.append(q37b[i])
                    if q37b[len(q37b)-1][0]==xposition and q37b[len(q37b)-1][1]==yposition:
                        q37b2=(q37b[(len(q37b))-1][0])
                        q37b3=(q37b[(len(q37b))-1][1])                
                        q37b1=[q37b2+60,q37b3]
                        all_black.append(q37b1)
                
            for i in range (0,len(q38b)):
                if q38b!=[]:
                    all_black.append(q38b[i])
                    if q38b[len(q38b)-1][0]==xposition and q38b[len(q38b)-1][1]==yposition:
                        q38b2=(q38b[(len(q38b))-1][0])
                        q38b3=(q38b[(len(q38b))-1][1])                
                        q38b1=[q38b2-60,q38b3]
                        all_black.append(q38b1)


            for i in range (0,len(q41b)):
                if q41b!=[]:
                    all_black.append(q41b[i])
                    if q41b[len(q41b)-1][0]==xposition and q41b[len(q41b)-1][1]==yposition:
                        q41b2=(q41b[(len(q41b))-1][0])
                        q41b3=(q41b[(len(q41b))-1][1])                
                        q41b1=[q41b2+60,q41b3+60]
                        all_black.append(q41b1)
                
            for i in range (0,len(q42b)):
                if q42b!=[]:
                    all_black.append(q42b[i])
                    if q42b[len(q42b)-1][0]==xposition and q42b[len(q42b)-1][1]==yposition:
                        q42b2=(q42b[(len(q42b))-1][0])
                        q42b3=(q42b[(len(q42b))-1][1])                
                        q42b1=[q42b2-60,q42b3-60]
                        all_black.append(q42b1)
                
            for i in range (0,len(q43b)):
                if q43b!=[]:
                    all_black.append(q43b[i])
                    if q43b[len(q43b)-1][0]==xposition and q43b[len(q43b)-1][1]==yposition:
                        q43b2=(q43b[(len(q43b))-1][0])
                        q43b3=(q43b[(len(q43b))-1][1])                
                        q43b1=[q43b2+60,q43b3-60]
                        all_black.append(q43b1)
                
            for i in range (0,len(q44b)):
                if q44b!=[]:
                    all_black.append(q44b[i])
                    if q44b[len(q44b)-1][0]==xposition and q44b[len(q44b)-1][1]==yposition:
                        q44b2=(q44b[(len(q44b))-1][0])
                        q44b3=(q44b[(len(q44b))-1][1])                
                        q44b1=[q44b2-60,q44b3+60]
                        all_black.append(q44b1)
            for i in range (0,len(q45b)):
                if q45b!=[]:
                    all_black.append(q45b[i])
                    if q45b[len(q45b)-1][0]==xposition and q45b[len(q45b)-1][1]==yposition:
                        q45b2=(q45b[(len(q45b))-1][0])
                        q45b3=(q45b[(len(q45b))-1][1])                
                        q45b1=[q45b2,q45b3+60]
                        all_black.append(q45b1)
                
            for i in range (0,len(q46b)):
                if q46b!=[]:
                    all_black.append(q46b[i])
                    if q46b[len(q46b)-1][0]==xposition and q46b[len(q46b)-1][1]==yposition:
                        q46b2=(q46b[(len(q46b))-1][0])
                        q46b3=(q46b[(len(q46b))-1][1])                
                        q46b1=[q46b2,q46b3-60]
                        all_black.append(q46b1)
                
            for i in range (0,len(q47b)):
                if q47b!=[]:
                    all_black.append(q47b[i])
                    if q47b[len(q47b)-1][0]==xposition and q47b[len(q47b)-1][1]==yposition:
                        q47b2=(q47b[(len(q47b))-1][0])
                        q47b3=(q47b[(len(q47b))-1][1])                
                        q47b1=[q47b2+60,q47b3]
                        all_black.append(q47b1)
                
            for i in range (0,len(q48b)):
                if q48b!=[]:
                    all_black.append(q48b[i])
                    if q48b[len(q48b)-1][0]==xposition and q48b[len(q48b)-1][1]==yposition:
                        q48b2=(q48b[(len(q48b))-1][0])
                        q48b3=(q48b[(len(q48b))-1][1])                
                        q48b1=[q48b2-60,q48b3]
                        all_black.append(q48b1)


            for i in range (0,len(k1b)):
                if k1b!=[]:
                    all_black.append(k1b[i])

            for i in range (0,len(p1b)):
                if p1b!=[]:
                    all_black.append(p1b[i])
            for i in range (0,len(p2b)):
                if p2b!=[]:
                    all_black.append(p2b[i])
            for i in range (0,len(p3b)):
                if p3b!=[]:
                    all_black.append(p3b[i])
            for i in range (0,len(p4b)):
                if p4b!=[]:
                    all_black.append(p4b[i])
            for i in range (0,len(p5b)):
                if p5b!=[]:
                    all_black.append(p5b[i])
            for i in range (0,len(p6b)):
                if p6b!=[]:
                    all_black.append(p6b[i])
            for i in range (0,len(p7b)):
                if p7b!=[]:
                    all_black.append(p7b[i])
            for i in range (0,len(p8b)):
                if p8b!=[]:
                    all_black.append(p8b[i])

            hw=1
        


        white_stalemate=False
        coordsr=coords
        coordsr2=coords2
        if moves==0:
            
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition    
            coords=[]
            coords2=[]
            check=False
            for i in range(0,len(all_black)):
                if all_black[i][0]==xposition and all_black[i][1]==yposition:
                    check=True
            if check==False:
                Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                vc="b1w"
                Bishop1w.possible_moves(coords,coords2,"b")
                if coords==[]:
                    Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                    vc="b2w"
                    Bishop2w.possible_moves(coords,coords2,"b")
                    if coords==[]:
                        Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                        vc="b3w"
                        Bishop3w.possible_moves(coords,coords2,"b")
                        if coords==[]:
                            Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                            vc="b4w"
                            Bishop4w.possible_moves(coords,coords2,"b")
                            if coords==[]:
                                Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                                vc="b5w"
                                Bishop5w.possible_moves(coords,coords2,"b")
                                if coords==[]:
                                    vc="r1w"
                                    Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                                    Rook1w.possible_moves(coords,coords2,"b")
                                    if coords==[]:
                                        vc="r2w"
                                        Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                                        Rook2w.possible_moves(coords,coords2,"b")
                                        if coords==[]:
                                            vc="r3w"
                                            Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                                            Rook3w.possible_moves(coords,coords2,"b")
                                            if coords==[]:
                                                vc="r4w"
                                                Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                                                Rook4w.possible_moves(coords,coords2,"b")
                                                if coords==[]:
                                                    vc="r5w"
                                                    Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                                                    Rook5w.possible_moves(coords,coords2,"b")
                                                    if coords==[]:
                                                        vc="kn1w"
                                                        Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                                                        Knight1w.possible_moves(coords,coords2,"b")
                                                        if coords==[]:
                                                            vc="kn2w"
                                                            Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                                                            Knight2w.possible_moves(coords,coords2,"b")
                                                            if coords==[]:
                                                                vc="kn3w"
                                                                Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                                                                Knight3w.possible_moves(coords,coords2,"b")
                                                                if coords==[]:
                                                                    vc="kn4w"
                                                                    Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                                                                    Knight4w.possible_moves(coords,coords2,"b")
                                                                    if coords==[]:
                                                                        vc="kn5w"
                                                                        Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                                                                        Knight5w.possible_moves(coords,coords2,"b")
                                                                        if coords==[]:
                                                                            vc="q1w"
                                                                            Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                                                                            Queen1w.possible_moves(coords,coords2,"b")
                                                                            if coords==[]:
                                                                                vc="q2w"
                                                                                Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                                                                                Queen2w.possible_moves(coords,coords2,"b")
                                                                                if coords==[]:
                                                                                    vc="q3w"
                                                                                    Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                                                                                    Queen3w.possible_moves(coords,coords2,"b")
                                                                                    if coords==[]:
                                                                                        vc="q4w"
                                                                                        Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                                                                                        Queen4w.possible_moves(coords,coords2,"b")
                                                                                        if coords==[]:
                                                                                            vc="k1w"
                                                                                            King1w=kingw(coords,coords2,kn1wmx,kn1wmy,"k1w","b")
                                                                                            King1w.possible_moves(coords,coords2,"b")
                                                                                            if coords==[]:
                                                                                                vc="p1w"
                                                                                                pawn1w=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                                                                                                pawn1w.possible_moves(coords,coords2,"b",moves21)
                                                                                                if coords==[]:
                                                                                                    vc="p2w"
                                                                                                    pawn2w=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                                                                                                    pawn2w.possible_moves(coords,coords2,"b",moves22)
                                                                                                    if coords==[]:
                                                                                                        vc="p3w"
                                                                                                        pawn3w=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                                                                                                        pawn3w.possible_moves(coords,coords2,"b",moves23)
                                                                                                        if coords==[]:
                                                                                                            vc="p4w"
                                                                                                            pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                                                                                                            pawn4w.possible_moves(coords,coords2,"b",moves24)
                                                                                                            if coords==[]:
                                                                                                                vc="p5w"
                                                                                                                pawn5w=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                                                                                                                pawn5w.possible_moves(coords,coords2,"b",moves25)
                                                                                                                if coords==[]:
                                                                                                                    vc="p6w"
                                                                                                                    pawn6w=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                                                                                                                    pawn6w.possible_moves(coords,coords2,"b",moves26)
                                                                                                                    if coords==[]:
                                                                                                                        vc="p7w"
                                                                                                                        pawn7w=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                                                                                                                        pawn7w.possible_moves(coords,coords2,"b",moves27)
                                                                                                                        if coords==[]:
                                                                                                                            vc="p8w"
                                                                                                                            Pawn8w=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                                                                                                                            Pawn8w.possible_moves(coords,coords2,"b",moves28)
                                                                                                                            if coords==[]:
                                                                                                                                white_stalemate=True
                                                                                                                            else:
                                                                                                                                coords=[]
                                                                                                                                coords2=[]
                                                                                                                        else:
                                                                                                                            coords=[]
                                                                                                                            coords2=[]
                                                                                                                    else:
                                                                                                                        coords=[]
                                                                                                                        coords2=[]
                                                                                                                else:
                                                                                                                    coords=[]
                                                                                                                    coords2=[]
                                                                                                            else:
                                                                                                                coords=[]
                                                                                                                coords2=[]
                                                                                                        else:
                                                                                                            coords=[]
                                                                                                            coords2=[]
                                                                                                    else:
                                                                                                        coords=[]
                                                                                                        coords2=[]
                                                                                                else:
                                                                                                    coords=[]
                                                                                                    coords2=[]
                                                                                            else:
                                                                                                coords=[]
                                                                                                coords2=[]
                                                                                        else:
                                                                                            coords=[]
                                                                                            coords2=[]
                                                                                    else:
                                                                                        coords=[]
                                                                                        coords2=[]
                                                                                else:
                                                                                    coords=[]
                                                                                    coords2=[]
                                                                            else:
                                                                                coords=[]
                                                                                coords2=[]
                                                                        else:
                                                                            coords=[]
                                                                            coords2=[]
                                                                    else:
                                                                        coords=[]
                                                                        coords2=[]
                                                                else:
                                                                    coords=[]
                                                                    coords2=[]
                                                            else:
                                                                coords=[]
                                                                coords2=[]
                                                        else:
                                                            coords=[]
                                                            coords2=[]
                                                    else:
                                                        coords=[]
                                                        coords2=[]
                                                else:
                                                    coords=[]
                                                    coords2=[]
                                            else:
                                                coords=[]
                                                coords2=[]
                                        else:
                                            coords=[]
                                            coords2=[]
                                    else:
                                        coords=[]
                                        coords2=[]
                                else:
                                    coords=[]
                                    coords2=[]
                            else:
                                coords=[]
                                coords2=[]
                        else:
                            coords=[]
                            coords2=[]
                    else:
                        coords=[]
                        coords2=[]
                else:
                    coords=[]
                    coords2=[]
            else:
                coords=[]
                coords2=[]
        coords=coordsr
        coords2=coordsr2
        
        black_stalemate=False                                                                        
        if moves==1:
            coordsr=coords
            coordsr2=coords2
            coords=[]
            coords2=[]
            check=False
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition 
            for i in range(0,len(all_white)):
                if all_white[i][0]==xposition and all_white[i][1]==yposition:
                    check=True
            if check==False:
                Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                vc="b1b"
                Bishop1b.possible_moves(coords,coords2,"w")
                if coords==[]:
                    Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
                    vc="b2b"
                    Bishop2b.possible_moves(coords,coords2,"w")
                    if coords==[]:
                        Bishop3b=bishopw(coords,coords2,b3bmx,b3bmy,"b3b","w")
                        vc="b3b"
                        Bishop3b.possible_moves(coords,coords2,"w")
                        if coords==[]:
                            Bishop4b=bishopw(coords,coords2,b4bmx,b4bmy,"b4b","w")
                            vc="b4b"
                            Bishop4b.possible_moves(coords,coords2,"w")
                            if coords==[]:
                                Bishop5b=bishopw(coords,coords2,b5bmx,b5bmy,"b5b","w")
                                vc="b5b"
                                Bishop5b.possible_moves(coords,coords2,"w")
                                if coords==[]:
                                    vc="r1b"
                                    Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                                    Rook1b.possible_moves(coords,coords2,"w")
                                    if coords==[]:
                                        vc="r2b"
                                        Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                                        Rook2b.possible_moves(coords,coords2,"w")
                                        if coords==[]:
                                            vc="r3b"
                                            Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                                            Rook3b.possible_moves(coords,coords2,"w")
                                            if coords==[]:
                                                vc="r4b"
                                                Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                                                Rook4b.possible_moves(coords,coords2,"w")
                                                if coords==[]:
                                                    vc="r5b"
                                                    Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                                                    Rook5b.possible_moves(coords,coords2,"w")
                                                    if coords==[]:
                                                        vc="kn1b"
                                                        Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                                                        Knight1b.possible_moves(coords,coords2,"w")
                                                        if coords==[]:
                                                            vc="kn2b"
                                                            Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                                                            Knight2b.possible_moves(coords,coords2,"w")
                                                            if coords==[]:
                                                                vc="kn3b"
                                                                Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                                                                Knight3b.possible_moves(coords,coords2,"w")
                                                                if coords==[]:
                                                                    vc="kn4b"
                                                                    Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                                                                    Knight4b.possible_moves(coords,coords2,"w")
                                                                    if coords==[]:
                                                                        vc="kn5b"
                                                                        Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                                                                        Knight5b.possible_moves(coords,coords2,"w")
                                                                        if coords==[]:
                                                                            vc="q1b"
                                                                            Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                                                                            Queen1b.possible_moves(coords,coords2,"w")
                                                                            if coords==[]:
                                                                                vc="q2b"
                                                                                Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                                                                                Queen2b.possible_moves(coords,coords2,"w")
                                                                                if coords==[]:
                                                                                    vc="q3b"
                                                                                    Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                                                                                    Queen3b.possible_moves(coords,coords2,"w")
                                                                                    if coords==[]:
                                                                                        vc="q4b"
                                                                                        Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                                                                                        Queen4b.possible_moves(coords,coords2,"w")
                                                                                        if coords==[]:
                                                                                            vc="k1b"
                                                                                            King1b=kingw(coords,coords2,kn1bmx,kn1bmy,"k1b","w")
                                                                                            King1b.possible_moves(coords,coords2,"w")
                                                                                            if coords==[]:
                                                                                                vc="p1b"
                                                                                                Pawn1b=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                                                                                                Pawn1b.possible_moves(coords,coords2,"w",moves21b)
                                                                                                if coords==[]:
                                                                                                    vc="p2b"
                                                                                                    Pawn2b=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                                                                                                    Pawn2b.possible_moves(coords,coords2,"w",moves22b)
                                                                                                    if coords==[]:
                                                                                                        vc="p3b"
                                                                                                        Pawn3b=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                                                                                                        Pawn3b.possible_moves(coords,coords2,"w",moves23b)
                                                                                                        if coords==[]:
                                                                                                            vc="p4b"
                                                                                                            Pawn4b=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                                                                                                            Pawn4b.possible_moves(coords,coords2,"w",moves24b)
                                                                                                            if coords==[]:
                                                                                                                vc="p5b"
                                                                                                                Pawn5b=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                                                                                                                Pawn5b.possible_moves(coords,coords2,"w",moves25b)
                                                                                                                if coords==[]:
                                                                                                                    vc="p6b"
                                                                                                                    Pawn6b=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                                                                                                                    Pawn6b.possible_moves(coords,coords2,"w",moves26b)
                                                                                                                    if coords==[]:
                                                                                                                        vc="p7b"
                                                                                                                        Pawn7b=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                                                                                                                        Pawn7b.possible_moves(coords,coords2,"w",moves27b)
                                                                                                                        if coords==[]:
                                                                                                                            vc="p8b"
                                                                                                                            Pawn8b=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                                                                                                                            Pawn8b.possible_moves(coords,coords2,"w",moves28b)
                                                                                                                            if coords==[]:
                                                                                                                                
                                                                                                                                black_stalemate=True

                                                                                                                            else:
                                                                                                                                coords=[]
                                                                                                                                coords2=[]
                                                                                                                        else:
                                                                                                                            coords=[]
                                                                                                                            coords2=[]
                                                                                                                    else:
                                                                                                                        coords=[]
                                                                                                                        coords2=[]
                                                                                                                else:
                                                                                                                    coords=[]
                                                                                                                    coords2=[]
                                                                                                            else:
                                                                                                                coords=[]
                                                                                                                coords2=[]
                                                                                                        else:
                                                                                                            coords=[]
                                                                                                            coords2=[]
                                                                                                    else:
                                                                                                        coords=[]
                                                                                                        coords2=[]
                                                                                                else:
                                                                                                    coords=[]
                                                                                                    coords2=[]
                                                                                            else:
                                                                                                coords=[]
                                                                                                coords2=[]
                                                                                        else:
                                                                                            coords=[]
                                                                                            coords2=[]
                                                                                    else:
                                                                                        coords=[]
                                                                                        coords2=[]
                                                                                else:
                                                                                    coords=[]
                                                                                    coords2=[]
                                                                            else:
                                                                                coords=[]
                                                                                coords2=[]
                                                                        else:
                                                                            coords=[]
                                                                            coords2=[]
                                                                    else:
                                                                        coords=[]
                                                                        coords2=[]
                                                                else:
                                                                    coords=[]
                                                                    coords2=[]
                                                            else:
                                                                coords=[]
                                                                coords2=[]
                                                        else:
                                                            coords=[]
                                                            coords2=[]
                                                    else:
                                                        coords=[]
                                                        coords2=[]
                                                else:
                                                    coords=[]
                                                    coords2=[]
                                            else:
                                                coords=[]
                                                coords2=[]
                                        else:
                                            coords=[]
                                            coords2=[]
                                    else:
                                        coords=[]
                                        coords2=[]
                                else:
                                    coords=[]
                                    coords2=[]
                            else:
                                coords=[]
                                coords2=[]
                        else:
                            coords=[]
                            coords2=[]
                    else:
                        coords=[]
                        coords2=[]
                else:
                    coords=[]
                    coords2=[]
            else:
                coords=[]
                coords2=[]
        coords=coordsr
        coords2=coordsr2


        num_of_pieces=0
        for i in range(0,8):
            for a in range(0,8):
                if Board[i][a][0]!="":
                    num_of_pieces=num_of_pieces+1
        if num_of_pieces==2:
            black_stalemate=True



        white_checkmate=False
        coordsr=coords
        coordsr2=coords2
        if moves==0:
            coords=[]
            coords2=[]
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition 
            check=False
            for i in range(0,len(all_black)):
                if all_black[i][0]==xposition and all_black[i][1]==yposition:
                    check=True
            if check==True:
                Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                vc="b1w"
                Bishop1w.possible_moves(coords,coords2,"b")
                if coords==[]:
                    Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                    vc="b2w"
                    Bishop2w.possible_moves(coords,coords2,"b")
                    if coords==[]:
                        Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                        vc="b3w"
                        Bishop3w.possible_moves(coords,coords2,"b")
                        if coords==[]:
                            Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                            vc="b4w"
                            Bishop4w.possible_moves(coords,coords2,"b")
                            if coords==[]:
                                Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                                vc="b5w"
                                Bishop5w.possible_moves(coords,coords2,"b")
                                if coords==[]:
                                    vc="r1w"
                                    Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                                    Rook1w.possible_moves(coords,coords2,"b")
                                    if coords==[]:
                                        vc="r2w"
                                        Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                                        Rook2w.possible_moves(coords,coords2,"b")
                                        if coords==[]:
                                            vc="r3w"
                                            Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                                            Rook3w.possible_moves(coords,coords2,"b")
                                            if coords==[]:
                                                vc="r4w"
                                                Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                                                Rook4w.possible_moves(coords,coords2,"b")
                                                if coords==[]:
                                                    vc="r5w"
                                                    Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                                                    Rook5w.possible_moves(coords,coords2,"b")
                                                    if coords==[]:
                                                        vc="kn1w"
                                                        Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                                                        Knight1w.possible_moves(coords,coords2,"b")
                                                        if coords==[]:
                                                            vc="kn2w"
                                                            Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                                                            Knight2w.possible_moves(coords,coords2,"b")
                                                            if coords==[]:
                                                                vc="kn3w"
                                                                Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                                                                Knight3w.possible_moves(coords,coords2,"b")
                                                                if coords==[]:
                                                                    vc="kn4w"
                                                                    Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                                                                    Knight4w.possible_moves(coords,coords2,"b")
                                                                    if coords==[]:
                                                                        vc="kn5w"
                                                                        Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                                                                        Knight5w.possible_moves(coords,coords2,"b")
                                                                        if coords==[]:
                                                                            vc="q1w"
                                                                            Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                                                                            Queen1w.possible_moves(coords,coords2,"b")
                                                                            if coords==[]:
                                                                                vc="q2w"
                                                                                Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                                                                                Queen2w.possible_moves(coords,coords2,"b")
                                                                                if coords==[]:
                                                                                    vc="q3w"
                                                                                    Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                                                                                    Queen3w.possible_moves(coords,coords2,"b")
                                                                                    if coords==[]:
                                                                                        vc="q4w"
                                                                                        Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                                                                                        Queen4w.possible_moves(coords,coords2,"b")
                                                                                        if coords==[]:
                                                                                            vc="k1w"
                                                                                            King1w=kingw(coords,coords2,kn1wmx,kn1wmy,"k1w","b")
                                                                                            King1w.possible_moves(coords,coords2,"b")
                                                                                            if coords==[]:
                                                                                                vc="p1w"
                                                                                                pawn1w=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                                                                                                pawn1w.possible_moves(coords,coords2,"b",moves21)
                                                                                                if coords==[]:
                                                                                                    vc="p2w"
                                                                                                    pawn2w=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                                                                                                    pawn2w.possible_moves(coords,coords2,"b",moves22)
                                                                                                    if coords==[]:
                                                                                                        vc="p3w"
                                                                                                        pawn3w=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                                                                                                        pawn3w.possible_moves(coords,coords2,"b",moves23)
                                                                                                        if coords==[]:
                                                                                                            vc="p4w"
                                                                                                            pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                                                                                                            pawn4w.possible_moves(coords,coords2,"b",moves24)
                                                                                                            if coords==[]:
                                                                                                                vc="p5w"
                                                                                                                pawn5w=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                                                                                                                pawn5w.possible_moves(coords,coords2,"b",moves25)
                                                                                                                if coords==[]:
                                                                                                                    vc="p6w"
                                                                                                                    pawn6w=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                                                                                                                    pawn6w.possible_moves(coords,coords2,"b",moves26)
                                                                                                                    if coords==[]:
                                                                                                                        vc="p7w"
                                                                                                                        pawn7w=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                                                                                                                        pawn7w.possible_moves(coords,coords2,"b",moves27)
                                                                                                                        if coords==[]:
                                                                                                                            vc="p8w"
                                                                                                                            Pawn8w=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                                                                                                                            Pawn8w.possible_moves(coords,coords2,"b",moves28)
                                                                                                                            if coords==[]:
                                                                                                                                white_checkmate=True
                                                                                                                            else:
                                                                                                                                coords=[]
                                                                                                                                coords2=[]
                                                                                                                        else:
                                                                                                                            coords=[]
                                                                                                                            coords2=[]
                                                                                                                    else:
                                                                                                                        coords=[]
                                                                                                                        coords2=[]
                                                                                                                else:
                                                                                                                    coords=[]
                                                                                                                    coords2=[]
                                                                                                            else:
                                                                                                                coords=[]
                                                                                                                coords2=[]
                                                                                                        else:
                                                                                                            coords=[]
                                                                                                            coords2=[]
                                                                                                    else:
                                                                                                        coords=[]
                                                                                                        coords2=[]
                                                                                                else:
                                                                                                    coords=[]
                                                                                                    coords2=[]
                                                                                            else:
                                                                                                coords=[]
                                                                                                coords2=[]
                                                                                        else:
                                                                                            coords=[]
                                                                                            coords2=[]
                                                                                    else:
                                                                                        coords=[]
                                                                                        coords2=[]
                                                                                else:
                                                                                    coords=[]
                                                                                    coords2=[]
                                                                            else:
                                                                                coords=[]
                                                                                coords2=[]
                                                                        else:
                                                                            coords=[]
                                                                            coords2=[]
                                                                    else:
                                                                        coords=[]
                                                                        coords2=[]
                                                                else:
                                                                    coords=[]
                                                                    coords2=[]
                                                            else:
                                                                coords=[]
                                                                coords2=[]
                                                        else:
                                                            coords=[]
                                                            coords2=[]
                                                    else:
                                                        coords=[]
                                                        coords2=[]
                                                else:
                                                    coords=[]
                                                    coords2=[]
                                            else:
                                                coords=[]
                                                coords2=[]
                                        else:
                                            coords=[]
                                            coords2=[]
                                    else:
                                        coords=[]
                                        coords2=[]
                                else:
                                    coords=[]
                                    coords2=[]
                            else:
                                coords=[]
                                coords2=[]
                        else:
                            coords=[]
                            coords2=[]
                    else:
                        coords=[]
                        coords2=[]
                else:
                    coords=[]
                    coords2=[]
            else:
                coords=[]
                coords2=[]
        coords=coordsr
        coords2=coordsr2
        
        black_checkmate=False                                                                        
        if moves==1:
            coordsr=coords
            coordsr2=coords2
            coords=[]
            coords2=[]
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition 
            check=False
            for i in range(0,len(all_white)):
                if all_white[i][0]==xposition and all_white[i][1]==yposition:
                    check=True
            if check==True:
                Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                vc="b1b"
                Bishop1b.possible_moves(coords,coords2,"w")
                if coords==[]:
                    Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
                    vc="b2b"
                    Bishop2b.possible_moves(coords,coords2,"w")
                    if coords==[]:
                        Bishop3b=bishopw(coords,coords2,b3bmx,b3bmy,"b3b","w")
                        vc="b3b"
                        Bishop3b.possible_moves(coords,coords2,"w")
                        if coords==[]:
                            Bishop4b=bishopw(coords,coords2,b4bmx,b4bmy,"b4b","w")
                            vc="b4b"
                            Bishop4b.possible_moves(coords,coords2,"w")
                            if coords==[]:
                                Bishop5b=bishopw(coords,coords2,b5bmx,b5bmy,"b5b","w")
                                vc="b5b"
                                Bishop5b.possible_moves(coords,coords2,"w")
                                if coords==[]:
                                    vc="r1b"
                                    Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                                    Rook1b.possible_moves(coords,coords2,"w")
                                    if coords==[]:
                                        vc="r2b"
                                        Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                                        Rook2b.possible_moves(coords,coords2,"w")
                                        if coords==[]:
                                            vc="r3b"
                                            Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                                            Rook3b.possible_moves(coords,coords2,"w")
                                            if coords==[]:
                                                vc="r4b"
                                                Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                                                Rook4b.possible_moves(coords,coords2,"w")
                                                if coords==[]:
                                                    vc="r5b"
                                                    Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                                                    Rook5b.possible_moves(coords,coords2,"w")
                                                    if coords==[]:
                                                        vc="kn1b"
                                                        Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                                                        Knight1b.possible_moves(coords,coords2,"w")
                                                        if coords==[]:
                                                            vc="kn2b"
                                                            Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                                                            Knight2b.possible_moves(coords,coords2,"w")
                                                            if coords==[]:
                                                                vc="kn3b"
                                                                Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                                                                Knight3b.possible_moves(coords,coords2,"w")
                                                                if coords==[]:
                                                                    vc="kn4b"
                                                                    Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                                                                    Knight4b.possible_moves(coords,coords2,"w")
                                                                    if coords==[]:
                                                                        vc="kn5b"
                                                                        Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                                                                        Knight5b.possible_moves(coords,coords2,"w")
                                                                        if coords==[]:
                                                                            vc="q1b"
                                                                            Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                                                                            Queen1b.possible_moves(coords,coords2,"w")
                                                                            if coords==[]:
                                                                                vc="q2b"
                                                                                Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                                                                                Queen2b.possible_moves(coords,coords2,"w")
                                                                                if coords==[]:
                                                                                    vc="q3b"
                                                                                    Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                                                                                    Queen3b.possible_moves(coords,coords2,"w")
                                                                                    if coords==[]:
                                                                                        vc="q4b"
                                                                                        Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                                                                                        Queen4b.possible_moves(coords,coords2,"w")
                                                                                        if coords==[]:
                                                                                            vc="k1b"
                                                                                            King1b=kingw(coords,coords2,kn1bmx,kn1bmy,"k1b","w")
                                                                                            King1b.possible_moves(coords,coords2,"w")
                                                                                            if coords==[]:
                                                                                                vc="p1b"
                                                                                                Pawn1b=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                                                                                                Pawn1b.possible_moves(coords,coords2,"w",moves21b)
                                                                                                if coords==[]:
                                                                                                    vc="p2b"
                                                                                                    Pawn2b=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                                                                                                    Pawn2b.possible_moves(coords,coords2,"w",moves22b)
                                                                                                    if coords==[]:
                                                                                                        vc="p3b"
                                                                                                        Pawn3b=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                                                                                                        Pawn3b.possible_moves(coords,coords2,"w",moves23b)
                                                                                                        if coords==[]:
                                                                                                            vc="p4b"
                                                                                                            Pawn4b=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                                                                                                            Pawn4b.possible_moves(coords,coords2,"w",moves24b)
                                                                                                            if coords==[]:
                                                                                                                vc="p5b"
                                                                                                                Pawn5b=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                                                                                                                Pawn5b.possible_moves(coords,coords2,"w",moves25b)
                                                                                                                if coords==[]:
                                                                                                                    vc="p6b"
                                                                                                                    Pawn6b=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                                                                                                                    Pawn6b.possible_moves(coords,coords2,"w",moves26b)
                                                                                                                    if coords==[]:
                                                                                                                        vc="p7b"
                                                                                                                        Pawn7b=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                                                                                                                        Pawn7b.possible_moves(coords,coords2,"w",moves27b)
                                                                                                                        if coords==[]:
                                                                                                                            vc="p8b"
                                                                                                                            Pawn8b=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                                                                                                                            Pawn8b.possible_moves(coords,coords2,"w",moves28b)
                                                                                                                            if coords==[]:
                                                                                                                                
                                                                                                                                black_checkmate=True
                                                                                                                            else:
                                                                                                                                coords=[]
                                                                                                                                coords2=[]
                                                                                                                        else:
                                                                                                                            coords=[]
                                                                                                                            coords2=[]
                                                                                                                    else:
                                                                                                                        coords=[]
                                                                                                                        coords2=[]
                                                                                                                else:
                                                                                                                    coords=[]
                                                                                                                    coords2=[]
                                                                                                            else:
                                                                                                                coords=[]
                                                                                                                coords2=[]
                                                                                                        else:
                                                                                                            coords=[]
                                                                                                            coords2=[]
                                                                                                    else:
                                                                                                        coords=[]
                                                                                                        coords2=[]
                                                                                                else:
                                                                                                    coords=[]
                                                                                                    coords2=[]
                                                                                            else:
                                                                                                coords=[]
                                                                                                coords2=[]
                                                                                        else:
                                                                                            coords=[]
                                                                                            coords2=[]
                                                                                    else:
                                                                                        coords=[]
                                                                                        coords2=[]
                                                                                else:
                                                                                    coords=[]
                                                                                    coords2=[]
                                                                            else:
                                                                                coords=[]
                                                                                coords2=[]
                                                                        else:
                                                                            coords=[]
                                                                            coords2=[]
                                                                    else:
                                                                        coords=[]
                                                                        coords2=[]
                                                                else:
                                                                    coords=[]
                                                                    coords2=[]
                                                            else:
                                                                coords=[]
                                                                coords2=[]
                                                        else:
                                                            coords=[]
                                                            coords2=[]
                                                    else:
                                                        coords=[]
                                                        coords2=[]
                                                else:
                                                    coords=[]
                                                    coords2=[]
                                            else:
                                                coords=[]
                                                coords2=[]
                                        else:
                                            coords=[]
                                            coords2=[]
                                    else:
                                        coords=[]
                                        coords2=[]
                                else:
                                    coords=[]
                                    coords2=[]
                            else:
                                coords=[]
                                coords2=[]
                        else:
                            coords=[]
                            coords2=[]
                    else:
                        coords=[]
                        coords2=[]
                else:
                    coords=[]
                    coords2=[]
            else:
                coords=[]
                coords2=[]
        coords=coordsr
        coords2=coordsr2
        if jkl==0:
            if black_checkmate==True or white_checkmate==True:
                jkb=jkb%2
                if jkb==0:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    gameDisplay.blit(checkmate,(17,173))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    jkb=jkb+1
                if jkb==1:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)                    
                    pygame.display.update()
                    pygame.time.delay(500)
                    jkb=jkb+1
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        view=True
                        jkl=1
        if jkl==1:
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)

            

        if jkl==0:
            if black_stalemate==True or white_stalemate==True:
                jkb=jkb%2
                if jkb==0:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    gameDisplay.blit(stalemate,(127,128))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    jkb=jkb+1
                if jkb==1:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)                    
                    pygame.display.update()
                    pygame.time.delay(500)
                    jkb=jkb+1
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        view=True
                        jkl=1
        if jkl==1:
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)

        if piece=="":
            if counter%2==1:
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                pygame.display.update()
                event3=wait2()
                counter=counter+1
                rfv=0
            elif counter%2!=1:
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                pygame.display.update()
                counter=counter+1
        moves=moves%2
        if moves==0:

    ######################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo1mx=b1wmx
                    bo1my=b1wmy
                    vc="b1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b1wmx,b1wmy=pygame.mouse.get_pos()
                    if b1wmx>xposition and b1wmx<xposition2 and b1wmy>yposition and b1wmy<yposition2:
                        piece="bishop1"
                        Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                        Bishop1w.possible_moves(coords,coords2,"b")
                    else:
                        b1wmx=bo1mx
                        b1wmy=bo1my  
            if piece=="bishop1":
                b1wmx,b1wmy=pygame.mouse.get_pos()
                g="b1w"
                b1wmx,b1wmy=pygame.mouse.get_pos()
                bo1mx=b1wmx
                bo1my=b1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b1wmx=convertx(b1wmx)
                b1wmy=converty(b1wmy)
                tg=Bishop1w.position(coords,coords2,b1wmx,b1wmy,"b1w")
                
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop1change=False
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b1wmy=(yposition)*60
                    b1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
                
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo2mx=b2wmx
                    bo2my=b2wmy
                    vc="b2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b2wmx,b2wmy=pygame.mouse.get_pos()
                    if b2wmx>xposition and b2wmx<xposition2 and b2wmy>yposition and b2wmy<yposition2:
                        piece="bishop2"
                        Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                        Bishop2w.possible_moves(coords,coords2,"b")
                    else:
                        b2wmx=bo2mx
                        b2wmy=bo2my  
            if piece=="bishop2":
                b2wmx,b2wmy=pygame.mouse.get_pos()
                g="b2w"


                b2wmx,b2wmy=pygame.mouse.get_pos()
                bo2mx=b2wmx
                bo2my=b2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                b2wmx=convertx(b2wmx)
                b2wmy=converty(b2wmy)
                tg=Bishop2w.position(coords,coords2,b2wmx,b2wmy,"b2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop2change=False
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b2wmy=(yposition)*60
                    b2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo3mx=b3wmx
                    bo3my=b3wmy
                    vc="b3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b3wmx,b3wmy=pygame.mouse.get_pos()
                    if b3wmx>xposition and b3wmx<xposition2 and b3wmy>yposition and b3wmy<yposition2:
                        piece="bishop3"
                        Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                        Bishop3w.possible_moves(coords,coords2,"b")
                    else:
                        b3wmx=bo3mx
                        b3wmy=bo3my  
            if piece=="bishop3":
                b3wmx,b3wmy=pygame.mouse.get_pos()
                g="b3w"


                b3wmx,b3wmy=pygame.mouse.get_pos()
                bo3mx=b3wmx
                bo3my=b3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                b3wmx=convertx(b3wmx)
                b3wmy=converty(b3wmy)
                tg=Bishop3w.position(coords,coords2,b3wmx,b3wmy,"b3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop3change=False
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b3wmy=(yposition)*60
                    b3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo4mx=b4wmx
                    bo4my=b4wmy
                    vc="b4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b4wmx,b4wmy=pygame.mouse.get_pos()
                    if b4wmx>xposition and b4wmx<xposition2 and b4wmy>yposition and b4wmy<yposition2:
                        piece="bishop4"
                        Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                        Bishop4w.possible_moves(coords,coords2,"b")
                    else:
                        b4wmx=bo4mx
                        b4wmy=bo4my  
            if piece=="bishop4":
                b4wmx,b4wmy=pygame.mouse.get_pos()
                g="b4w"


                b4wmx,b4wmy=pygame.mouse.get_pos()
                bo4mx=b4wmx
                bo4my=b4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                b4wmx=convertx(b4wmx)
                b4wmy=converty(b4wmy)
                tg=Bishop4w.position(coords,coords2,b4wmx,b4wmy,"b4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop4change=False
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b4wmy=(yposition)*60
                    b4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo5mx=b5wmx
                    bo5my=b5wmy
                    vc="b5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b5wmx,b5wmy=pygame.mouse.get_pos()
                    if b5wmx>xposition and b5wmx<xposition2 and b5wmy>yposition and b5wmy<yposition2:
                        piece="bishop5"
                        Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                        Bishop5w.possible_moves(coords,coords2,"b")
                    else:
                        b5wmx=bo5mx
                        b5wmy=bo5my  
            if piece=="bishop5":
                b5wmx,b5wmy=pygame.mouse.get_pos()
                g="b5w"


                b5wmx,b5wmy=pygame.mouse.get_pos()
                bo5mx=b5wmx
                bo5my=b5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                b5wmx=convertx(b5wmx)
                b5wmy=converty(b5wmy)
                tg=Bishop5w.position(coords,coords2,b5wmx,b5wmy,"b5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop5change=False
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b5wmy=(yposition)*60
                    b5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno1mx=kn1wmx
                    kno1my=kn1wmy
                    vc="kn1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn1wmx,kn1wmy=pygame.mouse.get_pos()
                    if kn1wmx>xposition and kn1wmx<xposition2 and kn1wmy>yposition and kn1wmy<yposition2:
                        piece="knight1"
                        Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                        Knight1w.possible_moves(coords,coords2,"b")
                    else:
                        kn1wmx=kno1mx
                        kn1wmy=kno1my  
            if piece=="knight1":
                kn1wmx,kn1wmy=pygame.mouse.get_pos()
                g="kn1w"


                kn1wmx,kn1wmy=pygame.mouse.get_pos()
                kno1mx=kn1wmx
                kno1my=kn1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn1wmx=convertx(kn1wmx)
                kn1wmy=converty(kn1wmy)
                tg=Knight1w.position(coords,coords2,kn1wmx,kn1wmy,"kn1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight1change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn1wmy=(yposition)*60
                    kn1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno2mx=kn2wmx
                    kno2my=kn2wmy
                    vc="kn2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn2wmx,kn2wmy=pygame.mouse.get_pos()
                    if kn2wmx>xposition and kn2wmx<xposition2 and kn2wmy>yposition and kn2wmy<yposition2:
                        piece="knight2"
                        Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                        Knight2w.possible_moves(coords,coords2,"b")
                    else:
                        kn2wmx=kno2mx
                        kn2wmy=kno2my  
            if piece=="knight2":
                kn2wmx,kn2wmy=pygame.mouse.get_pos()
                g="kn2w"


                kn2wmx,kn2wmy=pygame.mouse.get_pos()
                kno2mx=kn2wmx
                kno2my=kn2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn2wmx=convertx(kn2wmx)
                kn2wmy=converty(kn2wmy)
                tg=Knight2w.position(coords,coords2,kn2wmx,kn2wmy,"kn2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight2change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn2wmy=(yposition)*60
                    kn2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno3mx=kn3wmx
                    kno3my=kn3wmy
                    vc="kn3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn3wmx,kn3wmy=pygame.mouse.get_pos()
                    if kn3wmx>xposition and kn3wmx<xposition2 and kn3wmy>yposition and kn3wmy<yposition2:
                        piece="knight3"
                        Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                        Knight3w.possible_moves(coords,coords2,"b")
                    else:
                        kn3wmx=kno3mx
                        kn3wmy=kno3my  
            if piece=="knight3":
                kn3wmx,kn3wmy=pygame.mouse.get_pos()
                g="kn3w"


                kn3wmx,kn3wmy=pygame.mouse.get_pos()
                kno3mx=kn3wmx
                kno3my=kn3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn3wmx=convertx(kn3wmx)
                kn3wmy=converty(kn3wmy)
                tg=Knight3w.position(coords,coords2,kn3wmx,kn3wmy,"kn3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight3change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn3wmy=(yposition)*60
                    kn3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno4mx=kn4wmx
                    kno4my=kn4wmy
                    vc="kn4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn4wmx,kn4wmy=pygame.mouse.get_pos()
                    if kn4wmx>xposition and kn4wmx<xposition2 and kn4wmy>yposition and kn4wmy<yposition2:
                        piece="knight4"
                        Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                        Knight4w.possible_moves(coords,coords2,"b")
                    else:
                        kn4wmx=kno4mx
                        kn4wmy=kno4my  
            if piece=="knight4":
                kn4wmx,kn4wmy=pygame.mouse.get_pos()
                g="kn4w"


                kn4wmx,kn4wmy=pygame.mouse.get_pos()
                kno4mx=kn4wmx
                kno4my=kn4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn4wmx=convertx(kn4wmx)
                kn4wmy=converty(kn4wmy)
                tg=Knight4w.position(coords,coords2,kn4wmx,kn4wmy,"kn4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight4change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn4wmy=(yposition)*60
                    kn4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno5mx=kn5wmx
                    kno5my=kn5wmy
                    vc="kn5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn5wmx,kn5wmy=pygame.mouse.get_pos()
                    if kn5wmx>xposition and kn5wmx<xposition2 and kn5wmy>yposition and kn5wmy<yposition2:
                        piece="knight5"
                        Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                        Knight5w.possible_moves(coords,coords2,"b")
                    else:
                        kn5wmx=kno5mx
                        kn5wmy=kno5my  
            if piece=="knight5":
                kn5wmx,kn5wmy=pygame.mouse.get_pos()
                g="kn5w"


                kn5wmx,kn5wmy=pygame.mouse.get_pos()
                kno5mx=kn5wmx
                kno5my=kn5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn5wmx=convertx(kn5wmx)
                kn5wmy=converty(kn5wmy)
                tg=Knight5w.position(coords,coords2,kn5wmx,kn5wmy,"kn5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight5change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn5wmy=(yposition)*60
                    kn5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ko1mx=k1wmx
                    ko1my=k1wmy
                    vc="k1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    k1wmx,k1wmy=pygame.mouse.get_pos()
                    if k1wmx>xposition and k1wmx<xposition2 and k1wmy>yposition and k1wmy<yposition2:
                        piece="king1"
                        King1w=kingw(coords,coords2,kn1wmx,kn1wmy,"k1w","b")
                        King1w.possible_moves(coords,coords2,"b")
                    else:
                        k1wmx=ko1mx
                        k1wmy=ko1my  
            if piece=="king1":
                k1wmx,k1wmy=pygame.mouse.get_pos()
                g="k1w"


                k1wmx,k1wmy=pygame.mouse.get_pos()
                ko1mx=k1wmx
                ko1my=k1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                k1wmx=convertx(k1wmx)
                k1wmy=converty(k1wmy)
                tg=King1w.position(coords,coords2,k1wmx,k1wmy,"k1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    king1change=False
                    moves=moves+1
                    moves2kw=1
                    white_check=False
                    yposition=list_searchy(Board,"r1w")
                    xposition=list_searchx(Board,"r1w")
                    r1wmx=xposition*60
                    r1wmy=yposition*60
                    
                    yposition=list_searchy(Board,"r2w")
                    xposition=list_searchx(Board,"r2w")
                    r2wmx=xposition*60
                    r2wmy=yposition*60
                    hb=0
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    k1wmy=(yposition)*60
                    k1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro1mx=r1wmx
                    ro1my=r1wmy
                    vc="r1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r1wmx,r1wmy=pygame.mouse.get_pos()
                    if r1wmx>xposition and r1wmx<xposition2 and r1wmy>yposition and r1wmy<yposition2:
                        piece="rook1"
                        Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                        Rook1w.possible_moves(coords,coords2,"b")
                    else:
                        r1wmx=ro1mx
                        r1wmy=ro1my  
            if piece=="rook1":
                r1wmx,r1wmy=pygame.mouse.get_pos()
                g="r1w"


                r1wmx,r1wmy=pygame.mouse.get_pos()
                ro1mx=r1wmx
                ro1my=r1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r1wmx=convertx(r1wmx)
                r1wmy=converty(r1wmy)
                tg=Rook1w.position(coords,coords2,r1wmx,r1wmy,"r1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook1change=False
                    moves=moves+1
                    moves2r1w=1
                    white_check=False
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r1wmy=(yposition)*60
                    r1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro2mx=r2wmx
                    ro2my=r2wmy
                    vc="r2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r2wmx,r2wmy=pygame.mouse.get_pos()
                    if r2wmx>xposition and r2wmx<xposition2 and r2wmy>yposition and r2wmy<yposition2:
                        piece="rook2"
                        Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                        Rook2w.possible_moves(coords,coords2,"b")
                    else:
                        r2wmx=ro2mx
                        r2wmy=ro2my  
            if piece=="rook2":
                r2wmx,r2wmy=pygame.mouse.get_pos()
                g="r2w"


                r2wmx,r2wmy=pygame.mouse.get_pos()
                ro2mx=r2wmx
                ro2my=r2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r2wmx=convertx(r2wmx)
                r2wmy=converty(r2wmy)
                tg=Rook2w.position(coords,coords2,r2wmx,r2wmy,"r2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook2change=False
                    moves=moves+1
                    moves2r2w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r2wmy=(yposition)*60
                    r2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro3mx=r3wmx
                    ro3my=r3wmy
                    vc="r3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r3wmx,r3wmy=pygame.mouse.get_pos()
                    if r3wmx>xposition and r3wmx<xposition2 and r3wmy>yposition and r3wmy<yposition2:
                        piece="rook3"
                        Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                        Rook3w.possible_moves(coords,coords2,"b")
                    else:
                        r3wmx=ro3mx
                        r3wmy=ro3my  
            if piece=="rook3":
                r3wmx,r3wmy=pygame.mouse.get_pos()
                g="r3w"


                r3wmx,r3wmy=pygame.mouse.get_pos()
                ro3mx=r3wmx
                ro3my=r3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r3wmx=convertx(r3wmx)
                r3wmy=converty(r3wmy)
                tg=Rook3w.position(coords,coords2,r3wmx,r3wmy,"r3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook3change=False
                    moves=moves+1
                    moves2r3w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r3wmy=(yposition)*60
                    r3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro4mx=r4wmx
                    ro4my=r4wmy
                    vc="r4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r4wmx,r4wmy=pygame.mouse.get_pos()
                    if r4wmx>xposition and r4wmx<xposition2 and r4wmy>yposition and r4wmy<yposition2:
                        piece="rook4"
                        Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                        Rook4w.possible_moves(coords,coords2,"b")
                    else:
                        r4wmx=ro4mx
                        r4wmy=ro4my  
            if piece=="rook4":
                r4wmx,r4wmy=pygame.mouse.get_pos()
                g="r4w"


                r4wmx,r4wmy=pygame.mouse.get_pos()
                ro4mx=r4wmx
                ro4my=r4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r4wmx=convertx(r4wmx)
                r4wmy=converty(r4wmy)
                tg=Rook4w.position(coords,coords2,r4wmx,r4wmy,"r4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook4change=False
                    moves=moves+1
                    moves2r4w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r4wmy=(yposition)*60
                    r4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro5mx=r5wmx
                    ro5my=r5wmy
                    vc="r5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r5wmx,r5wmy=pygame.mouse.get_pos()
                    if r5wmx>xposition and r5wmx<xposition2 and r5wmy>yposition and r5wmy<yposition2:
                        piece="rook5"
                        Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                        Rook5w.possible_moves(coords,coords2,"b")
                    else:
                        r5wmx=ro5mx
                        r5wmy=ro5my  
            if piece=="rook5":
                r5wmx,r5wmy=pygame.mouse.get_pos()
                g="r5w"


                r5wmx,r5wmy=pygame.mouse.get_pos()
                ro5mx=r5wmx
                ro5my=r5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r5wmx=convertx(r5wmx)
                r5wmy=converty(r5wmy)
                tg=Rook5w.position(coords,coords2,r5wmx,r5wmy,"r5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook5change=False
                    moves=moves+1
                    moves2r5w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r5wmy=(yposition)*60
                    r5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo1mx=q1wmx
                    qo1my=q1wmy
                    vc="q1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q1wmx,q1wmy=pygame.mouse.get_pos()
                    if q1wmx>xposition and q1wmx<xposition2 and q1wmy>yposition and q1wmy<yposition2:
                        piece="queen1"
                        Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                        Queen1w.possible_moves(coords,coords2,"b")
                    else:
                        q1wmx=qo1mx
                        q1wmy=qo1my  
            if piece=="queen1":
                q1wmx,q1wmy=pygame.mouse.get_pos()
                g="q1w"


                q1wmx,q1wmy=pygame.mouse.get_pos()
                qo1mx=q1wmx
                qo1my=q1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                q1wmx=convertx(q1wmx)
                q1wmy=converty(q1wmy)
                tg=Queen1w.position(coords,coords2,q1wmx,q1wmy,"q1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen1change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q1wmy=(yposition)*60
                    q1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo2mx=q2wmx
                    qo2my=q2wmy
                    vc="q2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q2wmx,q2wmy=pygame.mouse.get_pos()
                    if q2wmx>xposition and q2wmx<xposition2 and q2wmy>yposition and q2wmy<yposition2:
                        piece="queen2"
                        Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                        Queen2w.possible_moves(coords,coords2,"b")
                    else:
                        q2wmx=qo2mx
                        q2wmy=qo2my  
            if piece=="queen2":
                q2wmx,q2wmy=pygame.mouse.get_pos()
                g="q2w"


                q2wmx,q2wmy=pygame.mouse.get_pos()
                qo2mx=q2wmx
                qo2my=q2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                q2wmx=convertx(q2wmx)
                q2wmy=converty(q2wmy)
                tg=Queen2w.position(coords,coords2,q2wmx,q2wmy,"q2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen2change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q2wmy=(yposition)*60
                    q2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo3mx=q3wmx
                    qo3my=q3wmy
                    vc="q3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q3wmx,q3wmy=pygame.mouse.get_pos()
                    if q3wmx>xposition and q3wmx<xposition2 and q3wmy>yposition and q3wmy<yposition2:
                        piece="queen3"
                        Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                        Queen3w.possible_moves(coords,coords2,"b")
                    else:
                        q3wmx=qo3mx
                        q3wmy=qo3my  
            if piece=="queen3":
                q3wmx,q3wmy=pygame.mouse.get_pos()
                g="q3w"


                q3wmx,q3wmy=pygame.mouse.get_pos()
                qo3mx=q3wmx
                qo3my=q3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                q3wmx=convertx(q3wmx)
                q3wmy=converty(q3wmy)
                tg=Queen3w.position(coords,coords2,q3wmx,q3wmy,"q3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen3change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q3wmy=(yposition)*60
                    q3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo4mx=q4wmx
                    qo4my=q4wmy
                    vc="q4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q4wmx,q4wmy=pygame.mouse.get_pos()
                    if q4wmx>xposition and q4wmx<xposition2 and q4wmy>yposition and q4wmy<yposition2:
                        piece="queen4"
                        Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                        Queen4w.possible_moves(coords,coords2,"b")
                    else:
                        q4wmx=qo4mx
                        q4wmy=qo4my  
            if piece=="queen4":
                q4wmx,q4wmy=pygame.mouse.get_pos()
                g="q4w"


                q4wmx,q4wmy=pygame.mouse.get_pos()
                qo4mx=q4wmx
                qo4my=q4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                q4wmx=convertx(q4wmx)
                q4wmy=converty(q4wmy)
                tg=Queen4w.position(coords,coords2,q4wmx,q4wmy,"q4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen4change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q4wmy=(yposition)*60
                    q4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po1mx=p1wmx
                    po1my=p1wmy
                    vc="p1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p1wmx,p1wmy=pygame.mouse.get_pos()
                    if p1wmx>xposition and p1wmx<xposition2 and p1wmy>yposition and p1wmy<yposition2:
                        piece="pawn1"
                        Pawn1w=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                        Pawn1w.possible_moves(coords,coords2,"b",moves21)
                    else:
                        p1wmx=po1mx
                        p1wmy=po1my  
            if piece=="pawn1":
                p1wmx,p1wmy=pygame.mouse.get_pos()
                g="p1w"


                p1wmx,p1wmy=pygame.mouse.get_pos()
                po1mx=p1wmx
                po1my=p1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p1wmx=convertx(p1wmx)
                p1wmy=converty(p1wmy)
                tg=Pawn1w.position(coords,coords2,p1wmx,p1wmy,"p1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn1change=False
                    moves=moves+1
                    moves21=moves21+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p1wmy=(yposition)*60
                    p1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po2mx=p2wmx
                    po2my=p2wmy
                    vc="p2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p2wmx,p2wmy=pygame.mouse.get_pos()
                    if p2wmx>xposition and p2wmx<xposition2 and p2wmy>yposition and p2wmy<yposition2:
                        piece="pawn2"
                        Pawn2w=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                        Pawn2w.possible_moves(coords,coords2,"b",moves22)
                    else:
                        p2wmx=po2mx
                        p2wmy=po2my  
            if piece=="pawn2":
                p2wmx,p2wmy=pygame.mouse.get_pos()
                g="p2w"


                p2wmx,p2wmy=pygame.mouse.get_pos()
                po2mx=p2wmx
                po2my=p2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p2wmx=convertx(p2wmx)
                p2wmy=converty(p2wmy)
                tg=Pawn2w.position(coords,coords2,p2wmx,p2wmy,"p2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn2change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    moves22=moves22+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p2wmy=(yposition)*60
                    p2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po3mx=p3wmx
                    po3my=p3wmy
                    vc="p3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p3wmx,p3wmy=pygame.mouse.get_pos()
                    if p3wmx>xposition and p3wmx<xposition2 and p3wmy>yposition and p3wmy<yposition2:
                        piece="pawn3"
                        Pawn3w=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                        Pawn3w.possible_moves(coords,coords2,"b",moves23)
                    else:
                        p3wmx=po3mx
                        p3wmy=po3my  
            if piece=="pawn3":
                p3wmx,p3wmy=pygame.mouse.get_pos()
                g="p3w"


                p3wmx,p3wmy=pygame.mouse.get_pos()
                po3mx=p3wmx
                po3my=p3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p3wmx=convertx(p3wmx)
                p3wmy=converty(p3wmy)
                tg=Pawn3w.position(coords,coords2,p3wmx,p3wmy,"p3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn3change=False
                    moves=moves+1
                    moves23=moves23+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p3wmy=(yposition)*60
                    p3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po4mx=p4wmx
                    po4my=p4wmy
                    vc="p4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p4wmx,p4wmy=pygame.mouse.get_pos()
                    if p4wmx>xposition and p4wmx<xposition2 and p4wmy>yposition and p4wmy<yposition2:
                        piece="pawn4"
                        Pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                        Pawn4w.possible_moves(coords,coords2,"b",moves24)
                    else:
                        p4wmx=po4mx
                        p4wmy=po4my  
            if piece=="pawn4":
                p4wmx,p4wmy=pygame.mouse.get_pos()
                g="p4w"


                p4wmx,p4wmy=pygame.mouse.get_pos()
                po4mx=p4wmx
                po4my=p4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p4wmx=convertx(p4wmx)
                p4wmy=converty(p4wmy)
                tg=Pawn4w.position(coords,coords2,p4wmx,p4wmy,"p4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn4change=False
                    moves=moves+1
                    moves24=moves24+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p4wmy=(yposition)*60
                    p4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po5mx=p5wmx
                    po5my=p5wmy
                    vc="p5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p5wmx,p5wmy=pygame.mouse.get_pos()
                    if p5wmx>xposition and p5wmx<xposition2 and p5wmy>yposition and p5wmy<yposition2:
                        piece="pawn5"
                        Pawn5w=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                        Pawn5w.possible_moves(coords,coords2,"b",moves25)
                    else:
                        p5wmx=po5mx
                        p5wmy=po5my  
            if piece=="pawn5":
                p5wmx,p5wmy=pygame.mouse.get_pos()
                g="p5w"


                p5wmx,p5wmy=pygame.mouse.get_pos()
                po5mx=p5wmx
                po5my=p5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p5wmx=convertx(p5wmx)
                p5wmy=converty(p5wmy)
                tg=Pawn5w.position(coords,coords2,p5wmx,p5wmy,"p5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn5change=False
                    moves=moves+1
                    white_check=False
                    hb=0
                    moves25=moves25+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p5wmy=(yposition)*60
                    p5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po6mx=p6wmx
                    po6my=p6wmy
                    vc="p6w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p6wmx,p6wmy=pygame.mouse.get_pos()
                    if p6wmx>xposition and p6wmx<xposition2 and p6wmy>yposition and p6wmy<yposition2:
                        piece="pawn6"
                        Pawn6w=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                        Pawn6w.possible_moves(coords,coords2,"b",moves26)
                    else:
                        p6wmx=po6mx
                        p6wmy=po6my  
            if piece=="pawn6":
                p6wmx,p6wmy=pygame.mouse.get_pos()
                g="p6w"


                p6wmx,p6wmy=pygame.mouse.get_pos()
                po6mx=p6wmx
                po6my=p6wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p6wmx=convertx(p6wmx)
                p6wmy=converty(p6wmy)
                tg=Pawn6w.position(coords,coords2,p6wmx,p6wmy,"p6w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn6change=False
                    moves=moves+1
                    hb=0
                    white_check=False
                    moves26=moves26+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p6wmy=(yposition)*60
                    p6wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po7mx=p7wmx
                    po7my=p7wmy
                    vc="p7w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p7wmx,p7wmy=pygame.mouse.get_pos()
                    if p7wmx>xposition and p7wmx<xposition2 and p7wmy>yposition and p7wmy<yposition2:
                        piece="pawn7"
                        Pawn7w=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                        Pawn7w.possible_moves(coords,coords2,"b",moves27)
                    else:
                        p7wmx=po7mx
                        p7wmy=po7my  
            if piece=="pawn7":
                p7wmx,p7wmy=pygame.mouse.get_pos()
                g="p7w"


                p7wmx,p7wmy=pygame.mouse.get_pos()
                po7mx=p7wmx
                po7my=p7wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p7wmx=convertx(p7wmx)
                p7wmy=converty(p7wmy)
                tg=Pawn7w.position(coords,coords2,p7wmx,p7wmy,"p7w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn7change=False
                    moves=moves+1
                    moves27=moves27+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p7wmy=(yposition)*60
                    p7wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po8mx=p8wmx
                    po8my=p8wmy
                    vc="p8w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p8wmx,p8wmy=pygame.mouse.get_pos()
                    if p8wmx>xposition and p8wmx<xposition2 and p8wmy>yposition and p8wmy<yposition2:
                        piece="pawn8"
                        Pawn8w=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                        Pawn8w.possible_moves(coords,coords2,"b",moves28)
                    else:
                        p8wmx=po8mx
                        p8wmy=po8my  
            if piece=="pawn8":
                p8wmx,p8wmy=pygame.mouse.get_pos()
                g="p8w"


                p8wmx,p8wmy=pygame.mouse.get_pos()
                po8mx=p8wmx
                po8my=p8wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                p8wmx=convertx(p8wmx)
                p8wmy=converty(p8wmy)
                tg=Pawn8w.position(coords,coords2,p8wmx,p8wmy,"p8w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn8change=False
                    moves=moves+1
                    hb=0

                    white_check=False
                    moves28=moves28+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p8wmy=(yposition)*60
                    p8wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################

        if moves==1:

            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro2bmx=r2bmx
                    ro2bmy=r2bmy
                    vc="r2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r2bmx,r2bmy=pygame.mouse.get_pos()
                    if r2bmx>xposition and r2bmx<xposition2 and r2bmy>yposition and r2bmy<yposition2:
                        piece="rook2b"
                        Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                        Rook2b.possible_moves(coords,coords2,"w")
                    else:
                        r2bmx=ro2bmx
                        r2bmy=ro2bmy  
            if piece=="rook2b":
                r2bmx,r2bmy=pygame.mouse.get_pos()
                g="r2b"


                r2bmx,r2bmy=pygame.mouse.get_pos()
                ro2bmx=r2bmx
                ro2bmy=r2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r2bmx=convertx(r2bmx)
                r2bmy=converty(r2bmy)
                tg=Rook2b.position(coords,coords2,r2bmx,r2bmy,"r2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook2bchange=False
                    moves2r2b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r2bmy=(yposition)*60
                    r2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro3bmx=r3bmx
                    ro3bmy=r3bmy
                    vc="r3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r3bmx,r3bmy=pygame.mouse.get_pos()
                    if r3bmx>xposition and r3bmx<xposition2 and r3bmy>yposition and r3bmy<yposition2:
                        piece="rook3b"
                        Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                        Rook3b.possible_moves(coords,coords2,"w")
                    else:
                        r3bmx=ro3bmx
                        r3bmy=ro3bmy  
            if piece=="rook3b":
                r3bmx,r3bmy=pygame.mouse.get_pos()
                g="r3b"


                r3bmx,r3bmy=pygame.mouse.get_pos()
                ro3bmx=r3bmx
                ro3bmy=r3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r3bmx=convertx(r3bmx)
                r3bmy=converty(r3bmy)
                tg=Rook3b.position(coords,coords2,r3bmx,r3bmy,"r3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook3bchange=False
                    moves2r3b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r3bmy=(yposition)*60
                    r3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro4bmx=r4bmx
                    ro4bmy=r4bmy
                    vc="r4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r4bmx,r4bmy=pygame.mouse.get_pos()
                    if r4bmx>xposition and r4bmx<xposition2 and r4bmy>yposition and r4bmy<yposition2:
                        piece="rook4b"
                        Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                        Rook4b.possible_moves(coords,coords2,"w")
                    else:
                        r4bmx=ro4bmx
                        r4bmy=ro4bmy  
            if piece=="rook4b":
                r4bmx,r4bmy=pygame.mouse.get_pos()
                g="r4b"


                r4bmx,r4bmy=pygame.mouse.get_pos()
                ro4bmx=r4bmx
                ro4bmy=r4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r4bmx=convertx(r4bmx)
                r4bmy=converty(r4bmy)
                tg=Rook4b.position(coords,coords2,r4bmx,r4bmy,"r4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook4bchange=False
                    moves2r4b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r4bmy=(yposition)*60
                    r4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro5bmx=r5bmx
                    ro5bmy=r5bmy
                    vc="r5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r5bmx,r5bmy=pygame.mouse.get_pos()
                    if r5bmx>xposition and r5bmx<xposition2 and r5bmy>yposition and r5bmy<yposition2:
                        piece="rook5b"
                        Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                        Rook5b.possible_moves(coords,coords2,"w")
                    else:
                        r5bmx=ro5bmx
                        r5bmy=ro5bmy  
            if piece=="rook5b":
                r5bmx,r5bmy=pygame.mouse.get_pos()
                g="r5b"


                r5bmx,r5bmy=pygame.mouse.get_pos()
                ro5bmx=r5bmx
                ro5bmy=r5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                r5bmx=convertx(r5bmx)
                r5bmy=converty(r5bmy)
                tg=Rook5b.position(coords,coords2,r5bmx,r5bmy,"r5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook5bchange=False
                    moves2r5b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r5bmy=(yposition)*60
                    r5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""

########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno2bmx=kn2bmx
                    kno2bmy=kn2bmy
                    vc="kn2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn2bmx,kn2bmy=pygame.mouse.get_pos()
                    if kn2bmx>xposition and kn2bmx<xposition2 and kn2bmy>yposition and kn2bmy<yposition2:
                        piece="knight2b"
                        Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                        Knight2b.possible_moves(coords,coords2,"w")
                    else:
                        kn2bmx=kno2bmx
                        kn2bmy=kno2bmy  
            if piece=="knight2b":
                kn2bmx,kn2bmy=pygame.mouse.get_pos()
                g="kn2b"


                kn2bmx,kn2bmy=pygame.mouse.get_pos()
                kno2bmx=kn2bmx
                kno2bmy=kn2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn2bmx=convertx(kn2bmx)
                kn2bmy=converty(kn2bmy)
                tg=Knight2b.position(coords,coords2,kn2bmx,kn2bmy,"kn2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight2bchange=False
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn2bmy=(yposition)*60
                    kn2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno3bmx=kn3bmx
                    kno3bmy=kn3bmy
                    vc="kn3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn3bmx,kn3bmy=pygame.mouse.get_pos()
                    if kn3bmx>xposition and kn3bmx<xposition2 and kn3bmy>yposition and kn3bmy<yposition2:
                        piece="knight3b"
                        Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                        Knight3b.possible_moves(coords,coords2,"w")
                    else:
                        kn3bmx=kno3bmx
                        kn3bmy=kno3bmy  
            if piece=="knight3b":
                kn3bmx,kn3bmy=pygame.mouse.get_pos()
                g="kn3b"


                kn3bmx,kn3bmy=pygame.mouse.get_pos()
                kno3bmx=kn3bmx
                kno3bmy=kn3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn3bmx=convertx(kn3bmx)
                kn3bmy=converty(kn3bmy)
                tg=Knight3b.position(coords,coords2,kn3bmx,kn3bmy,"kn3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight3bchange=False
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn3bmy=(yposition)*60
                    kn3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno4bmx=kn4bmx
                    kno4bmy=kn4bmy
                    vc="kn4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn4bmx,kn4bmy=pygame.mouse.get_pos()
                    if kn4bmx>xposition and kn4bmx<xposition2 and kn4bmy>yposition and kn4bmy<yposition2:
                        piece="knight4b"
                        Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                        Knight4b.possible_moves(coords,coords2,"w")
                    else:
                        kn4bmx=kno4bmx
                        kn4bmy=kno4bmy  
            if piece=="knight4b":
                kn4bmx,kn4bmy=pygame.mouse.get_pos()
                g="kn4b"


                kn4bmx,kn4bmy=pygame.mouse.get_pos()
                kno4bmx=kn4bmx
                kno4bmy=kn4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn4bmx=convertx(kn4bmx)
                kn4bmy=converty(kn4bmy)
                tg=Knight4b.position(coords,coords2,kn4bmx,kn4bmy,"kn4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight4bchange=False
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn4bmy=(yposition)*60
                    kn4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno5bmx=kn5bmx
                    kno5bmy=kn5bmy
                    vc="kn5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn5bmx,kn5bmy=pygame.mouse.get_pos()
                    if kn5bmx>xposition and kn5bmx<xposition2 and kn5bmy>yposition and kn5bmy<yposition2:
                        piece="knight5b"
                        Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                        Knight5b.possible_moves(coords,coords2,"w")
                    else:
                        kn5bmx=kno5bmx
                        kn5bmy=kno5bmy  
            if piece=="knight5b":
                kn5bmx,kn5bmy=pygame.mouse.get_pos()
                g="kn5b"


                kn5bmx,kn5bmy=pygame.mouse.get_pos()
                kno5bmx=kn5bmx
                kno5bmy=kn5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                kn5bmx=convertx(kn5bmx)
                kn5bmy=converty(kn5bmy)
                tg=Knight5b.position(coords,coords2,kn5bmx,kn5bmy,"kn5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight5bchange=False
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn5bmy=(yposition)*60
                    kn5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno1bmx=kn1bmx
                    kno1bmy=kn1bmy
                    vc="kn1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    kn1bmx,kn1bmy=pygame.mouse.get_pos()
                    if kn1bmx>xposition and kn1bmx<xposition2 and kn1bmy>yposition and kn1bmy<yposition2:
                        piece="knight1b"
                        Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                        Knight1b.possible_moves(coords,coords2,"w")
                    else:
                        kn1bmx=kno1bmx
                        kn1bmy=kno1bmy  
            if piece=="knight1b":
                kn1bmx,kn1bmy=pygame.mouse.get_pos()
                g="kn1b"


                kn1bmx,kn1bmy=pygame.mouse.get_pos()
                kno1bmx=kn1bmx
                kno1bmy=kn1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn1bmx=convertx(kn1bmx)
                kn1bmy=converty(kn1bmy)
                tg=Knight1b.position(coords,coords2,kn1bmx,kn1bmy,"kn1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    knight1bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn1bmy=(yposition)*60
                    kn1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro1bmx=r1bmx
                    ro1bmy=r1bmy
                    vc="r1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r1bmx,r1bmy=pygame.mouse.get_pos()
                    if r1bmx>xposition and r1bmx<xposition2 and r1bmy>yposition and r1bmy<yposition2:
                        piece="rook1b"
                        Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                        Rook1b.possible_moves(coords,coords2,"w")
                    else:
                        r1bmx=ro1bmx
                        r1bmy=ro1bmy  
            if piece=="rook1b":
                r1bmx,r1bmy=pygame.mouse.get_pos()
                g="r1b"


                r1bmx,r1bmy=pygame.mouse.get_pos()
                ro1bmx=r1bmx
                ro1bmy=r1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r1bmx=convertx(r1bmx)
                r1bmy=converty(r1bmy)
                tg=Rook1b.position(coords,coords2,r1bmx,r1bmy,"r1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    rook1bchange=False
                    moves=moves+1
                    moves2r1b=1
                    coords=[]
                    hw=0
                    black_check=False
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r1bmy=(yposition)*60
                    r1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo2bmx=b2bmx
                    bo2bmy=b2bmy
                    vc="b2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b2bmx,b2bmy=pygame.mouse.get_pos()
                    if b2bmx>xposition and b2bmx<xposition2 and b2bmy>yposition and b2bmy<yposition2:
                        piece="bishop2b"
                        Bishop2b=bishopw(coords,coords2,b2wmx,b2wmy,"b2b","w")
                        Bishop2b.possible_moves(coords,coords2,"w")
                    else:
                        b2bmx=bo2bmx
                        b2bmy=bo2bmy  
            if piece=="bishop2b":
                b2bmx,b2bmy=pygame.mouse.get_pos()
                g="b2b"


                b2bmx,b2bmy=pygame.mouse.get_pos()
                bo2bmx=b2bmx
                bo2bmy=b2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b2bmx=convertx(b2bmx)
                b2bmy=converty(b2bmy)
                tg=Bishop2b.position(coords,coords2,b2bmx,b2bmy,"b2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop2bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b2bmy=(yposition)*60
                    b2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#######################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo3bmx=b3bmx
                    bo3bmy=b3bmy
                    vc="b3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b3bmx,b3bmy=pygame.mouse.get_pos()
                    if b3bmx>xposition and b3bmx<xposition2 and b3bmy>yposition and b3bmy<yposition2:
                        piece="bishop3b"
                        Bishop3b=bishopw(coords,coords2,b3wmx,b3wmy,"b3b","w")
                        Bishop3b.possible_moves(coords,coords2,"w")
                    else:
                        b3bmx=bo3bmx
                        b3bmy=bo3bmy  
            if piece=="bishop3b":
                b3bmx,b3bmy=pygame.mouse.get_pos()
                g="b3b"


                b3bmx,b3bmy=pygame.mouse.get_pos()
                bo3bmx=b3bmx
                bo3bmy=b3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b3bmx=convertx(b3bmx)
                b3bmy=converty(b3bmy)
                tg=Bishop3b.position(coords,coords2,b3bmx,b3bmy,"b3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop3bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b3bmy=(yposition)*60
                    b3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#######################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo4bmx=b4bmx
                    bo4bmy=b4bmy
                    vc="b4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b4bmx,b4bmy=pygame.mouse.get_pos()
                    if b4bmx>xposition and b4bmx<xposition2 and b4bmy>yposition and b4bmy<yposition2:
                        piece="bishop4b"
                        Bishop4b=bishopw(coords,coords2,b4wmx,b4wmy,"b4b","w")
                        Bishop4b.possible_moves(coords,coords2,"w")
                    else:
                        b4bmx=bo4bmx
                        b4bmy=bo4bmy  
            if piece=="bishop4b":
                b4bmx,b4bmy=pygame.mouse.get_pos()
                g="b4b"


                b4bmx,b4bmy=pygame.mouse.get_pos()
                bo4bmx=b4bmx
                bo4bmy=b4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b4bmx=convertx(b4bmx)
                b4bmy=converty(b4bmy)
                tg=Bishop4b.position(coords,coords2,b4bmx,b4bmy,"b4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop4bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b4bmy=(yposition)*60
                    b4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
###############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo5bmx=b5bmx
                    bo5bmy=b5bmy
                    vc="b5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b5bmx,b5bmy=pygame.mouse.get_pos()
                    if b5bmx>xposition and b5bmx<xposition2 and b5bmy>yposition and b5bmy<yposition2:
                        piece="bishop5b"
                        Bishop5b=bishopw(coords,coords2,b5wmx,b5wmy,"b5b","w")
                        Bishop5b.possible_moves(coords,coords2,"w")
                    else:
                        b5bmx=bo5bmx
                        b5bmy=bo5bmy  
            if piece=="bishop5b":
                b5bmx,b5bmy=pygame.mouse.get_pos()
                g="b5b"


                b5bmx,b5bmy=pygame.mouse.get_pos()
                bo5bmx=b5bmx
                bo5bmy=b5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b5bmx=convertx(b5bmx)
                b5bmy=converty(b5bmy)
                tg=Bishop5b.position(coords,coords2,b5bmx,b5bmy,"b5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop5bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b5bmy=(yposition)*60
                    b5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#######################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo1bmx=b1bmx
                    bo1bmy=b1bmy
                    vc="b1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b1bmx,b1bmy=pygame.mouse.get_pos()
                    if b1bmx>xposition and b1bmx<xposition2 and b1bmy>yposition and b1bmy<yposition2:
                        piece="bishop1b"
                        Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                        Bishop1b.possible_moves(coords,coords2,"w")
                    else:
                        b1bmx=bo1bmx
                        b1bmy=bo1bmy  
            if piece=="bishop1b":
                b1bmx,b1bmy=pygame.mouse.get_pos()
                g="b1b"


                b1bmx,b1bmy=pygame.mouse.get_pos()
                bo1bmx=b1bmx
                bo1bmy=b1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b1bmx=convertx(b1bmx)
                b1bmy=converty(b1bmy)
                tg=Bishop1b.position(coords,coords2,b1bmx,b1bmy,"b1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    bishop1bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b1bmy=(yposition)*60
                    b1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo1bmx=q1bmx
                    qo1bmy=q1bmy
                    vc="q1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q1bmx,q1bmy=pygame.mouse.get_pos()
                    if q1bmx>xposition and q1bmx<xposition2 and q1bmy>yposition and q1bmy<yposition2:
                        piece="queen1b"
                        Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                        Queen1b.possible_moves(coords,coords2,"w")
                    else:
                        q1bmx=qo1bmx
                        q1bmy=qo1bmy  
            if piece=="queen1b":
                q1bmx,q1bmy=pygame.mouse.get_pos()
                g="q1b"


                q1bmx,q1bmy=pygame.mouse.get_pos()
                qo1bmx=q1bmx
                qo1bmy=q1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q1bmx=convertx(q1bmx)
                q1bmy=converty(q1bmy)
                tg=Queen1b.position(coords,coords2,q1bmx,q1bmy,"q1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen1bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q1bmy=(yposition)*60
                    q1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo2bmx=q2bmx
                    qo2bmy=q2bmy
                    vc="q2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q2bmx,q2bmy=pygame.mouse.get_pos()
                    if q2bmx>xposition and q2bmx<xposition2 and q2bmy>yposition and q2bmy<yposition2:
                        piece="queen2b"
                        Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                        Queen2b.possible_moves(coords,coords2,"w")
                    else:
                        q2bmx=qo2bmx
                        q2bmy=qo2bmy  
            if piece=="queen2b":
                q2bmx,q2bmy=pygame.mouse.get_pos()
                g="q2b"


                q2bmx,q2bmy=pygame.mouse.get_pos()
                qo2bmx=q2bmx
                qo2bmy=q2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q2bmx=convertx(q2bmx)
                q2bmy=converty(q2bmy)
                tg=Queen2b.position(coords,coords2,q2bmx,q2bmy,"q2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen2bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q2bmy=(yposition)*60
                    q2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo3bmx=q3bmx
                    qo3bmy=q3bmy
                    vc="q3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q3bmx,q3bmy=pygame.mouse.get_pos()
                    if q3bmx>xposition and q3bmx<xposition2 and q3bmy>yposition and q3bmy<yposition2:
                        piece="queen3b"
                        Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                        Queen3b.possible_moves(coords,coords2,"w")
                    else:
                        q3bmx=qo3bmx
                        q3bmy=qo3bmy  
            if piece=="queen3b":
                q3bmx,q3bmy=pygame.mouse.get_pos()
                g="q3b"


                q3bmx,q3bmy=pygame.mouse.get_pos()
                qo3bmx=q3bmx
                qo3bmy=q3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q3bmx=convertx(q3bmx)
                q3bmy=converty(q3bmy)
                tg=Queen3b.position(coords,coords2,q3bmx,q3bmy,"q3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen3bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q3bmy=(yposition)*60
                    q3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo4bmx=q4bmx
                    qo4bmy=q4bmy
                    vc="q4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q4bmx,q4bmy=pygame.mouse.get_pos()
                    if q4bmx>xposition and q4bmx<xposition2 and q4bmy>yposition and q4bmy<yposition2:
                        piece="queen4b"
                        Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                        Queen4b.possible_moves(coords,coords2,"w")
                    else:
                        q4bmx=qo4bmx
                        q4bmy=qo4bmy  
            if piece=="queen4b":
                q4bmx,q4bmy=pygame.mouse.get_pos()
                g="q4b"


                q4bmx,q4bmy=pygame.mouse.get_pos()
                qo4bmx=q4bmx
                qo4bmy=q4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q4bmx=convertx(q4bmx)
                q4bmy=converty(q4bmy)
                tg=Queen4b.position(coords,coords2,q4bmx,q4bmy,"q4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    queen4bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q4bmy=(yposition)*60
                    q4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ko1bmx=k1bmx
                    ko1bmy=k1bmy
                    vc="k1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    k1bmx,k1bmy=pygame.mouse.get_pos()
                    if k1bmx>xposition and k1bmx<xposition2 and k1bmy>yposition and k1bmy<yposition2:
                        piece="king1b"
                        King1b=kingw(coords,coords2,kn1wmx,kn1wmy,"k1b","w")
                        King1b.possible_moves(coords,coords2,"w")
                    else:
                        k1bmx=ko1bmx
                        k1bmy=ko1bmy  
            if piece=="king1b":
                k1bmx,k1bmy=pygame.mouse.get_pos()
                g="k1b"


                k1bmx,k1bmy=pygame.mouse.get_pos()
                ko1bmx=k1bmx
                ko1bmy=k1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                k1bmx=convertx(k1bmx)
                k1bmy=converty(k1bmy)
                tg=King1b.position(coords,coords2,k1bmx,k1bmy,"k1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    king1bchange=False
                    moves=moves+1
                    moves2kb=1
                    yposition=list_searchy(Board,"r1b")
                    xposition=list_searchx(Board,"r1b")
                    r1bmx=xposition*60
                    r1bmy=yposition*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    yposition=list_searchy(Board,"r2b")
                    xposition=list_searchx(Board,"r2b")
                    r2bmx=xposition*60
                    r2bmy=yposition*60
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    k1bmy=(yposition)*60
                    k1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
###################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po1bmx=p1bmx
                    po1bmy=p1bmy
                    vc="p1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p1bmx,p1bmy=pygame.mouse.get_pos()
                    if p1bmx>xposition and p1bmx<xposition2 and p1bmy>yposition and p1bmy<yposition2:
                        piece="pawn1b"
                        Pawn1b=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                        Pawn1b.possible_moves(coords,coords2,"w",moves21b)
                    else:
                        p1bmx=po1bmx
                        p1bmy=po1bmy  
            if piece=="pawn1b":
                p1bmx,p1bmy=pygame.mouse.get_pos()
                g="p1b"


                p1bmx,p1bmy=pygame.mouse.get_pos()
                po1bmx=p1bmx
                po1bmy=p1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p1bmx=convertx(p1bmx)
                p1bmy=converty(p1bmy)
                tg=Pawn1b.position(coords,coords2,p1bmx,p1bmy,"p1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn1bchange=False
                    moves=moves+1
                    black_check=False
                    hw=0
                    moves21b=moves21b+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p1bmy=(yposition)*60
                    p1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po2bmx=p2bmx
                    po2bmy=p2bmy
                    vc="p2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p2bmx,p2bmy=pygame.mouse.get_pos()
                    if p2bmx>xposition and p2bmx<xposition2 and p2bmy>yposition and p2bmy<yposition2:
                        piece="pawn2b"
                        Pawn2b=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                        Pawn2b.possible_moves(coords,coords2,"w",moves22b)
                    else:
                        p2bmx=po2bmx
                        p2bmy=po2bmy  
            if piece=="pawn2b":
                p2bmx,p2bmy=pygame.mouse.get_pos()
                g="p2b"


                p2bmx,p2bmy=pygame.mouse.get_pos()
                po2bmx=p2bmx
                po2bmy=p2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p2bmx=convertx(p2bmx)
                p2bmy=converty(p2bmy)
                tg=Pawn2b.position(coords,coords2,p1bmx,p1bmy,"p2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn2bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    moves22b=moves22b+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p2bmy=(yposition)*60
                    p2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po3bmx=p3bmx
                    po3bmy=p3bmy
                    vc="p3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p3bmx,p3bmy=pygame.mouse.get_pos()
                    if p3bmx>xposition and p3bmx<xposition2 and p3bmy>yposition and p3bmy<yposition2:
                        piece="pawn3b"
                        Pawn3b=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                        Pawn3b.possible_moves(coords,coords2,"w",moves23b)
                    else:
                        p3bmx=po3bmx
                        p3bmy=po3bmy  
            if piece=="pawn3b":
                p3bmx,p3bmy=pygame.mouse.get_pos()
                g="p3b"


                p3bmx,p3bmy=pygame.mouse.get_pos()
                po3bmx=p3bmx
                po3bmy=p3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p3bmx=convertx(p3bmx)
                p3bmy=converty(p3bmy)
                tg=Pawn3b.position(coords,coords2,p3bmx,p3bmy,"p3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn3bchange=False
                    moves=moves+1
                    moves23b=moves23b+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p3bmy=(yposition)*60
                    p3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po4bmx=p4bmx
                    po4bmy=p4bmy
                    vc="p4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p4bmx,p4bmy=pygame.mouse.get_pos()
                    if p4bmx>xposition and p4bmx<xposition2 and p4bmy>yposition and p4bmy<yposition2:
                        piece="pawn4b"
                        Pawn4b=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                        Pawn4b.possible_moves(coords,coords2,"w",moves24b)
                    else:
                        p4bmx=po4bmx
                        p4bmy=po4bmy  
            if piece=="pawn4b":
                p4bmx,p4bmy=pygame.mouse.get_pos()
                g="p4b"


                p4bmx,p4bmy=pygame.mouse.get_pos()
                po4bmx=p4bmx
                po4bmy=p4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p4bmx=convertx(p4bmx)
                p4bmy=converty(p4bmy)
                tg=Pawn4b.position(coords,coords2,p4bmx,p4bmy,"p4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn4bchange=False
                    moves=moves+1
                    black_check=False
                    moves24b=moves24b+1
                    hw=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p4bmy=(yposition)*60
                    p4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po5bmx=p5bmx
                    po5bmy=p5bmy
                    vc="p5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p5bmx,p5bmy=pygame.mouse.get_pos()
                    if p5bmx>xposition and p5bmx<xposition2 and p5bmy>yposition and p5bmy<yposition2:
                        piece="pawn5b"
                        Pawn5b=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                        Pawn5b.possible_moves(coords,coords2,"w",moves25b)
                    else:
                        p5bmx=po5bmx
                        p5bmy=po5bmy  
            if piece=="pawn5b":
                p5bmx,p5bmy=pygame.mouse.get_pos()
                g="p5b"


                p5bmx,p5bmy=pygame.mouse.get_pos()
                po5bmx=p5bmx
                po5bmy=p5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p5bmx=convertx(p5bmx)
                p5bmy=converty(p5bmy)
                tg=Pawn5b.position(coords,coords2,p5bmx,p5bmy,"p5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn5bchange=False
                    moves=moves+1
                    hw=0
                    moves25b=moves25b+1
                    coords=[]
                    black_check=False
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p5bmy=(yposition)*60
                    p5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po6bmx=p6bmx
                    po6bmy=p6bmy
                    vc="p6b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p6bmx,p6bmy=pygame.mouse.get_pos()
                    if p6bmx>xposition and p6bmx<xposition2 and p6bmy>yposition and p6bmy<yposition2:
                        piece="pawn6b"
                        Pawn6b=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                        Pawn6b.possible_moves(coords,coords2,"w",moves26b)
                    else:
                        p6bmx=po6bmx
                        p6bmy=po6bmy  
            if piece=="pawn6b":
                p6bmx,p6bmy=pygame.mouse.get_pos()
                g="p6b"
                p6bmx,p6bmy=pygame.mouse.get_pos()
                po6bmx=p6bmx
                po6bmy=p6bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p6bmx=convertx(p6bmx)
                p6bmy=converty(p6bmy)
                tg=Pawn6b.position(coords,coords2,p6bmx,p6bmy,"p6b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn6bchange=False
                    moves=moves+1
                    moves26b=moves26b+1
                    hw=0

                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p6bmy=(yposition)*60
                    p6bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po7bmx=p7bmx
                    po7bmy=p7bmy
                    vc="p7b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p7bmx,p7bmy=pygame.mouse.get_pos()
                    if p7bmx>xposition and p7bmx<xposition2 and p7bmy>yposition and p7bmy<yposition2:
                        piece="pawn7b"
                        Pawn7b=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                        Pawn7b.possible_moves(coords,coords2,"w",moves27b)
                    else:
                        p7bmx=po7bmx
                        p7bmy=po7bmy  
            if piece=="pawn7b":
                p7bmx,p7bmy=pygame.mouse.get_pos()
                g="p7b"


                p7bmx,p7bmy=pygame.mouse.get_pos()
                po7bmx=p7bmx
                po7bmy=p7bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p7bmx=convertx(p7bmx)
                p7bmy=converty(p7bmy)
                tg=Pawn7b.position(coords,coords2,p7bmx,p7bmy,"p7b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn7bchange=False
                    moves=moves+1
                    hw=0
                    black_check=False
                    moves27b=moves27b+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p7bmy=(yposition)*60
                    p7bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po8bmx=p8bmx
                    po8bmy=p8bmy
                    vc="p8b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p8bmx,p8bmy=pygame.mouse.get_pos()
                    if p8bmx>xposition and p8bmx<xposition2 and p8bmy>yposition and p8bmy<yposition2:
                        piece="pawn8b"
                        Pawn8b=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                        Pawn8b.possible_moves(coords,coords2,"w",moves28b)
                    else:
                        p8bmx=po8bmx
                        p8bmy=po8bmy  
            if piece=="pawn8b":
                p8bmx,p8bmy=pygame.mouse.get_pos()
                g="p8b"


                p8bmx,p8bmy=pygame.mouse.get_pos()
                po8bmx=p8bmx
                po8bmy=p8bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p8bmx=convertx(p8bmx)
                p8bmy=converty(p8bmy)
                tg=Pawn8b.position(coords,coords2,p8bmx,p8bmy,"p8b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    pawn8bchange=False
                    moves=moves+1
                    black_check=False
                    moves28b=moves28b+1
                    hw=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p8bmy=(yposition)*60
                    p8bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            
            
            
        yposition=list_searchy(Board,"p1b")
        xposition=list_searchx(Board,"p1b")
        
        if xposition==9:
            pawn_black1_status="dead"

        yposition=list_searchy(Board,"p2b")
        xposition=list_searchx(Board,"p2b")
        if xposition==9:
            pawn_black2_status="dead"

            
        yposition=list_searchy(Board,"p3b")
        xposition=list_searchx(Board,"p3b")
        if xposition==9:
            pawn_black3_status="dead"


        yposition=list_searchy(Board,"p4b")
        xposition=list_searchx(Board,"p4b")
        if xposition==9:
            pawn_black4_status="dead"

            
        yposition=list_searchy(Board,"p5b")
        xposition=list_searchx(Board,"p5b")
        if xposition==9:
            pawn_black5_status="dead"


            
        yposition=list_searchy(Board,"p6b")
        xposition=list_searchx(Board,"p6b")
        if xposition==9:
            pawn_black6_status="dead"


        yposition=list_searchy(Board,"p7b")
        xposition=list_searchx(Board,"p7b")
        if xposition==9:
            pawn_black7_status="dead"



        yposition=list_searchy(Board,"p8b")
        xposition=list_searchx(Board,"p8b")
        if xposition==9:
            pawn_black8_status="dead"
            


        yposition=list_searchy(Board,"p1w")
        xposition=list_searchx(Board,"p1w")
        if xposition==9:
            pawn_white1_status="dead"


        yposition=list_searchy(Board,"p2w")
        xposition=list_searchx(Board,"p2w")
        if xposition==9:
            pawn_white2_status="dead"

            
        yposition=list_searchy(Board,"p3w")
        xposition=list_searchx(Board,"p3w")
        if xposition==9:
            pawn_white3_status="dead"


        yposition=list_searchy(Board,"p4w")
        xposition=list_searchx(Board,"p4w")
        if xposition==9:
            pawn_white4_status="dead"

            
        yposition=list_searchy(Board,"p5w")
        xposition=list_searchx(Board,"p5w")
        if xposition==9:
            pawn_white5_status="dead"


            
        yposition=list_searchy(Board,"p6w")
        xposition=list_searchx(Board,"p6w")
        if xposition==9:
            pawn_white6_status="dead"


        yposition=list_searchy(Board,"p7w")
        xposition=list_searchx(Board,"p7w")
        if xposition==9:
            pawn_white7_status="dead"



        yposition=list_searchy(Board,"p8w")
        xposition=list_searchx(Board,"p8w")
        if xposition==9:
            pawn_white8_status="dead"

        yposition=list_searchy(Board,"r1w")
        xposition=list_searchx(Board,"r1w")
        if xposition==9:
            rook_white1_status="dead"

    
        yposition=list_searchy(Board,"r2w")
        xposition=list_searchx(Board,"r2w")
        if xposition==9:
            rook_white2_status="dead"

        yposition=list_searchy(Board,"r3w")
        xposition=list_searchx(Board,"r3w")
        if xposition==9:
            rook_white3_status="dead"

        yposition=list_searchy(Board,"r3w")
        xposition=list_searchx(Board,"r3w")
        if rook3w_spawn==0:
            if xposition!=9:
                rook_white3_status="alive"
                r3wmx=xposition*60
                r3wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                rook3w_spawn=1
                
        yposition=list_searchy(Board,"r4w")
        xposition=list_searchx(Board,"r4w")
        if xposition==9:
            rook_white4_status="dead"

        yposition=list_searchy(Board,"r4w")
        xposition=list_searchx(Board,"r4w")
        if rook4w_spawn==0:
            if xposition!=9:
                rook_white4_status="alive"
                r4wmx=xposition*60
                r4wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                rook4w_spawn=1
                
        yposition=list_searchy(Board,"r5w")
        xposition=list_searchx(Board,"r5w")
        if xposition==9:
            rook_white5_status="dead"

        yposition=list_searchy(Board,"r5w")
        xposition=list_searchx(Board,"r5w")
        if rook5w_spawn==0:
            if xposition!=9:
                rook_white5_status="alive"
                r5wmx=xposition*60
                r5wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                rook5w_spawn=1

        yposition=list_searchy(Board,"kn1w")
        xposition=list_searchx(Board,"kn1w")
        if xposition==9:
            knight_white1_status="dead"

        yposition=list_searchy(Board,"kn2w")
        xposition=list_searchx(Board,"kn2w")
        if xposition==9:
            knight_white2_status="dead"

        yposition=list_searchy(Board,"kn3w")
        xposition=list_searchx(Board,"kn3w")
        if xposition==9:
            knight_white3_status="dead"

        yposition=list_searchy(Board,"kn3w")
        xposition=list_searchx(Board,"kn3w")
        if knight3w_spawn==0:
            if xposition!=9:
                knight_white3_status="alive"
                kn3wmx=xposition*60
                kn3wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                knight3w_spawn=1

        yposition=list_searchy(Board,"kn4w")
        xposition=list_searchx(Board,"kn4w")
        if xposition==9:
            knight_white4_status="dead"

        yposition=list_searchy(Board,"kn4w")
        xposition=list_searchx(Board,"kn4w")
        if knight4w_spawn==0:
            if xposition!=9:
                knight_white4_status="alive"
                kn4wmx=xposition*60
                kn4wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                knight4w_spawn=1

        yposition=list_searchy(Board,"kn5w")
        xposition=list_searchx(Board,"kn5w")
        if xposition==9:
            knight_white5_status="dead"

        yposition=list_searchy(Board,"kn5w")
        xposition=list_searchx(Board,"kn5w")
        if knight5w_spawn==0:
            if xposition!=9:
                knight_white5_status="alive"
                kn5wmx=xposition*60
                kn5wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                knight5w_spawn=1
            
        yposition=list_searchy(Board,"b1w")
        xposition=list_searchx(Board,"b1w")
        if xposition==9:
            bishop_white1_status="dead"

            
        yposition=list_searchy(Board,"b2w")
        xposition=list_searchx(Board,"b2w")
        if xposition==9:
            bishop_white2_status="dead"

        yposition=list_searchy(Board,"b2w")
        xposition=list_searchx(Board,"b2w")
        if xposition==9:
            bishop_white2_status="dead"

        yposition=list_searchy(Board,"b3w")
        xposition=list_searchx(Board,"b3w")
        if xposition==9:
            bishop_white3_status="dead"
            
        yposition=list_searchy(Board,"b3w")
        xposition=list_searchx(Board,"b3w")
        if bishop3w_spawn==0:
            if xposition!=9:
                bishop_white3_status="alive"
                b3wmx=xposition*60
                b3wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                bishop3w_spawn=1

        yposition=list_searchy(Board,"b4w")
        xposition=list_searchx(Board,"b4w")
        if xposition==9:
            bishop_white4_status="dead"

        yposition=list_searchy(Board,"b4w")
        xposition=list_searchx(Board,"b4w")
        if bishop4w_spawn==0:
            if xposition!=9:
                bishop_white4_status="alive"
                b4wmx=xposition*60
                b4wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                bishop4w_spawn=1
                
        yposition=list_searchy(Board,"b5w")
        xposition=list_searchx(Board,"b5w")
        if xposition==9:
            bishop_white5_status="dead"
            
        yposition=list_searchy(Board,"b5w")
        xposition=list_searchx(Board,"b5w")
        if bishop5w_spawn==0:
            if xposition!=9:
                bishop_white5_status="alive"
                b5wmx=xposition*60
                b5wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                bishop5w_spawn=1
                
        yposition=list_searchy(Board,"k1w")
        xposition=list_searchx(Board,"k1w")
        if xposition==9:
            king_white_status="dead"    
        yposition=list_searchy(Board,"q1w")
        xposition=list_searchx(Board,"q1w")
        if xposition==9:
            queen_white_status="dead"

        yposition=list_searchy(Board,"q2w")
        xposition=list_searchx(Board,"q2w")
        if xposition==9:
            queen_white2_status="dead"

        yposition=list_searchy(Board,"q2w")
        xposition=list_searchx(Board,"q2w")
        if queen2w_spawn==0:
            if xposition!=9:
                queen_white2_status="alive"
                q2wmx=xposition*60
                q2wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                queen2w_spawn=1
                
        yposition=list_searchy(Board,"q3w")
        xposition=list_searchx(Board,"q3w")
        if xposition==9:
            queen_white3_status="dead"

        yposition=list_searchy(Board,"q3w")
        xposition=list_searchx(Board,"q3w")
        if queen3w_spawn==0:
            if xposition!=9:
                queen_white3_status="alive"
                q3wmx=xposition*60
                q3wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                queen3w_spawn=1
        yposition=list_searchy(Board,"q4w")
        xposition=list_searchx(Board,"q4w")
        if xposition==9:
            queen_white4_status="dead"

        yposition=list_searchy(Board,"q4w")
        xposition=list_searchx(Board,"q4w")
        if queen4w_spawn==0:
            if xposition!=9:
                queen_white4_status="alive"
                q4wmx=xposition*60
                q4wmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                queen4w_spawn=1

        yposition=list_searchy(Board,"r1b")
        xposition=list_searchx(Board,"r1b")
        if xposition==9:
            rook_black1_status="dead"

        yposition=list_searchy(Board,"r2b")
        xposition=list_searchx(Board,"r2b")
        if xposition==9:
            rook_black2_status="dead"

        yposition=list_searchy(Board,"r3b")
        xposition=list_searchx(Board,"r3b")
        if rook3b_spawn==0:
            if xposition==9:
                rook_black3_status="dead"
                yposition=list_searchy(Board,"r3b")
                xposition=list_searchx(Board,"r3b")
                rook3b_spawn=1
            
        if xposition!=9:
            rook_black3_status="alive"
            r3bmx=xposition*60
            r3bmy=yposition*60
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)

        yposition=list_searchy(Board,"r4b")
        xposition=list_searchx(Board,"r4b")
        if xposition==9:
            rook_black4_status="dead"
        yposition=list_searchy(Board,"r4b")
        xposition=list_searchx(Board,"r4b")
        if rook4b_spawn==0:
            if xposition!=9:
                rook_black4_status="alive"
                r4bmx=xposition*60
                r4bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                rook4b_spawn=1

        yposition=list_searchy(Board,"r5b")
        xposition=list_searchx(Board,"r5b")
        if xposition==9:
            rook_black5_status="dead"
        yposition=list_searchy(Board,"r5b")
        xposition=list_searchx(Board,"r5b")
        if rook5b_spawn==0:
            if xposition!=9:
                rook_black5_status="alive"
                r5bmx=xposition*60
                r5bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                rook5b_spawn=1
                
        yposition=list_searchy(Board,"kn1b")
        xposition=list_searchx(Board,"kn1b")
        if xposition==9:
            knight_black1_status="dead"

        yposition=list_searchy(Board,"kn2b")
        xposition=list_searchx(Board,"kn2b")
        if xposition==9:
            knight_black2_status="dead"

        yposition=list_searchy(Board,"kn3b")
        xposition=list_searchx(Board,"kn3b")
        if xposition==9:
            knight_black3_status="dead"
            
        yposition=list_searchy(Board,"kn3b")
        xposition=list_searchx(Board,"kn3b")
        if knight3b_spawn==0:
            if xposition!=9:
                knight_black3_status="alive"
                kn3bmx=xposition*60
                kn3bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                knight3b_spawn=1
                
        yposition=list_searchy(Board,"kn4b")
        xposition=list_searchx(Board,"kn4b")
        if xposition==9:
            knight_black4_status="dead"
        yposition=list_searchy(Board,"kn4b")
        xposition=list_searchx(Board,"kn4b")
        if knight4b_spawn==0:
            if xposition!=9:
                knight_black4_status="alive"
                kn4bmx=xposition*60
                kn4bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                knight4b_spawn=1
                
        yposition=list_searchy(Board,"kn5b")
        xposition=list_searchx(Board,"kn5b")
        if xposition==9:
            knight_black5_status="dead"
        yposition=list_searchy(Board,"kn5b")
        xposition=list_searchx(Board,"kn5b")
        if knight5b_spawn==0:
            if xposition!=9:
                knight_black5_status="alive"
                kn5bmx=xposition*60
                kn5bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                knight5b_spawn=1
                
        yposition=list_searchy(Board,"b1b")
        xposition=list_searchx(Board,"b1b")
        if xposition==9:
            bishop_black1_status="dead"

            
        yposition=list_searchy(Board,"b2b")
        xposition=list_searchx(Board,"b2b")
        if xposition==9:
            bishop_black2_status="dead"

        yposition=list_searchy(Board,"b3b")
        xposition=list_searchx(Board,"b3b")
        if xposition==9:
            bishop_black3_status="dead"
        yposition=list_searchy(Board,"b3b")
        xposition=list_searchx(Board,"b3b")
        if bishop3b_spawn==0:
            if xposition!=9:
                bishop_black3_status="alive"
                b3bmx=xposition*60
                b3bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                bishop3b_spawn=1

        yposition=list_searchy(Board,"b4b")
        xposition=list_searchx(Board,"b4b")
        if xposition==9:
            bishop_black4_status="dead"
        yposition=list_searchy(Board,"b4b")
        xposition=list_searchx(Board,"b4b")
        if bishop4b_spawn==0:
            if xposition!=9:
                bishop_black4_status="alive"
                b4bmx=xposition*60
                b4bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                bishop4b_spawn=1

        yposition=list_searchy(Board,"b5b")
        xposition=list_searchx(Board,"b5b")
        if xposition==9:
            bishop_black5_status="dead"
        yposition=list_searchy(Board,"b5b")
        xposition=list_searchx(Board,"b5b")
        if bishop5b_spawn==0:
            if xposition!=9:
                bishop_black5_status="alive"
                b5bmx=xposition*60
                b5bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                bishop5b_spawn=1
                
        yposition=list_searchy(Board,"k1b")
        xposition=list_searchx(Board,"k1b")
        if xposition==9:
            king_black_status="dead"

            
        yposition=list_searchy(Board,"q1b")
        xposition=list_searchx(Board,"q1b")
        if xposition==9:
            queen_black_status="dead"

        yposition=list_searchy(Board,"q2b")
        xposition=list_searchx(Board,"q2b")
        if xposition==9:
            queen_black2_status="dead"

        yposition=list_searchy(Board,"q2b")
        xposition=list_searchx(Board,"q2b")
        if queen2b_spawn==0:
            if xposition!=9:
                queen_black2_status="alive"
                q2bmx=xposition*60
                q2bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                queen2b_spawn=1
                
        yposition=list_searchy(Board,"q3b")
        xposition=list_searchx(Board,"q3b")
        if xposition==9:
            queen_black3_status="dead"

        yposition=list_searchy(Board,"q3b")
        xposition=list_searchx(Board,"q3b")
        if queen3b_spawn==0:
            if xposition!=9:
                queen_black3_status="alive"
                q3bmx=xposition*60
                q3bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                queen3b_spawn=1
                
        yposition=list_searchy(Board,"q4b")
        xposition=list_searchx(Board,"q4b")
        if xposition==9:
            queen_black4_status="dead"
 
        yposition=list_searchy(Board,"q4b")
        xposition=list_searchx(Board,"q4b")
        if queen4b_spawn==0:
            if xposition!=9:
                queen_black4_status="alive"
                q4bmx=xposition*60
                q4bmy=yposition*60
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                queen4b_spawn=1
           
        if rook1change==False:
            r1wmx,r1wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook1change=True

        if rook2change==False:
            r2wmx,r2wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook2change=True

        if rook3change==False:
            r3wmx,r3wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook3change=True

        if rook4change==False:
            r4wmx,r4wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook4change=True

        if rook5change==False:
            r5wmx,r5wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook5change=True
            
        if rook2bchange==False:
            r2bmx,r2bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook2bchange=True

        if rook1bchange==False:
            r1bmx,r1bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook1bchange=True

        if rook3bchange==False:
            r3bmx,r3bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook3bchange=True

        if rook4bchange==False:
            r4bmx,r4bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook4bchange=True

        if rook5bchange==False:
            r5bmx,r5bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            rook5bchange=True
            
        if bishop1change==False:
            b1wmx,b1wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop1change=True

            
        if bishop2change==False:
            b2wmx,b2wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop2change=True

        if bishop3change==False:
            b3wmx,b3wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop3change=True

        if bishop4change==False:
            b4wmx,b4wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop4change=True

        if bishop5change==False:
            b5wmx,b5wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop5change=True
            
        if bishop1bchange==False:
            b1bmx,b1bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop1bchange=True

        if bishop2bchange==False:
            b2bmx,b2bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop2bchange=True

        if bishop3bchange==False:
            b3bmx,b3bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop3bchange=True

        if bishop4bchange==False:
            b4bmx,b4bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop4bchange=True

        if bishop5bchange==False:
            b5bmx,b5bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            bishop5bchange=True
            
        if knight1change==False:
            kn1wmx,kn1wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight1change=True

        if knight2change==False:
            kn2wmx,kn2wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight2change=True

        if knight3change==False:
            kn3wmx,kn3wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight3change=True

        if knight4change==False:
            kn4wmx,kn4wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight4change=True

        if knight5change==False:
            kn5wmx,kn5wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight5change=True
            
        if knight1bchange==False:
            kn1bmx,kn1bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight1bchange=True

        if knight2bchange==False:
            kn2bmx,kn2bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight2bchange=True

        if knight3bchange==False:
            kn3bmx,kn3bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight3bchange=True

        if knight4bchange==False:
            kn4bmx,kn4bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight4bchange=True

        if knight5bchange==False:
            kn5bmx,kn5bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            knight5bchange=True

        if queen1change==False:
            q1wmx,q1wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen1change=True

        if queen1bchange==False:
            q1bmx,q1bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen1bchange=True

        if queen2change==False:
            q2wmx,q2wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen2change=True

        if queen2bchange==False:
            q2bmx,q2bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen2bchange=True

        if queen3change==False:
            q3wmx,q3wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen3change=True

        if queen3bchange==False:
            q3bmx,q3bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen3bchange=True

        if queen4change==False:
            q4wmx,q4wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen4change=True

        if queen4bchange==False:
            q4bmx,q4bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            queen4bchange=True
            
        if king1change==False:
            k1wmx,k1wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            king1change=True

        if king1bchange==False:
            k1bmx,k1bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            king1bchange=True

        if pawn1change==False:
            p1wmx,p1wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn1change=True

        if pawn2change==False:
            p2wmx,p2wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn2change=True

        if pawn3change==False:
            p3wmx,p3wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn3change=True

        if pawn4change==False:
            p4wmx,p4wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn4change=True

        if pawn5change==False:
            p5wmx,p5wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn5change=True

        if pawn6change==False:
            p6wmx,p6wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn6change=True

        if pawn7change==False:
            p7wmx,p7wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn7change=True

        if pawn8change==False:
            p8wmx,p8wmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn8change=True


        if pawn1bchange==False:
            p1bmx,p1bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn1bchange=True

        if pawn2bchange==False:
            p2bmx,p2bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn2bchange=True

        if pawn3bchange==False:
            p3bmx,p3bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn3bchange=True

        if pawn4bchange==False:
            p4bmx,p4bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn4bchange=True

        if pawn5bchange==False:
            p5bmx,p5bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn5bchange=True

        if pawn6bchange==False:
            p6bmx,p6bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn6bchange=True

        if pawn7bchange==False:
            p7bmx,p7bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn7bchange=True
            
        if pawn8bchange==False:
            p8bmx,p8bmy=pygame.mouse.get_pos()
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            pawn8bchange=True
        board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)

        for er in range (0, len(coords2)):
            pygame.draw.circle(win,(255,0,0),(coords2[0][0],coords2[0][1]),15,0)
        for er in range (0, len(coords)):
            pygame.draw.circle(win,(50,205,50),(coords[er][0],coords[er][1]),15,0)
            
    pygame.display.update()
pygame.QUIT
