import pygame
pygame.init()
from pygame.locals import *
def queen_moves(xposition,yposition,coords,Board,colour,y,x):
    for i in range(1,9):
        yposition,xposition=yposition+y,xposition+x
        if (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and  (yposition)<8 and (xposition)<8  and Board[(yposition)][(xposition)][0]=="" :
            coords.append([(xposition)*60+30,(yposition)*60+30])
        else:
            if (yposition)<8 and (xposition)<8 and  (yposition)>-1 and (xposition)>-1 and  (yposition)<8 and (xposition)<8  and Board[(yposition)][(xposition)][1]==colour:
                coords.append([(xposition)*60+30,(yposition)*60+30])
            break;
    return coords
def knight_moves(xposition,yposition,coords,Board,colour,y,x):
    if (yposition+y)<8 and (xposition+x)<8 and (yposition+y)>-1 and (xposition+x)>-1 and (yposition+y)>-1 and (xposition+x)>-1 and  (yposition+y)<8 and (xposition+x)<8  and Board[(yposition+y)][(xposition+x)][0]=="" :
        coords.append([(xposition+x)*60+30,(yposition+y)*60+30])
    else:
        if (yposition+y)<8 and (xposition+x)<8 and (yposition+y)>-1 and (xposition+x)>-1 and  (yposition+y)>-1 and (xposition+x)>-1 and  (yposition+y)<8 and (xposition+x)<8  and Board[(yposition+y)][(xposition+x)][1]==colour:
            coords.append([(xposition+x)*60+30,(yposition+y)*60+30])
    return(coords)
def king_moves(xposition,yposition,coords,Board,colour,y,x,all_white):
    fc=True
    for i in range (0,len(all_white)):
        if (xposition+x)*60==all_white[i][0] and (yposition+y)*60==all_white[i][1]:
            fc=False
    if (yposition+y)<8 and (xposition+x)<8 and (yposition+y)>-1 and (xposition+x)>-1 and  (yposition+y)<8 and (xposition+x)<8  and Board[(yposition+y)][(xposition+x)][0]=="" and fc==True:
        coords.append([(xposition+x)*60+30,(yposition+y)*60+30])
    else:
        if (yposition+y)<8 and (xposition+x)<8 and  (yposition+y)>-1 and (xposition+x)>-1 and  (yposition+y)<8 and (xposition+x)<8  and Board[(yposition+y)][(xposition+x)][1]==colour and fc==True:
            coords.append([(xposition+x)*60+30,(yposition+y)*60+30])
    return coords
def Protectors(black_check,white_check,attack,coords,attack_positions,Board,two_protectors,colour,black_protector,number,white_protector):
    if black_check==True or white_check==True:
        coords3=[]
        if len(attack)>1:
            for i in range(0,len(coords)):
                coords.pop()
        else:
            attack_positions2=[]
            for a in range (0,len(attack_positions)):
                attack_positions2.append([(attack_positions[a][0])+30,(attack_positions[a][1])+30])
            for i in range(0,len(coords)):
                coords3.append(coords[i])   
            for i in range(0,len(coords3)):
                coords.pop()
            for a in range (0,len(attack_positions2)):
                for i in range (0,len(coords3)):
                    if coords3[i]==attack_positions2[a]:
                        coords.append(coords3[i])
            for i in range (0,len(coords3)):
                if coords3[i][0]==(list_searchx(Board,attack[0][0]))*60+30 and coords3[i][1]==(list_searchy(Board,attack[0][0]))*60+30:
                    coords.append([(list_searchx(Board,attack[0][0]))*60+30,(list_searchy(Board,attack[0][0]))*60+30])
    if two_protectors==False:
        coords4=[]
        if colour=="w":
            for i in range (0,len(black_protector)):
                if black_protector[i][0]==number:
                    for a in range(0,len(coords)):
                        if black_protector[i][1]+30==coords[a][0] and black_protector[i][2]+30==coords[a][1]:
                            coords4.append([coords[a][0],coords[a][1]])
            for i in range (0,len(black_protector)):
                if black_protector[i][0]==number:
                    for i in range(0,len(coords)):
                        coords.pop()
                    for i in range (0,len(coords4)):
                        coords.append([coords4[i][0],coords4[i][1]])
        if colour=="b":
            for i in range (0,len(white_protector)):
                if white_protector[i][0]==number:
                    for a in range(0,len(coords)):
                        if white_protector[i][1]+30==coords[a][0] and white_protector[i][2]+30==coords[a][1]:
                            coords4.append([coords[a][0],coords[a][1]])
            for i in range (0,len(white_protector)):
                if white_protector[i][0]==number:
                    for i in range(0,len(coords)):
                        coords.pop()
                    for i in range (0,len(coords4)):
                        coords.append([coords4[i][0],coords4[i][1]])
    return coords
def queen1_attack(yposition,xposition,colour,q11,Board,king,black_protector,two_protectors,colour2,x,y,x2,y2):
    jk=False
    i,a,pos_spaces=0,0,[]
    king_attack=False
    two_protectors_backup=False
    while jk==False:
        yposition,xposition=yposition+y,xposition+x
        pos_spaces.append([(xposition)*60,(yposition)*60])
        if (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and Board[(yposition)][(xposition)][0]=="" :
            pos_spaces.append([(xposition)*60,(yposition)*60])
            q11.append([((xposition)*60),((yposition)*60)])
        else:
            jk=True
            if (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and Board[(yposition)][(xposition)][1]==colour:
                q11.append([((xposition)*60),((yposition)*60)])
                piece2,jk=Board[(yposition)][(xposition)][0],False
                while jk==False:
                    yposition,xposition=yposition+y2,xposition+x2
                    jk,a=True,a+1
                    pos_spaces.append([(xposition)*60,(yposition)*60])
                    if (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and Board[(yposition)][(xposition)][0]==king:
                        king_attack=True
                        for z in range(0,len(pos_spaces)):
                            black_protector.append([piece2,pos_spaces[z][0],pos_spaces[z][1]])
                    elif (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and Board[(yposition)][(xposition)][1]==colour:
                        two_protectors_backup=True
                        jk=False
                    elif (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1:
                        jk=False
                if two_protectors_backup==True and king_attack==False:
                    two_protectors_backup=False
            elif (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and Board[(yposition)][(xposition)][1]==colour2:
                q11.append([((xposition)*60),((yposition)*60)])
    if two_protectors_backup==True:
        two_protectors=True
    return q11,black_protector,two_protectors
def knight1_attack(yposition,xposition,kn1,Board,colour,colour2,x,y):
    yposition,xposition=yposition+y,xposition+x
    if (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and (yposition)>-1 and (xposition)>-1 and  (yposition)<8 and (xposition)<8  and Board[(yposition)][(xposition)][0]=="" :
        kn1.append([(xposition)*60,(yposition)*60])
    else:
        if (yposition)<8 and (xposition)<8 and (yposition)>-1 and (xposition)>-1 and  (yposition)>-1 and (xposition)>-1 and  (yposition)<8 and (xposition)<8  and Board[(yposition)][(xposition)][1]==colour or yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==colour2:
            kn1.append([(xposition)*60,(yposition)*60])
    return kn1
class queenw(object):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour):
        self.coords,self.coords2,self.bwmx,self.bwmy,self.number,self.colour=coords,coords2,bwmx,bwmy,number,colour
    def possible_moves(self,coords,coords2,colour,piece_backup,Checkmate_pass):
        self.colour,self.Checkmate_pass=colour,Checkmate_pass
        yposition,xposition=list_searchy(Board,self.number),list_searchx(Board,self.number)
        if xposition!=9:
            bo1mx,bo1my=self.bwmx,self.bwmy
            self.bwmx,self.bwmy=pygame.mouse.get_pos()
            if self.Checkmate_pass==True or self.bwmx>list_searchx(Board,self.number)*60 and self.bwmx<list_searchx(Board,self.number)*60+60 and self.bwmy>list_searchy(Board,self.number)*60 and self.bwmy<list_searchy(Board,self.number)*60+60:
                if self.number[0]=="b":
                    piece_backup="bishop"+self.number[1]
                if self.number[0]=="q":
                    piece_backup="queen"+self.number[1]
                if self.number[0]=="r":
                    piece_backup="rook"+self.number[1]
                if self.number[2]=="b":
                    piece_backup=piece_backup+"b"
                if self.number[0]=="q" or self.number[0]=="r":
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,0,1)
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,0,-1)
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,1,0)
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,-1,0)
                if self.number[0]=="q" or self.number[0]=="b":
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,1,1)
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,1,-1)
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,-1,1)
                    self.coords=queen_moves(xposition,yposition,self.coords,Board,self.colour,-1,-1)
                self.coords2.append([xposition*60+30,yposition*60+30])
                self.coords=Protectors(black_check,white_check,attack,self.coords,attack_positions,Board,two_protectors,self.colour,black_protector,self.number,white_protector)
            else:
                self.bwmx,self.bwmy=bo1mx,bo1my
        return piece_backup,self.bwmx,self.bwmy
    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords,self.coords2,tg=coords,coords2,0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                if (roomx-(roomx%60))+30==self.coords2[0][0] and roomy==(roomy-(roomy%60))+30==self.coords2[0][1]:
                    fv,tg,piece=1,1,""
                else:
                    for k1 in range (0, len(self.coords)):
                        if ((roomx-roomx%60)+30)==self.coords[k1][0] and ((roomy-roomy%60)+30)==self.coords[k1][1]:
                            piece=""
                            self.bwmx,self.bwmy=pygame.mouse.get_pos()
                            fv=2
                            self.bwmx,self.bwmy=convertx(self.bwmx)//60,converty(self.bwmy)//60
                            yposition,xposition=list_searchy(Board,self.number),list_searchx(Board,self.number)
                            firstposition1=Board[yposition][xposition][0]
                            firstposition2=Board[yposition][xposition][1]
                            Board[yposition][xposition][0],Board[yposition][xposition][1]="",""
                            Board[self.bwmy][self.bwmx][0],Board[self.bwmy][self.bwmx][1]="",""
                            Board[self.bwmy][self.bwmx][0],Board[self.bwmy][self.bwmx][1]=firstposition1,firstposition2
                            tg=2
                if fv==0:
                    tg=3
                    return tg
                if fv==1 or fv==2:
                    self.coords,self.coords2=[],[]
                    return tg
        else:
            return tg
class bishopw(queenw):
    line_filler=1
class rookw(queenw):
    line_filler=1
class knightw(queenw):
    def possible_moves(self,coords,coords2,colour,piece_backup,Checkmate_pass):
        self.colour,self.Checkmate_pass=colour,Checkmate_pass
        yposition,xposition=list_searchy(Board,self.number),list_searchx(Board,self.number)
        if xposition!=9:
            bo1mx,bo1my=self.bwmx,self.bwmy
            self.bwmx,self.bwmy=pygame.mouse.get_pos()
            if self.Checkmate_pass==True or self.bwmx>list_searchx(Board,self.number)*60 and self.bwmx<list_searchx(Board,self.number)*60+60 and self.bwmy>list_searchy(Board,self.number)*60 and self.bwmy<list_searchy(Board,self.number)*60+60:
                if self.number[3]=="b":
                    piece_backup="knight"+self.number[2]+"b"
                else:
                    piece_backup="knight"+self.number[2]
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,2,-1)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,2,1)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,-2,-1)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,-2,1)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,1,-2)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,1,2)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,-1,-2)
                self.coords=knight_moves(xposition,yposition,self.coords,Board,self.colour,-1,2)
                self.coords2.append([(xposition)*60+30,(yposition)*60+30])
                self.coords=Protectors(black_check,white_check,attack,self.coords,attack_positions,Board,two_protectors,self.colour,black_protector,self.number,white_protector)
            else:
                self.bwmx,self.bwmy=bo1mx,bo1my
        return piece_backup,self.bwmx,self.bwmy
class kingw(bishopw):
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour        
        if self.number=="k1b":
                yposition,xposition=list_searchy(Board,self.number),list_searchx(Board,self.number)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,1,1,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,1,-1,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,-1,1,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,-1,-1,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,0,1,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,0,-1,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,1,0,all_white)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,-1,0,all_white)
                self.coords2.append([xposition*60+30,yposition*60+30])
                if moves2kb==0 and moves2r2b==0:
                    castle=True
                    for i in range (0,len(all_white)):
                        if 240==all_white[i][0] and 420==all_white[i][1] or 360==all_white[i][0] and 420==all_white[i][1] or 300==all_white[i][0] and 420==all_white[i][1]:
                            castle=False
                    if castle==True and Board[7][5][0]=="" and Board[7][6][0]=="":
                        self.coords.append([390,450])
                if moves2kb==0 and moves2r1b==0:
                    castle=True
                    for i in range (0,len(all_white)):
                        if 60==all_white[i][0] and 420==all_white[i][1] or 120==all_white[i][0] and 420==all_white[i][1] or 180==all_white[i][0] and 420==all_white[i][1] or 240==all_white[i][0] and 420==all_white[i][1]:
                            castle=False
                    if castle==True and Board[7][1][0]=="" and Board[7][2][0]=="" and Board[7][3][0]=="":
                        self.coords.append([150,450])                        
        if self.number=="k1w":
                yposition=list_searchy(Board,self.number)
                xposition=list_searchx(Board,self.number)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,1,1,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,1,-1,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,-1,1,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,-1,-1,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,0,1,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,0,-1,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,1,0,all_black)
                self.coords=king_moves(xposition,yposition,self.coords,Board,self.colour,-1,0,all_black)
                self.coords2.append([xposition*60+30,yposition*60+30])
                if moves2kw==0 and moves2r2w==0:
                    castle=True
                    for i in range (0,len(all_black)):
                        if 240==all_black[i][0] and 0==all_black[i][1] or 360==all_black[i][0] and 0==all_black[i][1] or 300==all_black[i][0] and 0==all_black[i][1]:
                            castle=False
                    if castle==True and Board[0][5][0]=="" and Board[0][6][0]=="":
                        self.coords.append([390,30])
                if moves2kw==0 and moves2r1w==0:
                    castle=True
                    for i in range (0,len(all_black)):
                        if 60==all_black[i][0] and 0==all_black[i][1] or 120==all_black[i][0] and 0==all_black[i][1] or 180==all_black[i][0] and 0==all_black[i][1] or 240==all_black[i][0] and 0==all_black[i][1]:
                            castle=False
                    if castle==True and Board[0][1][0]=="" and Board[0][2][0]=="" and Board[0][3][0]=="":
                        self.coords.append([150,30])

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
                    fv,tg,piece=1,1,("")
                else:
                    for k1 in range (0, len(self.coords)):
                        if ((roomx-(roomx%60))+30)==self.coords[k1][0] and ((roomy-(roomy%60))+30)==self.coords[k1][1]:
                                if self.coords[k1][0]==150 and self.coords[k1][1]==450 and moves2kb==0 and moves2r1b==0:
                                    Board[7][0][0],Board[7][0][1]="",""
                                    Board[7][3][0],Board[7][3][1]="r1b","b"
                                if self.coords[k1][0]==390 and self.coords[k1][1]==450 and moves2kb==0 and moves2r2b==0:
                                    Board[7][7][0],Board[7][7][1]="",""
                                    Board[7][5][0],Board[7][5][1]="r2b",""
                                if self.coords[k1][0]==150 and self.coords[k1][1]==30 and moves2kw==0 and moves2r1w==0:
                                    Board[0][0][0],Board[0][0][1]="",""
                                    Board[0][3][0],Board[0][3][1]="r1w","w"
                                if self.coords[k1][0]==390 and self.coords[k1][1]==30 and moves2kw==0 and moves2r2w==0:
                                    Board[0][7][0],Board[0][7][1]="",""
                                    Board[0][5][0],Board[0][5][1]="r2w","w"
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
                                Board[yposition][xposition][0],Board[yposition][xposition][1]="",""
                                Board[self.bwmy][self.bwmx][0],Board[self.bwmy][self.bwmx][1]="",""
                                Board[self.bwmy][self.bwmx][0],Board[self.bwmy][self.bwmx][1]=firstposition1,firstposition2
                                tg=2
                if fv==0:
                    tg=3
                    return tg
                if fv==1 or fv==2:
                    self.coords,self.coords2=[],[]
                    return tg
                
        else:
            return tg                   
class pawnw(bishopw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour,moves2):
        self.coords,self.coords2,self.bwmx,self.bwmy,self.number,self.colour=coords,coords2,bwmx,bwmy,number,colour
        self.moves2=moves2    
    def possible_moves(self,coords,coords2,colour,moves2,piece_backup,Checkmate_pass,pawn_2_spaces_move):
        self.colour=colour
        self.Checkmate_pass=Checkmate_pass
        self.pawn_2_spaces_move=pawn_2_spaces_move
        yposition=list_searchy(Board,self.number)
        xposition=list_searchx(Board,self.number)
        if xposition!=9:
            bo1mx,bo1my=self.bwmx,self.bwmy
            self.bwmx,self.bwmy=pygame.mouse.get_pos()
            if self.Checkmate_pass==True or self.bwmx>list_searchx(Board,self.number)*60 and self.bwmx<list_searchx(Board,self.number)*60+60 and self.bwmy>list_searchy(Board,self.number)*60 and self.bwmy<list_searchy(Board,self.number)*60+60:
                if self.number[2]=="b":
                    piece_backup="pawn"+self.number[1]+"b"
                else:
                    piece_backup="pawn"+self.number[1]
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
                        yposition=list_searchy(Board,self.number)
                        xposition=list_searchx(Board,self.number)
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
                        yposition=list_searchy(Board,self.number)
                        xposition=list_searchx(Board,self.number)
                        self.coords2.append([xposition*60+30,yposition*60+30])
                        if (yposition-1)<8 and xposition<8 and (yposition-1)>-1 and xposition>-1 and  (yposition-1)<8 and xposition<8  and Board[(yposition-1)][xposition][0]=="" :
                            self.coords.append([xposition*60+30,(yposition-1)*60+30])
                self.coords=Protectors(black_check,white_check,attack,self.coords,attack_positions,Board,two_protectors,self.colour,black_protector,self.number,white_protector)
                for i in range(0,len(self.pawn_2_spaces_move)):
                    if self.pawn_2_spaces_move[i][0]==self.number:
                        if self.number[2]=="b":
                            self.coords.append([((list_searchx(Board,self.pawn_2_spaces_move[i][1]))*60+30),(((list_searchy(Board,self.pawn_2_spaces_move[i][1]))-1)*60+30)])
                        if self.number[2]=="w":
                            self.coords.append([((list_searchx(Board,self.pawn_2_spaces_move[i][1]))*60+30),(((list_searchy(Board,self.pawn_2_spaces_move[i][1]))+1)*60+30)])
            else:
                self.bwmx,self.bwmy=bo1mx,bo1my
        return piece_backup,self.bwmx,self.bwmy
    def position(self,coords,coords2,bwmx,bwmy,number,pawn_2_spaces_move):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.pawn_2_spaces_move=pawn_2_spaces_move
        tg=0
        global queenb_moves
        global queenw_moves
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                roomx,roomy=(roomx-roomx%60)+30,(roomy-roomy%60)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece,tg,self.coords,self.coords2=(""),1,[],[]
                    return tg,self.pawn_2_spaces_move
                en_passant_pass=True
                for k1 in range (0,(len(self.coords)),1):
                    if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                        yposition,original_position=(list_searchy(Board,self.number)),(list_searchy(Board,self.number))
                        xposition=list_searchx(Board,self.number)
                        if self.number[2]=="w":
                            if int(((self.coords[k1][1])-30))==(yposition+1)*60 and int(((self.coords[k1][0])-30))==(xposition+1)*60 or int(((self.coords[k1][1])-30))==(yposition+1)*60 and int(((self.coords[k1][0])-30))==(xposition-1)*60:
                                if Board[int(((self.coords[k1][1])-30)/60)][int(((self.coords[k1][0])-30)/60)][1]=="":
                                    Board[yposition][xposition][0]=""
                                    Board[yposition][xposition][1]=""
                                    Board[int(((self.coords[k1][1])-90)/60)][int(((self.coords[k1][0])-30)/60)][0]=""
                                    Board[int(((self.coords[k1][1])-90)/60)][int(((self.coords[k1][0])-30)/60)][1]=""                               
                                    Board[int(roomy/60)][int(roomx/60)][0]=self.number
                                    Board[int(roomy/60)][int(roomx/60)][1]=self.number[2]
                                    fv,tg,self.pawn_2_spaces_move,en_passant_pass=2,2,[],False
                        if self.number[2]=="b":
                            if int(((self.coords[k1][1])-30))==(yposition-1)*60 and int(((self.coords[k1][0])-30))==(xposition+1)*60 or int(((self.coords[k1][1])-30))==(yposition-1)*60 and int(((self.coords[k1][0])-30))==(xposition-1)*60:
                                if Board[int(((self.coords[k1][1])-30)/60)][int(((self.coords[k1][0])-30)/60)][1]=="":
                                    Board[yposition][xposition][0]=""
                                    Board[yposition][xposition][1]=""
                                    Board[int(((self.coords[k1][1])+30)/60)][int(((self.coords[k1][0])-30)/60)][0]=""
                                    Board[int(((self.coords[k1][1])+30)/60)][int(((self.coords[k1][0])-30)/60)][1]=""                               
                                    Board[int(roomy/60)][int(roomx/60)][0]=self.number
                                    Board[int(roomy/60)][int(roomx/60)][1]=self.number[2]
                                    fv,tg,self.pawn_2_spaces_move,en_passant_pass=2,2,[],False
                        if roomy==30 and self.number[2]=="b":
                            Board[yposition][xposition][0]=""
                            Board[yposition][xposition][1]=""                                        
                            Board[(roomy-30)//60][(roomx-30)//60][0]="q"+str(queenb_moves+2)+"b"
                            Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                            queenb_moves=queenb_moves+1
                            fv=2
                            tg=2
                        elif roomy==450 and self.number[2]=="w":
                            Board[yposition][xposition][0]=""
                            Board[yposition][xposition][1]=""                                        
                            Board[(roomy-30)//60][(roomx-30)//60][0]="q"+str(queenw_moves+2)+"w"
                            Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                            queenw_moves=queenw_moves+1
                            fv=2
                            tg=2
                        elif en_passant_pass==True:
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
                            Board[yposition][xposition][0],Board[yposition][xposition][1]="",""
                            Board[self.bwmy][self.bwmx][0],Board[self.bwmy][self.bwmx][1]="",""
                            Board[self.bwmy][self.bwmx][0],Board[self.bwmy][self.bwmx][1]=firstposition1,firstposition2
                            tg=2
                        final_position=(list_searchy(Board,self.number))
                        if self.number[2]=="w" and original_position-final_position==-2 and (list_searchy(Board,self.number))>-1 and (list_searchy(Board,self.number))<8 and (list_searchx(Board,self.number))-1>-1 and (list_searchx(Board,self.number))-1<8:
                            if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0])!="":
                                if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0])[0]=="p" and (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0])[2]=="b":
                                    self.pawn_2_spaces_move.append([(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0]),(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))][0])])
                        if self.number[2]=="w" and original_position-final_position==-2 and (list_searchy(Board,self.number))>-1 and (list_searchy(Board,self.number))<8 and (list_searchx(Board,self.number))+1>-1 and (list_searchx(Board,self.number))+1<8:
                            if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0])!="":
                                if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0])[0]=="p" and (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0])[2]=="b":
                                    self.pawn_2_spaces_move.append([(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0]),(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))][0])])
                        if self.number[2]=="b" and original_position-final_position==2 and (list_searchy(Board,self.number))>-1 and (list_searchy(Board,self.number))<8 and (list_searchx(Board,self.number))-1>-1 and (list_searchx(Board,self.number))-1<8:
                            if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0])!="":
                                if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0])[0]=="p" and (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0])[2]=="w":
                                    self.pawn_2_spaces_move.append([(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))-1][0]),(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))][0])])
                        if self.number[2]=="b" and original_position-final_position==2 and (list_searchy(Board,self.number))>-1 and (list_searchy(Board,self.number))<8 and (list_searchx(Board,self.number))+1>-1 and (list_searchx(Board,self.number))+1<8:
                            if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0])!="":
                                if (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0])[0]=="p" and (Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0])[2]=="w":
                                    self.pawn_2_spaces_move.append([(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))+1][0]),(Board[(list_searchy(Board,self.number))][(list_searchx(Board,self.number))][0])])
                        if fv==1 or fv==2:
                            self.coords,self.coords2=[],[]
                            return tg,self.pawn_2_spaces_move
                return tg,self.pawn_2_spaces_move
                            
        else:
            return tg,self.pawn_2_spaces_move
class pawnb(pawnw):
    line_filler=1
def wait2():
    fgh=False
    pygame.event.clear()
    while fgh==False:
        event3=pygame.event.wait()
        if event3.type==pygame.MOUSEBUTTONDOWN:
            fgh=True
    return event3
class queen1(object):
    def __init__(self,q11,q12,q13,q14,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        self.q11,self.q12,self.q13,self.q14=q11,q12,q13,q14
        self.q15,self.q16,self.q17,self.q18=q15,q16,q17,q18
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,q11,q12,q13,q14,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        if self.vc[0]=="q" or self.vc[0]=="b":
            self.q11,self.q12,self.q13,self.q14=q11,q12,q13,q14
        if self.vc[0]=="q" or self.vc[0]=="r":
            self.q15,self.q16,self.q17,self.q18=q15,q16,q17,q18
        self.vc=vc
        global two_protectors
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            if self.vc[0]=="q" or self.vc[0]=="b":
                self.q11,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q11,Board,self.king,black_protector,two_protectors,self.colour2,1,1,1,1)
                self.q12,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q12,Board,self.king,black_protector,two_protectors,self.colour2,1,-1,1,-1)
                self.q13,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q13,Board,self.king,black_protector,two_protectors,self.colour2,-1,1,-1,1)
                self.q14,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q14,Board,self.king,black_protector,two_protectors,self.colour2,-1,-1,-1,-1)
            if self.vc[0]=="q" or self.vc[0]=="r":
                self.q15,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q15,Board,self.king,black_protector,two_protectors,self.colour2,1,0,1,0)
                self.q16,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q16,Board,self.king,black_protector,two_protectors,self.colour2,-1,0,-1,0)
                self.q17,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q17,Board,self.king,black_protector,two_protectors,self.colour2,0,1,0,1)
                self.q18,black_protector,two_protectors=queen1_attack(yposition,xposition,self.colour,self.q18,Board,self.king,black_protector,two_protectors,self.colour2,0,-1,0,-1)

class bishop1(queen1):
    def __init__(self,q11,q12,q13,q14,black_protector,vc,king,colour,colour2):
        self.q11,self.q12,self.q13,self.q14=q11,q12,q13,q14
        self.vc,self.king,self.colour,self.colour2,self.black_protector=vc,king,colour,colour2,black_protector
class knight1(object):
    def __init__(self,kn1,black_protector,vc,king,colour,colour2):
        self.kn1=kn1
        self.vc,self.king,self.colour,self.colour2,self.black_protector=vc,king,colour,colour2,black_protector
    def check(self,kn1,black_protector,vc,king,colour,colour2):
        self.kn1=kn1
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,1,2)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,1,-2)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,-1,2)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,-1,-2)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,2,1)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,2,-1)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,-2,1)
            knight1_attack(yposition,xposition,self.kn1,Board,self.colour,self.colour2,-2,-1)
class rook1(queen1):
    def __init__(self,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        self.q15,self.q16,self.q17,self.q18=q15,q16,q17,q18
        self.vc,self.king,self.colour,self.colour2,self.black_protector=vc,king,colour,colour2,black_protector
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
        self.colour=colour        
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,1,1)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,1,-1)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,-1,1)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,-1,-1)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,0,1)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,0,-1)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,1,0)
            knight1_attack(yposition,xposition,self.k1w,Board,self.colour,self.colour2,-1,0)
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
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            if (yposition+1)<8 and (xposition-1)<8 and (yposition+1)>-1 and (xposition-1)>-1 and Board[(yposition+1)][(xposition-1)][1]=="" or (yposition+1)<8 and (xposition-1)<8 and (yposition+1)>-1 and (xposition-1)>-1 and Board[(yposition+1)][(xposition-1)][1]==self.colour or (yposition+1)<8 and (xposition-1)<8 and (yposition+1)>-1 and (xposition-1)>-1 and Board[(yposition+1)][(xposition-1)][1]==self.colour2:
                self.p1.append([((xposition-1))*60,((yposition+1))*60])            
        if yposition!=9 or xposition!=9:
            if (yposition+1)<8 and (xposition+1)<8 and (yposition+1)>-1 and (xposition+1)>-1 and Board[(yposition+1)][(xposition+1)][1]=="" or (yposition+1)<8 and (xposition+1)<8 and (yposition+1)>-1 and (xposition+1)>-1 and Board[(yposition+1)][(xposition+1)][1]==self.colour or (yposition+1)<8 and (xposition+1)<8 and (yposition+1)>-1 and (xposition+1)>-1 and Board[(yposition+1)][(xposition+1)][1]==self.colour2:
                self.p1.append([((xposition+1))*60,((yposition+1))*60])  
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
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            if (yposition-1)<8 and (xposition+1)<8 and (yposition-1)>-1 and (xposition+1)>-1 and Board[(yposition-1)][(xposition+1)][1]=="" or (yposition-1)<8 and (xposition+1)<8 and (yposition-1)>-1 and (xposition+1)>-1 and Board[(yposition-1)][(xposition+1)][1]==self.colour or (yposition-1)<8 and (xposition+1)<8 and (yposition-1)>-1 and (xposition+1)>-1 and Board[(yposition-1)][(xposition+1)][1]==self.colour2:
                self.p1b.append([((xposition+1))*60,((yposition-1))*60])            
        if yposition!=9 or xposition!=9:
            if (yposition-1)<8 and (xposition-1)<8 and (yposition-1)>-1 and (xposition-1)>-1 and Board[(yposition-1)][(xposition-1)][1]=="" or (yposition-1)<8 and (xposition-1)<8 and (yposition-1)>-1 and (xposition-1)>-1 and Board[(yposition-1)][(xposition-1)][1]==self.colour or (yposition-1)<8 and (xposition-1)<8 and (yposition-1)>-1 and (xposition-1)>-1 and Board[(yposition-1)][(xposition-1)][1]==self.colour2:
                self.p1b.append([((xposition-1))*60,((yposition-1))*60]) 
class attack_class_and_all_white(object):
    def __init__(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        self.vc=vc
        self.attack_piece=attack_piece
        self.black_check=black_check
        self.attack=attack
        self.attack_positions=attack_positions
        self.all_white=all_white
    def attack_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        yposition=(list_searchy(Board,"k1b"))*60
        xposition=(list_searchx(Board,"k1b"))*60
        for ju in range (0,len(self.attack_piece)):
            if xposition==self.attack_piece[ju][0] and yposition==self.attack_piece[ju][1]:
                self.attack.append([self.vc])
                self.attack_positions=self.attack_piece
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
        return self.attack_positions,self.attack

class attack_class_and_all_black(attack_class_and_all_white):
    def __init__(self,vc,attack_piece,black_check,attack,attack_positions,all_black):
        self.vc=vc
        self.attack_piece=attack_piece
        self.black_check=black_check
        self.attack=attack
        self.attack_positions=attack_positions
        self.all_black=all_black
    def attack_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        yposition=(list_searchy(Board,"k1w"))*60
        xposition=(list_searchx(Board,"k1w"))*60
        for ju in range (0,len(self.attack_piece)):
            if xposition==self.attack_piece[ju][0] and yposition==self.attack_piece[ju][1]:
                self.attack.append([self.vc])
                self.attack_positions=self.attack_piece
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
        return self.attack_positions,self.attack
    
def convertx(piecex):
    return piecex-(piecex%60)
def converty(piecey):
    return piecey-(piecey%60)
def position_display(x,y,piece,piece_display):
    if (list_searchy(Board,piece))!=9:
        gameDisplay.blit(piece_display,(x,y))
    else:
        gameDisplay.blit(piece_display,(481,481))
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
    position_display(k1bmx,k1bmy,"k1b",king_black)
    position_display(k1wmx,k1wmy,"k1w",king_white)
    position_display(q1bmx,q1bmy,"q1b",queen_black)
    position_display(q2bmx,q2bmy,"q2b",queen_black2)
    position_display(q3bmx,q3bmy,"q3b",queen_black3)
    position_display(q4bmx,q4bmy,"q4b",queen_black4)
    position_display(r1bmx,r1bmy,"r1b",rook_black1)
    position_display(r2bmx,r2bmy,"r2b",rook_black2)
    position_display(b1bmx,b1bmy,"b1b",bishop_black1)
    position_display(b2bmx,b2bmy,"b2b",bishop_black2)
    position_display(kn1bmx,kn1bmy,"kn1b",knight_black1)
    position_display(kn2bmx,kn2bmy,"kn2b",knight_black2)
    position_display(p1bmx,p1bmy,"p1b",pawn_black1)
    position_display(p2bmx,p2bmy,"p2b",pawn_black2)
    position_display(p3bmx,p3bmy,"p3b",pawn_black3)
    position_display(p4bmx,p4bmy,"p4b",pawn_black4)
    position_display(p5bmx,p5bmy,"p5b",pawn_black5)
    position_display(p6bmx,p6bmy,"p6b",pawn_black6)
    position_display(p7bmx,p7bmy,"p7b",pawn_black7)
    position_display(p8bmx,p8bmy,"p8b",pawn_black8)
    position_display(q1wmx,q1wmy,"q1w",queen_white)
    position_display(q2wmx,q2wmy,"q2w",queen_white2)
    position_display(q3wmx,q3wmy,"q3w",queen_white3)
    position_display(q4wmx,q4wmy,"q4w",queen_white4)
    position_display(r1wmx,r1wmy,"r1w",rook_white1)
    position_display(r2wmx,r2wmy,"r2w",rook_white2)
    position_display(b1wmx,b1wmy,"b1w",bishop_white1)
    position_display(b2wmx,b2wmy,"b2w",bishop_white2)
    position_display(kn1wmx,kn1wmy,"kn1w",knight_white1)
    position_display(kn2wmx,kn2wmy,"kn2w",knight_white2)
    position_display(p1wmx,p1wmy,"p1w",pawn_white1)
    position_display(p2wmx,p2wmy,"p2w",pawn_white2)
    position_display(p3wmx,p3wmy,"p3w",pawn_white3)
    position_display(p4wmx,p4wmy,"p4w",pawn_white4)
    position_display(p5wmx,p5wmy,"p5w",pawn_white5)
    position_display(p6wmx,p6wmy,"p6w",pawn_white6)
    position_display(p7wmx,p7wmy,"p7w",pawn_white7)
    position_display(p8wmx,p8wmy,"p8w",pawn_white8)    
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
def attack_append(piece,attack,Board,piece_attack):
    if piece[len(piece)-1]=="w":
        yposition,xposition=(list_searchy(Board,"k1b"))*60,(list_searchx(Board,"k1b")*60)
    else:
        yposition,xposition=(list_searchy(Board,"k1w"))*60,(list_searchx(Board,"k1w")*60)
    for ju in range (0,len(piece_attack)):
        if xposition==piece_attack[ju][0] and yposition==piece_attack[ju][1]:
            attack.append([piece])
    return attack
def all_white_append(piece_attack,all_white):
    for i in range (0,len(piece_attack)):
        if piece_attack!=[]:
            all_white.append(piece_attack[i])
    return all_white
def piece_place(piece,b1wmx,b1wmy,hb,white_check,moves,rfv,coords,coords2,vc,piece2,class_piece):
    if piece==piece2:
        b1wmx,b1wmy=pygame.mouse.get_pos()
        tg=class_piece.position(coords,coords2,convertx(b1wmx),converty(b1wmy),vc)                    
        if tg==2:
            hb,white_check,moves=0,False,moves+1
        if tg==3 or tg==2 or tg==1:
            coords,coords2,piece,rfv,b1wmx,b1wmy=[],[],"",1,(list_searchx(Board,vc))*60,(list_searchy(Board,vc))*60
    return piece,b1wmx,b1wmy,hb,white_check,moves,rfv,coords,coords2,vc,class_piece

def piece_place_pawn(piece,b1wmx,b1wmy,hb,white_check,moves,rfv,coords,coords2,vc,piece2,class_piece,pawn_2_spaces_move,moves21):
    if piece==piece2:
        b1wmx,b1wmy=pygame.mouse.get_pos()
        tg,pawn_2_spaces_move=class_piece.position(coords,coords2,convertx(b1wmx),converty(b1wmy),vc,pawn_2_spaces_move)                    
        if tg==2:
            hb,white_check,moves,moves21=0,False,moves+1,moves21+1
        if tg==3 or tg==2 or tg==1:
            coords,coords2,piece,rfv,b1wmx,b1wmy=[],[],"",1,(list_searchx(Board,vc))*60,(list_searchy(Board,vc))*60
    return piece,b1wmx,b1wmy,hb,white_check,moves,rfv,coords,coords2,vc,class_piece,pawn_2_spaces_move,moves21


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
pawn_2_spaces_move=[]
pos_spaces=[]
two_protectors=False

b11,b12,b13,b14=[],[],[],[]
b21,b22,b23,b24=[],[],[],[]
r11,r12,r13,r14=[],[],[],[]
r21,r22,r23,r24=[],[],[],[]
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
r11b,r12b,r13b,r14b=[],[],[],[]
r21b,r22b,r23b,r24b=[],[],[],[]
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
        r11,r12,r13,r14=[],[],[],[]
        r21,r22,r23,r24=[],[],[],[]
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
        r11b,r12b,r13b,r14b=[],[],[],[]
        r21b,r22b,r23b,r24b=[],[],[],[]
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
            Bishop1w2.check(b11,b12,b13,b14,"a","a","a","a",black_protector,"b1w","k1b","b","w") 
            Bishop2w2=bishop1(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")
            Bishop2w2.check(b21,b22,b23,b24,"a","a","a","a",black_protector,"b2w","k1b","b","w")
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
            knight2w2=knight1(kn2,black_protector,"kn2w","k1b","b","w")
            knight2w2.check(kn2,black_protector,"kn2w","k1b","b","w")
            Rook1w2=rook1(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")
            Rook1w2.check("a","a","a","a",r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")
            Rook2w2=rook1(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")
            Rook2w2.check("a","a","a","a",r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")
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

            attack_positions,attack=[],[]
            yposition,xposition=(list_searchy(Board,"k1b"))*60,(list_searchx(Board,"k1b")*60)
            
            Rook11w_attack=attack_class_and_all_white("r1w",r11,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook11w_attack.attack_class1("r1w",r11,black_check,attack,attack_positions,all_white)
            Rook12w_attack=attack_class_and_all_white("r1w",r12,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook12w_attack.attack_class1("r1w",r12,black_check,attack,attack_positions,all_white)
            Rook13w_attack=attack_class_and_all_white("r1w",r13,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook13w_attack.attack_class1("r1w",r13,black_check,attack,attack_positions,all_white)
            Rook14w_attack=attack_class_and_all_white("r1w",r14,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook14w_attack.attack_class1("r1w",r14,black_check,attack,attack_positions,all_white)

            Rook21w_attack=attack_class_and_all_white("r2w",r21,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook21w_attack.attack_class1("r1w",r21,black_check,attack,attack_positions,all_white)
            Rook22w_attack=attack_class_and_all_white("r2w",r22,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook22w_attack.attack_class1("r2w",r22,black_check,attack,attack_positions,all_white)
            Rook23w_attack=attack_class_and_all_white("r2w",r23,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook23w_attack.attack_class1("r1w",r23,black_check,attack,attack_positions,all_white)
            Rook24w_attack=attack_class_and_all_white("r2w",r24,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Rook24w_attack.attack_class1("r1w",r24,black_check,attack,attack_positions,all_white)

            Bishop11w_attack=attack_class_and_all_white("b1w",b11,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop11w_attack.attack_class1("b1w",b11,black_check,attack,attack_positions,all_white)
            Bishop12w_attack=attack_class_and_all_white("b1w",b12,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop12w_attack.attack_class1("b1w",b12,black_check,attack,attack_positions,all_white)
            Bishop13w_attack=attack_class_and_all_white("b1w",b13,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop13w_attack.attack_class1("b1w",b13,black_check,attack,attack_positions,all_white)
            Bishop14w_attack=attack_class_and_all_white("b1w",b14,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop14w_attack.attack_class1("b1w",b14,black_check,attack,attack_positions,all_white)
                    
            Bishop21w_attack=attack_class_and_all_white("b2w",b21,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop21w_attack.attack_class1("b2w",b21,black_check,attack,attack_positions,all_white)
            Bishop22w_attack=attack_class_and_all_white("b2w",b22,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop22w_attack.attack_class1("b2w",b22,black_check,attack,attack_positions,all_white)
            Bishop23w_attack=attack_class_and_all_white("b2w",b23,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop23w_attack.attack_class1("b2w",b23,black_check,attack,attack_positions,all_white)
            Bishop24w_attack=attack_class_and_all_white("b2w",b24,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Bishop24w_attack.attack_class1("b2w",b24,black_check,attack,attack_positions,all_white)

            Queen11w_attack=attack_class_and_all_white("q1w",q11,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen11w_attack.attack_class1("q1w",q11,black_check,attack,attack_positions,all_white)
            Queen12w_attack=attack_class_and_all_white("q1w",q12,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen12w_attack.attack_class1("q1w",q12,black_check,attack,attack_positions,all_white)
            Queen13w_attack=attack_class_and_all_white("q1w",q13,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen13w_attack.attack_class1("q1w",q13,black_check,attack,attack_positions,all_white)
            Queen14w_attack=attack_class_and_all_white("q1w",q14,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen14w_attack.attack_class1("q1w",q14,black_check,attack,attack_positions,all_white)
            Queen15w_attack=attack_class_and_all_white("q1w",q15,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen15w_attack.attack_class1("q1w",q15,black_check,attack,attack_positions,all_white)
            Queen16w_attack=attack_class_and_all_white("q1w",q16,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen16w_attack.attack_class1("q1w",q16,black_check,attack,attack_positions,all_white)
            Queen17w_attack=attack_class_and_all_white("q1w",q17,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen17w_attack.attack_class1("q1w",q17,black_check,attack,attack_positions,all_white)
            Queen18w_attack=attack_class_and_all_white("q1w",q18,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen18w_attack.attack_class1("q1w",q18,black_check,attack,attack_positions,all_white)

            Queen21w_attack=attack_class_and_all_white("q2w",q21,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen21w_attack.attack_class1("q2w",q21,black_check,attack,attack_positions,all_white)
            Queen22w_attack=attack_class_and_all_white("q2w",q22,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen22w_attack.attack_class1("q2w",q22,black_check,attack,attack_positions,all_white)
            Queen23w_attack=attack_class_and_all_white("q2w",q23,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen23w_attack.attack_class1("q2w",q23,black_check,attack,attack_positions,all_white)
            Queen24w_attack=attack_class_and_all_white("q2w",q24,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen24w_attack.attack_class1("q2w",q24,black_check,attack,attack_positions,all_white)
            Queen25w_attack=attack_class_and_all_white("q2w",q25,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen25w_attack.attack_class1("q2w",q25,black_check,attack,attack_positions,all_white)
            Queen26w_attack=attack_class_and_all_white("q2w",q26,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen26w_attack.attack_class1("q2w",q26,black_check,attack,attack_positions,all_white)
            Queen27w_attack=attack_class_and_all_white("q2w",q27,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen27w_attack.attack_class1("q2w",q27,black_check,attack,attack_positions,all_white)
            Queen28w_attack=attack_class_and_all_white("q2w",q28,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen28w_attack.attack_class1("q2w",q28,black_check,attack,attack_positions,all_white)
            
            Queen31w_attack=attack_class_and_all_white("q3w",q31,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen31w_attack.attack_class1("q3w",q31,black_check,attack,attack_positions,all_white)
            Queen32w_attack=attack_class_and_all_white("q3w",q32,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen32w_attack.attack_class1("q3w",q32,black_check,attack,attack_positions,all_white)
            Queen33w_attack=attack_class_and_all_white("q3w",q33,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen33w_attack.attack_class1("q3w",q33,black_check,attack,attack_positions,all_white)
            Queen34w_attack=attack_class_and_all_white("q3w",q34,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen34w_attack.attack_class1("q3w",q34,black_check,attack,attack_positions,all_white)
            Queen35w_attack=attack_class_and_all_white("q3w",q35,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen35w_attack.attack_class1("q3w",q35,black_check,attack,attack_positions,all_white)
            Queen36w_attack=attack_class_and_all_white("q3w",q36,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen36w_attack.attack_class1("q3w",q36,black_check,attack,attack_positions,all_white)
            Queen37w_attack=attack_class_and_all_white("q3w",q37,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen37w_attack.attack_class1("q3w",q37,black_check,attack,attack_positions,all_white)
            Queen38w_attack=attack_class_and_all_white("q3w",q38,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen38w_attack.attack_class1("q3w",q38,black_check,attack,attack_positions,all_white)
            
            Queen41w_attack=attack_class_and_all_white("q4w",q41,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen41w_attack.attack_class1("q4w",q41,black_check,attack,attack_positions,all_white)
            Queen42w_attack=attack_class_and_all_white("q4w",q42,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen42w_attack.attack_class1("q4w",q42,black_check,attack,attack_positions,all_white)
            Queen43w_attack=attack_class_and_all_white("q4w",q43,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen43w_attack.attack_class1("q4w",q43,black_check,attack,attack_positions,all_white)
            Queen44w_attack=attack_class_and_all_white("q4w",q44,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen44w_attack.attack_class1("q4w",q44,black_check,attack,attack_positions,all_white)
            Queen45w_attack=attack_class_and_all_white("q4w",q45,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen45w_attack.attack_class1("q4w",q45,black_check,attack,attack_positions,all_white)
            Queen46w_attack=attack_class_and_all_white("q4w",q46,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen46w_attack.attack_class1("q4w",q46,black_check,attack,attack_positions,all_white)
            Queen47w_attack=attack_class_and_all_white("q4w",q47,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen47w_attack.attack_class1("q4w",q47,black_check,attack,attack_positions,all_white)
            Queen48w_attack=attack_class_and_all_white("q4w",q48,black_check,attack,attack_positions,all_white)
            attack_positions,attack=Queen48w_attack.attack_class1("q4w",q48,black_check,attack,attack_positions,all_white)

            attack=attack_append("kn1w",attack,Board,kn1)
            attack=attack_append("kn2w",attack,Board,kn2)
            attack=attack_append("p1w",attack,Board,p1)
            attack=attack_append("p2w",attack,Board,p2)
            attack=attack_append("p3w",attack,Board,p3)
            attack=attack_append("p4w",attack,Board,p4)
            attack=attack_append("p5w",attack,Board,p5)
            attack=attack_append("p6w",attack,Board,p6)
            attack=attack_append("p7w",attack,Board,p7)
            attack=attack_append("p8w",attack,Board,p8)

            if attack!=[]:
                black_check=True
            all_white=all_white_append(k1w,all_white)
            all_white=all_white_append(kn1,all_white)
            all_white=all_white_append(kn2,all_white)
            all_white=all_white_append(p1,all_white)
            all_white=all_white_append(p2,all_white)
            all_white=all_white_append(p3,all_white)
            all_white=all_white_append(p4,all_white)
            all_white=all_white_append(p5,all_white)
            all_white=all_white_append(p6,all_white)
            all_white=all_white_append(p7,all_white)
            all_white=all_white_append(p8,all_white)
            hb=1
            
        if hw==0:
            two_protectors=False
            white_protector=[]
            pos_spaces=[]
            all_black=[]
            Bishop1b2=bishop1(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
            Bishop1b2.check(b11b,b12b,b13b,b14b,"a","a","a","a",white_protector,"b1b","k1w","w","b")    
            Bishop2b2=bishop1(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")
            Bishop2b2.check(b21b,b22b,b23b,b24b,"a","a","a","a",white_protector,"b2b","k1w","w","b")
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
            knight2b2=knight1(kn2b,white_protector,"kn2b","k1w","w","b")
            knight2b2.check(kn2b,white_protector,"kn2b","k1w","w","b")
            Rook1b2=rook1(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")
            Rook1b2.check("a","a","a","a",r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")
            Rook2b2=rook1(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")
            Rook2b2.check("a","a","a","a",r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")
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

            yposition,xposition=(list_searchy(Board,"k1w"))*60,(list_searchx(Board,"k1w"))*60
            attack,attack_positions=[],[]

            Rook11b_attack=attack_class_and_all_black("r1b",r11b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook11b_attack.attack_class1("r1b",r11b,white_check,attack,attack_positions,all_black)
            Rook12b_attack=attack_class_and_all_black("r1b",r12b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook12b_attack.attack_class1("r1b",r12b,white_check,attack,attack_positions,all_black)
            Rook13b_attack=attack_class_and_all_black("r1b",r13b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook13b_attack.attack_class1("r1b",r13b,white_check,attack,attack_positions,all_black)
            Rook14b_attack=attack_class_and_all_black("r1b",r14b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook14b_attack.attack_class1("r1b",r14b,white_check,attack,attack_positions,all_black)
                    
            Rook21b_attack=attack_class_and_all_black("r2b",r21b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook21b_attack.attack_class1("r2b",r21b,white_check,attack,attack_positions,all_black)
            Rook22b_attack=attack_class_and_all_black("r2b",r22b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook22b_attack.attack_class1("r2b",r22b,white_check,attack,attack_positions,all_black)
            Rook23b_attack=attack_class_and_all_black("r2b",r23b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook23b_attack.attack_class1("r2b",r23b,white_check,attack,attack_positions,all_black)
            Rook24b_attack=attack_class_and_all_black("r2b",r24b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Rook24b_attack.attack_class1("r2b",r24b,white_check,attack,attack_positions,all_black)
                    
            Bishop11b_attack=attack_class_and_all_black("b1b",b11b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop11b_attack.attack_class1("b1b",b11b,white_check,attack,attack_positions,all_black)
            Bishop12b_attack=attack_class_and_all_black("b1b",b12b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop12b_attack.attack_class1("b1b",b12b,white_check,attack,attack_positions,all_black)
            Bishop13b_attack=attack_class_and_all_black("b1b",b13b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop13b_attack.attack_class1("b1b",b13b,white_check,attack,attack_positions,all_black)
            Bishop14b_attack=attack_class_and_all_black("b1b",b14b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop14b_attack.attack_class1("b1b",b14b,white_check,attack,attack_positions,all_black)
                    
            Bishop21b_attack=attack_class_and_all_black("b2b",b21b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop21b_attack.attack_class1("b2b",b21b,white_check,attack,attack_positions,all_black)
            Bishop22b_attack=attack_class_and_all_black("b2b",b22b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop22b_attack.attack_class1("b2b",b22b,white_check,attack,attack_positions,all_black)
            Bishop23b_attack=attack_class_and_all_black("b2b",b23b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop23b_attack.attack_class1("b2b",b23b,white_check,attack,attack_positions,all_black)
            Bishop24b_attack=attack_class_and_all_black("b2b",b24b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Bishop24b_attack.attack_class1("b2b",b24b,white_check,attack,attack_positions,all_black)

            Queen11b_attack=attack_class_and_all_black("q1b",q11b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen11b_attack.attack_class1("q1b",q11b,white_check,attack,attack_positions,all_black)
            Queen12b_attack=attack_class_and_all_black("q1b",q12b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen12b_attack.attack_class1("q1b",q12b,white_check,attack,attack_positions,all_black)
            Queen13b_attack=attack_class_and_all_black("q1b",q13b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen13b_attack.attack_class1("q1b",q13b,white_check,attack,attack_positions,all_black)
            Queen14b_attack=attack_class_and_all_black("q1b",q14b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen14b_attack.attack_class1("q1b",q14b,white_check,attack,attack_positions,all_black)
            Queen15b_attack=attack_class_and_all_black("q1b",q15b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen15b_attack.attack_class1("q1b",q15b,white_check,attack,attack_positions,all_black)
            Queen16b_attack=attack_class_and_all_black("q1b",q16b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen16b_attack.attack_class1("q1b",q16b,white_check,attack,attack_positions,all_black)
            Queen17b_attack=attack_class_and_all_black("q1b",q17b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen17b_attack.attack_class1("q1b",q17b,white_check,attack,attack_positions,all_black)
            Queen18b_attack=attack_class_and_all_black("q1b",q18b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen18b_attack.attack_class1("q1b",q18b,white_check,attack,attack_positions,all_black)
            
            Queen21b_attack=attack_class_and_all_black("q2b",q21b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen21b_attack.attack_class1("q2b",q21b,white_check,attack,attack_positions,all_black)
            Queen22b_attack=attack_class_and_all_black("q2b",q22b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen22b_attack.attack_class1("q2b",q22b,white_check,attack,attack_positions,all_black)
            Queen23b_attack=attack_class_and_all_black("q2b",q23b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen23b_attack.attack_class1("q2b",q23b,white_check,attack,attack_positions,all_black)
            Queen24b_attack=attack_class_and_all_black("q2b",q24b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen24b_attack.attack_class1("q2b",q24b,white_check,attack,attack_positions,all_black)
            Queen25b_attack=attack_class_and_all_black("q2b",q25b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen25b_attack.attack_class1("q2b",q25b,white_check,attack,attack_positions,all_black)
            Queen26b_attack=attack_class_and_all_black("q2b",q26b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen26b_attack.attack_class1("q2b",q26b,white_check,attack,attack_positions,all_black)
            Queen27b_attack=attack_class_and_all_black("q2b",q27b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen27b_attack.attack_class1("q2b",q27b,white_check,attack,attack_positions,all_black)
            Queen28b_attack=attack_class_and_all_black("q2b",q28b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen28b_attack.attack_class1("q2b",q28b,white_check,attack,attack_positions,all_black)

            Queen31b_attack=attack_class_and_all_black("q3b",q31b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen31b_attack.attack_class1("q3b",q31b,white_check,attack,attack_positions,all_black)
            Queen32b_attack=attack_class_and_all_black("q3b",q32b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen32b_attack.attack_class1("q3b",q32b,white_check,attack,attack_positions,all_black)
            Queen33b_attack=attack_class_and_all_black("q3b",q33b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen33b_attack.attack_class1("q3b",q33b,white_check,attack,attack_positions,all_black)
            Queen34b_attack=attack_class_and_all_black("q3b",q34b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen34b_attack.attack_class1("q3b",q34b,white_check,attack,attack_positions,all_black)
            Queen35b_attack=attack_class_and_all_black("q3b",q35b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen35b_attack.attack_class1("q3b",q35b,white_check,attack,attack_positions,all_black)
            Queen36b_attack=attack_class_and_all_black("q3b",q36b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen36b_attack.attack_class1("q3b",q36b,white_check,attack,attack_positions,all_black)
            Queen37b_attack=attack_class_and_all_black("q3b",q37b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen37b_attack.attack_class1("q3b",q37b,white_check,attack,attack_positions,all_black)
            Queen38b_attack=attack_class_and_all_black("q3b",q38b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen38b_attack.attack_class1("q3b",q38b,white_check,attack,attack_positions,all_black)
            
            Queen41b_attack=attack_class_and_all_black("q1b",q41b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen41b_attack.attack_class1("q1b",q41b,white_check,attack,attack_positions,all_black)
            Queen42b_attack=attack_class_and_all_black("q1b",q42b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen42b_attack.attack_class1("q1b",q42b,white_check,attack,attack_positions,all_black)
            Queen43b_attack=attack_class_and_all_black("q1b",q43b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen43b_attack.attack_class1("q1b",q43b,white_check,attack,attack_positions,all_black)
            Queen44b_attack=attack_class_and_all_black("q1b",q44b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen44b_attack.attack_class1("q1b",q44b,white_check,attack,attack_positions,all_black)
            Queen45b_attack=attack_class_and_all_black("q1b",q45b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen45b_attack.attack_class1("q1b",q45b,white_check,attack,attack_positions,all_black)
            Queen46b_attack=attack_class_and_all_black("q1b",q46b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen46b_attack.attack_class1("q1b",q46b,white_check,attack,attack_positions,all_black)
            Queen47b_attack=attack_class_and_all_black("q1b",q47b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen47b_attack.attack_class1("q1b",q47b,white_check,attack,attack_positions,all_black)
            Queen48b_attack=attack_class_and_all_black("q1b",q48b,white_check,attack,attack_positions,all_black)
            attack_positions,attack=Queen48b_attack.attack_class1("q1b",q48b,white_check,attack,attack_positions,all_black)
            
            attack=attack_append("kn1b",attack,Board,kn1b)
            attack=attack_append("kn2b",attack,Board,kn2b)
            attack=attack_append("p1b",attack,Board,p1b)
            attack=attack_append("p2b",attack,Board,p2b)
            attack=attack_append("p3b",attack,Board,p3b)
            attack=attack_append("p4b",attack,Board,p4b)
            attack=attack_append("p5b",attack,Board,p5b)
            attack=attack_append("p6b",attack,Board,p6b)
            attack=attack_append("p7b",attack,Board,p7b)
            attack=attack_append("p8b",attack,Board,p8b)
            if attack!=[]:
                white_check=True
            all_black=all_white_append(k1b,all_black)
            all_black=all_white_append(kn1b,all_black)
            all_black=all_white_append(kn2b,all_black)
            all_black=all_white_append(p1b,all_black)
            all_black=all_white_append(p2b,all_black)
            all_black=all_white_append(p3b,all_black)
            all_black=all_white_append(p4b,all_black)
            all_black=all_white_append(p5b,all_black)
            all_black=all_white_append(p6b,all_black)
            all_black=all_white_append(p7b,all_black)
            all_black=all_white_append(p8b,all_black)
            hw=1
        white_stalemate=False
        white_checkmate=False
        coords_backup=coords
        coords_backup2=coords2
        if moves==0:
            coords=[]
            coords2=[]
            Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
            Bishop1w.possible_moves(coords,coords2,"b",piece,True)
            Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
            Bishop2w.possible_moves(coords,coords2,"b",piece,True)
            Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
            Rook1w.possible_moves(coords,coords2,"b",piece,True)
            Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
            Rook2w.possible_moves(coords,coords2,"b",piece,True)
            Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
            Knight1w.possible_moves(coords,coords2,"b",piece,True)
            Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
            Knight2w.possible_moves(coords,coords2,"b",piece,True)
            Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
            Queen1w.possible_moves(coords,coords2,"b",piece,True)
            Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
            Queen2w.possible_moves(coords,coords2,"b",piece,True)
            Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
            Queen3w.possible_moves(coords,coords2,"b",piece,True)
            Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
            Queen4w.possible_moves(coords,coords2,"b",piece,True)
            Pawn1w11=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
            Pawn1w11.possible_moves(coords,coords2,"b",moves21,piece,True,pawn_2_spaces_move)
            Pawn2w11=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
            Pawn2w11.possible_moves(coords,coords2,"b",moves22,piece,True,pawn_2_spaces_move)
            Pawn3w11=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
            Pawn3w11.possible_moves(coords,coords2,"b",moves23,piece,True,pawn_2_spaces_move)
            Pawn4w11=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
            Pawn4w11.possible_moves(coords,coords2,"b",moves24,piece,True,pawn_2_spaces_move)
            Pawn5w11=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
            Pawn5w11.possible_moves(coords,coords2,"b",moves25,piece,True,pawn_2_spaces_move)
            Pawn6w11=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
            Pawn6w11.possible_moves(coords,coords2,"b",moves26,piece,True,pawn_2_spaces_move)
            Pawn7w11=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
            Pawn7w11.possible_moves(coords,coords2,"b",moves27,piece,True,pawn_2_spaces_move)
            Pawn8w11=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
            Pawn8w11.possible_moves(coords,coords2,"b",moves28,piece,True,pawn_2_spaces_move)
            King1w=kingw(coords,coords2,k1wmx,k1wmy,"k1w","b")
            King1w.possible_moves(coords,coords2,"b")
            if coords==[] and white_check==True:
                white_checkmate=True
            if coords==[] and white_check==False:
                white_stalemate=True                
            coords=[]
            coords2=[]
        num_of_pieces=0
        for i in range(0,8):
            for a in range(0,8):
                if Board[i][a][0]!="":
                    num_of_pieces=num_of_pieces+1
        if num_of_pieces==2:
            black_stalemate=True
        if moves==1:
            coords=[]
            coords2=[]
            Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
            Bishop1b.possible_moves(coords,coords2,"w",piece,True)
            Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
            Bishop2b.possible_moves(coords,coords2,"w",piece,True)
            Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
            Rook1b.possible_moves(coords,coords2,"w",piece,True)
            Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
            Rook2b.possible_moves(coords,coords2,"w",piece,True)
            Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
            Knight1b.possible_moves(coords,coords2,"w",piece,True)
            Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
            Knight2b.possible_moves(coords,coords2,"w",piece,True)
            Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
            Queen1b.possible_moves(coords,coords2,"w",piece,True)
            Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
            Queen2b.possible_moves(coords,coords2,"w",piece,True)
            Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
            Queen3b.possible_moves(coords,coords2,"w",piece,True)
            Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
            Queen4b.possible_moves(coords,coords2,"w",piece,True)
            Pawn1b11=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
            Pawn1b11.possible_moves(coords,coords2,"w",moves21b,piece,True,pawn_2_spaces_move)
            Pawn2b11=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
            Pawn2b11.possible_moves(coords,coords2,"w",moves22b,piece,True,pawn_2_spaces_move)
            Pawn3b11=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
            Pawn3b11.possible_moves(coords,coords2,"w",moves23b,piece,True,pawn_2_spaces_move)
            Pawn4b11=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
            Pawn4b11.possible_moves(coords,coords2,"w",moves24b,piece,True,pawn_2_spaces_move)
            Pawn5b11=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
            Pawn5b11.possible_moves(coords,coords2,"w",moves25b,piece,True,pawn_2_spaces_move)
            Pawn6b11=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
            Pawn6b11.possible_moves(coords,coords2,"w",moves26b,piece,True,pawn_2_spaces_move)
            Pawn7b11=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
            Pawn7b11.possible_moves(coords,coords2,"w",moves27b,piece,True,pawn_2_spaces_move)
            Pawn8b11=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
            Pawn8b11.possible_moves(coords,coords2,"w",moves28b,piece,True,pawn_2_spaces_move)
            King1b=kingw(coords,coords2,k1bmx,k1bmy,"k1b","w")
            King1b.possible_moves(coords,coords2,"w")
            if coords==[] and black_check==True:
                black_checkmate=True
            if coords==[] and black_check==False:
                black_stalemate=True
                
            coords,coords2=[],[]
        coords,coords2=coords_backup,coords_backup2
        if Check_screen==True:
            black_checkmate,white_checkmate=False,False
            black_stalemate,white_stalemate=False,False
        if black_checkmate==True or white_checkmate==True or black_stalemate==True or white_stalemate==True:
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            if black_stalemate==True or white_stalemate==True:
                gameDisplay.blit(stalemate,(127,128))
            else:
                gameDisplay.blit(checkmate,(17,173))
            pygame.display.update()
            pygame.time.delay(1000)
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    Check_screen=True
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)                    
            pygame.display.update()
            pygame.time.delay(500)
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    Check_screen=True
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
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":                    
                    Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                    piece,b1wmx,b1wmy=Bishop1w.possible_moves(coords,coords2,"b",piece,False)
                    Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                    piece,b2wmx,b2wmy=Bishop2w.possible_moves(coords,coords2,"b",piece,False)
                    Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                    piece,kn1wmx,kn1wmy=Knight1w.possible_moves(coords,coords2,"b",piece,False)
                    Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                    piece,kn2wmx,kn2wmy=Knight2w.possible_moves(coords,coords2,"b",piece,False)
                    Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                    piece,r1wmx,r1wmy=Rook1w.possible_moves(coords,coords2,"b",piece,False)
                    Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                    piece,r2wmx,r2wmy=Rook2w.possible_moves(coords,coords2,"b",piece,False)
                    Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                    piece,q1wmx,q1wmy=Queen1w.possible_moves(coords,coords2,"b",piece,False)
                    Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                    piece,q2wmx,q2wmy=Queen2w.possible_moves(coords,coords2,"b",piece,False)
                    Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                    piece,q3wmx,q3wmy=Queen3w.possible_moves(coords,coords2,"b",piece,False)
                    Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                    piece,q4wmx,q4wmy=Queen4w.possible_moves(coords,coords2,"b",piece,False)
                    Pawn1w=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                    piece,p1wmx,p1wmy=Pawn1w.possible_moves(coords,coords2,"b",moves21,piece,False,pawn_2_spaces_move)
                    Pawn2w=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                    piece,p2wmx,p2wmy=Pawn2w.possible_moves(coords,coords2,"b",moves22,piece,False,pawn_2_spaces_move)
                    Pawn3w=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                    piece,p3wmx,p3wmy=Pawn3w.possible_moves(coords,coords2,"b",moves23,piece,False,pawn_2_spaces_move)
                    Pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                    piece,p4wmx,p4wmy=Pawn4w.possible_moves(coords,coords2,"b",moves24,piece,False,pawn_2_spaces_move)
                    Pawn5w=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                    piece,p5wmx,p5wmy=Pawn5w.possible_moves(coords,coords2,"b",moves25,piece,False,pawn_2_spaces_move)
                    Pawn6w=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                    piece,p6wmx,p6wmy=Pawn6w.possible_moves(coords,coords2,"b",moves26,piece,False,pawn_2_spaces_move)
                    Pawn7w=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                    piece,p7wmx,p7wmy=Pawn7w.possible_moves(coords,coords2,"b",moves27,piece,False,pawn_2_spaces_move)
                    Pawn8w=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                    piece,p8wmx,p8wmy=Pawn8w.possible_moves(coords,coords2,"b",moves28,piece,False,pawn_2_spaces_move)
                    ko1mx,ko1my=k1wmx,k1wmy
                    vc="k1w"
                    k1wmx,k1wmy=pygame.mouse.get_pos()
                    if k1wmx>list_searchx(Board,"k1w")*60 and k1wmx<list_searchx(Board,"k1w")*60+60 and k1wmy>list_searchy(Board,"k1w")*60 and k1wmy<list_searchy(Board,"k1w")*60+60:
                        piece="king1"
                        King1w=kingw(coords,coords2,k1wmx,k1wmy,"k1w","b")
                        King1w.possible_moves(coords,coords2,"b")
                    else:
                        k1wmx,k1wmy=ko1mx,ko1my
            piece,b1wmx,b1wmy,hb,white_check,moves,rfv,coords,coords2,vc,Bishop1w=piece_place(piece,b1wmx,b1wmy,hb,white_check,moves,rfv,coords,coords2,"b1w","bishop1",Bishop1w)
            piece,b2wmx,b2wmy,hb,white_check,moves,rfv,coords,coords2,vc,Bishop2w=piece_place(piece,b2wmx,b2wmy,hb,white_check,moves,rfv,coords,coords2,"b2w","bishop2",Bishop2w)
            piece,kn1wmx,kn1wmy,hb,white_check,moves,rfv,coords,coords2,vc,Knight1w=piece_place(piece,kn1wmx,kn1wmy,hb,white_check,moves,rfv,coords,coords2,"kn1w","knight1",Knight1w)
            piece,kn2wmx,kn2wmy,hb,white_check,moves,rfv,coords,coords2,vc,Knight2w=piece_place(piece,kn2wmx,kn2wmy,hb,white_check,moves,rfv,coords,coords2,"kn2w","knight2",Knight2w)
            piece,r1wmx,r1wmy,hb,white_check,moves,rfv,coords,coords2,vc,Rook1w=piece_place(piece,r1wmx,r1wmy,hb,white_check,moves,rfv,coords,coords2,"r1w","rook1",Rook1w)
            piece,r2wmx,r2wmy,hb,white_check,moves,rfv,coords,coords2,vc,Rook2w=piece_place(piece,r2wmx,r2wmy,hb,white_check,moves,rfv,coords,coords2,"r2w","rook2",Rook2w)
            piece,q1wmx,q1wmy,hb,white_check,moves,rfv,coords,coords2,vc,Queen1w=piece_place(piece,q1wmx,q1wmy,hb,white_check,moves,rfv,coords,coords2,"q1w","queen1",Queen1w)
            piece,q2wmx,q2wmy,hb,white_check,moves,rfv,coords,coords2,vc,Queen2w=piece_place(piece,q2wmx,q2wmy,hb,white_check,moves,rfv,coords,coords2,"q2w","queen2",Queen2w)
            piece,q3wmx,q3wmy,hb,white_check,moves,rfv,coords,coords2,vc,Queen3w=piece_place(piece,q3wmx,q3wmy,hb,white_check,moves,rfv,coords,coords2,"q3w","queen3",Queen3w)
            piece,q4wmx,q4wmy,hb,white_check,moves,rfv,coords,coords2,vc,Queen4w=piece_place(piece,q4wmx,q4wmy,hb,white_check,moves,rfv,coords,coords2,"q4w","queen4",Queen4w)

            piece,p1wmx,p1wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn1w,pawn_2_spaces_move,moves21=piece_place_pawn(piece,p1wmx,p1wmy,hb,white_check,moves,rfv,coords,coords2,"p1w","pawn1",Pawn1w,pawn_2_spaces_move,moves21)
            piece,p2wmx,p2wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn2w,pawn_2_spaces_move,moves22=piece_place_pawn(piece,p2wmx,p2wmy,hb,white_check,moves,rfv,coords,coords2,"p2w","pawn2",Pawn2w,pawn_2_spaces_move,moves22)
            piece,p3wmx,p3wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn3w,pawn_2_spaces_move,moves23=piece_place_pawn(piece,p3wmx,p3wmy,hb,white_check,moves,rfv,coords,coords2,"p3w","pawn3",Pawn3w,pawn_2_spaces_move,moves23)
            piece,p4wmx,p4wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn4w,pawn_2_spaces_move,moves24=piece_place_pawn(piece,p4wmx,p4wmy,hb,white_check,moves,rfv,coords,coords2,"p4w","pawn4",Pawn4w,pawn_2_spaces_move,moves24)
            piece,p5wmx,p5wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn5w,pawn_2_spaces_move,moves25=piece_place_pawn(piece,p5wmx,p5wmy,hb,white_check,moves,rfv,coords,coords2,"p5w","pawn5",Pawn5w,pawn_2_spaces_move,moves25)
            piece,p6wmx,p6wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn6w,pawn_2_spaces_move,moves26=piece_place_pawn(piece,p6wmx,p6wmy,hb,white_check,moves,rfv,coords,coords2,"p6w","pawn6",Pawn6w,pawn_2_spaces_move,moves26)
            piece,p7wmx,p7wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn7w,pawn_2_spaces_move,moves27=piece_place_pawn(piece,p7wmx,p7wmy,hb,white_check,moves,rfv,coords,coords2,"p7w","pawn7",Pawn7w,pawn_2_spaces_move,moves27)
            piece,p8wmx,p8wmy,hb,white_check,moves,rfv,coords,coords2,vc,Pawn8w,pawn_2_spaces_move,moves28=piece_place_pawn(piece,p8wmx,p8wmy,hb,white_check,moves,rfv,coords,coords2,"p8w","pawn8",Pawn8w,pawn_2_spaces_move,moves28)
            if piece=="king1":
                k1wmx,k1wmy=pygame.mouse.get_pos()
                tg=King1w.position(coords,coords2,convertx(k1wmx),converty(k1wmy),"k1w")                    
                if tg==2:
                    r1wmy,r1wmx=(list_searchy(Board,"r1w")*60),(list_searchx(Board,"r1w")*60)
                    r2wmy,r2wmx=(list_searchy(Board,"r2w")*60),(list_searchx(Board,"r2w")*60)
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,k1wmx,k1wmy=[],[],"",1,(list_searchx(Board,"k1w"))*60,(list_searchy(Board,"k1w"))*60

        if moves==1:
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                    piece,b1bmx,b1bmy=Bishop1b.possible_moves(coords,coords2,"w",piece,False)
                    Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
                    piece,b2bmx,b2bmy=Bishop2b.possible_moves(coords,coords2,"w",piece,False)
                    Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                    piece,r1bmx,r1bmy=Rook1b.possible_moves(coords,coords2,"w",piece,False)
                    Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                    piece,r2bmx,r2bmy=Rook2b.possible_moves(coords,coords2,"w",piece,False)
                    Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                    piece,kn1bmx,kn1bmy=Knight1b.possible_moves(coords,coords2,"w",piece,False)
                    Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                    piece,kn2bmx,kn2bmy=Knight2b.possible_moves(coords,coords2,"w",piece,False)
                    Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                    piece,q1bmx,q1bmy=Queen1b.possible_moves(coords,coords2,"w",piece,False)
                    Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                    piece,q2bmx,q2bmy=Queen2b.possible_moves(coords,coords2,"w",piece,False)
                    Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                    piece,q3bmx,q3bmy=Queen3b.possible_moves(coords,coords2,"w",piece,False)
                    Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                    piece,q4bmx,q4bmy=Queen4b.possible_moves(coords,coords2,"w",piece,False)
                    Pawn1b=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                    piece,p1bmx,p1bmy=Pawn1b.possible_moves(coords,coords2,"w",moves21b,piece,False,pawn_2_spaces_move)
                    Pawn2b=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                    piece,p2bmx,p2bmy=Pawn2b.possible_moves(coords,coords2,"w",moves22b,piece,False,pawn_2_spaces_move)
                    Pawn3b=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                    piece,p3bmx,p3bmy=Pawn3b.possible_moves(coords,coords2,"w",moves23b,piece,False,pawn_2_spaces_move)
                    Pawn4b=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                    piece,p4bmx,p4bmy=Pawn4b.possible_moves(coords,coords2,"w",moves24b,piece,False,pawn_2_spaces_move)
                    Pawn5b=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                    piece,p5bmx,p5bmy=Pawn5b.possible_moves(coords,coords2,"w",moves25b,piece,False,pawn_2_spaces_move)
                    Pawn6b=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                    piece,p6bmx,p6bmy=Pawn6b.possible_moves(coords,coords2,"w",moves26b,piece,False,pawn_2_spaces_move)
                    Pawn7b=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                    piece,p7bmx,p7bmy=Pawn7b.possible_moves(coords,coords2,"w",moves27b,piece,False,pawn_2_spaces_move)
                    Pawn8b=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                    piece,p8bmx,p8bmy=Pawn8b.possible_moves(coords,coords2,"w",moves28b,piece,False,pawn_2_spaces_move)
                    ko1mx,ko1my=k1bmx,k1bmy
                    vc="k1b"
                    k1bmx,k1bmy=pygame.mouse.get_pos()
                    if k1bmx>list_searchx(Board,"k1b")*60 and k1bmx<list_searchx(Board,"k1b")*60+60 and k1bmy>list_searchy(Board,"k1b")*60 and k1bmy<list_searchy(Board,"k1b")*60+60:
                        piece="king1b"
                        King1b=kingw(coords,coords2,k1bmx,k1bmy,"k1b","w")
                        King1b.possible_moves(coords,coords2,"w")
                    else:
                        k1bmx,k1bmy=ko1mx,ko1my
            if piece!="":          
                piece,b1bmx,b1bmy,hw,black_check,moves,rfv,coords,coords2,vc,Bishop1b=piece_place(piece,b1bmx,b1bmy,hw,black_check,moves,rfv,coords,coords2,"b1b","bishop1b",Bishop1b)
                piece,b2bmx,b2bmy,hw,black_check,moves,rfv,coords,coords2,vc,Bishop2b=piece_place(piece,b2bmx,b2bmy,hw,black_check,moves,rfv,coords,coords2,"b2b","bishop2b",Bishop2b)
                piece,kn1bmx,kn1bmy,hw,black_check,moves,rfv,coords,coords2,vc,Knight1b=piece_place(piece,kn1bmx,kn1bmy,hw,black_check,moves,rfv,coords,coords2,"kn1b","knight1b",Knight1b)
                piece,kn2bmx,kn2bmy,hw,black_check,moves,rfv,coords,coords2,vc,Knight2b=piece_place(piece,kn2bmx,kn2bmy,hw,black_check,moves,rfv,coords,coords2,"kn2b","knight2b",Knight2b)
                piece,r1bmx,r1bmy,hw,black_check,moves,rfv,coords,coords2,vc,Rook1b=piece_place(piece,r1bmx,r1bmy,hw,black_check,moves,rfv,coords,coords2,"r1b","rook1b",Rook1b)
                piece,r2bmx,r2bmy,hw,black_check,moves,rfv,coords,coords2,vc,Rook1b=piece_place(piece,r2bmx,r2bmy,hw,black_check,moves,rfv,coords,coords2,"r2b","rook2b",Rook2b)
                piece,q1bmx,q1bmy,hw,black_check,moves,rfv,coords,coords2,vc,Queen1b=piece_place(piece,q1bmx,q1bmy,hw,black_check,moves,rfv,coords,coords2,"q1b","queen1b",Queen1b)
                piece,q2bmx,q2bmy,hw,black_check,moves,rfv,coords,coords2,vc,Queen2b=piece_place(piece,q2bmx,q2bmy,hw,black_check,moves,rfv,coords,coords2,"q2b","queen2b",Queen2b)
                piece,q3bmx,q3bmy,hw,black_check,moves,rfv,coords,coords2,vc,Queen3b=piece_place(piece,q3bmx,q3bmy,hw,black_check,moves,rfv,coords,coords2,"q3b","queen3b",Queen3b)
                piece,q4bmx,q4bmy,hw,black_check,moves,rfv,coords,coords2,vc,Queen4b=piece_place(piece,q4bmx,q4bmy,hw,black_check,moves,rfv,coords,coords2,"q4b","queen4b",Queen4b)

                piece,p1bmx,p1bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn1b,pawn_2_spaces_move,moves21b=piece_place_pawn(piece,p1bmx,p1bmy,hw,black_check,moves,rfv,coords,coords2,"p1b","pawn1b",Pawn1b,pawn_2_spaces_move,moves21b)
                piece,p2bmx,p2bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn2b,pawn_2_spaces_move,moves22b=piece_place_pawn(piece,p2bmx,p2bmy,hw,black_check,moves,rfv,coords,coords2,"p2b","pawn2b",Pawn2b,pawn_2_spaces_move,moves22b)
                piece,p3bmx,p3bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn3b,pawn_2_spaces_move,moves23b=piece_place_pawn(piece,p3bmx,p3bmy,hw,black_check,moves,rfv,coords,coords2,"p3b","pawn3b",Pawn3b,pawn_2_spaces_move,moves23b)
                piece,p4bmx,p4bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn4b,pawn_2_spaces_move,moves24b=piece_place_pawn(piece,p4bmx,p4bmy,hw,black_check,moves,rfv,coords,coords2,"p4b","pawn4b",Pawn4b,pawn_2_spaces_move,moves24b)
                piece,p5bmx,p5bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn5b,pawn_2_spaces_move,moves25b=piece_place_pawn(piece,p5bmx,p5bmy,hw,black_check,moves,rfv,coords,coords2,"p5b","pawn5b",Pawn5b,pawn_2_spaces_move,moves25b)
                piece,p6bmx,p6bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn6b,pawn_2_spaces_move,moves26b=piece_place_pawn(piece,p6bmx,p6bmy,hw,black_check,moves,rfv,coords,coords2,"p6b","pawn6b",Pawn6b,pawn_2_spaces_move,moves26b)
                piece,p7bmx,p7bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn7b,pawn_2_spaces_move,moves27b=piece_place_pawn(piece,p7bmx,p7bmy,hw,black_check,moves,rfv,coords,coords2,"p7b","pawn7b",Pawn7b,pawn_2_spaces_move,moves27b)
                piece,p8bmx,p8bmy,hw,black_check,moves,rfv,coords,coords2,vc,Pawn8b,pawn_2_spaces_move,moves28b=piece_place_pawn(piece,p8bmx,p8bmy,hw,black_check,moves,rfv,coords,coords2,"p8b","pawn8b",Pawn8b,pawn_2_spaces_move,moves28b)

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
        if queen2w_spawn==0 and list_searchx(Board,"q2w")!=9:
            q2wmx,q2wmy=pygame.mouse.get_pos() 
            queen2w_spawn=1
        if queen3w_spawn==0 and list_searchx(Board,"q3w")!=9:
            q3wmx,q3wmy=pygame.mouse.get_pos() 
            queen3w_spawn=1
        if queen4w_spawn==0 and list_searchx(Board,"q4w")!=9:
            q4wmx,q4wmy=pygame.mouse.get_pos() 
            queen4w_spawn=1
        if queen2b_spawn==0 and list_searchx(Board,"q2b")!=9:
            q2bmx,q2bmy=pygame.mouse.get_pos() 
            queen2b_spawn=1
        if queen3b_spawn==0 and list_searchx(Board,"q3b")!=9:
            q3bmx,q3bmy=pygame.mouse.get_pos() 
            queen3b_spawn=1
        if queen4b_spawn==0 and list_searchx(Board,"q4b")!=9:
            q4bmx,q4bmy=pygame.mouse.get_pos() 
            queen4b_spawn=1
        board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
        for er in range (0, len(coords2)):
            pygame.draw.circle(win,(255,0,0),(coords2[0][0],coords2[0][1]),15,0)
        for er in range (0, len(coords)):
            pygame.draw.circle(win,(50,205,50),(coords[er][0],coords[er][1]),15,0)       
    pygame.display.update()
pygame.QUIT
