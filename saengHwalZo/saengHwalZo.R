set.seed(2022) 

saengHwalZo <- read_excel("saenghwalzo.xlsx")
HunNaeGi<-saengHwalZo$class21[0:30] #21학번
HwaSeok<-saengHwalZo$class21[31:36] #20학번
SaeNaeGi<-saengHwalZo$class22 #22학번

A <- c() 
m<-matrix(1:84,ncol=6)  
rownames(m)<-c("1조", "2조", "3조", "4조", "5조", "6조", "7조", "8조", "9조", "10조", "11조", "12조", "13조", "14조")

for (i in 1:14) {
  if(i<3){ #20학번 3명, 22학번 3명 두 조
    A<-sample(HwaSeok,3)
    HwaSeok<-HwaSeok[! HwaSeok %in% A]
    A<-c(A, sample(SaeNaeGi,3))
    SaeNaeGi<-SaeNaeGi[! SaeNaeGi %in% A]
    m[i,] <- A
    A <- c()
  } else if(i>=3 && i<9){ #21학번 3명, 22학번 3명 여섯 조
    A<-sample(HunNaeGi,3)
    HunNaeGi<-HunNaeGi[! HunNaeGi %in% A]
    A<-c(A, sample(SaeNaeGi,3)) 
    SaeNaeGi<-SaeNaeGi[! SaeNaeGi %in% A]
    m[i,] <- A
    A <- c()
  } else{ #21학번 2명, 22학번 4명 다섯 조 + 21학번 2명, 22학번 3명 한 조
    A<-sample(HunNaeGi,2)
    HunNaeGi<-HunNaeGi[! HunNaeGi %in% A]
    A<-c(A, sample(SaeNaeGi,4)) 
    SaeNaeGi<-SaeNaeGi[! SaeNaeGi %in% A]
    m[i,] <- A
    A <- c()
  }
}
View(m)