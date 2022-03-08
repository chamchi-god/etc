set.seed(2022) 

saengHwalZo <- read_excel("saenghwalzo/saenghwalzo.xlsx")
HunNaeGi<-saengHwalZo$class21[0:30] #21학번
HwaSeok<-saengHwalZo$class21[31:36] #20학번
SaeNaeGi<-saengHwalZo$class22 #22학번

zo<-matrix(1:84,ncol=6)  
rownames(m)<-c("1조", "2조", "3조", "4조", "5조", "6조", "7조", "8조", "9조", "10조", "11조", "12조", "13조", "14조")

makingZo<-function(sunbae, hubae = SaeNaeGi, sunbaeNum){
  A <- c()
  A<-sample(sunbae,sunbaeNum)
  if(sunbae == HunNaeGi){
    HunNaeGi <<- HunNaeGi[! HunNaeGi %in% A]
  } else{
    HwaSeok <<- HwaSeok[! HwaSeok %in% A]
  }
  A<-c(A, sample(SaeNaeGi,6-sunbaeNum)) 
  SaeNaeGi <<- SaeNaeGi[! SaeNaeGi %in% A]
  return(A)
}

for (i in 1:14) {
  if(i<3){ #20학번 3명, 22학번 3명 두 조
    zo[i,]<-makingZo(HwaSeok, SaeNaeGi, 3)
  } else if(i>=3 && i<9){ #21학번 3명, 22학번 3명 여섯 조
    zo[i,]<-makingZo(HunNaeGi, SaeNaeGi, 3)
  } else{ #21학번 2명, 22학번 4명 다섯 조 + 21학번 2명, 22학번 3명 한 조
    zo[i,]<-makingZo(HunNaeGi, SaeNaeGi, 2)
  }
}

View(zo)

