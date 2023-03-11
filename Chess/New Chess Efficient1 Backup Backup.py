import pygame
pygame.init()
from pygame.locals import *
class queenw(object):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            if vc[0]=="q" or vc[0]=="r":
                for i in range(1,9):
                    if (yposition)<8 and (xposition+i)<8 and (yposition)>-1 and (xposition+i)>-1 and  (yposition)<8 and (xposition+i)<8  and Board[(yposition)][(xposition+i)][0]=="" :
                        self.coords.append([(xposition+i)*60+30,(yposition)*60+30])
                    else:
                        if (yposition)<8 and (xposition+i)<8 and  (yposition)>-1 and (xposition+i)>-1 and  (yposition)<8 and (xposition+i)<8  and Board[(yposition)][(xposition+i)][1]==self.colour:
                            self.coords.append([(xposition+i)*60+30,(yposition)*60+30])
                        break;
                for i in range(1,9):
                    if (yposition)<8 and (xposition-i)<8 and (yposition)>-1 and (xposition-i)>-1 and  (yposition)<8 and (xposition-i)<8  and Board[(yposition)][(xposition-i)][0]=="" :
                        self.coords.append([(xposition-i)*60+30,(yposition)*60+30])
                    else:
                        if (yposition)<8 and (xposition-i)<8 and  (yposition)>-1 and (xposition-i)>-1 and  (yposition)<8 and (xposition-i)<8  and Board[(yposition)][(xposition-i)][1]==self.colour:
                            self.coords.append([(xposition-i)*60+30,(yposition)*60+30])
                        break;
                for i in range(1,9):
                    if (yposition-i)<8 and (xposition)<8 and (yposition-i)>-1 and (xposition)>-1 and  (yposition-i)<8 and (xposition)<8  and Board[(yposition-i)][(xposition)][0]=="" :
                        self.coords.append([(xposition)*60+30,(yposition-i)*60+30])
                    else:
                        if (yposition-i)<8 and (xposition)<8 and  (yposition-i)>-1 and (xposition)>-1 and  (yposition-i)<8 and (xposition)<8  and Board[(yposition-i)][(xposition)][1]==self.colour:
                            self.coords.append([(xposition)*60+30,(yposition-i)*60+30])
                        break;
                for i in range(1,9):
                    if (yposition+i)<8 and (xposition)<8 and (yposition+i)>-1 and (xposition)>-1 and  (yposition+i)<8 and (xposition)<8  and Board[(yposition+i)][(xposition)][0]=="" :
                        self.coords.append([(xposition)*60+30,(yposition+i)*60+30])
                    else:
                        if (yposition+i)<8 and (xposition)<8 and  (yposition+i)>-1 and (xposition)>-1 and  (yposition+i)<8 and (xposition)<8  and Board[(yposition+i)][(xposition)][1]==self.colour:
                            self.coords.append([(xposition)*60+30,(yposition+i)*60+30])
                        break;
            if vc[0]=="q" or vc[0]=="b":
                for i in range(1,9):
                    if (yposition+i)<8 and (xposition+i)<8 and (yposition+i)>-1 and (xposition+i)>-1 and  (yposition+i)<8 and (xposition+i)<8  and Board[(yposition+i)][(xposition+i)][0]=="" :
                        self.coords.append([(xposition+i)*60+30,(yposition+i)*60+30])
                    else:
                        if (yposition+i)<8 and (xposition+i)<8 and  (yposition+i)>-1 and (xposition+i)>-1 and  (yposition+i)<8 and (xposition+i)<8  and Board[(yposition+i)][(xposition+i)][1]==self.colour:
                            self.coords.append([(xposition+i)*60+30,(yposition+i)*60+30])
                        break;
                for i in range(1,9):
                    if (yposition-i)<8 and (xposition-i)<8 and (yposition-i)>-1 and (xposition-i)>-1 and  (yposition-i)<8 and (xposition-i)<8  and Board[(yposition-i)][(xposition-i)][0]=="" :
                        self.coords.append([(xposition-i)*60+30,(yposition-i)*60+30])
                    else:
                        if (yposition-i)<8 and (xposition-i)<8 and  (yposition-i)>-1 and (xposition-i)>-1 and  (yposition-i)<8 and (xposition-i)<8  and Board[(yposition-i)][(xposition-i)][1]==self.colour:
                            self.coords.append([(xposition-i)*60+30,(yposition-i)*60+30])
                        break;
                for i in range(1,9):
                    if (yposition-i)<8 and (xposition+i)<8 and (yposition-i)>-1 and (xposition+i)>-1 and  (yposition-i)<8 and (xposition+i)<8  and Board[(yposition-i)][(xposition+i)][0]=="" :
                        self.coords.append([(xposition+i)*60+30,(yposition-i)*60+30])
                    else:
                        if (yposition-i)<8 and (xposition+i)<8 and  (yposition-i)>-1 and (xposition+i)>-1 and  (yposition-i)<8 and (xposition+i)<8  and Board[(yposition-i)][(xposition+i)][1]==self.colour:
                            self.coords.append([(xposition+i)*60+30,(yposition-i)*60+30])
                        break;
                for i in range(1,9):
                    if (yposition+i)<8 and (xposition-i)<8 and (yposition+i)>-1 and (xposition-i)>-1 and  (yposition+i)<8 and (xposition-i)<8  and Board[(yposition+i)][(xposition-i)][0]=="" :
                        self.coords.append([(xposition-i)*60+30,(yposition+i)*60+30])
                    else:
                        if (yposition+i)<8 and (xposition-i)<8 and  (yposition+i)>-1 and (xposition-i)>-1 and  (yposition+i)<8 and (xposition-i)<8  and Board[(yposition+i)][(xposition-i)][1]==self.colour:
                            self.coords.append([(xposition-i)*60+30,(yposition+i)*60+30])
                        break;
            self.coords2.append([xposition*60+30,yposition*60+30])
            if black_check==True or white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([(attack_positions[a][0])+30,(attack_positions[a][1])+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==(list_searchx(Board,attack[0][0]))*60+30 and coords3[i][1]==(list_searchy(Board,attack[0][0]))*60+30:
                            self.coords.append([(list_searchx(Board,attack[0][0]))*60+30,(list_searchy(Board,attack[0][0]))*60+30])
            if two_protectors==False:
                coords4=[]
                if self.colour=="w":
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
                if (roomx-(roomx%60))+30==self.coords2[0][0] and roomy==(roomy-(roomy%60))+30==self.coords2[0][1]:
                    piece=""
                    fv=1
                    tg=1
                else:
                    for k1 in range (0, len(self.coords)):
                        if ((roomx-roomx%60)+30)==self.coords[k1][0] and ((roomy-roomy%60)+30)==self.coords[k1][1]:
                                piece=""
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)//60
                                self.bwmy=converty(self.bwmy)//60
                                yposition=(list_searchy(Board,self.number))
                                xposition=(list_searchx(Board,self.number))
                                firstposition1=(Board[yposition][xposition][0])
                                firstposition2=(Board[yposition][xposition][1])
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
class bishopw(queenw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
class rookw(queenw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
class knightw(bishopw):
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour        
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            if (2+yposition)<8 and (xposition-1)<8 and (2+yposition)>-1 and (xposition-1)>-1 and (2+yposition)>-1 and (xposition-1)>-1 and  (2+yposition)<8 and (xposition-1)<8  and Board[(2+yposition)][(xposition-1)][0]=="" :
                self.coords.append([(xposition-1)*60+30,(2+yposition)*60+30])
            else:
                if (2+yposition)<8 and (xposition-1)<8 and (2+yposition)>-1 and (xposition-1)>-1 and  (2+yposition)>-1 and (xposition-1)>-1 and  (2+yposition)<8 and (xposition-1)<8  and Board[(2+yposition)][(xposition-1)][1]==self.colour:
                    self.coords.append([(xposition-1)*60+30,(2+yposition)*60+30])
            if (yposition+2)<8 and (xposition+1)<8 and (yposition+2)>-1 and (xposition+1)>-1 and (yposition+2)>-1 and (xposition+1)>-1 and  (yposition+2)<8 and (xposition+1)<8  and Board[(yposition+2)][(xposition+1)][0]=="" :
                self.coords.append([(xposition+1)*60+30,(yposition+2)*60+30])
            else:
                if (yposition+2)<8 and (xposition+1)<8 and (yposition+2)>-1 and (xposition+1)>-1 and  (yposition+2)>-1 and (xposition+1)>-1 and  (yposition+2)<8 and (xposition+1)<8  and Board[(yposition+2)][(xposition+1)][1]==self.colour:
                    self.coords.append([(xposition+1)*60+30,(yposition+2)*60+30])
            if (yposition-2)<8 and (xposition+1)<8 and (yposition-2)>-1 and (xposition+1)>-1 and (yposition-2)>-1 and (xposition+1)>-1 and  (yposition-2)<8 and (xposition+1)<8  and Board[(yposition-2)][(xposition+1)][0]=="" :
                self.coords.append([(xposition+1)*60+30,(yposition-2)*60+30])
            else:
                if (yposition-2)<8 and (xposition+1)<8 and (yposition-2)>-1 and (xposition+1)>-1 and  (yposition-2)>-1 and (xposition+1)>-1 and  (yposition-2)<8 and (xposition+1)<8  and Board[(yposition-2)][(xposition+1)][1]==self.colour:
                    self.coords.append([(xposition+1)*60+30,(yposition-2)*60+30])
            if (yposition-2)<8 and (xposition-1)<8 and (yposition-2)>-1 and (xposition-1)>-1 and (yposition-2)>-1 and (xposition-1)>-1 and  (yposition-2)<8 and (xposition-1)<8  and Board[(yposition-2)][(xposition-1)][0]=="" :
                self.coords.append([(xposition-1)*60+30,(yposition-2)*60+30])
            else:
                if (yposition-2)<8 and (xposition-1)<8 and (yposition-2)>-1 and (xposition-1)>-1 and  (yposition-2)>-1 and (xposition-1)>-1 and  (yposition-2)<8 and (xposition-1)<8  and Board[(yposition-2)][(xposition-1)][1]==self.colour:
                    self.coords.append([(xposition-1)*60+30,(yposition-2)*60+30])
            if (yposition-1)<8 and (xposition-2)<8 and (yposition-1)>-1 and (xposition-2)>-1 and (yposition-1)>-1 and (xposition-2)>-1 and  (yposition-1)<8 and (xposition-2)<8  and Board[(yposition-1)][(xposition-2)][0]=="" :
                self.coords.append([(xposition-2)*60+30,(yposition-1)*60+30])
            else:
                if (yposition-1)<8 and (xposition-2)<8 and (yposition-1)>-1 and (xposition-2)>-1 and  (yposition-1)>-1 and (xposition-2)>-1 and  (yposition-1)<8 and (xposition-2)<8  and Board[(yposition-1)][(xposition-2)][1]==self.colour:
                    self.coords.append([(xposition-2)*60+30,(yposition-1)*60+30])
            if (yposition+1)<8 and (xposition-2)<8 and (yposition+1)>-1 and (xposition-2)>-1 and (yposition+1)>-1 and (xposition-2)>-1 and  (yposition+1)<8 and (xposition-2)<8  and Board[(yposition+1)][(xposition-2)][0]=="" :
                self.coords.append([(xposition-2)*60+30,(yposition+1)*60+30])
            else:
                if (yposition+1)<8 and (xposition-2)<8 and (yposition+1)>-1 and (xposition-2)>-1 and  (yposition+1)>-1 and (xposition-2)>-1 and  (yposition+1)<8 and (xposition-2)<8  and Board[(yposition+1)][(xposition-2)][1]==self.colour:
                    self.coords.append([(xposition-2)*60+30,(yposition+1)*60+30])
            if (yposition+1)<8 and (xposition+2)<8 and (yposition+1)>-1 and (xposition+2)>-1 and (yposition+1)>-1 and (xposition+2)>-1 and  (yposition+1)<8 and (xposition+2)<8  and Board[(yposition+1)][(xposition+2)][0]=="" :
                self.coords.append([(xposition+2)*60+30,(yposition+1)*60+30])
            else:
                if (yposition+1)<8 and (xposition+2)<8 and (yposition+1)>-1 and (xposition+2)>-1 and  (yposition+1)>-1 and (xposition+2)>-1 and  (yposition+1)<8 and (xposition+2)<8  and Board[(yposition+1)][(xposition+2)][1]==self.colour:
                    self.coords.append([(xposition+2)*60+30,(yposition+1)*60+30])
            if (yposition-1)<8 and (xposition+2)<8 and (yposition-1)>-1 and (xposition+2)>-1 and (yposition-1)>-1 and (xposition+2)>-1 and  (yposition-1)<8 and (xposition+2)<8  and Board[(yposition-1)][(xposition+2)][0]=="" :
                self.coords.append([(xposition+2)*60+30,(yposition-1)*60+30])
            else:
                if (yposition-1)<8 and (xposition+2)<8 and (yposition-1)>-1 and (xposition+2)>-1 and  (yposition-1)>-1 and (xposition+2)>-1 and  (yposition-1)<8 and (xposition+2)<8  and Board[(yposition-1)][(xposition+2)][1]==self.colour:
                    self.coords.append([(xposition+2)*60+30,(yposition-1)*60+30])
            self.coords2.append([(xposition)*60+30,(yposition)*60+30])
            if black_check==True or white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([(attack_positions[a][0])+30,(attack_positions[a][1])+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==(list_searchx(Board,attack[0][0]))*60+30 and coords3[i][1]==(list_searchy(Board,attack[0][0]))*60+30:
                            self.coords.append([(list_searchx(Board,attack[0][0]))*60+30,(list_searchy(Board,attack[0][0]))*60+30])
            if two_protectors==False:
                coords4=[]
                if self.colour=="w":
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
                fc=True
                for i in range (0,len(all_white)):
                    if (1+xposition)*60==all_white[i][0] and (1+yposition)*60==all_white[i][1]:
                        fc=False
                if (1+yposition)<8 and (1+xposition)<8 and (1+yposition)>-1 and (1+xposition)>-1 and  (1+yposition)<8 and (1+xposition)<8  and Board[(1+yposition)][(1+xposition)][0]=="" and fc==True:
                    self.coords.append([(1+xposition)*60+30,(1+yposition)*60+30])
                else:
                    if (1+yposition)<8 and (1+xposition)<8 and  (1+yposition)>-1 and (1+xposition)>-1 and  (1+yposition)<8 and (1+xposition)<8  and Board[(1+yposition)][(1+xposition)][1]==self.colour and fc==True:
                        self.coords.append([(1+xposition)*60+30,(1+yposition)*60+30])
                fc=True
                for i in range (0,len(all_white)):
                    if (xposition-1)*60==all_white[i][0] and (yposition-1)*60==all_white[i][1]:
                        fc=False
                if (yposition-1)<8 and (xposition-1)<8 and (yposition-1)>-1 and (xposition-1)>-1 and  (yposition-1)<8 and (xposition-1)<8  and Board[(yposition-1)][(xposition-1)][0]=="" and fc==True:
                    self.coords.append([(xposition-1)*60+30,(yposition-1)*60+30])
                else:
                    if (yposition-1)<8 and (xposition-1)<8 and  (yposition-1)>-1 and (xposition-1)>-1 and  (yposition-1)<8 and (xposition-1)<8  and Board[(yposition-1)][(xposition-1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition-1)*60+30,(yposition-1)*60+30])
                fc=True
                for i in range (0,len(all_white)):
                    if (xposition+1)*60==all_white[i][0] and (yposition-1)*60==all_white[i][1]:
                        fc=False
                if (yposition-1)<8 and (xposition+1)<8 and (yposition-1)>-1 and (xposition+1)>-1 and  (yposition-1)<8 and (xposition+1)<8  and Board[(yposition-1)][(xposition+1)][0]=="" and fc==True:
                    self.coords.append([(xposition+1)*60+30,(yposition-1)*60+30])
                else:
                    if (yposition-1)<8 and (xposition+1)<8 and  (yposition-1)>-1 and (xposition+1)>-1 and  (yposition-1)<8 and (xposition+1)<8  and Board[(yposition-1)][(xposition+1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition+1)*60+30,(yposition-1)*60+30])
                fc=True
                for i in range (0,len(all_white)):
                    if (xposition-1)*60==all_white[i][0] and (yposition+1)*60==all_white[i][1]:
                        fc=False
                if (yposition+1)<8 and (xposition-1)<8 and (yposition+1)>-1 and (xposition-1)>-1 and  (yposition+1)<8 and (xposition-1)<8  and Board[(yposition+1)][(xposition-1)][0]=="" and fc==True:
                    self.coords.append([(xposition-1)*60+30,(yposition+1)*60+30])
                else:
                    if (yposition+1)<8 and (xposition-1)<8 and  (yposition+1)>-1 and (xposition-1)>-1 and  (yposition+1)<8 and (xposition-1)<8  and Board[(yposition+1)][(xposition-1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition-1)*60+30,(yposition+1)*60+30])

                self.coords2.append([xposition*60+30,yposition*60+30])

                fc=True
                for i in range (0,len(all_white)):
                    if (1+xposition)*60==all_white[i][0] and (yposition)*60==all_white[i][1]:
                        fc=False
                if (yposition)<8 and (1+xposition)<8 and (yposition)>-1 and (1+xposition)>-1 and  (yposition)<8 and (1+xposition)<8  and Board[(yposition)][(1+xposition)][0]=="" and fc==True:
                    self.coords.append([(1+xposition)*60+30,(yposition)*60+30])
                else:
                    if (yposition)<8 and (1+xposition)<8 and  (yposition)>-1 and (1+xposition)>-1 and  (yposition)<8 and (1+xposition)<8  and Board[(yposition)][(1+xposition)][1]==self.colour and fc==True:
                        self.coords.append([(1+xposition)*60+30,(yposition)*60+30])
                fc=True
                for i in range (0,len(all_white)):
                    if (xposition-1)*60==all_white[i][0] and (yposition)*60==all_white[i][1]:
                        fc=False
                if (yposition)<8 and (xposition-1)<8 and (yposition)>-1 and (xposition-1)>-1 and  (yposition)<8 and (xposition-1)<8  and Board[(yposition)][(xposition-1)][0]=="" and fc==True:
                    self.coords.append([(xposition-1)*60+30,(yposition)*60+30])
                else:
                    if (yposition)<8 and (xposition-1)<8 and  (yposition)>-1 and (xposition-1)>-1 and  (yposition)<8 and (xposition-1)<8  and Board[(yposition)][(xposition-1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition-1)*60+30,(yposition)*60+30])
                fc=True
                for i in range (0,len(all_white)):
                    if (xposition)*60==all_white[i][0] and (yposition-1)*60==all_white[i][1]:
                        fc=False
                if (yposition-1)<8 and (xposition)<8 and (yposition-1)>-1 and (xposition)>-1 and  (yposition-1)<8 and (xposition)<8  and Board[(yposition-1)][(xposition)][0]=="" and fc==True:
                    self.coords.append([(xposition)*60+30,(yposition-1)*60+30])
                else:
                    if (yposition-1)<8 and (xposition)<8 and  (yposition-1)>-1 and (xposition)>-1 and  (yposition-1)<8 and (xposition)<8  and Board[(yposition-1)][(xposition)][1]==self.colour and fc==True:
                        self.coords.append([(xposition)*60+30,(yposition-1)*60+30])
                fc=True
                for i in range (0,len(all_white)):
                    if (xposition)*60==all_white[i][0] and (yposition+1)*60==all_white[i][1]:
                        fc=False
                if (yposition+1)<8 and (xposition)<8 and (yposition+1)>-1 and (xposition)>-1 and  (yposition+1)<8 and (xposition)<8  and Board[(yposition+1)][(xposition)][0]=="" and fc==True:
                    self.coords.append([(xposition)*60+30,(yposition+1)*60+30])
                else:
                    if (yposition+1)<8 and (xposition)<8 and  (yposition+1)>-1 and (xposition)>-1 and  (yposition+1)<8 and (xposition)<8  and Board[(yposition+1)][(xposition)][1]==self.colour and fc==True:
                        self.coords.append([(xposition)*60+30,(yposition+1)*60+30])
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
                fc=True
                for i in range (0,len(all_black)):
                    if (1+xposition)*60==all_black[i][0] and (1+yposition)*60==all_black[i][1]:
                        fc=False
                if (1+yposition)<8 and (1+xposition)<8 and (1+yposition)>-1 and (1+xposition)>-1 and  (1+yposition)<8 and (1+xposition)<8  and Board[(1+yposition)][(1+xposition)][0]=="" and fc==True:
                    self.coords.append([(1+xposition)*60+30,(1+yposition)*60+30])
                else:
                    if (1+yposition)<8 and (1+xposition)<8 and  (1+yposition)>-1 and (1+xposition)>-1 and  (1+yposition)<8 and (1+xposition)<8  and Board[(1+yposition)][(1+xposition)][1]==self.colour and fc==True:
                        self.coords.append([(1+xposition)*60+30,(1+yposition)*60+30])
                fc=True
                for i in range (0,len(all_black)):
                    if (xposition-1)*60==all_black[i][0] and (yposition-1)*60==all_black[i][1]:
                        fc=False
                if (yposition-1)<8 and (xposition-1)<8 and (yposition-1)>-1 and (xposition-1)>-1 and  (yposition-1)<8 and (xposition-1)<8  and Board[(yposition-1)][(xposition-1)][0]=="" and fc==True:
                    self.coords.append([(xposition-1)*60+30,(yposition-1)*60+30])
                else:
                    if (yposition-1)<8 and (xposition-1)<8 and  (yposition-1)>-1 and (xposition-1)>-1 and  (yposition-1)<8 and (xposition-1)<8  and Board[(yposition-1)][(xposition-1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition-1)*60+30,(yposition-1)*60+30])
                fc=True
                for i in range (0,len(all_black)):
                    if (xposition+1)*60==all_black[i][0] and (yposition-1)*60==all_black[i][1]:
                        fc=False
                if (yposition-1)<8 and (xposition+1)<8 and (yposition-1)>-1 and (xposition+1)>-1 and  (yposition-1)<8 and (xposition+1)<8  and Board[(yposition-1)][(xposition+1)][0]=="" and fc==True:
                    self.coords.append([(xposition+1)*60+30,(yposition-1)*60+30])
                else:
                    if (yposition-1)<8 and (xposition+1)<8 and  (yposition-1)>-1 and (xposition+1)>-1 and  (yposition-1)<8 and (xposition+1)<8  and Board[(yposition-1)][(xposition+1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition+1)*60+30,(yposition-1)*60+30])
                fc=True
                for i in range (0,len(all_black)):
                    if (xposition-1)*60==all_black[i][0] and (yposition+1)*60==all_black[i][1]:
                        fc=False
                if (yposition+1)<8 and (xposition-1)<8 and (yposition+1)>-1 and (xposition-1)>-1 and  (yposition+1)<8 and (xposition-1)<8  and Board[(yposition+1)][(xposition-1)][0]=="" and fc==True:
                    self.coords.append([(xposition-1)*60+30,(yposition+1)*60+30])
                else:
                    if (yposition+1)<8 and (xposition-1)<8 and  (yposition+1)>-1 and (xposition-1)>-1 and  (yposition+1)<8 and (xposition-1)<8  and Board[(yposition+1)][(xposition-1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition-1)*60+30,(yposition+1)*60+30])

                self.coords2.append([xposition*60+30,yposition*60+30])

                fc=True
                for i in range (0,len(all_black)):
                    if (1+xposition)*60==all_black[i][0] and (yposition)*60==all_black[i][1]:
                        fc=False
                if (yposition)<8 and (1+xposition)<8 and (yposition)>-1 and (1+xposition)>-1 and  (yposition)<8 and (1+xposition)<8  and Board[(yposition)][(1+xposition)][0]=="" and fc==True:
                    self.coords.append([(1+xposition)*60+30,(yposition)*60+30])
                else:
                    if (yposition)<8 and (1+xposition)<8 and  (yposition)>-1 and (1+xposition)>-1 and  (yposition)<8 and (1+xposition)<8  and Board[(yposition)][(1+xposition)][1]==self.colour and fc==True:
                        self.coords.append([(1+xposition)*60+30,(yposition)*60+30])
                fc=True
                for i in range (0,len(all_black)):
                    if (xposition-1)*60==all_black[i][0] and (yposition)*60==all_black[i][1]:
                        fc=False
                if (yposition)<8 and (xposition-1)<8 and (yposition)>-1 and (xposition-1)>-1 and  (yposition)<8 and (xposition-1)<8  and Board[(yposition)][(xposition-1)][0]=="" and fc==True:
                    self.coords.append([(xposition-1)*60+30,(yposition)*60+30])
                else:
                    if (yposition)<8 and (xposition-1)<8 and  (yposition)>-1 and (xposition-1)>-1 and  (yposition)<8 and (xposition-1)<8  and Board[(yposition)][(xposition-1)][1]==self.colour and fc==True:
                        self.coords.append([(xposition-1)*60+30,(yposition)*60+30])
                fc=True
                for i in range (0,len(all_black)):
                    if (xposition)*60==all_black[i][0] and (yposition-1)*60==all_black[i][1]:
                        fc=False
                if (yposition-1)<8 and (xposition)<8 and (yposition-1)>-1 and (xposition)>-1 and  (yposition-1)<8 and (xposition)<8  and Board[(yposition-1)][(xposition)][0]=="" and fc==True:
                    self.coords.append([(xposition)*60+30,(yposition-1)*60+30])
                else:
                    if (yposition-1)<8 and (xposition)<8 and  (yposition-1)>-1 and (xposition)>-1 and  (yposition-1)<8 and (xposition)<8  and Board[(yposition-1)][(xposition)][1]==self.colour and fc==True:
                        self.coords.append([(xposition)*60+30,(yposition-1)*60+30])
                fc=True
                for i in range (0,len(all_black)):
                    if (xposition)*60==all_black[i][0] and (yposition+1)*60==all_black[i][1]:
                        fc=False
                if (yposition+1)<8 and (xposition)<8 and (yposition+1)>-1 and (xposition)>-1 and  (yposition+1)<8 and (xposition)<8  and Board[(yposition+1)][(xposition)][0]=="" and fc==True:
                    self.coords.append([(xposition)*60+30,(yposition+1)*60+30])
                else:
                    if (yposition+1)<8 and (xposition)<8 and  (yposition+1)>-1 and (xposition)>-1 and  (yposition+1)<8 and (xposition)<8  and Board[(yposition+1)][(xposition)][1]==self.colour and fc==True:
                        self.coords.append([(xposition)*60+30,(yposition+1)*60+30])
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
                if ((roomx-(roomx%60))+30)==self.coords2[0][0] and ((roomy-(roomy%60))+30)==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                else:
                    for k1 in range (0, len(self.coords)):
                        if ((roomx-(roomx%60))+30)==self.coords[k1][0] and ((roomy-(roomy%60))+30)==self.coords[k1][1]:
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
            self.coords2.append([xposition*60+30,yposition*60+30])
            if self.colour=="b":
                if (1+yposition)<8 and (xposition-1)<8 and Board[(1+yposition)][xposition-1][1]=="b":
                    self.coords.append([(xposition-1)*60+30,(1+yposition)*60+30])
                if (1+yposition)<8 and (1+xposition)<8 and Board[(1+yposition)][(1+xposition)][1]=="b" :
                    self.coords.append([(1+xposition)*60+30,(1+yposition)*60+30])
                if self.moves2==0:
                    self.coords2.append([xposition*60+30,yposition*60+30])
                    if (yposition+1)<8 and xposition<8 and (yposition+1)>-1 and xposition>-1 and  (yposition+1)<8 and xposition<8  and Board[(yposition+1)][xposition][0]=="" :
                        self.coords.append([xposition*60+30,(yposition+1)*60+30])
                        if (2+yposition)<8 and xposition<8 and (2+yposition)>-1 and xposition>-1 and  (2+yposition)<8 and xposition<8  and Board[(2+yposition)][xposition][0]=="" :
                            self.coords.append([xposition*60+30,(yposition+2)*60+30])
                else:
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    self.coords2.append([xposition*60+30,yposition*60+30])
                    if (yposition+1)<8 and xposition<8 and (yposition+1)>-1 and xposition>-1 and  (yposition+1)<8 and xposition<8  and Board[(yposition+1)][xposition][0]=="" :
                        self.coords.append([xposition*60+30,(yposition+1)*60+30])
            if self.colour=="w":
                if (yposition-1)<8 and (xposition-1)<8 and Board[(yposition-1)][xposition-1][1]=="w":
                    self.coords.append([(xposition-1)*60+30,(yposition-1)*60+30])
                if (yposition-1)<8 and (1+xposition)<8 and Board[(yposition-1)][(1+xposition)][1]=="w" :
                    self.coords.append([(1+xposition)*60+30,(yposition-1)*60+30])
                if self.moves2==0:
                    self.coords2.append([xposition*60+30,yposition*60+30])
                    if (yposition-1)<8 and xposition<8 and (yposition-1)>-1 and xposition>-1 and  (yposition-1)<8 and xposition<8  and Board[(yposition-1)][xposition][0]=="" :
                        self.coords.append([xposition*60+30,(yposition-1)*60+30])
                        if (yposition-2)<8 and xposition<8 and (yposition-2)>-1 and xposition>-1 and  (yposition-2)<8 and xposition<8  and Board[(yposition-2)][xposition][0]=="" :
                            self.coords.append([xposition*60+30,(yposition-2)*60+30])
                else:
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    self.coords2.append([xposition*60+30,yposition*60+30])
                    if (yposition-1)<8 and xposition<8 and (yposition-1)>-1 and xposition>-1 and  (yposition-1)<8 and xposition<8  and Board[(yposition-1)][xposition][0]=="" :
                        self.coords.append([xposition*60+30,(yposition-1)*60+30])
                    
            if black_check==True or white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([(attack_positions[a][0])+30,(attack_positions[a][1])+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        coords.pop()
                    for a in range (0,len(attack_positions2)):
                        for i in range (0,len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==(list_searchx(Board,attack[0][0]))*60+30 and coords3[i][1]==(list_searchy(Board,attack[0][0]))*60+30:
                            self.coords.append([(list_searchx(Board,attack[0][0]))*60+30,(list_searchy(Board,attack[0][0]))*60+30])
            if two_protectors==False:
                coords4=[]
                if self.colour=="w":
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
                                yposition=(list_searchy(Board,self.number))
                                xposition=list_searchx(Board,self.number)
                                event2=wait()
                                if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
                                    if queenw_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q2w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                    elif queenw_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                    elif queenw_moves==2:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
                                    if rookw_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                    elif rookw_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                    elif rookw_moves==2:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
                                    if bishopw_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                    elif bishopw_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                    elif bishopw_moves==2:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
                                    if knightw_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                    elif knightw_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                    elif knightw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                        
                            else:
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)//60
                                self.bwmy=converty(self.bwmy)//60
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

class pawnb(pawnw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour,moves2):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
        self.moves2=moves2
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
                                yposition=(list_searchy(Board,self.number))
                                xposition=list_searchx(Board,self.number)
                                event2=wait()
                                if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
                                    if queenb_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q2b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                    elif queenb_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                    elif queenb_moves==2:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
                                    if rookb_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                    elif rookb_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                    elif rookb_moves==2:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
                                    if bishopb_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                    elif bishopb_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                    elif bishopb_moves==2:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
                                    if knightb_moves==0:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                                    elif knightb_moves==1:
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                                    elif knightb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                            else:
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)//60
                                self.bwmy=converty(self.bwmy)//60
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
class Status(object):
    def __init__(self,vc,pawn_black1_status):
        self.vc=vc
        self.pawn_black1_status=pawn_black1_status
    def Status2(self,vc,pawn_black1_status):
        xposition=list_searchx(Board,self.vc)        
        if xposition==9:
            self.pawn_black1_status="dead"
class Status1(object):
    def __init__(self,vc,queen_black4_status,queen4b_spawn,q4bmx,q4bmy):
        self.vc=vc
        self.queen_black4_status=queen_black4_status
        self.queen4b_spawn=queen4b_spawn
        self.q4bmx=q4bmx
        self.q4bmy=q4bmy
    def Status21(self,vc,queen_black4_status,queen4b_spawn,q4bmx,q4bmy):
        xposition=list_searchx(Board,self.vc)
        yposition=list_searchy(Board,self.vc)
        if self.queen4b_spawn==0:
            if xposition<9:
                self.q4bmx=xposition*60
                self.q4bmy=yposition*60
                self.queen_black4_status="alive"
                self.queen4b_spawn=1

class attack_class_and_all_white(object):
    def __init__(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        self.vc=vc
        self.attack_piece=attack_piece
        self.black_check=black_check
        self.attack=attack
        self.attack_positions=attack_positions
        self.all_white=all_white
    def attack_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        if vc[2]=="b":            
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
        else:
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
        xposition=60*xposition
        yposition=60*yposition
        for ju in range (0,len(self.attack_piece)):
            if xposition==self.attack_piece[ju][0] and yposition==self.attack_piece[ju][1]:
                self.attack.append([self.vc])
                self.attack_positions=self.attack_piece
    def all_white_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        yposition=list_searchy(Board,"k1b")
        xposition=list_searchx(Board,"k1b")
        xposition=60*xposition
        yposition=60*yposition
        for i in range (0,len(self.attack_piece)):
            if self.attack_piece!=[]:
                self.all_white.append(self.attack_piece[i])
                if self.attack_piece[len(self.attack_piece)-1][0]==xposition and self.attack_piece[len(self.attack_piece)-1][1]==yposition:
                    yposition1=list_searchy(Board,self.vc)*60
                    xposition1=list_searchx(Board,self.vc)*60
                    x_addition=self.attack_piece[0][0]-xposition1
                    y_addition=self.attack_piece[0][1]-yposition1
                    r122=(self.attack_piece[(len(self.attack_piece))-1][0])
                    r123=(self.attack_piece[(len(self.attack_piece))-1][1])                
                    r121=[r122+x_addition,r123+y_addition]
                    self.all_white.append(r121)

class attack_class_and_all_black(attack_class_and_all_white):
    def __init__(self,vc,attack_piece,black_check,attack,attack_positions,all_black):
        self.vc=vc
        self.attack_piece=attack_piece
        self.black_check=black_check
        self.attack=attack
        self.attack_positions=attack_positions
        self.all_black=all_black
    def all_black_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_black):
        yposition=list_searchy(Board,"k1w")
        xposition=list_searchx(Board,"k1w")
        xposition=60*xposition
        yposition=60*yposition
        for i in range (0,len(self.attack_piece)):
            if self.attack_piece!=[]:
                self.all_black.append(self.attack_piece[i])
                if self.attack_piece[len(self.attack_piece)-1][0]==xposition and self.attack_piece[len(self.attack_piece)-1][1]==yposition:
                    yposition1=list_searchy(Board,self.vc)*60
                    xposition1=list_searchx(Board,self.vc)*60
                    x_addition=self.attack_piece[0][0]-xposition1
                    y_addition=self.attack_piece[0][1]-yposition1
                    r122=(self.attack_piece[(len(self.attack_piece))-1][0])
                    r123=(self.attack_piece[(len(self.attack_piece))-1][1])                
                    r121=[r122+x_addition,r123+y_addition]
                    self.all_black.append(r121)
class all_black_class(object):
    def __init__(self,all_black,piece_attack,piece):
        self.all_black=all_black
        self.piece_attack=piece_attack
        self.piece=piece
    def all_black_class1(self,all_black,piece_attack,piece):
        yposition=list_searchy(Board,"k1w")
        xposition=list_searchx(Board,"k1w")
        xposition=60*xposition
        yposition=60*yposition
        for i in range (0,len(self.piece_attack)):
            if self.piece_attack!=[]:
                self.all_black.append(self.piece_attack[i])
                if self.piece_attack[len(self.piece_attack)-1][0]==xposition and self.piece_attack[len(self.piece_attack)-1][1]==yposition:
                    yposition1=list_searchy(Board,self.piece)*60
                    xposition1=list_searchx(Board,self.piece)*60
                    x_addition=self.piece_attack[0][0]-xposition1
                    y_addition=self.piece_attack[0][1]-yposition1
                    r122=(self.piece_attack[(len(self.piece_attack))-1][0])
                    r123=(self.piece_attack[(len(self.piece_attack))-1][1])                
                    r121=[r122+x_addition,r123+y_addition]
                    self.all_black.append(r121)
def convertx(piecex):
    return piecex-(piecex%60)

def converty(piecey):
    return piecey-(piecey%60)

def board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy):
    r1wmx,r1wmy,r2wmx,r2wmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy=(convertx(r1wmx)),(converty(r1wmy)),(convertx(r2wmx)),(converty(r2wmy)),(convertx(r3wmx)),(converty(r3wmy)),(convertx(r4wmx)),(converty(r4wmy)),(convertx(r5wmx)),(converty(r5wmy))
    r1bmx,r1bmy,r2bmx,r2bmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy=(convertx(r1bmx)),(converty(r1bmy)),(convertx(r2bmx)),(converty(r2bmy)),(convertx(r3bmx)),(converty(r3bmy)),(convertx(r4bmx)),(converty(r4bmy)),(convertx(r5bmx)),(converty(r5bmy))
    
    b1wmx,b1wmy,b2wmx,b2wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy=(convertx(b1wmx)),(converty(b1wmy)),(convertx(b2wmx)),(converty(b2wmy)),(convertx(b3wmx)),(converty(b3wmy)),(convertx(b4wmx)),(converty(b4wmy)),(convertx(b5wmx)),(converty(b5wmy))
    b1bmx,b1bmy,b2bmx,b2bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy=(convertx(b1bmx)),(converty(b1bmy)),(convertx(b2bmx)),(converty(b2bmy)),(convertx(b3bmx)),(converty(b3bmy)),(convertx(b4bmx)),(converty(b4bmy)),(convertx(b5bmx)),(converty(b5bmy))

    kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy=(convertx(kn1wmx)),(converty(kn1wmy)),(convertx(kn2wmx)),(converty(kn2wmy)),(convertx(kn3wmx)),(converty(kn3wmy)),(convertx(kn4wmx)),(converty(kn4wmy)),(convertx(kn5wmx)),(converty(kn5wmy))
    kn1bmx,kn1bmy,kn2bmx,kn2bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy=(convertx(kn1bmx)),(converty(kn1bmy)),(convertx(kn2bmx)),(converty(kn2bmy)),(convertx(kn3bmx)),(converty(kn3bmy)),(convertx(kn4bmx)),(converty(kn4bmy)),(convertx(kn5bmx)),(converty(kn5bmy))

    q1wmx,q1wmy,q2wmx,q2wmy,q3wmx,q3wmy,q4wmx,q4wmy=(convertx(q1wmx)),(converty(q1wmy)),(convertx(q2wmx)),(converty(q2wmy)),(convertx(q3wmx)),(converty(q3wmy)),(convertx(q4wmx)),(converty(q4wmy))
    q1bmx,q1bmy,q2bmx,q2bmy,q3bmx,q3bmy,q4bmx,q4bmy=(convertx(q1bmx)),(converty(q1bmy)),(convertx(q2bmx)),(converty(q2bmy)),(convertx(q3bmx)),(converty(q3bmy)),(convertx(q4bmx)),(converty(q4bmy))

    k1wmx,k1wmy,k1bmx,k1bmy=(convertx(k1wmx)),(converty(k1wmy)),(convertx(k1bmx)),(converty(k1bmy))
    
    p6wmx,p6wmy,p7wmx,p7wmy,p8wmx,p8wmy=(convertx(p6wmx)),(converty(p6wmy)),(convertx(p7wmx)),(converty(p7wmy)),(convertx(p8wmx)),(converty(p8wmy))
    p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy=(convertx(p6bmx)),(converty(p6bmy)),(convertx(p7bmx)),(converty(p7bmy)),(convertx(p8bmx)),(converty(p8bmy))

    p1wmx,p1wmy,p2wmx,p2wmy,p3wmx,p3wmy,p4wmx,p4wmy,p5wmx,p5wmy=(convertx(p1wmx)),(converty(p1wmy)),(convertx(p2wmx)),(converty(p2wmy)),(convertx(p3wmx)),(converty(p3wmy)),(convertx(p4wmx)),(converty(p4wmy)),(convertx(p5wmx)),(converty(p5wmy))
    p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p5bmx,p5bmy=(convertx(p1bmx)),(converty(p1bmy)),(convertx(p2bmx)),(converty(p2bmy)),(convertx(p3bmx)),(converty(p3bmy)),(convertx(p4bmx)),(converty(p4bmy)),(convertx(p5bmx)),(converty(p5bmy))
    
    win.blit(bg,(0,0))
    if king_black_status=="alive":
        gameDisplay.blit(king_black,(k1bmx,k1bmy))
    if king_white_status=="alive":
        gameDisplay.blit(king_white,(k1wmx,k1wmy))
    if queen_black_status=="alive":
        gameDisplay.blit(queen_black,(q1bmx,q1bmy))
    else:
        gameDisplay.blit(queen_black,(481,481))
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
        gameDisplay.blit(queen_white,(481,481))
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

rook_white1,rook_white2,rook_white3,rook_white4,rook_white5=pygame.image.load("rook_white.png"),pygame.image.load("rook_white.png"),pygame.image.load("rook_white.png"),pygame.image.load("rook_white.png"),pygame.image.load("rook_white.png")
rook_black1,rook_black2,rook_black3,rook_black4,rook_black5=pygame.image.load("rook_black.png"),pygame.image.load("rook_black.png"),pygame.image.load("rook_black.png"),pygame.image.load("rook_black.png"),pygame.image.load("rook_black.png")

knight_white1,knight_white2,knight_white3,knight_white4,knight_white5=pygame.image.load("knight_white.png"),pygame.image.load("knight_white.png"),pygame.image.load("knight_white.png"),pygame.image.load("knight_white.png"),pygame.image.load("knight_white.png")
knight_black1,knight_black2,knight_black3,knight_black4,knight_black5=pygame.image.load("knight_black.png"),pygame.image.load("knight_black.png"),pygame.image.load("knight_black.png"),pygame.image.load("knight_black.png"),pygame.image.load("knight_black.png")

pawn_white1,pawn_white2,pawn_white3,pawn_white4,pawn_white5=pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png")
pawn_white5,pawn_white6,pawn_white7,pawn_white8=pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png"),pygame.image.load("pawn_white.png")

pawn_black1,pawn_black2,pawn_black3,pawn_black4,pawn_black5=pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png")
pawn_black5,pawn_black6,pawn_black7,pawn_black8=pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png"),pygame.image.load("pawn_black.png")

queen_white,queen_white2,queen_white3,queen_white4=pygame.image.load("queen_white.png"),pygame.image.load("queen_white.png"),pygame.image.load("queen_white.png"),pygame.image.load("queen_white.png")
queen_black,queen_black2,queen_black3,queen_black4=pygame.image.load("queen_black.png"),pygame.image.load("queen_black.png"),pygame.image.load("queen_black.png"),pygame.image.load("queen_black.png")

king_white=pygame.image.load("king_white.png")
king_black=pygame.image.load("king_black.png")

bishop_white1,bishop_white2,bishop_white3,bishop_white4,bishop_white5=pygame.image.load("bishop_white.png"),pygame.image.load("bishop_white.png"),pygame.image.load("bishop_white.png"),pygame.image.load("bishop_white.png"),pygame.image.load("bishop_white.png")
bishop_black1,bishop_black2,bishop_black3,bishop_black4,bishop_black5=pygame.image.load("bishop_black.png"),pygame.image.load("bishop_black.png"),pygame.image.load("bishop_black.png"),pygame.image.load("bishop_black.png"),pygame.image.load("bishop_black.png")

checkmate,stalemate,bg=pygame.image.load("checkmate.png"),pygame.image.load("stalemate.png"),pygame.image.load("ChessBoard.png")

rook_white1_status,rook_white2_status,rook_white3_status,rook_white4_status,rook_white5_status="alive","alive","alive","alive","alive"
rook_black1_status,rook_black2_status,rook_black3_status,rook_black4_status,rook_black5_status="alive","alive","alive","alive","alive"

knight_white1_status,knight_white2_status,knight_white3_status,knight_white4_status,knight_white5_status="alive","alive","alive","alive","alive"
knight_black1_status,knight_black2_status,knight_black3_status,knight_black4_status,knight_black5_status="alive","alive","alive","alive","alive"

bishop_white1_status,bishop_white2_status,bishop_white3_status,bishop_white4_status,bishop_white5_status="alive","alive","alive","alive","alive"
bishop_black1_status,bishop_black2_status,bishop_black3_status,bishop_black4_status,bishop_black5_status="alive","alive","alive","alive","alive"

king_white_status="alive"
king_black_status="alive"

queen_white_status,queen_white2_status,queen_white3_status,queen_white4_status="alive","alive","alive","alive"
queen_black_status,queen_black2_status,queen_black3_status,queen_black4_status="alive","alive","alive","alive"

pawn_white1_status,pawn_white2_status,pawn_white3_status,pawn_white4_status,pawn_white5_status="alive","alive","alive","alive","alive"
pawn_black1_status,pawn_black2_status,pawn_black3_status,pawn_black4_status,pawn_black5_status="alive","alive","alive","alive","alive"
pawn_white6_status,pawn_white7_status,pawn_white8_status="alive","alive","alive"
pawn_black6_status,pawn_black7_status,pawn_black8_status="alive","alive","alive"

rookb_moves,bishopb_moves,queenb_moves,knightb_moves=0,0,0,0
rookw_moves,bishopw_moves,queenw_moves,knightw_moves=0,0,0,0

Board=[[["r1w","w"],["kn1w","w"],["b1w","w"],["q1w", "w"],["k1w", "w"],["b2w","w"],["kn2w","w"],["r2w","w"]],
       [["p1w","w"],["p2w", "w"],["p3w","w"],["p4w","w"],["p5w","w"],["p6w","w"],["p7w", "w"],["p8w","w"]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["p1b","b"],["p2b", "b"],["p3b","b"],["p4b","b"],["p5b","b"],["p6b","b"],["p7b", "b"],["p8b","b"]],
       [["r1b","b"],["kn1b","b"],["b1b","b"],["q1b", "b"],["k1b", "b"],["b2b","b"],["kn2b","b"],["r2b","b"]]]

attack=[]
r1wmx,r1wmy,r2wmx,r2wmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy=0,0,420,0,481,481,481,481,481,481
r1bmx,r1bmy,r2bmx,r2bmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy=0,420,420,420,481,481,481,481,481,481

b1wmx,b1wmy,b2wmx,b2wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy=120,0,300,0,481,481,481,481,481,481
b1bmx,b1bmy,b2bmx,b2bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy=120,420,300,420,481,481,481,481,481,481

kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy=60,0,360,0,481,481,481,481,481,481
kn1bmx,kn1bmy,kn2bmx,kn2bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy=60,420,360,420,481,481,481,481,481,481

q1wmx,q1wmy,q2wmx,q2wmy,q3wmx,q3wmy,q4wmx,q4wmy=180,0,481,481,481,481,481,481
q1bmx,q1bmy,q2bmx,q2bmy,q3bmx,q3bmy,q4bmx,q4bmy=180,420,481,481,481,481,481,481

k1wmx,k1wmy,k1bmx,k1bmy=240,0,240,420

p1wmx,p1wmy,p2wmx,p2wmy,p3wmx,p3wmy,p4wmx,p4wmy,p5wmx,p5wmy,p6wmx,p6wmy,p7wmx,p7wmy,p8wmx,p8wmy=0,60,60,60,120,60,180,60,240,60,300,60,360,60,420,60
p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p5bmx,p5bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy=0,360,60,360,120,360,180,360,240,360,300,360,360,360,420,360

moves=0
hb=0
hw=0
black=(255,0,0)
run=True
piece=""
board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
pygame.display.update()
coords,coords2=[],[]

moves28,moves27,moves26,moves25,moves24,moves23,moves22,moves21=0,0,0,0,0,0,0,0
moves28b,moves27b,moves26b,moves25b,moves24b,moves23b,moves22b,moves21b=0,0,0,0,0,0,0,0

moves2kw,moves2r1w,moves2r2w=0,0,0
moves2kb,moves2r1b,moves2r2b=0,0,0

pos_spaces=[]
two_protectors=False

b11,b12,b13,b14=[],[],[],[]
b21,b22,b23,b24=[],[],[],[]
b31,b32,b33,b34=[],[],[],[]
b41,b42,b43,b44=[],[],[],[]
b51,b52,b53,b54=[],[],[],[]

r11,r12,r13,r14=[],[],[],[]
r21,r22,r23,r24=[],[],[],[]
r31,r32,r33,r34=[],[],[],[]
r41,r42,r43,r44=[],[],[],[]
r51,r52,r53,r54=[],[],[],[]

kn1=[]
kn2=[]

q11,q12,q13,q14,q15,q16,q17,q18=[],[],[],[],[],[],[],[]
q21,q22,q23,q24,q25,q26,q27,q28=[],[],[],[],[],[],[],[]
q31,q32,q33,q34,q35,q36,q37,q38=[],[],[],[],[],[],[],[]
q41,q42,q43,q44,q45,q46,q47,q48=[],[],[],[],[],[],[],[]

k1w=[]
k1b=[]

p1,p2,p3,p4,p5,p6,p7,p8=[],[],[],[],[],[],[],[]

b11b,b12b,b13b,b14b=[],[],[],[]
b21b,b22b,b23b,b24b=[],[],[],[]
b31b,b32b,b33b,b34b=[],[],[],[]
b41b,b42b,b43b,b44b=[],[],[],[]
b51b,b52b,b53b,b54b=[],[],[],[]

r11b,r12b,r13b,r14b=[],[],[],[]
r21b,r22b,r23b,r24b=[],[],[],[]
r31b,r32b,r33b,r34b=[],[],[],[]
r41b,r42b,r43b,r44b=[],[],[],[]
r51b,r52b,r53b,r54b=[],[],[],[]

kn1,kn2,kn3,kn4,kn5=[],[],[],[],[]
kn1b,kn2b,kn3b,kn4b,kn5b=[],[],[],[],[]

q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b=[],[],[],[],[],[],[],[]
q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b=[],[],[],[],[],[],[],[]
q31b,q32b,q33b,q34b,q35b,q36b,q37b,q38b=[],[],[],[],[],[],[],[]
q41b,q42b,q43b,q44b,q45b,q46b,q47b,q48b=[],[],[],[],[],[],[],[]

p1b,p2b,p3b,p4b,p5b,p6b,p7b,p8b=[],[],[],[],[],[],[],[]

jkl=0
jkb=0

attack_positions=[]
black_check,white_check=False,False
white_checkmate,black_checkmate=False,False
white_stalemate,black_stalemate=False,False
black_protector,white_protector=[],[]

queen2w_spawn,queen3w_spawn,queen4w_spawn=0,0,0
queen2b_spawn,queen3b_spawn,queen4b_spawn=0,0,0

bishop3b_spawn,bishop4b_spawn,bishop5b_spawn=0,0,0
bishop3w_spawn,bishop4w_spawn,bishop5w_spawn=0,0,0

rook3w_spawn,rook4w_spawn,rook5w_spawn=0,0,0
rook3b_spawn,rook4b_spawn,rook5b_spawn=0,0,0

knight3w_spawn,knight4w_spawn,knight5w_spawn=0,0,0
knight3b_spawn,knight4b_spawn,knight5b_spawn=0,0,0

counter=0
event3=wait2()
rfv=0
Check_screen=False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False        
        b11,b12,b13,b14=[],[],[],[]
        b21,b22,b23,b24=[],[],[],[]
        b31,b32,b33,b34=[],[],[],[]
        b41,b42,b43,b44=[],[],[],[]
        b51,b52,b53,b54=[],[],[],[]

        r11,r12,r13,r14=[],[],[],[]
        r21,r22,r23,r24=[],[],[],[]
        r31,r32,r33,r34=[],[],[],[]
        r41,r42,r43,r44=[],[],[],[]
        r51,r52,r53,r54=[],[],[],[]

        kn1=[]
        kn2=[]

        q11,q12,q13,q14,q15,q16,q17,q18=[],[],[],[],[],[],[],[]
        q21,q22,q23,q24,q25,q26,q27,q28=[],[],[],[],[],[],[],[]
        q31,q32,q33,q34,q35,q36,q37,q38=[],[],[],[],[],[],[],[]
        q41,q42,q43,q44,q45,q46,q47,q48=[],[],[],[],[],[],[],[]

        k1w=[]
        k1b=[]

        p1,p2,p3,p4,p5,p6,p7,p8=[],[],[],[],[],[],[],[]

        b11b,b12b,b13b,b14b=[],[],[],[]
        b21b,b22b,b23b,b24b=[],[],[],[]
        b31b,b32b,b33b,b34b=[],[],[],[]
        b41b,b42b,b43b,b44b=[],[],[],[]
        b51b,b52b,b53b,b54b=[],[],[],[]

        r11b,r12b,r13b,r14b=[],[],[],[]
        r21b,r22b,r23b,r24b=[],[],[],[]
        r31b,r32b,r33b,r34b=[],[],[],[]
        r41b,r42b,r43b,r44b=[],[],[],[]
        r51b,r52b,r53b,r54b=[],[],[],[]
        
        kn1,kn2,kn3,kn4,kn5=[],[],[],[],[]
        kn1b,kn2b,kn3b,kn4b,kn5b=[],[],[],[],[]

        q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b=[],[],[],[],[],[],[],[]
        q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b=[],[],[],[],[],[],[],[]
        q31b,q32b,q33b,q34b,q35b,q36b,q37b,q38b=[],[],[],[],[],[],[],[]
        q41b,q42b,q43b,q44b,q45b,q46b,q47b,q48b=[],[],[],[],[],[],[],[]

        p1b,p2b,p3b,p4b,p5b,p6b,p7b,p8b=[],[],[],[],[],[],[],[]
        
        if hb==0:
            two_protectors=False
            black_protector=[]
            pos_spaces=[]
            all_white=[]
            Bishop1w2=bishop1(b11,b12,b13,b14,black_protector,"b1w","k1b","b","w")
            Bishop1w2.check(b11,b12,b13,b14,black_protector,"b1w","k1b","b","w")
                
            Bishop2w2=bishop1(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")
            Bishop2w2.check(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")

            Bishop3w3=bishop1(b31,b32,b33,b34,black_protector,"b3w","k1b","b","w")
            Bishop3w3.check(b31,b32,b33,b34,black_protector,"b3w","k1b","b","w")

            Bishop4w4=bishop1(b41,b42,b43,b44,black_protector,"b4w","k1b","b","w")
            Bishop4w4.check(b41,b42,b43,b44,black_protector,"b4w","k1b","b","w")

            Bishop5w5=bishop1(b51,b52,b53,b54,black_protector,"b5w","k1b","b","w")
            Bishop5w5.check(b51,b52,b53,b54,black_protector,"b5w","k1b","b","w")

            Queen1w2=queen1(q11,q12,q13,q14,q15,q16,q17,q18,black_protector,"q1w","k1b","b","w")
            Queen1w2.check(q11,q12,q13,q14,q15,q16,q17,q18,black_protector,"q1w","k1b","b","w")

            Queen2w2=queen1(q21,q22,q23,q24,q25,q26,q27,q28,black_protector,"q2w","k1b","b","w")
            Queen2w2.check(q21,q22,q23,q24,q25,q26,q27,q28,black_protector,"q2w","k1b","b","w")

            Queen4w4=queen1(q41,q42,q43,q44,q45,q46,q47,q48,black_protector,"q4w","k1b","b","w")
            Queen4w4.check(q41,q42,q43,q44,q45,q46,q47,q48,black_protector,"q4w","k1b","b","w")

            Queen3w3=queen1(q31,q32,q33,q34,q35,q36,q37,q38,black_protector,"q3w","k1b","b","w")
            Queen3w3.check(q31,q32,q33,q34,q35,q36,q37,q38,black_protector,"q3w","k1b","b","w")

            knight1w2=knight1(kn1,black_protector,"kn1w","k1b","b","w")
            knight1w2.check(kn1,black_protector,"kn1w","k1b","b","w")            

            knight2w2=knight1(kn1,black_protector,"kn2w","k1b","b","w")
            knight2w2.check(kn1,black_protector,"kn2w","k1b","b","w")

            knight3w3=knight1(kn3,black_protector,"kn3w","k1b","b","w")
            knight3w3.check(kn3,black_protector,"kn3w","k1b","b","w")

            knight4w4=knight1(kn4,black_protector,"kn4w","k1b","b","w")
            knight4w4.check(kn4,black_protector,"kn4w","k1b","b","w")

            knight5w2=knight1(kn5,black_protector,"kn5w","k1b","b","w")
            knight5w2.check(kn5,black_protector,"kn5w","k1b","b","w") 

            Rook1w2=rook1(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")
            Rook1w2.check(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")

            Rook2w2=rook1(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")
            Rook2w2.check(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")

            Rook3w2=rook1(r31,r32,r33,r34,black_protector,"r3w","k1b","b","w")
            Rook3w2.check(r31,r32,r33,r34,black_protector,"r3w","k1b","b","w")

            Rook4w2=rook1(r41,r42,r43,r44,black_protector,"r4w","k1b","b","w")
            Rook4w2.check(r41,r42,r43,r44,black_protector,"r4w","k1b","b","w")

            Rook5w2=rook1(r51,r52,r53,r54,black_protector,"r5w","k1b","b","w")
            Rook5w2.check(r51,r52,r53,r54,black_protector,"r5w","k1b","b","w")

            Pawn1w2=pawn1w(p1,"p1w","b","w")
            Pawn1w2.check(p1,"p1w","b","w")

            Pawn2w2=pawn1w(p2,"p2w","b","w")
            Pawn2w2.check(p2,"p2w","b","w")

            Pawn3w2=pawn1w(p3,"p3w","b","w")
            Pawn3w2.check(p3,"p3w","b","w")

            Pawn4w2=pawn1w(p4,"p4w","b","w")
            Pawn4w2.check(p4,"p4w","b","w")

            Pawn5w2=pawn1w(p5,"p5w","b","w")
            Pawn5w2.check(p5,"p5w","b","w")

            Pawn6w2=pawn1w(p6,"p6w","b","w")
            Pawn6w2.check(p6,"p6w","b","w")

            Pawn7w2=pawn1w(p7,"p7w","b","w")
            Pawn7w2.check(p7,"p7w","b","w")

            Pawn8w2=pawn1w(p8,"p8w","b","w")
            Pawn8w2.check(p8,"p8w","b","w")

            King1w2=king1(k1w,"k1w","b","w")
            King1w2.check(k1w,"k1w","b","w")

            attack_positions=[]
            attack=[]
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition
            
            Rook11w_attack=attack_class_and_all_white("r1w",r11,black_check,attack,attack_positions,all_white)
            Rook11w_attack.attack_class1("r1w",r11,black_check,attack,attack_positions,all_white)
            Rook11w_attack.all_white_class1("r1w",r11,black_check,attack,attack_positions,all_white)
            attack_positions=Rook11w_attack.attack_positions
            attack=Rook11w_attack.attack
            
            Rook12w_attack=attack_class_and_all_white("r1w",r12,black_check,attack,attack_positions,all_white)
            Rook12w_attack.attack_class1("r1w",r12,black_check,attack,attack_positions,all_white)
            Rook12w_attack.all_white_class1("r1w",r12,black_check,attack,attack_positions,all_white)
            attack_positions=Rook12w_attack.attack_positions
            attack=Rook12w_attack.attack

            Rook13w_attack=attack_class_and_all_white("r1w",r13,black_check,attack,attack_positions,all_white)
            Rook13w_attack.attack_class1("r1w",r13,black_check,attack,attack_positions,all_white)
            Rook13w_attack.all_white_class1("r1w",r13,black_check,attack,attack_positions,all_white)
            attack_positions=Rook13w_attack.attack_positions
            attack=Rook13w_attack.attack
            
            Rook14w_attack=attack_class_and_all_white("r1w",r14,black_check,attack,attack_positions,all_white)
            Rook14w_attack.attack_class1("r1w",r14,black_check,attack,attack_positions,all_white)
            Rook14w_attack.all_white_class1("r1w",r14,black_check,attack,attack_positions,all_white)
            attack_positions=Rook14w_attack.attack_positions
            attack=Rook14w_attack.attack
                    
            Rook21w_attack=attack_class_and_all_white("r2w",r21,black_check,attack,attack_positions,all_white)
            Rook21w_attack.attack_class1("r2w",r21,black_check,attack,attack_positions,all_white)
            Rook21w_attack.all_white_class1("r2w",r21,black_check,attack,attack_positions,all_white)
            attack_positions=Rook21w_attack.attack_positions
            attack=Rook21w_attack.attack
            
            Rook22w_attack=attack_class_and_all_white("r2w",r22,black_check,attack,attack_positions,all_white)
            Rook22w_attack.attack_class1("r2w",r22,black_check,attack,attack_positions,all_white)
            Rook22w_attack.all_white_class1("r2w",r22,black_check,attack,attack_positions,all_white)
            attack_positions=Rook22w_attack.attack_positions
            attack=Rook22w_attack.attack

            Rook23w_attack=attack_class_and_all_white("r2w",r23,black_check,attack,attack_positions,all_white)
            Rook23w_attack.attack_class1("r2w",r23,black_check,attack,attack_positions,all_white)
            Rook23w_attack.all_white_class1("r2w",r23,black_check,attack,attack_positions,all_white)
            attack_positions=Rook23w_attack.attack_positions
            attack=Rook23w_attack.attack
            
            Rook24w_attack=attack_class_and_all_white("r2w",r24,black_check,attack,attack_positions,all_white)
            Rook24w_attack.attack_class1("r2w",r24,black_check,attack,attack_positions,all_white)
            Rook24w_attack.all_white_class1("r2w",r24,black_check,attack,attack_positions,all_white)
            attack_positions=Rook24w_attack.attack_positions
            attack=Rook24w_attack.attack

            Rook31w_attack=attack_class_and_all_white("r3w",r31,black_check,attack,attack_positions,all_white)
            Rook31w_attack.attack_class1("r3w",r31,black_check,attack,attack_positions,all_white)
            Rook31w_attack.all_white_class1("r3w",r31,black_check,attack,attack_positions,all_white)
            attack_positions=Rook31w_attack.attack_positions
            attack=Rook31w_attack.attack
            
            Rook32w_attack=attack_class_and_all_white("r3w",r32,black_check,attack,attack_positions,all_white)
            Rook32w_attack.attack_class1("r3w",r32,black_check,attack,attack_positions,all_white)
            Rook32w_attack.all_white_class1("r3w",r32,black_check,attack,attack_positions,all_white)
            attack_positions=Rook32w_attack.attack_positions
            attack=Rook32w_attack.attack

            Rook33w_attack=attack_class_and_all_white("r3w",r33,black_check,attack,attack_positions,all_white)
            Rook33w_attack.attack_class1("r3w",r33,black_check,attack,attack_positions,all_white)
            Rook33w_attack.all_white_class1("r3w",r33,black_check,attack,attack_positions,all_white)
            attack_positions=Rook33w_attack.attack_positions
            attack=Rook33w_attack.attack
            
            Rook34w_attack=attack_class_and_all_white("r3w",r34,black_check,attack,attack_positions,all_white)
            Rook34w_attack.attack_class1("r3w",r34,black_check,attack,attack_positions,all_white)
            Rook34w_attack.all_white_class1("r3w",r34,black_check,attack,attack_positions,all_white)
            attack_positions=Rook34w_attack.attack_positions
            attack=Rook34w_attack.attack
            
            Rook41w_attack=attack_class_and_all_white("r4w",r41,black_check,attack,attack_positions,all_white)
            Rook41w_attack.attack_class1("r4w",r41,black_check,attack,attack_positions,all_white)
            Rook41w_attack.all_white_class1("r4w",r41,black_check,attack,attack_positions,all_white)
            attack_positions=Rook41w_attack.attack_positions
            attack=Rook41w_attack.attack
            
            Rook42w_attack=attack_class_and_all_white("r4w",r42,black_check,attack,attack_positions,all_white)
            Rook42w_attack.attack_class1("r4w",r42,black_check,attack,attack_positions,all_white)
            Rook42w_attack.all_white_class1("r4w",r42,black_check,attack,attack_positions,all_white)
            attack_positions=Rook42w_attack.attack_positions
            attack=Rook42w_attack.attack

            Rook43w_attack=attack_class_and_all_white("r4w",r43,black_check,attack,attack_positions,all_white)
            Rook43w_attack.attack_class1("r4w",r43,black_check,attack,attack_positions,all_white)
            Rook43w_attack.all_white_class1("r4w",r43,black_check,attack,attack_positions,all_white)
            attack_positions=Rook43w_attack.attack_positions
            attack=Rook43w_attack.attack
            
            Rook44w_attack=attack_class_and_all_white("r4w",r44,black_check,attack,attack_positions,all_white)
            Rook44w_attack.attack_class1("r4w",r44,black_check,attack,attack_positions,all_white)
            Rook44w_attack.all_white_class1("r4w",r44,black_check,attack,attack_positions,all_white)
            attack_positions=Rook44w_attack.attack_positions
            attack=Rook44w_attack.attack

            Rook51w_attack=attack_class_and_all_white("r5w",r51,black_check,attack,attack_positions,all_white)
            Rook51w_attack.attack_class1("r5w",r51,black_check,attack,attack_positions,all_white)
            Rook51w_attack.all_white_class1("r5w",r51,black_check,attack,attack_positions,all_white)
            attack_positions=Rook51w_attack.attack_positions
            attack=Rook51w_attack.attack
            
            Rook52w_attack=attack_class_and_all_white("r5w",r52,black_check,attack,attack_positions,all_white)
            Rook52w_attack.attack_class1("r5w",r52,black_check,attack,attack_positions,all_white)
            Rook52w_attack.all_white_class1("r5w",r52,black_check,attack,attack_positions,all_white)
            attack_positions=Rook52w_attack.attack_positions
            attack=Rook52w_attack.attack

            Rook53w_attack=attack_class_and_all_white("r5w",r53,black_check,attack,attack_positions,all_white)
            Rook53w_attack.attack_class1("r5w",r53,black_check,attack,attack_positions,all_white)
            Rook53w_attack.all_white_class1("r5w",r53,black_check,attack,attack_positions,all_white)
            attack_positions=Rook53w_attack.attack_positions
            attack=Rook53w_attack.attack
            
            Rook54w_attack=attack_class_and_all_white("r5w",r54,black_check,attack,attack_positions,all_white)
            Rook54w_attack.attack_class1("r5w",r54,black_check,attack,attack_positions,all_white)
            Rook54w_attack.all_white_class1("r5w",r54,black_check,attack,attack_positions,all_white)
            attack_positions=Rook54w_attack.attack_positions
            attack=Rook54w_attack.attack
                    
            Bishop11w_attack=attack_class_and_all_white("b1w",b11,black_check,attack,attack_positions,all_white)
            Bishop11w_attack.attack_class1("b1w",b11,black_check,attack,attack_positions,all_white)
            Bishop11w_attack.all_white_class1("b1w",b11,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop11w_attack.attack_positions
            attack=Bishop11w_attack.attack
            
            Bishop12w_attack=attack_class_and_all_white("b1w",b12,black_check,attack,attack_positions,all_white)
            Bishop12w_attack.attack_class1("b1w",b12,black_check,attack,attack_positions,all_white)
            Bishop12w_attack.all_white_class1("b1w",b12,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop12w_attack.attack_positions
            attack=Bishop12w_attack.attack

            Bishop13w_attack=attack_class_and_all_white("b1w",b13,black_check,attack,attack_positions,all_white)
            Bishop13w_attack.attack_class1("b1w",b13,black_check,attack,attack_positions,all_white)
            Bishop13w_attack.all_white_class1("b1w",b13,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop13w_attack.attack_positions
            attack=Bishop13w_attack.attack
            
            Bishop14w_attack=attack_class_and_all_white("b1w",b14,black_check,attack,attack_positions,all_white)
            Bishop14w_attack.attack_class1("b1w",b14,black_check,attack,attack_positions,all_white)
            Bishop14w_attack.all_white_class1("b1w",b14,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop14w_attack.attack_positions
            attack=Bishop14w_attack.attack
                    
            Bishop21w_attack=attack_class_and_all_white("b2w",b21,black_check,attack,attack_positions,all_white)
            Bishop21w_attack.attack_class1("b2w",b21,black_check,attack,attack_positions,all_white)
            Bishop21w_attack.all_white_class1("b2w",b21,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop21w_attack.attack_positions
            attack=Bishop21w_attack.attack
            
            Bishop22w_attack=attack_class_and_all_white("b2w",b22,black_check,attack,attack_positions,all_white)
            Bishop22w_attack.attack_class1("b2w",b22,black_check,attack,attack_positions,all_white)
            Bishop22w_attack.all_white_class1("b2w",b22,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop22w_attack.attack_positions
            attack=Bishop22w_attack.attack

            Bishop23w_attack=attack_class_and_all_white("b2w",b23,black_check,attack,attack_positions,all_white)
            Bishop23w_attack.attack_class1("b2w",b23,black_check,attack,attack_positions,all_white)
            Bishop23w_attack.all_white_class1("b2w",b23,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop23w_attack.attack_positions
            attack=Bishop23w_attack.attack
            
            Bishop24w_attack=attack_class_and_all_white("b2w",b24,black_check,attack,attack_positions,all_white)
            Bishop24w_attack.attack_class1("b2w",b24,black_check,attack,attack_positions,all_white)
            Bishop24w_attack.all_white_class1("b2w",b24,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop24w_attack.attack_positions
            attack=Bishop24w_attack.attack

            Bishop31w_attack=attack_class_and_all_white("b3w",b31,black_check,attack,attack_positions,all_white)
            Bishop31w_attack.attack_class1("b3w",b31,black_check,attack,attack_positions,all_white)
            Bishop31w_attack.all_white_class1("b3w",b31,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop31w_attack.attack_positions
            attack=Bishop31w_attack.attack
            
            Bishop32w_attack=attack_class_and_all_white("b3w",b32,black_check,attack,attack_positions,all_white)
            Bishop32w_attack.attack_class1("b3w",b32,black_check,attack,attack_positions,all_white)
            Bishop32w_attack.all_white_class1("b3w",b32,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop32w_attack.attack_positions
            attack=Bishop32w_attack.attack

            Bishop33w_attack=attack_class_and_all_white("b3w",b33,black_check,attack,attack_positions,all_white)
            Bishop33w_attack.attack_class1("b3w",b33,black_check,attack,attack_positions,all_white)
            Bishop33w_attack.all_white_class1("b3w",b33,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop33w_attack.attack_positions
            attack=Bishop33w_attack.attack
            
            Bishop34w_attack=attack_class_and_all_white("b3w",b34,black_check,attack,attack_positions,all_white)
            Bishop34w_attack.attack_class1("b3w",b34,black_check,attack,attack_positions,all_white)
            Bishop34w_attack.all_white_class1("b3w",b34,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop34w_attack.attack_positions
            attack=Bishop34w_attack.attack
            
            Bishop41w_attack=attack_class_and_all_white("b4w",b41,black_check,attack,attack_positions,all_white)
            Bishop41w_attack.attack_class1("b4w",b41,black_check,attack,attack_positions,all_white)
            Bishop41w_attack.all_white_class1("b4w",b41,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop41w_attack.attack_positions
            attack=Bishop41w_attack.attack
            
            Bishop42w_attack=attack_class_and_all_white("b4w",b42,black_check,attack,attack_positions,all_white)
            Bishop42w_attack.attack_class1("b4w",b42,black_check,attack,attack_positions,all_white)
            Bishop42w_attack.all_white_class1("b4w",b42,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop42w_attack.attack_positions
            attack=Bishop42w_attack.attack

            Bishop43w_attack=attack_class_and_all_white("b4w",b43,black_check,attack,attack_positions,all_white)
            Bishop43w_attack.attack_class1("b4w",b43,black_check,attack,attack_positions,all_white)
            Bishop43w_attack.all_white_class1("b4w",b43,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop43w_attack.attack_positions
            attack=Bishop43w_attack.attack
            
            Bishop44w_attack=attack_class_and_all_white("b4w",b44,black_check,attack,attack_positions,all_white)
            Bishop44w_attack.attack_class1("b4w",b44,black_check,attack,attack_positions,all_white)
            Bishop44w_attack.all_white_class1("b4w",b44,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop44w_attack.attack_positions
            attack=Bishop44w_attack.attack

            Bishop51w_attack=attack_class_and_all_white("b5w",b51,black_check,attack,attack_positions,all_white)
            Bishop51w_attack.attack_class1("b5w",b51,black_check,attack,attack_positions,all_white)
            Bishop51w_attack.all_white_class1("b5w",b51,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop51w_attack.attack_positions
            attack=Bishop51w_attack.attack
            
            Bishop52w_attack=attack_class_and_all_white("b5w",b52,black_check,attack,attack_positions,all_white)
            Bishop52w_attack.attack_class1("b5w",b52,black_check,attack,attack_positions,all_white)
            Bishop52w_attack.all_white_class1("b5w",b52,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop52w_attack.attack_positions
            attack=Bishop52w_attack.attack

            Bishop53w_attack=attack_class_and_all_white("b5w",b53,black_check,attack,attack_positions,all_white)
            Bishop53w_attack.attack_class1("b5w",b53,black_check,attack,attack_positions,all_white)
            Bishop53w_attack.all_white_class1("b5w",b53,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop53w_attack.attack_positions
            attack=Bishop53w_attack.attack
            
            Bishop54w_attack=attack_class_and_all_white("b5w",b54,black_check,attack,attack_positions,all_white)
            Bishop54w_attack.attack_class1("b5w",b54,black_check,attack,attack_positions,all_white)
            Bishop54w_attack.all_white_class1("b5w",b54,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop54w_attack.attack_positions
            attack=Bishop54w_attack.attack

            Queen11w_attack=attack_class_and_all_white("q1w",q11,black_check,attack,attack_positions,all_white)
            Queen11w_attack.attack_class1("q1w",q11,black_check,attack,attack_positions,all_white)
            Queen11w_attack.all_white_class1("q1w",q11,black_check,attack,attack_positions,all_white)
            attack_positions=Queen11w_attack.attack_positions
            attack=Queen11w_attack.attack
            
            Queen12w_attack=attack_class_and_all_white("q1w",q12,black_check,attack,attack_positions,all_white)
            Queen12w_attack.attack_class1("q1w",q12,black_check,attack,attack_positions,all_white)
            Queen12w_attack.all_white_class1("q1w",q12,black_check,attack,attack_positions,all_white)
            attack_positions=Queen12w_attack.attack_positions
            attack=Queen12w_attack.attack

            Queen13w_attack=attack_class_and_all_white("q1w",q13,black_check,attack,attack_positions,all_white)
            Queen13w_attack.attack_class1("q1w",q13,black_check,attack,attack_positions,all_white)
            Queen13w_attack.all_white_class1("q1w",q13,black_check,attack,attack_positions,all_white)
            attack_positions=Queen13w_attack.attack_positions
            attack=Queen13w_attack.attack
            
            Queen14w_attack=attack_class_and_all_white("q1w",q14,black_check,attack,attack_positions,all_white)
            Queen14w_attack.attack_class1("q1w",q14,black_check,attack,attack_positions,all_white)
            Queen14w_attack.all_white_class1("q1w",q14,black_check,attack,attack_positions,all_white)
            attack_positions=Queen14w_attack.attack_positions
            attack=Queen14w_attack.attack

            Queen15w_attack=attack_class_and_all_white("q1w",q15,black_check,attack,attack_positions,all_white)
            Queen15w_attack.attack_class1("q1w",q15,black_check,attack,attack_positions,all_white)
            Queen15w_attack.all_white_class1("q1w",q15,black_check,attack,attack_positions,all_white)
            attack_positions=Queen15w_attack.attack_positions
            attack=Queen15w_attack.attack
            
            Queen16w_attack=attack_class_and_all_white("q1w",q16,black_check,attack,attack_positions,all_white)
            Queen16w_attack.attack_class1("q1w",q16,black_check,attack,attack_positions,all_white)
            Queen16w_attack.all_white_class1("q1w",q16,black_check,attack,attack_positions,all_white)
            attack_positions=Queen16w_attack.attack_positions
            attack=Queen16w_attack.attack
            
            Queen17w_attack=attack_class_and_all_white("q1w",q17,black_check,attack,attack_positions,all_white)
            Queen17w_attack.attack_class1("q1w",q17,black_check,attack,attack_positions,all_white)
            Queen17w_attack.all_white_class1("q1w",q17,black_check,attack,attack_positions,all_white)
            attack_positions=Queen17w_attack.attack_positions
            attack=Queen17w_attack.attack
            
            Queen18w_attack=attack_class_and_all_white("q1w",q18,black_check,attack,attack_positions,all_white)
            Queen18w_attack.attack_class1("q1w",q18,black_check,attack,attack_positions,all_white)
            Queen18w_attack.all_white_class1("q1w",q18,black_check,attack,attack_positions,all_white)
            attack_positions=Queen18w_attack.attack_positions
            attack=Queen18w_attack.attack
            
            Queen21w_attack=attack_class_and_all_white("q2w",q21,black_check,attack,attack_positions,all_white)
            Queen21w_attack.attack_class1("q2w",q21,black_check,attack,attack_positions,all_white)
            Queen21w_attack.all_white_class1("q2w",q21,black_check,attack,attack_positions,all_white)
            attack_positions=Queen21w_attack.attack_positions
            attack=Queen21w_attack.attack
            
            Queen22w_attack=attack_class_and_all_white("q2w",q22,black_check,attack,attack_positions,all_white)
            Queen22w_attack.attack_class1("q2w",q22,black_check,attack,attack_positions,all_white)
            Queen22w_attack.all_white_class1("q2w",q22,black_check,attack,attack_positions,all_white)
            attack_positions=Queen22w_attack.attack_positions
            attack=Queen22w_attack.attack

            Queen23w_attack=attack_class_and_all_white("q2w",q23,black_check,attack,attack_positions,all_white)
            Queen23w_attack.attack_class1("q2w",q23,black_check,attack,attack_positions,all_white)
            Queen23w_attack.all_white_class1("q2w",q23,black_check,attack,attack_positions,all_white)
            attack_positions=Queen23w_attack.attack_positions
            attack=Queen23w_attack.attack
            
            Queen24w_attack=attack_class_and_all_white("q2w",q24,black_check,attack,attack_positions,all_white)
            Queen24w_attack.attack_class1("q2w",q24,black_check,attack,attack_positions,all_white)
            Queen24w_attack.all_white_class1("q2w",q24,black_check,attack,attack_positions,all_white)
            attack_positions=Queen24w_attack.attack_positions
            attack=Queen24w_attack.attack

            Queen25w_attack=attack_class_and_all_white("q2w",q25,black_check,attack,attack_positions,all_white)
            Queen25w_attack.attack_class1("q2w",q25,black_check,attack,attack_positions,all_white)
            Queen25w_attack.all_white_class1("q2w",q25,black_check,attack,attack_positions,all_white)
            attack_positions=Queen25w_attack.attack_positions
            attack=Queen25w_attack.attack
            
            Queen26w_attack=attack_class_and_all_white("q2w",q26,black_check,attack,attack_positions,all_white)
            Queen26w_attack.attack_class1("q2w",q26,black_check,attack,attack_positions,all_white)
            Queen26w_attack.all_white_class1("q2w",q26,black_check,attack,attack_positions,all_white)
            attack_positions=Queen26w_attack.attack_positions
            attack=Queen26w_attack.attack
            
            Queen27w_attack=attack_class_and_all_white("q2w",q27,black_check,attack,attack_positions,all_white)
            Queen27w_attack.attack_class1("q2w",q27,black_check,attack,attack_positions,all_white)
            Queen27w_attack.all_white_class1("q2w",q27,black_check,attack,attack_positions,all_white)
            attack_positions=Queen27w_attack.attack_positions
            attack=Queen27w_attack.attack
            
            Queen28w_attack=attack_class_and_all_white("q2w",q28,black_check,attack,attack_positions,all_white)
            Queen28w_attack.attack_class1("q2w",q28,black_check,attack,attack_positions,all_white)
            Queen28w_attack.all_white_class1("q2w",q28,black_check,attack,attack_positions,all_white)
            attack_positions=Queen28w_attack.attack_positions
            attack=Queen28w_attack.attack
            
            Queen31w_attack=attack_class_and_all_white("q3w",q31,black_check,attack,attack_positions,all_white)
            Queen31w_attack.attack_class1("q3w",q31,black_check,attack,attack_positions,all_white)
            Queen31w_attack.all_white_class1("q3w",q31,black_check,attack,attack_positions,all_white)
            attack_positions=Queen31w_attack.attack_positions
            attack=Queen31w_attack.attack
            
            Queen32w_attack=attack_class_and_all_white("q3w",q32,black_check,attack,attack_positions,all_white)
            Queen32w_attack.attack_class1("q3w",q32,black_check,attack,attack_positions,all_white)
            Queen32w_attack.all_white_class1("q3w",q32,black_check,attack,attack_positions,all_white)
            attack_positions=Queen32w_attack.attack_positions
            attack=Queen32w_attack.attack

            Queen33w_attack=attack_class_and_all_white("q3w",q33,black_check,attack,attack_positions,all_white)
            Queen33w_attack.attack_class1("q3w",q33,black_check,attack,attack_positions,all_white)
            Queen33w_attack.all_white_class1("q3w",q33,black_check,attack,attack_positions,all_white)
            attack_positions=Queen33w_attack.attack_positions
            attack=Queen33w_attack.attack
            
            Queen34w_attack=attack_class_and_all_white("q3w",q34,black_check,attack,attack_positions,all_white)
            Queen34w_attack.attack_class1("q3w",q34,black_check,attack,attack_positions,all_white)
            Queen34w_attack.all_white_class1("q3w",q34,black_check,attack,attack_positions,all_white)
            attack_positions=Queen34w_attack.attack_positions
            attack=Queen34w_attack.attack

            Queen35w_attack=attack_class_and_all_white("q3w",q35,black_check,attack,attack_positions,all_white)
            Queen35w_attack.attack_class1("q3w",q35,black_check,attack,attack_positions,all_white)
            Queen35w_attack.all_white_class1("q3w",q35,black_check,attack,attack_positions,all_white)
            attack_positions=Queen35w_attack.attack_positions
            attack=Queen35w_attack.attack
            
            Queen36w_attack=attack_class_and_all_white("q3w",q36,black_check,attack,attack_positions,all_white)
            Queen36w_attack.attack_class1("q3w",q36,black_check,attack,attack_positions,all_white)
            Queen36w_attack.all_white_class1("q3w",q36,black_check,attack,attack_positions,all_white)
            attack_positions=Queen36w_attack.attack_positions
            attack=Queen36w_attack.attack
            
            Queen37w_attack=attack_class_and_all_white("q3w",q37,black_check,attack,attack_positions,all_white)
            Queen37w_attack.attack_class1("q3w",q37,black_check,attack,attack_positions,all_white)
            Queen37w_attack.all_white_class1("q3w",q37,black_check,attack,attack_positions,all_white)
            attack_positions=Queen37w_attack.attack_positions
            attack=Queen37w_attack.attack
            
            Queen38w_attack=attack_class_and_all_white("q3w",q38,black_check,attack,attack_positions,all_white)
            Queen38w_attack.attack_class1("q3w",q38,black_check,attack,attack_positions,all_white)
            Queen38w_attack.all_white_class1("q3w",q38,black_check,attack,attack_positions,all_white)
            attack_positions=Queen38w_attack.attack_positions
            attack=Queen38w_attack.attack
            
            Queen41w_attack=attack_class_and_all_white("q3w",q41,black_check,attack,attack_positions,all_white)
            Queen41w_attack.attack_class1("q3w",q41,black_check,attack,attack_positions,all_white)
            Queen41w_attack.all_white_class1("q3w",q41,black_check,attack,attack_positions,all_white)
            attack_positions=Queen41w_attack.attack_positions
            attack=Queen41w_attack.attack
            
            Queen42w_attack=attack_class_and_all_white("q3w",q42,black_check,attack,attack_positions,all_white)
            Queen42w_attack.attack_class1("q3w",q42,black_check,attack,attack_positions,all_white)
            Queen42w_attack.all_white_class1("q3w",q42,black_check,attack,attack_positions,all_white)
            attack_positions=Queen42w_attack.attack_positions
            attack=Queen42w_attack.attack

            Queen43w_attack=attack_class_and_all_white("q3w",q43,black_check,attack,attack_positions,all_white)
            Queen43w_attack.attack_class1("q3w",q43,black_check,attack,attack_positions,all_white)
            Queen43w_attack.all_white_class1("q3w",q43,black_check,attack,attack_positions,all_white)
            attack_positions=Queen43w_attack.attack_positions
            attack=Queen43w_attack.attack
            
            Queen44w_attack=attack_class_and_all_white("q3w",q44,black_check,attack,attack_positions,all_white)
            Queen44w_attack.attack_class1("q3w",q44,black_check,attack,attack_positions,all_white)
            Queen44w_attack.all_white_class1("q3w",q44,black_check,attack,attack_positions,all_white)
            attack_positions=Queen44w_attack.attack_positions
            attack=Queen44w_attack.attack

            Queen45w_attack=attack_class_and_all_white("q3w",q45,black_check,attack,attack_positions,all_white)
            Queen45w_attack.attack_class1("q3w",q45,black_check,attack,attack_positions,all_white)
            Queen45w_attack.all_white_class1("q3w",q45,black_check,attack,attack_positions,all_white)
            attack_positions=Queen45w_attack.attack_positions
            attack=Queen45w_attack.attack
            
            Queen46w_attack=attack_class_and_all_white("q3w",q46,black_check,attack,attack_positions,all_white)
            Queen46w_attack.attack_class1("q3w",q46,black_check,attack,attack_positions,all_white)
            Queen46w_attack.all_white_class1("q3w",q46,black_check,attack,attack_positions,all_white)
            attack_positions=Queen46w_attack.attack_positions
            attack=Queen46w_attack.attack
            
            Queen47w_attack=attack_class_and_all_white("q3w",q47,black_check,attack,attack_positions,all_white)
            Queen47w_attack.attack_class1("q3w",q47,black_check,attack,attack_positions,all_white)
            Queen47w_attack.all_white_class1("q3w",q47,black_check,attack,attack_positions,all_white)
            attack_positions=Queen47w_attack.attack_positions
            attack=Queen47w_attack.attack
            
            Queen48w_attack=attack_class_and_all_white("q3w",q48,black_check,attack,attack_positions,all_white)
            Queen48w_attack.attack_class1("q3w",q48,black_check,attack,attack_positions,all_white)
            Queen48w_attack.all_white_class1("q3w",q48,black_check,attack,attack_positions,all_white)
            attack_positions=Queen48w_attack.attack_positions
            attack=Queen48w_attack.attack
            
            for ju in range (0,len(kn1)):
                if xposition==kn1[ju][0] and yposition==kn1[ju][1]:
                    attack.append(["kn1w"])
            for ju in range (0,len(kn2)):
                if xposition==kn2[ju][0] and yposition==kn2[ju][1]:
                    attack.append(["kn2w"])
            for ju in range (0,len(kn3)):
                if xposition==kn3[ju][0] and yposition==kn3[ju][1]:
                    attack.append(["kn3w"])
            for ju in range (0,len(kn4)):
                if xposition==kn4[ju][0] and yposition==kn4[ju][1]:
                    attack.append(["kn4w"])
            for ju in range (0,len(kn5)):
                if xposition==kn5[ju][0] and yposition==kn5[ju][1]:
                    attack.append(["kn5w"])  
            for ju in range (0,len(p1)):
                if xposition==p1[ju][0] and yposition==p1[ju][1]:
                    attack.append(["p1w"])
            for ju in range (0,len(p2)):
                if xposition==p2[ju][0] and yposition==p2[ju][1]:
                    attack.append(["p2w"])   
            for ju in range (0,len(p3)):
                if xposition==p3[ju][0] and yposition==p3[ju][1]:
                    attack.append(["p3w"])
            for ju in range (0,len(p4)):
                if xposition==p4[ju][0] and yposition==p4[ju][1]:
                    attack.append(["p4w"])
            for ju in range (0,len(p5)):
                if xposition==p5[ju][0] and yposition==p5[ju][1]:
                    attack.append(["p5w"])
            for ju in range (0,len(p6)):
                if xposition==p6[ju][0] and yposition==p6[ju][1]:
                    attack.append(["p6w"])
            for ju in range (0,len(p7)):
                if xposition==p7[ju][0] and yposition==p7[ju][1]:
                    attack.append(["p7w"])
            for ju in range (0,len(p8)):               
                if xposition==p8[ju][0] and yposition==p8[ju][1]:
                    attack.append(["p8w"])
            if attack!=[]:
                black_check=True
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
            for i in range (0,len(k1w)):
                if k1w!=[]:
                    all_white.append(k1w[i])                
            hb=1
            
        if hw==0:
            two_protectors=False
            white_protector=[]
            pos_spaces=[]
            all_black=[]
            Bishop1b2=bishop1(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
            Bishop1b2.check(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
                
            Bishop2b2=bishop1(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")
            Bishop2b2.check(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")

            Bishop3b3=bishop1(b31b,b32b,b33b,b34b,white_protector,"b3b","k1w","w","b")
            Bishop3b3.check(b31b,b32b,b33b,b34b,white_protector,"b3b","k1w","w","b")

            Bishop4b4=bishop1(b41b,b42b,b43b,b44b,white_protector,"b4b","k1w","w","b")
            Bishop4b4.check(b41b,b42b,b43b,b44b,white_protector,"b4b","k1w","w","b")

            Bishop5b5=bishop1(b51b,b52b,b53b,b54b,white_protector,"b5b","k1w","w","b")
            Bishop5b5.check(b51b,b52b,b53b,b54b,white_protector,"b5b","k1w","w","b")

            Queen1b2=queen1(q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b,white_protector,"q1b","k1w","w","b")
            Queen1b2.check(q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b,white_protector,"q1b","k1w","w","b")

            Queen2b2=queen1(q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b,white_protector,"q2b","k1w","w","b")
            Queen2b2.check(q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b,white_protector,"q2b","k1w","w","b")

            Queen4b4=queen1(q41b,q42b,q43b,q44b,q45b,q46b,q47b,q48b,white_protector,"q4b","k1w","w","b")
            Queen4b4.check(q41b,q42b,q43b,q44b,q45b,q46b,q47b,q48b,white_protector,"q4b","k1w","w","b")

            Queen3b3=queen1(q31b,q32b,q33b,q34b,q35b,q36b,q37b,q38b,white_protector,"q3b","k1w","w","b")
            Queen3b3.check(q31b,q32b,q33b,q34b,q35b,q36b,q37b,q38b,white_protector,"q3b","k1w","w","b")

            knight1b2=knight1(kn1b,white_protector,"kn1b","k1w","w","b")
            knight1b2.check(kn1b,white_protector,"kn1b","k1w","w","b")            

            knight2b2=knight1(kn1b,white_protector,"kn2b","k1w","w","b")
            knight2b2.check(kn1b,white_protector,"kn2b","k1w","w","b")

            knight3b3=knight1(kn3b,white_protector,"kn3b","k1w","w","b")
            knight3b3.check(kn3b,white_protector,"kn3b","k1w","w","b")

            knight4b4=knight1(kn4b,white_protector,"kn4b","k1w","w","b")
            knight4b4.check(kn4b,white_protector,"kn4b","k1w","w","b")

            knight5b2=knight1(kn5b,white_protector,"kn5b","k1w","w","b")
            knight5b2.check(kn5b,white_protector,"kn5b","k1w","w","b") 

            Rook1b2=rook1(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")
            Rook1b2.check(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")

            Rook2b2=rook1(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")
            Rook2b2.check(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")

            Rook3b2=rook1(r31b,r32b,r33b,r34b,white_protector,"r3b","k1w","w","b")
            Rook3b2.check(r31b,r32b,r33b,r34b,white_protector,"r3b","k1w","w","b")

            Rook4b2=rook1(r41b,r42b,r43b,r44b,white_protector,"r4b","k1w","w","b")
            Rook4b2.check(r41b,r42b,r43b,r44b,white_protector,"r4b","k1w","w","b")

            Rook5b2=rook1(r51b,r52b,r53b,r54b,white_protector,"r5b","k1w","w","b")
            Rook5b2.check(r51b,r52b,r53b,r54b,white_protector,"r5b","k1w","w","b")

            King1b2=king1(k1b,"k1b","w","b")
            King1b2.check(k1b,"k1b","w","b")

            Pawn1b2=pawn1b(p1b,"p1b","w","b")
            Pawn1b2.check(p1b,"p1b","w","b")

            Pawn2b2=pawn1b(p2b,"p2b","w","b")
            Pawn2b2.check(p2b,"p2b","w","b")

            Pawn3b2=pawn1b(p3b,"p3b","w","b")
            Pawn3b2.check(p3b,"p3b","w","b")

            Pawn4b2=pawn1b(p4b,"p4b","w","b")
            Pawn4b2.check(p4b,"p4b","w","b")

            Pawn5b2=pawn1b(p5b,"p5b","w","b")
            Pawn5b2.check(p5b,"p5b","w","b")

            Pawn6b2=pawn1b(p6b,"p6b","w","b")
            Pawn6b2.check(p6b,"p6b","w","b")

            Pawn7b2=pawn1b(p7b,"p7b","w","b")
            Pawn7b2.check(p7b,"p7b","w","b")

            Pawn8b2=pawn1b(p8b,"p8b","w","b")
            Pawn8b2.check(p8b,"p8b","w","b")

            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition
            attack=[]
            attack_positions=[]
            
            Rook11b_attack=attack_class_and_all_black("r1b",r11b,white_check,attack,attack_positions,all_black)
            Rook11b_attack.attack_class1("r1b",r11b,white_check,attack,attack_positions,all_black)
            Rook11b_attack.all_black_class1("r1b",r11b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook11b_attack.attack_positions
            attack=Rook11b_attack.attack
            
            Rook12b_attack=attack_class_and_all_black("r1b",r12b,white_check,attack,attack_positions,all_black)
            Rook12b_attack.attack_class1("r1b",r12b,white_check,attack,attack_positions,all_black)
            Rook12b_attack.all_black_class1("r1b",r12b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook12b_attack.attack_positions
            attack=Rook12b_attack.attack

            Rook13b_attack=attack_class_and_all_black("r1b",r13b,white_check,attack,attack_positions,all_black)
            Rook13b_attack.attack_class1("r1b",r13b,white_check,attack,attack_positions,all_black)
            Rook13b_attack.all_black_class1("r1b",r13b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook13b_attack.attack_positions
            attack=Rook13b_attack.attack
            
            Rook14b_attack=attack_class_and_all_black("r1b",r14b,white_check,attack,attack_positions,all_black)
            Rook14b_attack.attack_class1("r1b",r14b,white_check,attack,attack_positions,all_black)
            Rook14b_attack.all_black_class1("r1b",r14b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook14b_attack.attack_positions
            attack=Rook14b_attack.attack
                    
            Rook21b_attack=attack_class_and_all_black("r1b",r21b,white_check,attack,attack_positions,all_black)
            Rook21b_attack.attack_class1("r1b",r21b,white_check,attack,attack_positions,all_black)
            Rook21b_attack.all_black_class1("r1b",r21b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook21b_attack.attack_positions
            attack=Rook21b_attack.attack
            
            Rook22b_attack=attack_class_and_all_black("r1b",r22b,white_check,attack,attack_positions,all_black)
            Rook22b_attack.attack_class1("r1b",r22b,white_check,attack,attack_positions,all_black)
            Rook22b_attack.all_black_class1("r1b",r22b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook22b_attack.attack_positions
            attack=Rook22b_attack.attack

            Rook23b_attack=attack_class_and_all_black("r1b",r23b,white_check,attack,attack_positions,all_black)
            Rook23b_attack.attack_class1("r1b",r23b,white_check,attack,attack_positions,all_black)
            Rook23b_attack.all_black_class1("r1b",r23b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook23b_attack.attack_positions
            attack=Rook23b_attack.attack
            
            Rook24b_attack=attack_class_and_all_black("r1b",r24b,white_check,attack,attack_positions,all_black)
            Rook24b_attack.attack_class1("r1b",r24b,white_check,attack,attack_positions,all_black)
            Rook24b_attack.all_black_class1("r1b",r24b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook24b_attack.attack_positions
            attack=Rook24b_attack.attack

            Rook31b_attack=attack_class_and_all_black("r1b",r31b,white_check,attack,attack_positions,all_black)
            Rook31b_attack.attack_class1("r1b",r31b,white_check,attack,attack_positions,all_black)
            Rook31b_attack.all_black_class1("r1b",r31b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook31b_attack.attack_positions
            attack=Rook31b_attack.attack
            
            Rook32b_attack=attack_class_and_all_black("r1b",r32b,white_check,attack,attack_positions,all_black)
            Rook32b_attack.attack_class1("r1b",r32b,white_check,attack,attack_positions,all_black)
            Rook32b_attack.all_black_class1("r1b",r32b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook32b_attack.attack_positions
            attack=Rook32b_attack.attack

            Rook33b_attack=attack_class_and_all_black("r1b",r33b,white_check,attack,attack_positions,all_black)
            Rook33b_attack.attack_class1("r1b",r33b,white_check,attack,attack_positions,all_black)
            Rook33b_attack.all_black_class1("r1b",r33b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook33b_attack.attack_positions
            attack=Rook33b_attack.attack
            
            Rook34b_attack=attack_class_and_all_black("r1b",r34b,white_check,attack,attack_positions,all_black)
            Rook34b_attack.attack_class1("r1b",r34b,white_check,attack,attack_positions,all_black)
            Rook34b_attack.all_black_class1("r1b",r34b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook34b_attack.attack_positions
            attack=Rook34b_attack.attack
            
            Rook41b_attack=attack_class_and_all_black("r1b",r41b,white_check,attack,attack_positions,all_black)
            Rook41b_attack.attack_class1("r1b",r41b,white_check,attack,attack_positions,all_black)
            Rook41b_attack.all_black_class1("r1b",r41b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook41b_attack.attack_positions
            attack=Rook41b_attack.attack
            
            Rook42b_attack=attack_class_and_all_black("r1b",r42b,white_check,attack,attack_positions,all_black)
            Rook42b_attack.attack_class1("r1b",r42b,white_check,attack,attack_positions,all_black)
            Rook42b_attack.all_black_class1("r1b",r42b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook42b_attack.attack_positions
            attack=Rook42b_attack.attack

            Rook43b_attack=attack_class_and_all_black("r1b",r43b,white_check,attack,attack_positions,all_black)
            Rook43b_attack.attack_class1("r1b",r43b,white_check,attack,attack_positions,all_black)
            Rook43b_attack.all_black_class1("r1b",r43b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook43b_attack.attack_positions
            attack=Rook43b_attack.attack
            
            Rook44b_attack=attack_class_and_all_black("r1b",r44b,white_check,attack,attack_positions,all_black)
            Rook44b_attack.attack_class1("r1b",r44b,white_check,attack,attack_positions,all_black)
            Rook44b_attack.all_black_class1("r1b",r44b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook44b_attack.attack_positions
            attack=Rook44b_attack.attack

            Rook51b_attack=attack_class_and_all_black("r1b",r51b,white_check,attack,attack_positions,all_black)
            Rook51b_attack.attack_class1("r1b",r51b,white_check,attack,attack_positions,all_black)
            Rook51b_attack.all_black_class1("r1b",r51b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook51b_attack.attack_positions
            attack=Rook51b_attack.attack
            
            Rook52b_attack=attack_class_and_all_black("r1b",r52b,white_check,attack,attack_positions,all_black)
            Rook52b_attack.attack_class1("r1b",r52b,white_check,attack,attack_positions,all_black)
            Rook52b_attack.all_black_class1("r1b",r52b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook52b_attack.attack_positions
            attack=Rook52b_attack.attack

            Rook53b_attack=attack_class_and_all_black("r1b",r53b,white_check,attack,attack_positions,all_black)
            Rook53b_attack.attack_class1("r1b",r53b,white_check,attack,attack_positions,all_black)
            Rook53b_attack.all_black_class1("r1b",r53b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook53b_attack.attack_positions
            attack=Rook53b_attack.attack
            
            Rook54b_attack=attack_class_and_all_black("r1b",r54b,white_check,attack,attack_positions,all_black)
            Rook54b_attack.attack_class1("r1b",r54b,white_check,attack,attack_positions,all_black)
            Rook54b_attack.all_black_class1("r1b",r54b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook54b_attack.attack_positions
            attack=Rook54b_attack.attack
                    
            Bishop11b_attack=attack_class_and_all_black("b1b",b11b,white_check,attack,attack_positions,all_black)
            Bishop11b_attack.attack_class1("b1b",b11b,white_check,attack,attack_positions,all_black)
            Bishop11b_attack.all_black_class1("b1b",b11b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop11b_attack.attack_positions
            attack=Bishop11b_attack.attack
            
            Bishop12b_attack=attack_class_and_all_black("b1b",b12b,white_check,attack,attack_positions,all_black)
            Bishop12b_attack.attack_class1("b1b",b12b,white_check,attack,attack_positions,all_black)
            Bishop12b_attack.all_black_class1("b1b",b12b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop12b_attack.attack_positions
            attack=Bishop12b_attack.attack

            Bishop13b_attack=attack_class_and_all_black("b1b",b13b,white_check,attack,attack_positions,all_black)
            Bishop13b_attack.attack_class1("b1b",b13b,white_check,attack,attack_positions,all_black)
            Bishop13b_attack.all_black_class1("b1b",b13b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop13b_attack.attack_positions
            attack=Bishop13b_attack.attack
            
            Bishop14b_attack=attack_class_and_all_black("b1b",b14b,white_check,attack,attack_positions,all_black)
            Bishop14b_attack.attack_class1("b1b",b14b,white_check,attack,attack_positions,all_black)
            Bishop14b_attack.all_black_class1("b1b",b14b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop14b_attack.attack_positions
            attack=Bishop14b_attack.attack
                    
            Bishop21b_attack=attack_class_and_all_black("b1b",b21b,white_check,attack,attack_positions,all_black)
            Bishop21b_attack.attack_class1("b1b",b21b,white_check,attack,attack_positions,all_black)
            Bishop21b_attack.all_black_class1("b1b",b21b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop21b_attack.attack_positions
            attack=Bishop21b_attack.attack
            
            Bishop22b_attack=attack_class_and_all_black("b1b",b22b,white_check,attack,attack_positions,all_black)
            Bishop22b_attack.attack_class1("b1b",b22b,white_check,attack,attack_positions,all_black)
            Bishop22b_attack.all_black_class1("b1b",b22b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop22b_attack.attack_positions
            attack=Bishop22b_attack.attack

            Bishop23b_attack=attack_class_and_all_black("b1b",b23b,white_check,attack,attack_positions,all_black)
            Bishop23b_attack.attack_class1("b1b",b23b,white_check,attack,attack_positions,all_black)
            Bishop23b_attack.all_black_class1("b1b",b23b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop23b_attack.attack_positions
            attack=Bishop23b_attack.attack
            
            Bishop24b_attack=attack_class_and_all_black("b1b",b24b,white_check,attack,attack_positions,all_black)
            Bishop24b_attack.attack_class1("b1b",b24b,white_check,attack,attack_positions,all_black)
            Bishop24b_attack.all_black_class1("b1b",b24b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop24b_attack.attack_positions
            attack=Bishop24b_attack.attack

            Bishop31b_attack=attack_class_and_all_black("b1b",b31b,white_check,attack,attack_positions,all_black)
            Bishop31b_attack.attack_class1("b1b",b31b,white_check,attack,attack_positions,all_black)
            Bishop31b_attack.all_black_class1("b1b",b31b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop31b_attack.attack_positions
            attack=Bishop31b_attack.attack
            
            Bishop32b_attack=attack_class_and_all_black("b1b",b32b,white_check,attack,attack_positions,all_black)
            Bishop32b_attack.attack_class1("b1b",b32b,white_check,attack,attack_positions,all_black)
            Bishop32b_attack.all_black_class1("b1b",b32b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop32b_attack.attack_positions
            attack=Bishop32b_attack.attack

            Bishop33b_attack=attack_class_and_all_black("b1b",b33b,white_check,attack,attack_positions,all_black)
            Bishop33b_attack.attack_class1("b1b",b33b,white_check,attack,attack_positions,all_black)
            Bishop33b_attack.all_black_class1("b1b",b33b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop33b_attack.attack_positions
            attack=Bishop33b_attack.attack
            
            Bishop34b_attack=attack_class_and_all_black("b1b",b34b,white_check,attack,attack_positions,all_black)
            Bishop34b_attack.attack_class1("b1b",b34b,white_check,attack,attack_positions,all_black)
            Bishop34b_attack.all_black_class1("b1b",b34b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop34b_attack.attack_positions
            attack=Bishop34b_attack.attack
            
            Bishop41b_attack=attack_class_and_all_black("b1b",b41b,white_check,attack,attack_positions,all_black)
            Bishop41b_attack.attack_class1("b1b",b41b,white_check,attack,attack_positions,all_black)
            Bishop41b_attack.all_black_class1("b1b",b41b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop41b_attack.attack_positions
            attack=Bishop41b_attack.attack
            
            Bishop42b_attack=attack_class_and_all_black("b1b",b42b,white_check,attack,attack_positions,all_black)
            Bishop42b_attack.attack_class1("b1b",b42b,white_check,attack,attack_positions,all_black)
            Bishop42b_attack.all_black_class1("b1b",b42b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop42b_attack.attack_positions
            attack=Bishop42b_attack.attack

            Bishop43b_attack=attack_class_and_all_black("b1b",b43b,white_check,attack,attack_positions,all_black)
            Bishop43b_attack.attack_class1("b1b",b43b,white_check,attack,attack_positions,all_black)
            Bishop43b_attack.all_black_class1("b1b",b43b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop43b_attack.attack_positions
            attack=Bishop43b_attack.attack
            
            Bishop44b_attack=attack_class_and_all_black("b1b",b44b,white_check,attack,attack_positions,all_black)
            Bishop44b_attack.attack_class1("b1b",b44b,white_check,attack,attack_positions,all_black)
            Bishop44b_attack.all_black_class1("b1b",b44b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop44b_attack.attack_positions
            attack=Bishop44b_attack.attack

            Bishop51b_attack=attack_class_and_all_black("b1b",b51b,white_check,attack,attack_positions,all_black)
            Bishop51b_attack.attack_class1("b1b",b51b,white_check,attack,attack_positions,all_black)
            Bishop51b_attack.all_black_class1("b1b",b51b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop51b_attack.attack_positions
            attack=Bishop51b_attack.attack
            
            Bishop52b_attack=attack_class_and_all_black("b1b",b52b,white_check,attack,attack_positions,all_black)
            Bishop52b_attack.attack_class1("b1b",b52b,white_check,attack,attack_positions,all_black)
            Bishop52b_attack.all_black_class1("b1b",b52b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop52b_attack.attack_positions
            attack=Bishop52b_attack.attack

            Bishop53b_attack=attack_class_and_all_black("b1b",b53b,white_check,attack,attack_positions,all_black)
            Bishop53b_attack.attack_class1("b1b",b53b,white_check,attack,attack_positions,all_black)
            Bishop53b_attack.all_black_class1("b1b",b53b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop53b_attack.attack_positions
            attack=Bishop53b_attack.attack
            
            Bishop54b_attack=attack_class_and_all_black("b1b",b54b,white_check,attack,attack_positions,all_black)
            Bishop54b_attack.attack_class1("b1b",b54b,white_check,attack,attack_positions,all_black)
            Bishop54b_attack.all_black_class1("b1b",b54b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop54b_attack.attack_positions
            attack=Bishop54b_attack.attack

            Queen11b_attack=attack_class_and_all_black("q1b",q11b,white_check,attack,attack_positions,all_black)
            Queen11b_attack.attack_class1("q1b",q11b,white_check,attack,attack_positions,all_black)
            Queen11b_attack.all_black_class1("q1b",q11b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen11b_attack.attack_positions
            attack=Queen11b_attack.attack
            
            Queen12b_attack=attack_class_and_all_black("q1b",q12b,white_check,attack,attack_positions,all_black)
            Queen12b_attack.attack_class1("q1b",q12b,white_check,attack,attack_positions,all_black)
            Queen12b_attack.all_black_class1("q1b",q12b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen12b_attack.attack_positions
            attack=Queen12b_attack.attack

            Queen13b_attack=attack_class_and_all_black("q1b",q13b,white_check,attack,attack_positions,all_black)
            Queen13b_attack.attack_class1("q1b",q13b,white_check,attack,attack_positions,all_black)
            Queen13b_attack.all_black_class1("q1b",q13b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen13b_attack.attack_positions
            attack=Queen13b_attack.attack
            
            Queen14b_attack=attack_class_and_all_black("q1b",q14b,white_check,attack,attack_positions,all_black)
            Queen14b_attack.attack_class1("q1b",q14b,white_check,attack,attack_positions,all_black)
            Queen14b_attack.all_black_class1("q1b",q14b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen14b_attack.attack_positions
            attack=Queen14b_attack.attack

            Queen15b_attack=attack_class_and_all_black("q1b",q15b,white_check,attack,attack_positions,all_black)
            Queen15b_attack.attack_class1("q1b",q15b,white_check,attack,attack_positions,all_black)
            Queen15b_attack.all_black_class1("q1b",q15b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen15b_attack.attack_positions
            attack=Queen15b_attack.attack
            
            Queen16b_attack=attack_class_and_all_black("q1b",q16b,white_check,attack,attack_positions,all_black)
            Queen16b_attack.attack_class1("q1b",q16b,white_check,attack,attack_positions,all_black)
            Queen16b_attack.all_black_class1("q1b",q16b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen16b_attack.attack_positions
            attack=Queen16b_attack.attack
            
            Queen17b_attack=attack_class_and_all_black("q1b",q17b,white_check,attack,attack_positions,all_black)
            Queen17b_attack.attack_class1("q1b",q17b,white_check,attack,attack_positions,all_black)
            Queen17b_attack.all_black_class1("q1b",q17b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen17b_attack.attack_positions
            attack=Queen17b_attack.attack
            
            Queen18b_attack=attack_class_and_all_black("q1b",q18b,white_check,attack,attack_positions,all_black)
            Queen18b_attack.attack_class1("q1b",q18b,white_check,attack,attack_positions,all_black)
            Queen18b_attack.all_black_class1("q1b",q18b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen18b_attack.attack_positions
            attack=Queen18b_attack.attack
            
            Queen21b_attack=attack_class_and_all_black("q1b",q21b,white_check,attack,attack_positions,all_black)
            Queen21b_attack.attack_class1("q1b",q21b,white_check,attack,attack_positions,all_black)
            Queen21b_attack.all_black_class1("q1b",q21b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen21b_attack.attack_positions
            attack=Queen21b_attack.attack
            
            Queen22b_attack=attack_class_and_all_black("q1b",q22b,white_check,attack,attack_positions,all_black)
            Queen22b_attack.attack_class1("q1b",q22b,white_check,attack,attack_positions,all_black)
            Queen22b_attack.all_black_class1("q1b",q22b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen22b_attack.attack_positions
            attack=Queen22b_attack.attack

            Queen23b_attack=attack_class_and_all_black("q1b",q23b,white_check,attack,attack_positions,all_black)
            Queen23b_attack.attack_class1("q1b",q23b,white_check,attack,attack_positions,all_black)
            Queen23b_attack.all_black_class1("q1b",q23b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen23b_attack.attack_positions
            attack=Queen23b_attack.attack
            
            Queen24b_attack=attack_class_and_all_black("q1b",q24b,white_check,attack,attack_positions,all_black)
            Queen24b_attack.attack_class1("q1b",q24b,white_check,attack,attack_positions,all_black)
            Queen24b_attack.all_black_class1("q1b",q24b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen24b_attack.attack_positions
            attack=Queen24b_attack.attack

            Queen25b_attack=attack_class_and_all_black("q1b",q25b,white_check,attack,attack_positions,all_black)
            Queen25b_attack.attack_class1("q1b",q25b,white_check,attack,attack_positions,all_black)
            Queen25b_attack.all_black_class1("q1b",q25b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen25b_attack.attack_positions
            attack=Queen25b_attack.attack
            
            Queen26b_attack=attack_class_and_all_black("q1b",q26b,white_check,attack,attack_positions,all_black)
            Queen26b_attack.attack_class1("q1b",q26b,white_check,attack,attack_positions,all_black)
            Queen26b_attack.all_black_class1("q1b",q26b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen26b_attack.attack_positions
            attack=Queen26b_attack.attack
            
            Queen27b_attack=attack_class_and_all_black("q1b",q27b,white_check,attack,attack_positions,all_black)
            Queen27b_attack.attack_class1("q1b",q27b,white_check,attack,attack_positions,all_black)
            Queen27b_attack.all_black_class1("q1b",q27b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen27b_attack.attack_positions
            attack=Queen27b_attack.attack
            
            Queen28b_attack=attack_class_and_all_black("q1b",q28b,white_check,attack,attack_positions,all_black)
            Queen28b_attack.attack_class1("q1b",q28b,white_check,attack,attack_positions,all_black)
            Queen28b_attack.all_black_class1("q1b",q28b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen28b_attack.attack_positions
            attack=Queen28b_attack.attack

            Queen31b_attack=attack_class_and_all_black("q1b",q31b,white_check,attack,attack_positions,all_black)
            Queen31b_attack.attack_class1("q1b",q31b,white_check,attack,attack_positions,all_black)
            Queen31b_attack.all_black_class1("q1b",q31b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen31b_attack.attack_positions
            attack=Queen31b_attack.attack
            
            Queen32b_attack=attack_class_and_all_black("q1b",q32b,white_check,attack,attack_positions,all_black)
            Queen32b_attack.attack_class1("q1b",q32b,white_check,attack,attack_positions,all_black)
            Queen32b_attack.all_black_class1("q1b",q32b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen32b_attack.attack_positions
            attack=Queen32b_attack.attack

            Queen33b_attack=attack_class_and_all_black("q1b",q33b,white_check,attack,attack_positions,all_black)
            Queen33b_attack.attack_class1("q1b",q33b,white_check,attack,attack_positions,all_black)
            Queen33b_attack.all_black_class1("q1b",q33b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen33b_attack.attack_positions
            attack=Queen33b_attack.attack
            
            Queen34b_attack=attack_class_and_all_black("q1b",q34b,white_check,attack,attack_positions,all_black)
            Queen34b_attack.attack_class1("q1b",q34b,white_check,attack,attack_positions,all_black)
            Queen34b_attack.all_black_class1("q1b",q34b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen34b_attack.attack_positions
            attack=Queen34b_attack.attack

            Queen35b_attack=attack_class_and_all_black("q1b",q35b,white_check,attack,attack_positions,all_black)
            Queen35b_attack.attack_class1("q1b",q35b,white_check,attack,attack_positions,all_black)
            Queen35b_attack.all_black_class1("q1b",q35b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen35b_attack.attack_positions
            attack=Queen35b_attack.attack
            
            Queen36b_attack=attack_class_and_all_black("q1b",q36b,white_check,attack,attack_positions,all_black)
            Queen36b_attack.attack_class1("q1b",q36b,white_check,attack,attack_positions,all_black)
            Queen36b_attack.all_black_class1("q1b",q36b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen36b_attack.attack_positions
            attack=Queen36b_attack.attack
            
            Queen37b_attack=attack_class_and_all_black("q1b",q37b,white_check,attack,attack_positions,all_black)
            Queen37b_attack.attack_class1("q1b",q37b,white_check,attack,attack_positions,all_black)
            Queen37b_attack.all_black_class1("q1b",q37b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen37b_attack.attack_positions
            attack=Queen37b_attack.attack
            
            Queen38b_attack=attack_class_and_all_black("q1b",q38b,white_check,attack,attack_positions,all_black)
            Queen38b_attack.attack_class1("q1b",q38b,white_check,attack,attack_positions,all_black)
            Queen38b_attack.all_black_class1("q1b",q38b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen38b_attack.attack_positions
            attack=Queen38b_attack.attack
            
            Queen41b_attack=attack_class_and_all_black("q1b",q41b,white_check,attack,attack_positions,all_black)
            Queen41b_attack.attack_class1("q1b",q41b,white_check,attack,attack_positions,all_black)
            Queen41b_attack.all_black_class1("q1b",q41b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen41b_attack.attack_positions
            attack=Queen41b_attack.attack
            
            Queen42b_attack=attack_class_and_all_black("q1b",q42b,white_check,attack,attack_positions,all_black)
            Queen42b_attack.attack_class1("q1b",q42b,white_check,attack,attack_positions,all_black)
            Queen42b_attack.all_black_class1("q1b",q42b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen42b_attack.attack_positions
            attack=Queen42b_attack.attack

            Queen43b_attack=attack_class_and_all_black("q1b",q43b,white_check,attack,attack_positions,all_black)
            Queen43b_attack.attack_class1("q1b",q43b,white_check,attack,attack_positions,all_black)
            Queen43b_attack.all_black_class1("q1b",q43b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen43b_attack.attack_positions
            attack=Queen43b_attack.attack
            
            Queen44b_attack=attack_class_and_all_black("q1b",q44b,white_check,attack,attack_positions,all_black)
            Queen44b_attack.attack_class1("q1b",q44b,white_check,attack,attack_positions,all_black)
            Queen44b_attack.all_black_class1("q1b",q44b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen44b_attack.attack_positions
            attack=Queen44b_attack.attack

            Queen45b_attack=attack_class_and_all_black("q1b",q45b,white_check,attack,attack_positions,all_black)
            Queen45b_attack.attack_class1("q1b",q45b,white_check,attack,attack_positions,all_black)
            Queen45b_attack.all_black_class1("q1b",q45b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen45b_attack.attack_positions
            attack=Queen45b_attack.attack
            
            Queen46b_attack=attack_class_and_all_black("q1b",q46b,white_check,attack,attack_positions,all_black)
            Queen46b_attack.attack_class1("q1b",q46b,white_check,attack,attack_positions,all_black)
            Queen46b_attack.all_black_class1("q1b",q46b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen46b_attack.attack_positions
            attack=Queen46b_attack.attack
            
            Queen47b_attack=attack_class_and_all_black("q1b",q47b,white_check,attack,attack_positions,all_black)
            Queen47b_attack.attack_class1("q1b",q47b,white_check,attack,attack_positions,all_black)
            Queen47b_attack.all_black_class1("q1b",q47b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen47b_attack.attack_positions
            attack=Queen47b_attack.attack
            
            Queen48b_attack=attack_class_and_all_black("q1b",q48b,white_check,attack,attack_positions,all_black)
            Queen48b_attack.attack_class1("q1b",q48b,white_check,attack,attack_positions,all_black)
            Queen48b_attack.all_black_class1("q1b",q48b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen48b_attack.attack_positions
            attack=Queen48b_attack.attack
            
            for ju in range (0,len(kn1b)):
                if xposition==kn1b[ju][0] and yposition==kn1b[ju][1]:
                    attack.append(["kn1b"])
            for ju in range (0,len(kn2b)):
                if xposition==kn2b[ju][0] and yposition==kn2b[ju][1]:
                    attack.append(["kn2b"])
            for ju in range (0,len(kn3b)):
                if xposition==kn3b[ju][0] and yposition==kn3b[ju][1]:
                    attack.append(["kn3b"])
            for ju in range (0,len(kn4b)):
                if xposition==kn4b[ju][0] and yposition==kn4b[ju][1]:
                    attack.append(["kn4b"])
            for ju in range (0,len(kn5b)):
                if xposition==kn5b[ju][0] and yposition==kn5b[ju][1]:
                    attack.append(["kn5b"])
            for ju in range (0,len(p1b)):
                if xposition==p1b[ju][0] and yposition==p1b[ju][1]:
                    attack.append(["p1b"])
            for ju in range (0,len(p2b)):
                if xposition==p2b[ju][0] and yposition==p2b[ju][1]:
                    attack.append(["p2b"])
            for ju in range (0,len(p3b)):
                if xposition==p3b[ju][0] and yposition==p3b[ju][1]:
                    attack.append(["p3b"])
            for ju in range (0,len(p4b)):
                if xposition==p4b[ju][0] and yposition==p4b[ju][1]:
                    attack.append(["p4b"])
            for ju in range (0,len(p5b)):
                if xposition==p5b[ju][0] and yposition==p5b[ju][1]:
                    attack.append(["p5b"])
            for ju in range (0,len(p6b)):
                if xposition==p6b[ju][0] and yposition==p6b[ju][1]:
                    attack.append(["p6b"])
            for ju in range (0,len(p7b)):
                if xposition==p7b[ju][0] and yposition==p7b[ju][1]:
                    attack.append(["p7b"])
            for ju in range (0,len(p8b)):               
                if xposition==p8b[ju][0] and yposition==p8b[ju][1]:
                    attack.append(["p8b"])
                    
            if attack!=[]:
                white_check=True
                
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
            for i in range (0,len(k1w)):
                if k1w!=[]:
                    all_black.append(k1w[i])
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
        white_checkmate=False
        coords_backup=coords
        coords_backup2=coords2
        if moves==0:
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition
            coords=[]
            coords2=[]
            King1w2=king1(k1w,"k1w","b","w")
            King1w2.check(k1w,"k1w","b","w")
            vc="k1w"
            King1w=kingw(coords,coords2,kn1wmx,kn1wmy,"k1w","b")
            King1w.possible_moves(coords,coords2,"b")
            if white_check==False and all_white==k1w and coords==[]:
                white_stalemate=True
            if white_check==True and coords==[]:
                Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                vc="b1w"
                Bishop1w.possible_moves(coords,coords2,"b")
                Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                vc="b2w"
                Bishop2w.possible_moves(coords,coords2,"b")
                Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                vc="b3w"
                Bishop3w.possible_moves(coords,coords2,"b")
                Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                vc="b4w"
                Bishop4w.possible_moves(coords,coords2,"b")
                Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                vc="b5w"
                Bishop5w.possible_moves(coords,coords2,"b")
                vc="r1w"
                Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                Rook1w.possible_moves(coords,coords2,"b")
                vc="r2w"
                Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                Rook2w.possible_moves(coords,coords2,"b")
                vc="r3w"
                Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                Rook3w.possible_moves(coords,coords2,"b")
                vc="r4w"
                Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                Rook4w.possible_moves(coords,coords2,"b")
                vc="r5w"
                Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                Rook5w.possible_moves(coords,coords2,"b")
                vc="kn1w"
                Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                Knight1w.possible_moves(coords,coords2,"b")
                vc="kn2w"
                Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                Knight2w.possible_moves(coords,coords2,"b")
                vc="kn3w"
                Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                Knight3w.possible_moves(coords,coords2,"b")
                vc="kn4w"
                Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                Knight4w.possible_moves(coords,coords2,"b")
                vc="kn5w"
                Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                Knight5w.possible_moves(coords,coords2,"b")
                vc="q1w"
                Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                Queen1w.possible_moves(coords,coords2,"b")
                vc="q2w"
                Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                Queen2w.possible_moves(coords,coords2,"b")
                vc="q3w"
                Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                Queen3w.possible_moves(coords,coords2,"b")
                vc="q4w"
                Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                Queen4w.possible_moves(coords,coords2,"b")
                vc="p1w"
                Pawn1w11=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                Pawn1w11.possible_moves(coords,coords2,"b",moves21)
                vc="p2w"
                Pawn2w11=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                Pawn2w11.possible_moves(coords,coords2,"b",moves22)
                vc="p3w"
                Pawn3w11=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                Pawn3w11.possible_moves(coords,coords2,"b",moves23)
                vc="p4w"
                Pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                Pawn4w.possible_moves(coords,coords2,"b",moves24)
                vc="p5w"
                Pawn5w11=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                Pawn5w11.possible_moves(coords,coords2,"b",moves25)
                vc="p6w"
                Pawn6w11=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                Pawn6w11.possible_moves(coords,coords2,"b",moves26)
                vc="p7w"
                Pawn7w11=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                Pawn7w11.possible_moves(coords,coords2,"b",moves27)
                vc="p8w"
                Pawn8w11=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                Pawn8w11.possible_moves(coords,coords2,"b",moves28)
                if coords==[]:
                    white_checkmate=True
            coords=[]
            coords2=[]
        num_of_pieces=0
        for i in range(0,8):
            for a in range(0,8):
                if Board[i][a][0]!="":
                    num_of_pieces=num_of_pieces+1
        if num_of_pieces==2:
            black_stalemate=True
        black_stalemate=False
        black_checkmate=False
        if moves==1:
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition    
            coords=[]
            coords2=[]
            King1b2=king1(k1b,"k1b","w","b")
            King1b2.check(k1b,"k1b","w","b")
            vc="k1b"
            King1b=kingw(coords,coords2,kn1bmx,kn1bmy,"k1b","w")
            King1b.possible_moves(coords,coords2,"w")
            if black_check==False and all_black==k1b and coords==[]:
                black_stalemate=True
            if black_check==True and coords==[]:
                Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                vc="b1b"
                Bishop1b.possible_moves(coords,coords2,"w")
                Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
                vc="b2b"
                Bishop2b.possible_moves(coords,coords2,"w")
                Bishop3b=bishopw(coords,coords2,b3bmx,b3bmy,"b3b","w")
                vc="b3b"
                Bishop3b.possible_moves(coords,coords2,"w")
                Bishop4b=bishopw(coords,coords2,b4bmx,b4bmy,"b4b","w")
                vc="b4b"
                Bishop4b.possible_moves(coords,coords2,"w")
                Bishop5b=bishopw(coords,coords2,b5bmx,b5bmy,"b5b","w")
                vc="b5b"
                Bishop5b.possible_moves(coords,coords2,"w")
                vc="r1b"
                Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                Rook1b.possible_moves(coords,coords2,"w")
                vc="r2b"
                Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                Rook2b.possible_moves(coords,coords2,"w")
                print(coords,"jjjjjjjjjjjjjjjjjjjjjjjjjjj")
                vc="r3b"
                Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                Rook3b.possible_moves(coords,coords2,"w")
                vc="r4b"
                Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                Rook4b.possible_moves(coords,coords2,"w")
                vc="r5b"
                Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                Rook5b.possible_moves(coords,coords2,"w")
                vc="kn1b"
                Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                Knight1b.possible_moves(coords,coords2,"w")
                vc="kn2b"
                Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                Knight2b.possible_moves(coords,coords2,"w")
                vc="kn3b"
                Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                Knight3b.possible_moves(coords,coords2,"w")
                vc="kn4b"
                Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                Knight4b.possible_moves(coords,coords2,"w")
                vc="kn5b"
                Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                Knight5b.possible_moves(coords,coords2,"w")
                vc="q1b"
                Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                Queen1b.possible_moves(coords,coords2,"w")
                vc="q2b"
                Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                Queen2b.possible_moves(coords,coords2,"w")
                vc="q3b"
                Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                Queen3b.possible_moves(coords,coords2,"w")
                vc="q4b"
                Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                Queen4b.possible_moves(coords,coords2,"w")
                vc="p1b"
                Pawn1b11=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                Pawn1b11.possible_moves(coords,coords2,"w",moves21b)
                vc="p2b"
                Pawn2b11=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                Pawn2b11.possible_moves(coords,coords2,"w",moves22b)
                vc="p3b"
                Pawn3b11=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                Pawn3b11.possible_moves(coords,coords2,"w",moves23b)
                vc="p4b"
                Pawn4b11=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                Pawn4b11.possible_moves(coords,coords2,"w",moves24b)
                vc="p5b"
                Pawn5b11=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                Pawn5b11.possible_moves(coords,coords2,"w",moves25b)
                vc="p6b"
                Pawn6b11=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                Pawn6b11.possible_moves(coords,coords2,"w",moves26b)
                vc="p7b"
                Pawn7b11=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                Pawn7b11.possible_moves(coords,coords2,"w",moves27b)
                vc="p8b"
                Pawn8b11=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                Pawn8b11.possible_moves(coords,coords2,"w",moves28b)
                if coords==[]:
                    black_checkmate=True
            coords=[]
            coords2=[]
        coords=coords_backup
        coords2=coords_backup2
        if Check_screen==True:
            black_checkmate=False
            white_checkmate=False
            black_stalemate=False
            white_stalemate=False
        if black_checkmate==True or white_checkmate==True or black_stalemate==True or white_stalemate==True:
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            if black_stalemate==True or white_stalemate==True:
                gameDisplay.blit(stalemate,(127,128))
            else:
                gameDisplay.blit(checkmate,(17,173))
            pygame.display.update()
            pygame.time.delay(1000)
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)                    
            pygame.display.update()
            pygame.time.delay(500)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    Check_screen==True
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
                    bo1mx,bo1my=b1wmx,b1wmy
                    vc="b1w"
                    b1wmx,b1wmy=pygame.mouse.get_pos()
                    if b1wmx>list_searchx(Board,"b1w")*60 and b1wmx<list_searchx(Board,"b1w")*60+60 and b1wmy>list_searchy(Board,"b1w")*60 and b1wmy<list_searchy(Board,"b1w")*60+60:
                        piece="bishop1"
                        Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                        Bishop1w.possible_moves(coords,coords2,"b")
                    else:
                        b1wmx,b1wmy=bo1mx,bo1my
                    bo2mx,bo2my=b2wmx,b2wmy
                    vc="b2w"
                    b2wmx,b2wmy=pygame.mouse.get_pos()
                    if b2wmx>list_searchx(Board,"b2w")*60 and b2wmx<list_searchx(Board,"b2w")*60+60 and b2wmy>list_searchy(Board,"b2w")*60 and b2wmy<list_searchy(Board,"b2w")*60+60:
                        piece="bishop2"
                        Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                        Bishop2w.possible_moves(coords,coords2,"b")
                    else:
                        b2wmx,b2wmy=bo2mx,bo2my 
                    bo3mx,bo3my=b3wmx,b3wmy
                    vc="b3w"
                    b3wmx,b3wmy=pygame.mouse.get_pos()
                    if b3wmx>list_searchx(Board,"b3w")*60 and b3wmx<list_searchx(Board,"b3w")*60+60 and b3wmy>list_searchy(Board,"b3w")*60 and b3wmy<list_searchy(Board,"b3w")*60+60:
                        piece="bishop3"
                        Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                        Bishop3w.possible_moves(coords,coords2,"b")
                    else:
                        b3wmx,b3wmy=bo3mx,bo3my
                    bo4mx,bo4my=b4wmx,b4wmy
                    vc="b4w"
                    b4wmx,b4wmy=pygame.mouse.get_pos()
                    if b4wmx>list_searchx(Board,"b4w")*60 and b4wmx<list_searchx(Board,"b4w")*60+60 and b4wmy>list_searchy(Board,"b4w")*60 and b4wmy<list_searchy(Board,"b4w")*60+60:
                        piece="bishop4"
                        Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                        Bishop4w.possible_moves(coords,coords2,"b")
                    else:
                        b4wmx,b4wmy=bo4mx,bo4my
                    bo5mx,bo5my=b5wmx,b5wmy
                    vc="b5w"
                    b5wmx,b5wmy=pygame.mouse.get_pos()
                    if b5wmx>list_searchx(Board,"b5w")*60 and b5wmx<list_searchx(Board,"b5w")*60+60 and b5wmy>list_searchy(Board,"b5w")*60 and b5wmy<list_searchy(Board,"b5w")*60+60:
                        piece="bishop5"
                        Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                        Bishop5w.possible_moves(coords,coords2,"b")
                    else:
                        b5wmx,b5wmy=bo5mx,bo5my                        
                    kno1mx,kno1my=kn1wmx,kn1wmy
                    vc="kn1w"
                    kn1wmx,kn1wmy=pygame.mouse.get_pos()
                    if kn1wmx>list_searchx(Board,"kn1w")*60 and kn1wmx<list_searchx(Board,"kn1w")*60+60 and kn1wmy>list_searchy(Board,"kn1w")*60 and kn1wmy<list_searchy(Board,"kn1w")*60+60:
                        piece="knight1"
                        Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                        Knight1w.possible_moves(coords,coords2,"b")
                    else:
                        kn1wmx,kn1wmy=kno1mx,kno1my
                    kno2mx,kno2my=kn2wmx,kn2wmy
                    vc="kn2w"
                    kn2wmx,kn2wmy=pygame.mouse.get_pos()
                    if kn2wmx>list_searchx(Board,"kn2w")*60 and kn2wmx<list_searchx(Board,"kn2w")*60+60 and kn2wmy>list_searchy(Board,"kn2w")*60 and kn2wmy<list_searchy(Board,"kn2w")*60+60:
                        piece="knight2"
                        Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                        Knight2w.possible_moves(coords,coords2,"b")
                    else:
                        kn2wmx,kn2wmy=kno2mx,kno2my                        
                    kno3mx,kno3my=kn3wmx,kn3wmy
                    vc="kn3w"
                    kn3wmx,kn3wmy=pygame.mouse.get_pos()
                    if kn3wmx>list_searchx(Board,"kn3w")*60 and kn3wmx<list_searchx(Board,"kn3w")*60+60 and kn3wmy>list_searchy(Board,"kn3w")*60 and kn3wmy<list_searchy(Board,"kn3w")*60+60:
                        piece="knight3"
                        Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                        Knight3w.possible_moves(coords,coords2,"b")
                    else:
                        kn3wmx,kn3wmy=kno3mx,kno3my
                    kno4mx,kno4my=kn4wmx,kn4wmy
                    vc="kn4w"
                    kn4wmx,kn4wmy=pygame.mouse.get_pos()
                    if kn4wmx>list_searchx(Board,"kn4w")*60 and kn4wmx<list_searchx(Board,"kn4w")*60+60 and kn4wmy>list_searchy(Board,"kn4w")*60 and kn4wmy<list_searchy(Board,"kn4w")*60+60:
                        piece="knight4"
                        Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                        Knight4w.possible_moves(coords,coords2,"b")
                    else:
                        kn4wmx,kn4wmy=kno4mx,kno4my 
                    kno5mx,kno5my=kn5wmx,kn5wmy
                    vc="kn5w"
                    kn5wmx,kn5wmy=pygame.mouse.get_pos()
                    if kn5wmx>list_searchx(Board,"kn5w")*60 and kn5wmx<list_searchx(Board,"kn5w")*60+60 and kn5wmy>list_searchy(Board,"kn5w")*60 and kn5wmy<list_searchy(Board,"kn5w")*60+60:
                        piece="knight5"
                        Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                        Knight5w.possible_moves(coords,coords2,"b")
                    else:
                        kn5wmx,kn5wmy=kno5mx,kno5my
                    ro1mx,ro1my=r1wmx,r1wmy
                    vc="r1w"
                    r1wmx,r1wmy=pygame.mouse.get_pos()
                    if r1wmx>list_searchx(Board,"r1w")*60 and r1wmx<list_searchx(Board,"r1w")*60+60 and r1wmy>list_searchy(Board,"r1w")*60 and r1wmy<list_searchy(Board,"r1w")*60+60:
                        piece="rook1"
                        Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                        Rook1w.possible_moves(coords,coords2,"b")
                    else:
                        r1wmx,r1wmy=ro1mx,ro1my
                    ro2mx,ro2my=r2wmx,r2wmy
                    vc="r2w"
                    r2wmx,r2wmy=pygame.mouse.get_pos()
                    if r2wmx>list_searchx(Board,"r2w")*60 and r2wmx<list_searchx(Board,"r2w")*60+60 and r2wmy>list_searchy(Board,"r2w")*60 and r2wmy<list_searchy(Board,"r2w")*60+60:
                        piece="rook2"
                        Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                        Rook2w.possible_moves(coords,coords2,"b")
                    else:
                        r2wmx,r2wmy=ro2mx,ro2my                        
                    ro3mx,ro3my=r3wmx,r3wmy
                    vc="r3w"
                    r3wmx,r3wmy=pygame.mouse.get_pos()
                    if r3wmx>list_searchx(Board,"r3w")*60 and r3wmx<list_searchx(Board,"r3w")*60+60 and r3wmy>list_searchy(Board,"r3w")*60 and r3wmy<list_searchy(Board,"r3w")*60+60:
                        piece="rook3"
                        Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                        Rook3w.possible_moves(coords,coords2,"b")
                    else:
                        r3wmx,r3wmy=ro3mx,ro3my
                    ro4mx,ro4my=r4wmx,r4wmy
                    vc="r4w"
                    r4wmx,r4wmy=pygame.mouse.get_pos()
                    if r4wmx>list_searchx(Board,"r4w")*60 and r4wmx<list_searchx(Board,"r4w")*60+60 and r4wmy>list_searchy(Board,"r4w")*60 and r4wmy<list_searchy(Board,"r4w")*60+60:
                        piece="rook4"
                        Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                        Rook4w.possible_moves(coords,coords2,"b")
                    else:
                        r4wmx,r4wmy=ro4mx,ro4my 
                    ro5mx,ro5my=r5wmx,r5wmy
                    vc="r5w"
                    r5wmx,r5wmy=pygame.mouse.get_pos()
                    if r5wmx>list_searchx(Board,"r5w")*60 and r5wmx<list_searchx(Board,"r5w")*60+60 and r5wmy>list_searchy(Board,"r5w")*60 and r5wmy<list_searchy(Board,"r5w")*60+60:
                        piece="rook5"
                        Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                        Rook5w.possible_moves(coords,coords2,"b")
                    else:
                        r5wmx,r5wmy=ro5mx,ro5my
                    qo1mx,qo1my=q1wmx,q1wmy
                    vc="q1w"
                    q1wmx,q1wmy=pygame.mouse.get_pos()
                    if q1wmx>list_searchx(Board,"q1w")*60 and q1wmx<list_searchx(Board,"q1w")*60+60 and q1wmy>list_searchy(Board,"q1w")*60 and q1wmy<list_searchy(Board,"q1w")*60+60:
                        piece="queen1"
                        Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                        Queen1w.possible_moves(coords,coords2,"b")
                    else:
                        q1wmx,q1wmy=qo1mx,qo1my
                    qo2mx,qo2my=q2wmx,q2wmy
                    vc="q2w"
                    q2wmx,q2wmy=pygame.mouse.get_pos()
                    if q2wmx>list_searchx(Board,"q2w")*60 and q2wmx<list_searchx(Board,"q2w")*60+60 and q2wmy>list_searchy(Board,"q2w")*60 and q2wmy<list_searchy(Board,"q2w")*60+60:
                        piece="queen2"
                        Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                        Queen2w.possible_moves(coords,coords2,"b")
                    else:
                        q2wmx,q2wmy=qo2mx,qo2my                        
                    qo3mx,qo3my=q3wmx,q3wmy
                    vc="q3w"
                    q3wmx,q3wmy=pygame.mouse.get_pos()
                    if q3wmx>list_searchx(Board,"q3w")*60 and q3wmx<list_searchx(Board,"q3w")*60+60 and q3wmy>list_searchy(Board,"q3w")*60 and q3wmy<list_searchy(Board,"q3w")*60+60:
                        piece="queen3"
                        Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                        Queen3w.possible_moves(coords,coords2,"b")
                    else:
                        q3wmx,q3wmy=qo3mx,qo3my
                    qo4mx,qo4my=q4wmx,q4wmy
                    vc="q4w"
                    q4wmx,q4wmy=pygame.mouse.get_pos()
                    if q4wmx>list_searchx(Board,"q4w")*60 and q4wmx<list_searchx(Board,"q4w")*60+60 and q4wmy>list_searchy(Board,"q4w")*60 and q4wmy<list_searchy(Board,"q4w")*60+60:
                        piece="queen4"
                        Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                        Queen4w.possible_moves(coords,coords2,"b")
                    else:
                        q4wmx,q4wmy=qo4mx,qo4my 
                    po1mx,po1my=p1wmx,p1wmy
                    vc="p1w"
                    p1wmx,p1wmy=pygame.mouse.get_pos()
                    if p1wmx>list_searchx(Board,"p1w")*60 and p1wmx<list_searchx(Board,"p1w")*60+60 and p1wmy>list_searchy(Board,"p1w")*60 and p1wmy<list_searchy(Board,"p1w")*60+60:
                        piece="pawn1"
                        Pawn1w=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                        Pawn1w.possible_moves(coords,coords2,"b",moves21)
                    else:
                        p1wmx,p1wmy=po1mx,po1my
                    po2mx,po2my=p2wmx,p2wmy
                    vc="p2w"
                    p2wmx,p2wmy=pygame.mouse.get_pos()
                    if p2wmx>list_searchx(Board,"p2w")*60 and p2wmx<list_searchx(Board,"p2w")*60+60 and p2wmy>list_searchy(Board,"p2w")*60 and p2wmy<list_searchy(Board,"p2w")*60+60:
                        piece="pawn2"
                        Pawn2w=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                        Pawn2w.possible_moves(coords,coords2,"b",moves22)
                    else:
                        p2wmx,p2wmy=po2mx,po2my                        
                    po3mx,po3my=p3wmx,p3wmy
                    vc="p3w"
                    p3wmx,p3wmy=pygame.mouse.get_pos()
                    if p3wmx>list_searchx(Board,"p3w")*60 and p3wmx<list_searchx(Board,"p3w")*60+60 and p3wmy>list_searchy(Board,"p3w")*60 and p3wmy<list_searchy(Board,"p3w")*60+60:
                        piece="pawn3"
                        Pawn3w=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                        Pawn3w.possible_moves(coords,coords2,"b",moves23)
                    else:
                        p3wmx,p3wmy=po3mx,po3my
                    po4mx,po4my=p4wmx,p4wmy
                    vc="p4w"
                    p4wmx,p4wmy=pygame.mouse.get_pos()
                    if p4wmx>list_searchx(Board,"p4w")*60 and p4wmx<list_searchx(Board,"p4w")*60+60 and p4wmy>list_searchy(Board,"p4w")*60 and p4wmy<list_searchy(Board,"p4w")*60+60:
                        piece="pawn4"
                        Pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                        Pawn4w.possible_moves(coords,coords2,"b",moves24)
                    else:
                        p4wmx,p4wmy=po4mx,po4my
                    po5mx,po5my=p5wmx,p5wmy
                    vc="p5w"
                    p5wmx,p5wmy=pygame.mouse.get_pos()
                    if p5wmx>list_searchx(Board,"p5w")*60 and p5wmx<list_searchx(Board,"p5w")*60+60 and p5wmy>list_searchy(Board,"p5w")*60 and p5wmy<list_searchy(Board,"p5w")*60+60:
                        piece="pawn5"
                        Pawn5w=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                        Pawn5w.possible_moves(coords,coords2,"b",moves25)
                    else:
                        p5wmx,p5wmy=po5mx,po5my
                    po6mx,po6my=p6wmx,p6wmy
                    vc="p6w"
                    p6wmx,p6wmy=pygame.mouse.get_pos()
                    if p6wmx>list_searchx(Board,"p6w")*60 and p6wmx<list_searchx(Board,"p6w")*60+60 and p6wmy>list_searchy(Board,"p6w")*60 and p6wmy<list_searchy(Board,"p6w")*60+60:
                        piece="pawn6"
                        Pawn6w=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                        Pawn6w.possible_moves(coords,coords2,"b",moves26)
                    else:
                        p6wmx,p6wmy=po6mx,po6my
                    po7mx,po7my=p7wmx,p7wmy
                    vc="p7w"
                    p7wmx,p7wmy=pygame.mouse.get_pos()
                    if p7wmx>list_searchx(Board,"p7w")*60 and p7wmx<list_searchx(Board,"p7w")*60+60 and p7wmy>list_searchy(Board,"p7w")*60 and p7wmy<list_searchy(Board,"p7w")*60+60:
                        piece="pawn7"
                        Pawn7w=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                        Pawn7w.possible_moves(coords,coords2,"b",moves27)
                    else:
                        p7wmx,p7wmy=po7mx,po7my
                    po8mx,po8my=p8wmx,p8wmy
                    vc="p8w"
                    p8wmx,p8wmy=pygame.mouse.get_pos()
                    if p8wmx>list_searchx(Board,"p8w")*60 and p8wmx<list_searchx(Board,"p8w")*60+60 and p8wmy>list_searchy(Board,"p8w")*60 and p8wmy<list_searchy(Board,"p8w")*60+60:
                        piece="pawn8"
                        Pawn8w=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                        Pawn8w.possible_moves(coords,coords2,"b",moves28)
                    else:
                        p8wmx,p8wmy=po8mx,po8my
                    ko1mx,ko1my=k1wmx,k1wmy
                    vc="k1w"
                    k1wmx,k1wmy=pygame.mouse.get_pos()
                    if k1wmx>list_searchx(Board,"k1w")*60 and k1wmx<list_searchx(Board,"k1w")*60+60 and k1wmy>list_searchy(Board,"k1w")*60 and k1wmy<list_searchy(Board,"k1w")*60+60:
                        piece="king1"
                        King1w=kingw(coords,coords2,k1wmx,k1wmy,"k1w","b")
                        King1w.possible_moves(coords,coords2,"b")
                    else:
                        k1wmx,k1wmy=ko1mx,ko1my            
            if piece=="bishop1":
                b1wmx,b1wmy=pygame.mouse.get_pos()
                tg=Bishop1w.position(coords,coords2,convertx(b1wmx),converty(b1wmy),"b1w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b1wmx,b1wmy=[],[],"",1,(list_searchx(Board,"b1w"))*60,(list_searchy(Board,"b1w"))*60
            if piece=="bishop2":
                b2wmx,b2wmy=pygame.mouse.get_pos()
                tg=Bishop2w.position(coords,coords2,convertx(b2wmx),converty(b2wmy),"b2w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b2wmx,b2wmy=[],[],"",1,(list_searchx(Board,"b2w"))*60,(list_searchy(Board,"b2w"))*60
            if piece=="bishop3":
                b3wmx,b3wmy=pygame.mouse.get_pos()
                tg=Bishop3w.position(coords,coords2,convertx(b3wmx),converty(b3wmy),"b3w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b3wmx,b3wmy=[],[],"",1,(list_searchx(Board,"b3w"))*60,(list_searchy(Board,"b3w"))*60
            if piece=="bishop4":
                b4wmx,b4wmy=pygame.mouse.get_pos()
                tg=Bishop4w.position(coords,coords2,convertx(b4wmx),converty(b4wmy),"b4w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b4wmx,b4wmy=[],[],"",1,(list_searchx(Board,"b4w"))*60,(list_searchy(Board,"b4w"))*60
            if piece=="bishop5":
                b5wmx,b5wmy=pygame.mouse.get_pos()
                tg=Bishop5w.position(coords,coords2,convertx(b5wmx),converty(b5wmy),"b5w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b5wmx,b5wmy=[],[],"",1,(list_searchx(Board,"b5w"))*60,(list_searchy(Board,"b5w"))*60
                    
            if piece=="knight1":
                kn1wmx,kn1wmy=pygame.mouse.get_pos()
                tg=Knight1w.position(coords,coords2,convertx(kn1wmx),converty(kn1wmy),"kn1w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn1wmx,kn1wmy=[],[],"",1,(list_searchx(Board,"kn1w"))*60,(list_searchy(Board,"kn1w"))*60
            if piece=="knight2":
                kn2wmx,kn2wmy=pygame.mouse.get_pos()
                tg=Knight2w.position(coords,coords2,convertx(kn2wmx),converty(kn2wmy),"kn2w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn2wmx,kn2wmy=[],[],"",1,(list_searchx(Board,"kn2w"))*60,(list_searchy(Board,"kn2w"))*60
            if piece=="knight3":
                kn3wmx,kn3wmy=pygame.mouse.get_pos()
                tg=Knight3w.position(coords,coords2,convertx(kn3wmx),converty(kn3wmy),"kn3w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn3wmx,kn3wmy=[],[],"",1,(list_searchx(Board,"kn3w"))*60,(list_searchy(Board,"kn3w"))*60
            if piece=="knight4":
                kn4wmx,kn4wmy=pygame.mouse.get_pos()
                tg=Knight4w.position(coords,coords2,convertx(kn4wmx),converty(kn4wmy),"kn4w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==1 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn4wmx,kn4wmy=[],[],"",1,(list_searchx(Board,"kn4w"))*60,(list_searchy(Board,"kn4w"))*60
            if piece=="knight5":
                kn5wmx,kn5wmy=pygame.mouse.get_pos()
                tg=Knight5w.position(coords,coords2,convertx(kn5wmx),converty(kn5wmy),"kn5w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==1 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn5wmx,kn5wmy=[],[],"",1,(list_searchx(Board,"kn5w"))*60,(list_searchy(Board,"kn5w"))*60

            if piece=="rook1":
                r1wmx,r1wmy=pygame.mouse.get_pos()
                tg=Rook1w.position(coords,coords2,convertx(r1wmx),converty(r1wmy),"r1w")                    
                if tg==2:
                    hb,white_check,moves,moves2r1w=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r1wmx,r1wmy=[],[],"",1,(list_searchx(Board,"r1w"))*60,(list_searchy(Board,"r1w"))*60
            if piece=="rook2":
                r2wmx,r2wmy=pygame.mouse.get_pos()
                tg=Rook2w.position(coords,coords2,convertx(r2wmx),converty(r2wmy),"r2w")                    
                if tg==2:
                    hb,white_check,moves,moves2r2w=0,False,moves+1,1

                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r2wmx,r2wmy=[],[],"",1,(list_searchx(Board,"r2w"))*60,(list_searchy(Board,"r2w"))*60
            if piece=="rook3":
                r3wmx,r3wmy=pygame.mouse.get_pos()
                tg=Rook3w.position(coords,coords2,convertx(r3wmx),converty(r3wmy),"r3w")                    
                if tg==2:
                    hb,white_check,moves,moves2r3w=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r3wmx,r3wmy=[],[],"",1,(list_searchx(Board,"r3w"))*60,(list_searchy(Board,"r3w"))*60
            if piece=="rook4":
                r4wmx,r4wmy=pygame.mouse.get_pos()
                tg=Rook4w.position(coords,coords2,convertx(r4wmx),converty(r4wmy),"r4w")                    
                if tg==2:
                    hb,white_check,moves,moves2r4w=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r4wmx,r4wmy=[],[],"",1,(list_searchx(Board,"r4w"))*60,(list_searchy(Board,"r4w"))*60
            if piece=="rook5":
                r5wmx,r5wmy=pygame.mouse.get_pos()
                tg=Rook5w.position(coords,coords2,convertx(r5wmx),converty(r5wmy),"r5w")                    
                if tg==2:
                    hb,white_check,moves,moves2r5w=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r5wmx,r5wmy=[],[],"",1,(list_searchx(Board,"r5w"))*60,(list_searchy(Board,"r5w"))*60

            if piece=="queen1":
                q1wmx,q1wmy=pygame.mouse.get_pos()
                tg=Queen1w.position(coords,coords2,convertx(q1wmx),converty(q1wmy),"q1w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q1wmx,q1wmy=[],[],"",1,(list_searchx(Board,"q1w"))*60,(list_searchy(Board,"q1w"))*60
            if piece=="queen2":
                q2wmx,q2wmy=pygame.mouse.get_pos()
                tg=Queen2w.position(coords,coords2,convertx(q2wmx),converty(q2wmy),"q2w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q2wmx,q2wmy=[],[],"",1,(list_searchx(Board,"q2w"))*60,(list_searchy(Board,"q2w"))*60
            if piece=="queen3":
                q3wmx,q3wmy=pygame.mouse.get_pos()
                tg=Queen3w.position(coords,coords2,convertx(q3wmx),converty(q3wmy),"q3w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q3wmx,q3wmy=[],[],"",1,(list_searchx(Board,"q3w"))*60,(list_searchy(Board,"q3w"))*60
            if piece=="queen4":
                q4wmx,q4wmy=pygame.mouse.get_pos()
                tg=Queen4w.position(coords,coords2,convertx(q4wmx),converty(q4wmy),"q4w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q4wmx,q4wmy=[],[],"",1,(list_searchx(Board,"q4w"))*60,(list_searchy(Board,"q4w"))*60

            if piece=="pawn1":
                p1wmx,p1wmy=pygame.mouse.get_pos()
                tg=Pawn1w.position(coords,coords2,convertx(p1wmx),converty(p1wmy),"p1w")                    
                if tg==2:
                    hb,white_check,moves,moves21=0,False,moves+1,moves21+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p1wmx,p1wmy=[],[],"",1,(list_searchx(Board,"p1w"))*60,(list_searchy(Board,"p1w"))*60
            if piece=="pawn2":
                p2wmx,p2wmy=pygame.mouse.get_pos()
                tg=Pawn2w.position(coords,coords2,convertx(p2wmx),converty(p2wmy),"p2w")                    
                if tg==2:
                    hb,white_check,moves,moves22=0,False,moves+1,moves22+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p2wmx,p2wmy=[],[],"",1,(list_searchx(Board,"p2w"))*60,(list_searchy(Board,"p2w"))*60
            if piece=="pawn3":
                p3wmx,p3wmy=pygame.mouse.get_pos()
                tg=Pawn3w.position(coords,coords2,convertx(p3wmx),converty(p3wmy),"p3w")                    
                if tg==2:
                    hb,white_check,moves,moves23=0,False,moves+1,moves23+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p3wmx,p3wmy=[],[],"",1,(list_searchx(Board,"p3w"))*60,(list_searchy(Board,"p3w"))*60
            if piece=="pawn4":
                p4wmx,p4wmy=pygame.mouse.get_pos()
                tg=Pawn4w.position(coords,coords2,convertx(p4wmx),converty(p4wmy),"p4w")                    
                if tg==2:
                    hb,white_check,moves,moves24=0,False,moves+1,moves24+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p4wmx,p4wmy=[],[],"",1,(list_searchx(Board,"p4w"))*60,(list_searchy(Board,"p4w"))*60
            if piece=="pawn5":
                p5wmx,p5wmy=pygame.mouse.get_pos()
                tg=Pawn5w.position(coords,coords2,convertx(p5wmx),converty(p5wmy),"p5w")                    
                if tg==2:
                    hb,white_check,moves,moves25=0,False,moves+1,moves25+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p5wmx,p5wmy=[],[],"",1,(list_searchx(Board,"p5w"))*60,(list_searchy(Board,"p5w"))*60
            if piece=="pawn6":
                p6wmx,p6wmy=pygame.mouse.get_pos()
                tg=Pawn6w.position(coords,coords2,convertx(p6wmx),converty(p6wmy),"p6w")                    
                if tg==2:
                    hb,white_check,moves,moves26=0,False,moves+1,moves26+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p6wmx,p6wmy=[],[],"",1,(list_searchx(Board,"p6w"))*60,(list_searchy(Board,"p6w"))*60
            if piece=="pawn7":
                p7wmx,p7wmy=pygame.mouse.get_pos()
                tg=Pawn7w.position(coords,coords2,convertx(p7wmx),converty(p7wmy),"p7w")                    
                if tg==2:
                    hb,white_check,moves,moves27=0,False,moves+1,moves27+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p7wmx,p7wmy=[],[],"",1,(list_searchx(Board,"p7w"))*60,(list_searchy(Board,"p7w"))*60
            if piece=="pawn8":
                p8wmx,p8wmy=pygame.mouse.get_pos()
                tg=Pawn8w.position(coords,coords2,convertx(p8wmx),converty(p8wmy),"p8w")                    
                if tg==2:
                    hb,white_check,moves,moves28=0,False,moves+1,moves28+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p8wmx,p8wmy=[],[],"",1,(list_searchx(Board,"p8w"))*60,(list_searchy(Board,"p8w"))*60
            if piece=="king1":
                k1wmx,k1wmy=pygame.mouse.get_pos()
                tg=King1w.position(coords,coords2,convertx(k1wmx),converty(k1wmy),"k1w")                    
                if tg==2:
                    r1wmy=list_searchy(Board,"r1w")*60
                    r1wmx=list_searchx(Board,"r1w")*60
                    r2wmy=list_searchy(Board,"r2w")*60
                    r2wmx=list_searchx(Board,"r2w")*60
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,k1wmx,k1wmy=[],[],"",1,(list_searchx(Board,"k1w"))*60,(list_searchy(Board,"k1w"))*60
#############################################################################
        if moves==1:
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo1mx,bo1my=b1bmx,b1bmy
                    vc="b1b"
                    b1bmx,b1bmy=pygame.mouse.get_pos()
                    if b1bmx>list_searchx(Board,"b1b")*60 and b1bmx<list_searchx(Board,"b1b")*60+60 and b1bmy>list_searchy(Board,"b1b")*60 and b1bmy<list_searchy(Board,"b1b")*60+60:
                        piece="bishop1b"
                        Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                        Bishop1b.possible_moves(coords,coords2,"w")
                    else:
                        b1bmx,b1bmy=bo1mx,bo1my
                    bo2mx,bo2my=b2bmx,b2bmy
                    vc="b2b"
                    b2bmx,b2bmy=pygame.mouse.get_pos()
                    if b2bmx>list_searchx(Board,"b2b")*60 and b2bmx<list_searchx(Board,"b2b")*60+60 and b2bmy>list_searchy(Board,"b2b")*60 and b2bmy<list_searchy(Board,"b2b")*60+60:
                        piece="bishop2b"
                        Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
                        Bishop2b.possible_moves(coords,coords2,"w")
                    else:
                        b2bmx,b2bmy=bo2mx,bo2my 
                    bo3mx,bo3my=b3bmx,b3bmy
                    vc="b3b"
                    b3bmx,b3bmy=pygame.mouse.get_pos()
                    if b3bmx>list_searchx(Board,"b3b")*60 and b3bmx<list_searchx(Board,"b3b")*60+60 and b3bmy>list_searchy(Board,"b3b")*60 and b3bmy<list_searchy(Board,"b3b")*60+60:
                        piece="bishop3b"
                        Bishop3b=bishopw(coords,coords2,b3bmx,b3bmy,"b3b","w")
                        Bishop3b.possible_moves(coords,coords2,"w")
                    else:
                        b3bmx,b3bmy=bo3mx,bo3my
                    bo4mx,bo4my=b4bmx,b4bmy
                    vc="b4b"
                    b4bmx,b4bmy=pygame.mouse.get_pos()
                    if b4bmx>list_searchx(Board,"b4b")*60 and b4bmx<list_searchx(Board,"b4b")*60+60 and b4bmy>list_searchy(Board,"b4b")*60 and b4bmy<list_searchy(Board,"b4b")*60+60:
                        piece="bishop4b"
                        Bishop4b=bishopw(coords,coords2,b4bmx,b4bmy,"b4b","w")
                        Bishop4b.possible_moves(coords,coords2,"w")
                    else:
                        b4bmx,b4bmy=bo4mx,bo4my
                    bo5mx,bo5my=b5bmx,b5bmy
                    vc="b5b"
                    b5bmx,b5bmy=pygame.mouse.get_pos()
                    if b5bmx>list_searchx(Board,"b5b")*60 and b5bmx<list_searchx(Board,"b5b")*60+60 and b5bmy>list_searchy(Board,"b5b")*60 and b5bmy<list_searchy(Board,"b5b")*60+60:
                        piece="bishop5b"
                        Bishop5b=bishopw(coords,coords2,b5bmx,b5bmy,"b5b","w")
                        Bishop5b.possible_moves(coords,coords2,"w")
                    else:
                        b5bmx,b5bmy=bo5mx,bo5my                        
                    kno1mx,kno1my=kn1bmx,kn1bmy
                    vc="kn1b"
                    kn1bmx,kn1bmy=pygame.mouse.get_pos()
                    if kn1bmx>list_searchx(Board,"kn1b")*60 and kn1bmx<list_searchx(Board,"kn1b")*60+60 and kn1bmy>list_searchy(Board,"kn1b")*60 and kn1bmy<list_searchy(Board,"kn1b")*60+60:
                        piece="knight1b"
                        Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                        Knight1b.possible_moves(coords,coords2,"w")
                    else:
                        kn1bmx,kn1bmy=kno1mx,kno1my
                    kno2mx,kno2my=kn2bmx,kn2bmy
                    vc="kn2b"
                    kn2bmx,kn2bmy=pygame.mouse.get_pos()
                    if kn2bmx>list_searchx(Board,"kn2b")*60 and kn2bmx<list_searchx(Board,"kn2b")*60+60 and kn2bmy>list_searchy(Board,"kn2b")*60 and kn2bmy<list_searchy(Board,"kn2b")*60+60:
                        piece="knight2b"
                        Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                        Knight2b.possible_moves(coords,coords2,"w")
                    else:
                        kn2bmx,kn2bmy=kno2mx,kno2my                        
                    kno3mx,kno3my=kn3bmx,kn3bmy
                    vc="kn3b"
                    kn3bmx,kn3bmy=pygame.mouse.get_pos()
                    if kn3bmx>list_searchx(Board,"kn3b")*60 and kn3bmx<list_searchx(Board,"kn3b")*60+60 and kn3bmy>list_searchy(Board,"kn3b")*60 and kn3bmy<list_searchy(Board,"kn3b")*60+60:
                        piece="knight3b"
                        Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                        Knight3b.possible_moves(coords,coords2,"w")
                    else:
                        kn3bmx,kn3bmy=kno3mx,kno3my
                    kno4mx,kno4my=kn4bmx,kn4bmy
                    vc="kn4b"
                    kn4bmx,kn4bmy=pygame.mouse.get_pos()
                    if kn4bmx>list_searchx(Board,"kn4b")*60 and kn4bmx<list_searchx(Board,"kn4b")*60+60 and kn4bmy>list_searchy(Board,"kn4b")*60 and kn4bmy<list_searchy(Board,"kn4b")*60+60:
                        piece="knight4b"
                        Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                        Knight4b.possible_moves(coords,coords2,"w")
                    else:
                        kn4bmx,kn4bmy=kno4mx,kno4my 
                    kno5mx,kno5my=kn5bmx,kn5bmy
                    vc="kn5b"
                    kn5bmx,kn5bmy=pygame.mouse.get_pos()
                    if kn5bmx>list_searchx(Board,"kn5b")*60 and kn5bmx<list_searchx(Board,"kn5b")*60+60 and kn5bmy>list_searchy(Board,"kn5b")*60 and kn5bmy<list_searchy(Board,"kn5b")*60+60:
                        piece="knight5b"
                        Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                        Knight5b.possible_moves(coords,coords2,"w")
                    else:
                        kn5bmx,kn5bmy=kno5mx,kno5my
                    ro1mx,ro1my=r1bmx,r1bmy
                    vc="r1b"
                    r1bmx,r1bmy=pygame.mouse.get_pos()
                    if r1bmx>list_searchx(Board,"r1b")*60 and r1bmx<list_searchx(Board,"r1b")*60+60 and r1bmy>list_searchy(Board,"r1b")*60 and r1bmy<list_searchy(Board,"r1b")*60+60:
                        piece="rook1b"
                        Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                        Rook1b.possible_moves(coords,coords2,"w")
                    else:
                        r1bmx,r1bmy=ro1mx,ro1my
                    ro2mx,ro2my=r2bmx,r2bmy
                    vc="r2b"
                    r2bmx,r2bmy=pygame.mouse.get_pos()
                    if r2bmx>list_searchx(Board,"r2b")*60 and r2bmx<list_searchx(Board,"r2b")*60+60 and r2bmy>list_searchy(Board,"r2b")*60 and r2bmy<list_searchy(Board,"r2b")*60+60:
                        piece="rook2b"
                        Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                        Rook2b.possible_moves(coords,coords2,"w")
                    else:
                        r2bmx,r2bmy=ro2mx,ro2my                        
                    ro3mx,ro3my=r3bmx,r3bmy
                    vc="r3b"
                    r3bmx,r3bmy=pygame.mouse.get_pos()
                    if r3bmx>list_searchx(Board,"r3b")*60 and r3bmx<list_searchx(Board,"r3b")*60+60 and r3bmy>list_searchy(Board,"r3b")*60 and r3bmy<list_searchy(Board,"r3b")*60+60:
                        piece="rook3b"
                        Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                        Rook3b.possible_moves(coords,coords2,"w")
                    else:
                        r3bmx,r3bmy=ro3mx,ro3my
                    ro4mx,ro4my=r4bmx,r4bmy
                    vc="r4b"
                    r4bmx,r4bmy=pygame.mouse.get_pos()
                    if r4bmx>list_searchx(Board,"r4b")*60 and r4bmx<list_searchx(Board,"r4b")*60+60 and r4bmy>list_searchy(Board,"r4b")*60 and r4bmy<list_searchy(Board,"r4b")*60+60:
                        piece="rook4b"
                        Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                        Rook4b.possible_moves(coords,coords2,"w")
                    else:
                        r4bmx,r4bmy=ro4mx,ro4my 
                    ro5mx,ro5my=r5bmx,r5bmy
                    vc="r5b"
                    r5bmx,r5bmy=pygame.mouse.get_pos()
                    if r5bmx>list_searchx(Board,"r5b")*60 and r5bmx<list_searchx(Board,"r5b")*60+60 and r5bmy>list_searchy(Board,"r5b")*60 and r5bmy<list_searchy(Board,"r5b")*60+60:
                        piece="rook5b"
                        Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                        Rook5b.possible_moves(coords,coords2,"w")
                    else:
                        r5bmx,r5bmy=ro5mx,ro5my
                    qo1mx,qo1my=q1bmx,q1bmy
                    vc="q1b"
                    q1bmx,q1bmy=pygame.mouse.get_pos()
                    if q1bmx>list_searchx(Board,"q1b")*60 and q1bmx<list_searchx(Board,"q1b")*60+60 and q1bmy>list_searchy(Board,"q1b")*60 and q1bmy<list_searchy(Board,"q1b")*60+60:
                        piece="queen1b"
                        Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                        Queen1b.possible_moves(coords,coords2,"w")
                    else:
                        q1bmx,q1bmy=qo1mx,qo1my
                    qo2mx,qo2my=q2bmx,q2bmy
                    vc="q2b"
                    q2bmx,q2bmy=pygame.mouse.get_pos()
                    if q2bmx>list_searchx(Board,"q2b")*60 and q2bmx<list_searchx(Board,"q2b")*60+60 and q2bmy>list_searchy(Board,"q2b")*60 and q2bmy<list_searchy(Board,"q2b")*60+60:
                        piece="queen2b"
                        Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                        Queen2b.possible_moves(coords,coords2,"w")
                    else:
                        q2bmx,q2bmy=qo2mx,qo2my                        
                    qo3mx,qo3my=q3bmx,q3bmy
                    vc="q3b"
                    q3bmx,q3bmy=pygame.mouse.get_pos()
                    if q3bmx>list_searchx(Board,"q3b")*60 and q3bmx<list_searchx(Board,"q3b")*60+60 and q3bmy>list_searchy(Board,"q3b")*60 and q3bmy<list_searchy(Board,"q3b")*60+60:
                        piece="queen3b"
                        Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                        Queen3b.possible_moves(coords,coords2,"w")
                    else:
                        q3bmx,q3bmy=qo3mx,qo3my
                    qo4mx,qo4my=q4bmx,q4bmy
                    vc="q4b"
                    q4bmx,q4bmy=pygame.mouse.get_pos()
                    if q4bmx>list_searchx(Board,"q4b")*60 and q4bmx<list_searchx(Board,"q4b")*60+60 and q4bmy>list_searchy(Board,"q4b")*60 and q4bmy<list_searchy(Board,"q4b")*60+60:
                        piece="queen4b"
                        Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                        Queen4b.possible_moves(coords,coords2,"w")
                    else:
                        q4bmx,q4bmy=qo4mx,qo4my 
                    po1mx,po1my=p1bmx,p1bmy
                    vc="p1b"
                    p1bmx,p1bmy=pygame.mouse.get_pos()
                    if p1bmx>list_searchx(Board,"p1b")*60 and p1bmx<list_searchx(Board,"p1b")*60+60 and p1bmy>list_searchy(Board,"p1b")*60 and p1bmy<list_searchy(Board,"p1b")*60+60:
                        piece="pawn1b"
                        Pawn1b=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                        Pawn1b.possible_moves(coords,coords2,"w",moves21b)
                    else:
                        p1bmx,p1bmy=po1mx,po1my
                    po2mx,po2my=p2bmx,p2bmy
                    vc="p2b"
                    p2bmx,p2bmy=pygame.mouse.get_pos()
                    if p2bmx>list_searchx(Board,"p2b")*60 and p2bmx<list_searchx(Board,"p2b")*60+60 and p2bmy>list_searchy(Board,"p2b")*60 and p2bmy<list_searchy(Board,"p2b")*60+60:
                        piece="pawn2b"
                        Pawn2b=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                        Pawn2b.possible_moves(coords,coords2,"w",moves22b)
                    else:
                        p2bmx,p2bmy=po2mx,po2my                        
                    po3mx,po3my=p3bmx,p3bmy
                    vc="p3b"
                    p3bmx,p3bmy=pygame.mouse.get_pos()
                    if p3bmx>list_searchx(Board,"p3b")*60 and p3bmx<list_searchx(Board,"p3b")*60+60 and p3bmy>list_searchy(Board,"p3b")*60 and p3bmy<list_searchy(Board,"p3b")*60+60:
                        piece="pawn3b"
                        Pawn3b=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                        Pawn3b.possible_moves(coords,coords2,"w",moves23b)
                    else:
                        p3bmx,p3bmy=po3mx,po3my
                    po4mx,po4my=p4bmx,p4bmy
                    vc="p4b"
                    p4bmx,p4bmy=pygame.mouse.get_pos()
                    if p4bmx>list_searchx(Board,"p4b")*60 and p4bmx<list_searchx(Board,"p4b")*60+60 and p4bmy>list_searchy(Board,"p4b")*60 and p4bmy<list_searchy(Board,"p4b")*60+60:
                        piece="pawn4b"
                        Pawn4b=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                        Pawn4b.possible_moves(coords,coords2,"w",moves24b)
                    else:
                        p4bmx,p4bmy=po4mx,po4my
                    po5mx,po5my=p5bmx,p5bmy
                    vc="p5b"
                    p5bmx,p5bmy=pygame.mouse.get_pos()
                    if p5bmx>list_searchx(Board,"p5b")*60 and p5bmx<list_searchx(Board,"p5b")*60+60 and p5bmy>list_searchy(Board,"p5b")*60 and p5bmy<list_searchy(Board,"p5b")*60+60:
                        piece="pawn5b"
                        Pawn5b=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                        Pawn5b.possible_moves(coords,coords2,"w",moves25b)
                    else:
                        p5bmx,p5bmy=po5mx,po5my
                    po6mx,po6my=p6bmx,p6bmy
                    vc="p6b"
                    p6bmx,p6bmy=pygame.mouse.get_pos()
                    if p6bmx>list_searchx(Board,"p6b")*60 and p6bmx<list_searchx(Board,"p6b")*60+60 and p6bmy>list_searchy(Board,"p6b")*60 and p6bmy<list_searchy(Board,"p6b")*60+60:
                        piece="pawn6b"
                        Pawn6b=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                        Pawn6b.possible_moves(coords,coords2,"w",moves26b)
                    else:
                        p6bmx,p6bmy=po6mx,po6my
                    po7mx,po7my=p7bmx,p7bmy
                    vc="p7b"
                    p7bmx,p7bmy=pygame.mouse.get_pos()
                    if p7bmx>list_searchx(Board,"p7b")*60 and p7bmx<list_searchx(Board,"p7b")*60+60 and p7bmy>list_searchy(Board,"p7b")*60 and p7bmy<list_searchy(Board,"p7b")*60+60:
                        piece="pawn7b"
                        Pawn7b=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                        Pawn7b.possible_moves(coords,coords2,"w",moves27b)
                    else:
                        p7bmx,p7bmy=po7mx,po7my
                    po8mx,po8my=p8bmx,p8bmy
                    vc="p8b"
                    p8bmx,p8bmy=pygame.mouse.get_pos()
                    if p8bmx>list_searchx(Board,"p8b")*60 and p8bmx<list_searchx(Board,"p8b")*60+60 and p8bmy>list_searchy(Board,"p8b")*60 and p8bmy<list_searchy(Board,"p8b")*60+60:
                        piece="pawn8b"
                        Pawn8b=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                        Pawn8b.possible_moves(coords,coords2,"w",moves28b)
                    else:
                        p8bmx,p8bmy=po8mx,po8my
                    ko1mx,ko1my=k1bmx,k1bmy
                    vc="k1b"
                    k1bmx,k1bmy=pygame.mouse.get_pos()
                    if k1bmx>list_searchx(Board,"k1b")*60 and k1bmx<list_searchx(Board,"k1b")*60+60 and k1bmy>list_searchy(Board,"k1b")*60 and k1bmy<list_searchy(Board,"k1b")*60+60:
                        piece="king1b"
                        King1b=kingw(coords,coords2,k1bmx,k1bmy,"k1b","w")
                        King1b.possible_moves(coords,coords2,"w")
                    else:
                        k1bmx,k1bmy=ko1mx,ko1my            
            if piece=="bishop1b":
                b1bmx,b1bmy=pygame.mouse.get_pos()
                tg=Bishop1b.position(coords,coords2,convertx(b1bmx),converty(b1bmy),"b1b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b1bmx,b1bmy=[],[],"",1,(list_searchx(Board,"b1b"))*60,(list_searchy(Board,"b1b"))*60
            if piece=="bishop2b":
                b2bmx,b2bmy=pygame.mouse.get_pos()
                tg=Bishop2b.position(coords,coords2,convertx(b2bmx),converty(b2bmy),"b2b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b2bmx,b2bmy=[],[],"",1,(list_searchx(Board,"b2b"))*60,(list_searchy(Board,"b2b"))*60
            if piece=="bishop3b":
                b3bmx,b3bmy=pygame.mouse.get_pos()
                tg=Bishop3b.position(coords,coords2,convertx(b3bmx),converty(b3bmy),"b3b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b3bmx,b3bmy=[],[],"",1,(list_searchx(Board,"b3b"))*60,(list_searchy(Board,"b3b"))*60
            if piece=="bishop4b":
                b4bmx,b4bmy=pygame.mouse.get_pos()
                tg=Bishop4b.position(coords,coords2,convertx(b4bmx),converty(b4bmy),"b4b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b4bmx,b4bmy=[],[],"",1,(list_searchx(Board,"b4b"))*60,(list_searchy(Board,"b4b"))*60
            if piece=="bishop5b":
                b5bmx,b5bmy=pygame.mouse.get_pos()
                tg=Bishop5b.position(coords,coords2,convertx(b5bmx),converty(b5bmy),"b5b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b5bmx,b5bmy=[],[],"",1,(list_searchx(Board,"b5b"))*60,(list_searchy(Board,"b5b"))*60
                    
            if piece=="knight1b":
                kn1bmx,kn1bmy=pygame.mouse.get_pos()
                tg=Knight1b.position(coords,coords2,convertx(kn1bmx),converty(kn1bmy),"kn1b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn1bmx,kn1bmy=[],[],"",1,(list_searchx(Board,"kn1b"))*60,(list_searchy(Board,"kn1b"))*60
            if piece=="knight2b":
                kn2bmx,kn2bmy=pygame.mouse.get_pos()
                tg=Knight2b.position(coords,coords2,convertx(kn2bmx),converty(kn2bmy),"kn2b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn2bmx,kn2bmy=[],[],"",1,(list_searchx(Board,"kn2b"))*60,(list_searchy(Board,"kn2b"))*60
            if piece=="knight3b":
                kn3bmx,kn3bmy=pygame.mouse.get_pos()
                tg=Knight3b.position(coords,coords2,convertx(kn3bmx),converty(kn3bmy),"kn3b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn3bmx,kn3bmy=[],[],"",1,(list_searchx(Board,"kn3b"))*60,(list_searchy(Board,"kn3b"))*60
            if piece=="knight4b":
                kn4bmx,kn4bmy=pygame.mouse.get_pos()
                tg=Knight4b.position(coords,coords2,convertx(kn4bmx),converty(kn4bmy),"kn4b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==1 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn4bmx,kn4bmy=[],[],"",1,(list_searchx(Board,"kn4b"))*60,(list_searchy(Board,"kn4b"))*60
            if piece=="knight5b":
                kn5bmx,kn5bmy=pygame.mouse.get_pos()
                tg=Knight5b.position(coords,coords2,convertx(kn5bmx),converty(kn5bmy),"kn5b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==1 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,kn5bmx,kn5bmy=[],[],"",1,(list_searchx(Board,"kn5b"))*60,(list_searchy(Board,"kn5b"))*60

            if piece=="rook1b":
                r1bmx,r1bmy=pygame.mouse.get_pos()
                tg=Rook1b.position(coords,coords2,convertx(r1bmx),converty(r1bmy),"r1b")                    
                if tg==2:
                    hw,black_check,moves,moves2r1b=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r1bmx,r1bmy=[],[],"",1,(list_searchx(Board,"r1b"))*60,(list_searchy(Board,"r1b"))*60
            if piece=="rook2b":
                r2bmx,r2bmy=pygame.mouse.get_pos()
                tg=Rook2b.position(coords,coords2,convertx(r2bmx),converty(r2bmy),"r2b")                    
                if tg==2:
                    hw,black_check,moves,moves2r2b=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r2bmx,r2bmy=[],[],"",1,(list_searchx(Board,"r2b"))*60,(list_searchy(Board,"r2b"))*60
            if piece=="rook3b":
                r3bmx,r3bmy=pygame.mouse.get_pos()
                tg=Rook3b.position(coords,coords2,convertx(r3bmx),converty(r3bmy),"r3b")                    
                if tg==2:
                    hw,black_check,moves,moves2r3b=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r3bmx,r3bmy=[],[],"",1,(list_searchx(Board,"r3b"))*60,(list_searchy(Board,"r3b"))*60
            if piece=="rook4b":
                r4bmx,r4bmy=pygame.mouse.get_pos()
                tg=Rook4b.position(coords,coords2,convertx(r4bmx),converty(r4bmy),"r4b")                    
                if tg==2:
                    hw,black_check,moves,moves2r4b=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r4bmx,r4bmy=[],[],"",1,(list_searchx(Board,"r4b"))*60,(list_searchy(Board,"r4b"))*60
            if piece=="rook5b":
                r5bmx,r5bmy=pygame.mouse.get_pos()
                tg=Rook5b.position(coords,coords2,convertx(r5bmx),converty(r5bmy),"r5b")                    
                if tg==2:
                    hw,black_check,moves,moves2r5b=0,False,moves+1,1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,r5bmx,r5bmy=[],[],"",1,(list_searchx(Board,"r5b"))*60,(list_searchy(Board,"r5b"))*60

            if piece=="queen1b":
                q1bmx,q1bmy=pygame.mouse.get_pos()
                tg=Queen1b.position(coords,coords2,convertx(q1bmx),converty(q1bmy),"q1b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q1bmx,q1bmy=[],[],"",1,(list_searchx(Board,"q1b"))*60,(list_searchy(Board,"q1b"))*60
            if piece=="queen2b":
                q2bmx,q2bmy=pygame.mouse.get_pos()
                tg=Queen2b.position(coords,coords2,convertx(q2bmx),converty(q2bmy),"q2b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q2bmx,q2bmy=[],[],"",1,(list_searchx(Board,"q2b"))*60,(list_searchy(Board,"q2b"))*60
            if piece=="queen3b":
                q3bmx,q3bmy=pygame.mouse.get_pos()
                tg=Queen3b.position(coords,coords2,convertx(q3bmx),converty(q3bmy),"q3b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q3bmx,q3bmy=[],[],"",1,(list_searchx(Board,"q3b"))*60,(list_searchy(Board,"q3b"))*60
            if piece=="queen4b":
                q4bmx,q4bmy=pygame.mouse.get_pos()
                tg=Queen4b.position(coords,coords2,convertx(q4bmx),converty(q4bmy),"q4b")                    
                if tg==2:
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,q4bmx,q4bmy=[],[],"",1,(list_searchx(Board,"q4b"))*60,(list_searchy(Board,"q4b"))*60

            if piece=="pawn1b":
                p1bmx,p1bmy=pygame.mouse.get_pos()
                tg=Pawn1b.position(coords,coords2,convertx(p1bmx),converty(p1bmy),"p1b")                    
                if tg==2:
                    hw,black_check,moves,moves21b=0,False,moves+1,moves21b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p1bmx,p1bmy=[],[],"",1,(list_searchx(Board,"p1b"))*60,(list_searchy(Board,"p1b"))*60
            if piece=="pawn2b":
                p2bmx,p2bmy=pygame.mouse.get_pos()
                tg=Pawn2b.position(coords,coords2,convertx(p2bmx),converty(p2bmy),"p2b")                    
                if tg==2:
                    hw,black_check,moves,moves22b=0,False,moves+1,moves22b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p2bmx,p2bmy=[],[],"",1,(list_searchx(Board,"p2b"))*60,(list_searchy(Board,"p2b"))*60
            if piece=="pawn3b":
                p3bmx,p3bmy=pygame.mouse.get_pos()
                tg=Pawn3b.position(coords,coords2,convertx(p3bmx),converty(p3bmy),"p3b")                    
                if tg==2:
                    hw,black_check,moves,moves23b=0,False,moves+1,moves23b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p3bmx,p3bmy=[],[],"",1,(list_searchx(Board,"p3b"))*60,(list_searchy(Board,"p3b"))*60
            if piece=="pawn4b":
                p4bmx,p4bmy=pygame.mouse.get_pos()
                tg=Pawn4b.position(coords,coords2,convertx(p4bmx),converty(p4bmy),"p4b")                    
                if tg==2:
                    hw,black_check,moves,moves24b=0,False,moves+1,moves24b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p4bmx,p4bmy=[],[],"",1,(list_searchx(Board,"p4b"))*60,(list_searchy(Board,"p4b"))*60
            if piece=="pawn5b":
                p5bmx,p5bmy=pygame.mouse.get_pos()
                tg=Pawn5b.position(coords,coords2,convertx(p5bmx),converty(p5bmy),"p5b")                    
                if tg==2:
                    hw,black_check,moves,moves25b=0,False,moves+1,moves25b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p5bmx,p5bmy=[],[],"",1,(list_searchx(Board,"p5b"))*60,(list_searchy(Board,"p5b"))*60
            if piece=="pawn6b":
                p6bmx,p6bmy=pygame.mouse.get_pos()
                tg=Pawn6b.position(coords,coords2,convertx(p6bmx),converty(p6bmy),"p6b")                    
                if tg==2:
                    hw,black_check,moves,moves26b=0,False,moves+1,moves26b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p6bmx,p6bmy=[],[],"",1,(list_searchx(Board,"p6b"))*60,(list_searchy(Board,"p6b"))*60
            if piece=="pawn7b":
                p7bmx,p7bmy=pygame.mouse.get_pos()
                tg=Pawn7b.position(coords,coords2,convertx(p7bmx),converty(p7bmy),"p7b")                    
                if tg==2:
                    hw,black_check,moves,moves27b=0,False,moves+1,moves27b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p7bmx,p7bmy=[],[],"",1,(list_searchx(Board,"p7b"))*60,(list_searchy(Board,"p7b"))*60
            if piece=="pawn8b":
                p8bmx,p8bmy=pygame.mouse.get_pos()
                tg=Pawn8b.position(coords,coords2,convertx(p8bmx),converty(p8bmy),"p8b")                    
                if tg==2:
                    hw,black_check,moves,moves28b=0,False,moves+1,moves28b+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,p8bmx,p8bmy=[],[],"",1,(list_searchx(Board,"p8b"))*60,(list_searchy(Board,"p8b"))*60
            if piece=="king1b":
                k1bmx,k1bmy=pygame.mouse.get_pos()
                tg=King1b.position(coords,coords2,convertx(k1bmx),converty(k1bmy),"k1b")                    
                if tg==2:
                    r1bmy=list_searchy(Board,"r1b")*60
                    r1bmx=list_searchx(Board,"r1b")*60
                    r2bmy=list_searchy(Board,"r2b")*60
                    r2bmx=list_searchx(Board,"r2b")*60
                    hw,black_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,k1bmx,k1bmy=[],[],"",1,(list_searchx(Board,"k1b"))*60,(list_searchy(Board,"k1b"))*60

####################################################################
        Pawn1b_status=Status("p1b",pawn_black1_status)
        Pawn1b_status.Status2("p1b",pawn_black1_status)
        pawn_black1_status=Pawn1b_status.pawn_black1_status

        Pawn2b_status=Status("p2b",pawn_black2_status)
        Pawn2b_status.Status2("p2b",pawn_black2_status)
        pawn_black2_status=Pawn2b_status.pawn_black1_status
        
        Pawn3b_status=Status("p3b",pawn_black3_status)
        Pawn3b_status.Status2("p3b",pawn_black3_status)
        pawn_black3_status=Pawn3b_status.pawn_black1_status

        Pawn4b_status=Status("p4b",pawn_black4_status)
        Pawn4b_status.Status2("p4b",pawn_black4_status)
        pawn_black4_status=Pawn4b_status.pawn_black1_status

        Pawn5b_status=Status("p5b",pawn_black5_status)
        Pawn5b_status.Status2("p5b",pawn_black5_status)
        pawn_black5_status=Pawn5b_status.pawn_black1_status

        Pawn6b_status=Status("p6b",pawn_black6_status)
        Pawn6b_status.Status2("p6b",pawn_black6_status)
        pawn_black6_status=Pawn6b_status.pawn_black1_status

        Pawn7b_status=Status("p7b",pawn_black7_status)
        Pawn7b_status.Status2("p7b",pawn_black7_status)
        pawn_black7_status=Pawn7b_status.pawn_black1_status

        Pawn8b_status=Status("p8b",pawn_black8_status)
        Pawn8b_status.Status2("p8b",pawn_black8_status)
        pawn_black8_status=Pawn8b_status.pawn_black1_status

        
        Pawn1w_status=Status("p1w",pawn_white1_status)
        Pawn1w_status.Status2("p1w",pawn_white1_status)
        pawn_white1_status=Pawn1w_status.pawn_black1_status

        Pawn2w_status=Status("p2w",pawn_white2_status)
        Pawn2w_status.Status2("p2w",pawn_white2_status)
        pawn_white2_status=Pawn2w_status.pawn_black1_status
        
        Pawn3w_status=Status("p3w",pawn_white3_status)
        Pawn3w_status.Status2("p3w",pawn_white3_status)
        pawn_white3_status=Pawn3w_status.pawn_black1_status

        Pawn4w_status=Status("p4w",pawn_white4_status)
        Pawn4w_status.Status2("p4w",pawn_white4_status)
        pawn_white4_status=Pawn4w_status.pawn_black1_status

        Pawn5w_status=Status("p5w",pawn_white5_status)
        Pawn5w_status.Status2("p5w",pawn_white5_status)
        pawn_white5_status=Pawn5w_status.pawn_black1_status

        Pawn6w_status=Status("p6w",pawn_white6_status)
        Pawn6w_status.Status2("p6w",pawn_white6_status)
        pawn_white6_status=Pawn6w_status.pawn_black1_status

        Pawn7w_status=Status("p7w",pawn_white7_status)
        Pawn7w_status.Status2("p7w",pawn_white7_status)
        pawn_white7_status=Pawn7w_status.pawn_black1_status

        Pawn8w_status=Status("p8w",pawn_white8_status)
        Pawn8w_status.Status2("p8w",pawn_white8_status)
        pawn_white8_status=Pawn8w_status.pawn_black1_status

        rook1w_status=Status("r1w",rook_white1_status)
        rook1w_status.Status2("r1w",rook_white1_status)
        rook_white1_status=rook1w_status.pawn_black1_status

        rook2w_status=Status("r2w",rook_white2_status)
        rook2w_status.Status2("r2w",rook_white2_status)
        rook_white2_status=rook2w_status.pawn_black1_status
        
        rook3w_status=Status("r3w",rook_white3_status)
        rook3w_status.Status2("r3w",rook_white3_status)
        rook_white3_status=rook3w_status.pawn_black1_status

        rook4w_status=Status("r4w",rook_white4_status)
        rook4w_status.Status2("r4w",rook_white4_status)
        rook_white4_status=rook4w_status.pawn_black1_status

        rook5w_status=Status("r5w",rook_white5_status)
        rook5w_status.Status2("r5w",rook_white5_status)
        rook_white5_status=rook5w_status.pawn_black1_status


        knight1w_status=Status("kn1w",knight_white1_status)
        knight1w_status.Status2("kn1w",knight_white1_status)
        knight_white1_status=knight1w_status.pawn_black1_status

        knight2w_status=Status("kn2w",knight_white2_status)
        knight2w_status.Status2("kn2w",knight_white2_status)
        knight_white2_status=knight2w_status.pawn_black1_status
        
        knight3w_status=Status("kn3w",knight_white3_status)
        knight3w_status.Status2("kn3w",knight_white3_status)
        knight_white3_status=knight3w_status.pawn_black1_status

        knight4w_status=Status("kn4w",knight_white4_status)
        knight4w_status.Status2("kn4w",knight_white4_status)
        knight_white4_status=knight4w_status.pawn_black1_status

        knight5w_status=Status("kn5w",knight_white5_status)
        knight5w_status.Status2("kn5w",knight_white5_status)
        knight_white5_status=knight5w_status.pawn_black1_status


        bishop1w_status=Status("b1w",bishop_white1_status)
        bishop1w_status.Status2("b1w",bishop_white1_status)
        bishop_white1_status=bishop1w_status.pawn_black1_status

        bishop2w_status=Status("b2w",bishop_white2_status)
        bishop2w_status.Status2("b2w",bishop_white2_status)
        bishop_white2_status=bishop2w_status.pawn_black1_status
        
        bishop3w_status=Status("b3w",bishop_white3_status)
        bishop3w_status.Status2("b3w",bishop_white3_status)
        bishop_white3_status=bishop3w_status.pawn_black1_status

        bishop4w_status=Status("b4w",bishop_white4_status)
        bishop4w_status.Status2("b4w",bishop_white4_status)
        bishop_white4_status=bishop4w_status.pawn_black1_status

        bishop5w_status=Status("b5w",bishop_white5_status)
        bishop5w_status.Status2("b5w",bishop_white5_status)
        bishop_white5_status=bishop5w_status.pawn_black1_status

        queen1w_status=Status("q1w",queen_white_status)
        queen1w_status.Status2("q1w",queen_white_status)
        queen_white_status=queen1w_status.pawn_black1_status

        queen2w_status=Status("q2w",queen_white2_status)
        queen2w_status.Status2("q2w",queen_white2_status)
        queen_white2_status=queen2w_status.pawn_black1_status

        queen3w_status=Status("q3w",queen_white3_status)
        queen3w_status.Status2("q3w",queen_white3_status)
        queen_white3_status=queen3w_status.pawn_black1_status

        queen4w_status=Status("q4w",queen_white4_status)
        queen4w_status.Status2("q4w",queen_white4_status)
        queen_white4_status=queen4w_status.pawn_black1_status


        rook1b_status=Status("r1b",rook_black1_status)
        rook1b_status.Status2("r1b",rook_black1_status)
        rook_black1_status=rook1b_status.pawn_black1_status

        rook2b_status=Status("r2b",rook_black2_status)
        rook2b_status.Status2("r2b",rook_black2_status)
        rook_black2_status=rook2b_status.pawn_black1_status
        
        rook3b_status=Status("r3b",rook_black3_status)
        rook3b_status.Status2("r3b",rook_black3_status)
        rook_black3_status=rook3b_status.pawn_black1_status

        rook4b_status=Status("r4b",rook_black4_status)
        rook4b_status.Status2("r4b",rook_black4_status)
        rook_black4_status=rook4b_status.pawn_black1_status

        rook5b_status=Status("r5b",rook_black5_status)
        rook5b_status.Status2("r5b",rook_black5_status)
        rook_black5_status=rook5b_status.pawn_black1_status


        knight1b_status=Status("kn1b",knight_black1_status)
        knight1b_status.Status2("kn1b",knight_black1_status)
        knight_black1_status=knight1b_status.pawn_black1_status

        knight2b_status=Status("kn2b",knight_black2_status)
        knight2b_status.Status2("kn2b",knight_black2_status)
        knight_black2_status=knight2b_status.pawn_black1_status
        
        knight3b_status=Status("kn3b",knight_black3_status)
        knight3b_status.Status2("kn3b",knight_black3_status)
        knight_black3_status=knight3b_status.pawn_black1_status

        knight4b_status=Status("kn4b",knight_black4_status)
        knight4b_status.Status2("kn4b",knight_black4_status)
        knight_black4_status=knight4b_status.pawn_black1_status

        knight5b_status=Status("kn5b",knight_black5_status)
        knight5b_status.Status2("kn5b",knight_black5_status)
        knight_black5_status=knight5b_status.pawn_black1_status


        bishop1b_status=Status("b1b",bishop_black1_status)
        bishop1b_status.Status2("b1b",bishop_black1_status)
        bishop_black1_status=bishop1b_status.pawn_black1_status

        bishop2b_status=Status("b2b",bishop_black2_status)
        bishop2b_status.Status2("b2b",bishop_black2_status)
        bishop_black2_status=bishop2b_status.pawn_black1_status
        
        bishop3b_status=Status("b3b",bishop_black3_status)
        bishop3b_status.Status2("b3b",bishop_black3_status)
        bishop_black3_status=bishop3b_status.pawn_black1_status

        bishop4b_status=Status("b4b",bishop_black4_status)
        bishop4b_status.Status2("b4b",bishop_black4_status)
        bishop_black4_status=bishop4b_status.pawn_black1_status

        bishop5b_status=Status("b5b",bishop_black5_status)
        bishop5b_status.Status2("b5b",bishop_black5_status)
        bishop_black5_status=bishop5b_status.pawn_black1_status


        queen1b_status=Status("q1b",queen_black_status)
        queen1b_status.Status2("q1b",queen_black_status)
        queen_black_status=queen1b_status.pawn_black1_status

        queen2b_status=Status("q2b",queen_black2_status)
        queen2b_status.Status2("q2b",queen_black2_status)
        queen_black2_status=queen2b_status.pawn_black1_status
        
        queen3b_status=Status("q3b",queen_black3_status)
        queen3b_status.Status2("q3b",queen_black3_status)
        queen_black3_status=queen3b_status.pawn_black1_status

        queen4b_status=Status("q4b",queen_black4_status)
        queen4b_status.Status2("q4b",queen_black4_status)
        queen_black4_status=queen4b_status.pawn_black1_status
    

        rook3w1_status=Status1("r3w",rook_white3_status,rook3w_spawn,r3wmx,r3wmy)
        rook3w1_status.Status21("r3w",rook_white3_status,rook3w_spawn,r3wmx,r3wmy)
        rook3w_spawn=rook3w1_status.queen4b_spawn
        rook_white3_status=rook3w1_status.queen_black4_status
        if rook3w_spawn==1:
            r3wmx=rook3w1_status.q4bmx 
            r3wmy=rook3w1_status.q4bmy
            rook3w_spawn=3
                
        rook4w1_status=Status1("r4w",rook_white4_status,rook4w_spawn,r4wmx,r4wmy)
        rook4w1_status.Status21("r4w",rook_white4_status,rook4w_spawn,r4wmx,r4wmy)
        rook4w_spawn=rook4w1_status.queen4b_spawn
        rook_white4_status=rook4w1_status.queen_black4_status
        if rook4w_spawn==1:
            r4wmx=rook4w1_status.q4bmx 
            r4wmy=rook4w1_status.q4bmy
            rook4w_spawn=4

        rook5w1_status=Status1("r5w",rook_white5_status,rook5w_spawn,r5wmx,r5wmy)
        rook5w1_status.Status21("r5w",rook_white5_status,rook5w_spawn,r5wmx,r5wmy)
        rook5w_spawn=rook5w1_status.queen4b_spawn
        rook_white5_status=rook5w1_status.queen_black4_status
        if rook5w_spawn==1:
            r5wmx=rook5w1_status.q4bmx 
            r5wmy=rook5w1_status.q4bmy
            rook5w_spawn=5
            
        knight3w1_status=Status1("kn3w",knight_white3_status,knight3w_spawn,kn3wmx,kn3wmy)
        knight3w1_status.Status21("kn3w",knight_white3_status,knight3w_spawn,kn3wmx,kn3wmy)
        knight3w_spawn=knight3w1_status.queen4b_spawn
        knight_white3_status=knight3w1_status.queen_black4_status
        if knight3w_spawn==1:
            kn3wmx=knight3w1_status.q4bmx 
            kn3wmy=knight3w1_status.q4bmy
            knight3w_spawn=3
                
        knight4w1_status=Status1("kn4w",knight_white4_status,knight4w_spawn,kn4wmx,kn4wmy)
        knight4w1_status.Status21("kn4w",knight_white4_status,knight4w_spawn,kn4wmx,kn4wmy)
        knight4w_spawn=knight4w1_status.queen4b_spawn
        knight_white4_status=knight4w1_status.queen_black4_status
        if knight4w_spawn==1:
            kn4wmx=knight4w1_status.q4bmx 
            kn4wmy=knight4w1_status.q4bmy
            knight4w_spawn=4

        knight5w1_status=Status1("kn5w",knight_white5_status,knight5w_spawn,kn5wmx,kn5wmy)
        knight5w1_status.Status21("kn5w",knight_white5_status,knight5w_spawn,kn5wmx,kn5wmy)
        knight5w_spawn=knight5w1_status.queen4b_spawn
        knight_white5_status=knight5w1_status.queen_black4_status
        if knight5w_spawn==1:
            kn5wmx=knight5w1_status.q4bmx 
            kn5wmy=knight5w1_status.q4bmy
            knight5w_spawn=5
                
        bishop3w1_status=Status1("b3w",bishop_white3_status,bishop3w_spawn,b3wmx,b3wmy)
        bishop3w1_status.Status21("b3w",bishop_white3_status,bishop3w_spawn,b3wmx,b3wmy)
        bishop3w_spawn=bishop3w1_status.queen4b_spawn
        bishop_white3_status=bishop3w1_status.queen_black4_status
        if bishop3w_spawn==1:
            b3wmx=bishop3w1_status.q4bmx 
            b3wmy=bishop3w1_status.q4bmy
            bishop3w_spawn=3
                
        bishop4w1_status=Status1("b4w",bishop_white4_status,bishop4w_spawn,b4wmx,b4wmy)
        bishop4w1_status.Status21("b4w",bishop_white4_status,bishop4w_spawn,b4wmx,b4wmy)
        bishop4w_spawn=bishop4w1_status.queen4b_spawn
        bishop_white4_status=bishop4w1_status.queen_black4_status
        if bishop4w_spawn==1:
            b4wmx=bishop4w1_status.q4bmx 
            b4wmy=bishop4w1_status.q4bmy
            bishop4w_spawn=4

        bishop5w1_status=Status1("b5w",bishop_white5_status,bishop5w_spawn,b5wmx,b5wmy)
        bishop5w1_status.Status21("b5w",bishop_white5_status,bishop5w_spawn,b5wmx,b5wmy)
        bishop5w_spawn=bishop5w1_status.queen4b_spawn
        bishop_white5_status=bishop5w1_status.queen_black4_status
        if bishop5w_spawn==1:
            b5wmx=bishop5w1_status.q4bmx 
            b5wmy=bishop5w1_status.q4bmy
            bishop5w_spawn=5
                
        queen2w1_status=Status1("q2w",queen_white2_status,queen2w_spawn,q2wmx,q2wmy)
        queen2w1_status.Status21("q2w",queen_white2_status,queen2w_spawn,q2wmx,q2wmy)
        queen2w_spawn=queen2w1_status.queen4b_spawn
        queen_white2_status=queen2w1_status.queen_black4_status
        if queen2w_spawn==1:
            q2wmx=queen2w1_status.q4bmx 
            q2wmy=queen2w1_status.q4bmy
            queen2w_spawn=2
            
        queen3w1_status=Status1("q3w",queen_white3_status,queen3w_spawn,q3wmx,q3wmy)
        queen3w1_status.Status21("q3w",queen_white3_status,queen3w_spawn,q3wmx,q3wmy)
        queen3w_spawn=queen3w1_status.queen4b_spawn
        queen_white3_status=queen3w1_status.queen_black4_status
        if queen3w_spawn==1:
            q3wmx=queen3w1_status.q4bmx 
            q3wmy=queen3w1_status.q4bmy
            queen3w_spawn=3
                
        queen4w1_status=Status1("q4w",queen_white4_status,queen4w_spawn,q4wmx,q4wmy)
        queen4w1_status.Status21("q4w",queen_white4_status,queen4w_spawn,q4wmx,q4wmy)
        queen4w_spawn=queen4w1_status.queen4b_spawn
        queen_white4_status=queen4w1_status.queen_black4_status
        if queen4w_spawn==1:
            q4wmx=queen4w1_status.q4bmx 
            q4wmy=queen4w1_status.q4bmy
            queen4w_spawn=4
            
        rook3b1_status=Status1("r3b",rook_black3_status,rook3b_spawn,r3bmx,r3bmy)
        rook3b1_status.Status21("r3b",rook_black3_status,rook3b_spawn,r3bmx,r3bmy)
        rook3b_spawn=rook3b1_status.queen4b_spawn
        rook_black3_status=rook3b1_status.queen_black4_status
        if rook3b_spawn==1:
            r3bmx=rook3b1_status.q4bmx 
            r3bmy=rook3b1_status.q4bmy
            rook3b_spawn=3
                
        rook4b1_status=Status1("r4b",rook_black4_status,rook4b_spawn,r4bmx,r4bmy)
        rook4b1_status.Status21("r4b",rook_black4_status,rook4b_spawn,r4bmx,r4bmy)
        rook4b_spawn=rook4b1_status.queen4b_spawn
        rook_black4_status=rook4b1_status.queen_black4_status
        if rook4b_spawn==1:
            r4bmx=rook4b1_status.q4bmx 
            r4bmy=rook4b1_status.q4bmy
            rook4b_spawn=4

        rook5b1_status=Status1("r5b",rook_black5_status,rook5b_spawn,r5bmx,r5bmy)
        rook5b1_status.Status21("r5b",rook_black5_status,rook5b_spawn,r5bmx,r5bmy)
        rook5b_spawn=rook5b1_status.queen4b_spawn
        rook_black5_status=rook5b1_status.queen_black4_status
        if rook5b_spawn==1:
            r5bmx=rook5b1_status.q4bmx 
            r5bmy=rook5b1_status.q4bmy
            rook5b_spawn=5
            
        knight3b1_status=Status1("kn3b",knight_black3_status,knight3b_spawn,kn3bmx,kn3bmy)
        knight3b1_status.Status21("kn3b",knight_black3_status,knight3b_spawn,kn3bmx,kn3bmy)
        knight3b_spawn=knight3b1_status.queen4b_spawn
        knight_black3_status=knight3b1_status.queen_black4_status
        if knight3b_spawn==1:
            kn3bmx=knight3b1_status.q4bmx 
            kn3bmy=knight3b1_status.q4bmy
            knight3b_spawn=3
                
        knight4b1_status=Status1("kn4b",knight_black4_status,knight4b_spawn,kn4bmx,kn4bmy)
        knight4b1_status.Status21("kn4b",knight_black4_status,knight4b_spawn,kn4bmx,kn4bmy)
        knight4b_spawn=knight4b1_status.queen4b_spawn
        knight_black4_status=knight4b1_status.queen_black4_status
        if knight4b_spawn==1:
            kn4bmx=knight4b1_status.q4bmx 
            kn4bmy=knight4b1_status.q4bmy
            knight4b_spawn=4

        knight5b1_status=Status1("kn5b",knight_black5_status,knight5b_spawn,kn5bmx,kn5bmy)
        knight5b1_status.Status21("kn5b",knight_black5_status,knight5b_spawn,kn5bmx,kn5bmy)
        knight5b_spawn=knight5b1_status.queen4b_spawn
        knight_black5_status=knight5b1_status.queen_black4_status
        if knight5b_spawn==1:
            kn5bmx=knight5b1_status.q4bmx 
            kn5bmy=knight5b1_status.q4bmy
            knight5b_spawn=5
                
        bishop3b1_status=Status1("b3b",bishop_black3_status,bishop3b_spawn,b3bmx,b3bmy)
        bishop3b1_status.Status21("b3b",bishop_black3_status,bishop3b_spawn,b3bmx,b3bmy)
        bishop3b_spawn=bishop3b1_status.queen4b_spawn
        bishop_black3_status=bishop3b1_status.queen_black4_status
        if bishop3b_spawn==1:
            b3bmx=bishop3b1_status.q4bmx 
            b3bmy=bishop3b1_status.q4bmy
            bishop3b_spawn=3
                
        bishop4b1_status=Status1("b4b",bishop_black4_status,bishop4b_spawn,b4bmx,b4bmy)
        bishop4b1_status.Status21("b4b",bishop_black4_status,bishop4b_spawn,b4bmx,b4bmy)
        bishop4b_spawn=bishop4b1_status.queen4b_spawn
        bishop_black4_status=bishop4b1_status.queen_black4_status
        if bishop4b_spawn==1:
            b4bmx=bishop4b1_status.q4bmx 
            b4bmy=bishop4b1_status.q4bmy
            bishop4b_spawn=4

        bishop5b1_status=Status1("b5b",bishop_black5_status,bishop5b_spawn,b5bmx,b5bmy)
        bishop5b1_status.Status21("b5b",bishop_black5_status,bishop5b_spawn,b5bmx,b5bmy)
        bishop5b_spawn=bishop5b1_status.queen4b_spawn
        bishop_black5_status=bishop5b1_status.queen_black4_status
        if bishop5b_spawn==1:
            b5bmx=bishop5b1_status.q4bmx 
            b5bmy=bishop5b1_status.q4bmy
            bishop5b_spawn=2
                
        queen2b1_status=Status1("q2b",queen_black2_status,queen2b_spawn,q2bmx,q2bmy)
        queen2b1_status.Status21("q2b",queen_black2_status,queen2b_spawn,q2bmx,q2bmy)
        queen2b_spawn=queen2b1_status.queen4b_spawn
        queen_black2_status=queen2b1_status.queen_black4_status
        if queen2b_spawn==1:
            q2bmx=queen2b1_status.q4bmx 
            q2bmy=queen2b1_status.q4bmy
            queen2b_spawn=2
            
        queen3b1_status=Status1("q3b",queen_black3_status,queen3b_spawn,q3bmx,q3bmy)
        queen3b1_status.Status21("q3b",queen_black3_status,queen3b_spawn,q3bmx,q3bmy)
        queen3b_spawn=queen3b1_status.queen4b_spawn
        queen_black3_status=queen3b1_status.queen_black4_status
        if queen3b_spawn==1:
            q3bmx=queen3b1_status.q4bmx 
            q3bmy=queen3b1_status.q4bmy
            queen3b_spawn=3
        
        queen4b1_status=Status1("q4b",queen_black4_status,queen4b_spawn,q4bmx,q4bmy)
        queen4b1_status.Status21("q4b",queen_black4_status,queen4b_spawn,q4bmx,q4bmy)
        queen4b_spawn=queen4b1_status.queen4b_spawn
        queen_black4_status=queen4b1_status.queen_black4_status
        if queen4b_spawn==1:
            q4bmx=queen4b1_status.q4bmx 
            q4bmy=queen4b1_status.q4bmy
            queen4b_spawn=4
            
        board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
        for er in range (0, len(coords2)):
            pygame.draw.circle(win,(255,0,0),(coords2[0][0],coords2[0][1]),15,0)
        for er in range (0, len(coords)):
            pygame.draw.circle(win,(50,205,50),(coords[er][0],coords[er][1]),15,0)
            
    pygame.display.update()
pygame.QUIT
