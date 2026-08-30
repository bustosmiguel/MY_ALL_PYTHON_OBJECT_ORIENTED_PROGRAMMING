


# Representing Data -------------------------------------------------------

# hello/hello1.
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

print("hello, world")

# Demonstrates a bug
prin("hello, world")
# A bug, because cant´t find "PRIN" function f().
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
# hello/hello4 
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

readline("What's your name? ")
readline("What's your name? ")
print("Hello, Carter")


# hello/hello5.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

name<-readline("What's your name? ")
print("Hello, name")

# hello/hello6.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

name<-readline("What's your name? ")

greeting<-paste("Hello, ",name)
print(greeting)

# hello/hello7.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

name<-readline("What's your name? ")
greeting<-paste("Hello, ",name,sep="")
print(greeting)


# hello/hello8.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

name<-readline("What's your name? ")
greeting<-paste0("Hello, ",name)
print(greeting)


# hello/hello9.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

name<-readline("What's your name? ")
print(paste("Hello,",name))



# hello/hello10.R
# Ask user for name
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

name<-readline("What's your name? ")

# Say hello to user
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

print(paste("Hello,",name))


# count/count1.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


mario<-readline("Enter votes for Mario: ")
peach<-readline("Enter votes for Peach: ")
bowser<-readline("Enter votes for Bowser: ")

total<-mario+peach+bowser

print(paste("Total votes:",total))



# count/count2.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

mario<-readline("Enter votes for Mario: ")
peach<-readline("Enter votes for Peach: ")
bowser<-readline("Enter votes for Bowser: ")

mario<-as.integer(mario)
peach<-as.integer(peach)
bowser<-as.integer(bowser)

total<-mario+peach+bowser

print(paste("Total votes:",total))

# count/count3.R
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
mario<-as.integer(readline("Enter votes for Mario: "))
peach<-as.integer(readline("Enter votes for Peach: "))


bowser<-as.integer(readline("Enter votes for Bowser: "))

total<-sum(mario,peach,bowser)

print(paste("Total votes:",total))


# tabulate/tabulate1.
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.table("votes.csv")
View(votes)

# tabulate/tabulate2
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.table(
  "votes.csv",
  sep=",")
View(votes)


# tabulate/tabulate3
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.table(
  "votes.csv",
  sep=",",
  header=TRUE
  )
View(votes)


# tabulate/tabulate4
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.csv("votes.csv")
View(votes)


# tabulate/tabulate5
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.csv("votes.csv")

votes[,1]
votes[,2]
votes[,3]


# tabulate/tabulate6
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.csv("votes.csv")

colnames(votes)

votes$candidate
votes$poll
votes$mail


# tabulate/tabulate7
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.csv("votes.csv")

sum(votes$poll[1],votes$poll[2],votes$poll[3])


# tabulate/tabulate8
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
votes<-read.csv("votes.csv")

sum(votes$poll)
sum(votes$mail)


# tabulate/tabulate9
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

votes<-read.csv("votes.csv")

votes$poll[1]+votes$mail[1]
votes$poll[2]+votes$mail[2]
votes$poll[3]+votes$mail[3]


# tabulate/tabulate10
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

votes<-read.csv("votes.csv")

votes$poll+votes$mail

# tabulate/tabulate11
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

votes<-read.csv("votes.csv")

votes$total<-votes$poll+votes$mail


# tabulate/tabulate12
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

votes<-read.csv("votes.csv")

votes$total<-votes$poll+votes$mail

write.csv(votes,"totals.csv")


# tabulate/tabulate13
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

votes<-read.csv("votes.csv")

votes$total<-votes$poll+votes$mail

write.csv(votes,"totals.csv",row.names=FALSE)



#voters/voters1.
# Demonstrates reading data from a URL
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

url<-"https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters<-read.csv(url)


#voters/voters2.
# Demonstrates finding number of rows and columns in a large data set
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

url<-"https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters<-read.csv(url)

nrow(voters)
ncol(voters)


#voters/voters3.
# Demonstrates finding unique values in a vector
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

url<-"https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters<-read.csv(url)

unique(voters$voter_category)


#voters/voters4
# Demonstrates NA
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

url<-"https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters<-read.csv(url)

voters$Q22
unique(voters$Q22)


#voters/voters5
# Demonstrates converting a vector to a factor
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

url<-"https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters<-read.csv(url)

voters$Q21

factor(
voters$Q21
)


factor(
  voters$Q21,
  labels=c("?","Yes","No","Unsure/Undecided")
  )
 
 
 #voters/voters6
# Demonstrates excluding values from the levels of a factor
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

url<-"https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters<-read.csv(url)

voters$Q21<-factor(
  voters$Q21,
  labels=c("Yes","No","Unsure/Undecided"),
  exclude=c(-1)
  )





# Transforming Data -------------------------------------------------------


# Demonstrates loading data from an RData file
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")
mean(temps)
# Demonstrates identifying outliers by index
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")

temps[2]
temps[4]
temps[7]

temps[c(2,4,7)]
# Demonstrates removing outliers by index
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")
no_outliers<-temps[-c(2,4,7)]

mean(no_outliers)
mean(temps)
# Demonstrates identifying outliers with logical expressions
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")

temps[1]<0
temps[2]<0
temps[3]<0

# Demonstrates comparison operators are vectorized
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")

temps<0

# Demonstrates `which` to return indices for which a logical expression is TRUE
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")

which(temps<0)


# Demonstrates identifying outliers with compound logical expressions
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")
temps<0|temps>60

# Demonstrates `any` and `all` to test for outliers
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")

any(temps<0|temps>60)
all(temps<0|temps>60)

# Demonstrates subsetting a vector with a logical vector
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")
filter<-temps<0|temps>60
temps[filter]

# Demonstrates negating a logical expression with !
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")
filter<-!(temps<0|temps>60)
temps[filter]


# Demonstrates removing outliers
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

load("temps.RData")

no_outliers<-temps[!(temps<0|temps>60)]
save(no_outliers,file="no_outliersRRRRRRRData")

outliers<-temps[temps<0|temps>60]
save(outliers,file="outliersRRRRRRRData")

# Reads a CSV of data
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
View(chicks)


# Demonstrates `mean` calculation with NA values
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
average_weight<-mean(chicks$weight)
average_weight


# Demonstrates nAM to remove NA values from mean calculation
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
average_weight<-mean(chicks$weight,naRRRRRRRm=TRUE)
average_weight


# Demonstrates computing casein average with explicit indexes
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
casein_chicks<-chicks[c(1,2,3),]
mean(casein_chicks$weight)


# Demonstrates constructing sequential vector with :
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
casein_chicks<-chicks[1:3,]
mean(casein_chicks$weight)



# Demonstrates logical expression to identify rows with casein feed
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
chicks$feed=="casein"



# Demonstrates subsetting data frame with logical vector
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")

filter<-chicks$feed=="casein"
casein_chicks<-chicks[filter,]
mean(casein_chicks$weight)



# Demonstrates subsetting with `subset`
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")

casein_chicks<-subset(chicks,feed=="casein")
mean(casein_chicks$weight,naRRRRRRRm=TRUE)



# Demonstrates failing to remove NA values
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
chicks$weight!=NA


# Demonstrates identifying NA values with `is.na`
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")

is.na(chicks$weight)
!is.na(chicks$weight)

chicks$chick[is.na(chicks$weight)]



# Demonstrates removing NA values and resetting row names
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")

chicks<-subset(chicks,!is.na(weight))
rownames(chicks)

rownames(chicks)<-NULL
rownames(chicks)


# Demonstrates interactive program to view data by feed type
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

# Read and clean data
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Determine feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)

 # Prompt user with options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 cat("1.",feed_options[1])
 cat("2.",feed_options[2])
 cat("3.",feed_options[3])
 cat("4.",feed_options[4])
 cat("5.",feed_options[5])
 cat("6.",feed_options[6])
 feed_choice<-as.integer(readline("Feed type: "))
 
 
 
# Demonstrates \n# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


# Read and clean data
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Determine feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)

 # Prompt user with options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 cat("1.",feed_options[1],"\n")
 cat("2.",feed_options[2],"\n")
 cat("3.",feed_options[3],"\n")
 cat("4.",feed_options[4],"\n")
 cat("5.",feed_options[5],"\n")
 cat("6.",feed_options[6],"\n")
 feed_choice<-as.integer(readline("Feed type: "))
 
 
# Demonstrates interactive program to view data by feed type
# Read and clean data
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Determine feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)

 # Format feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 formatted_options<-paste0(1:length(feed_options),". ",feed_options)

 # Prompt user with options
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 cat(formatted_options,sep="\n")
 feed_choice<-as.integer(readline("Feed type: "))
 
 
 
# Demonstrates interactive program to view data by feed type
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 
# Read and clean data
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Determine feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)

 # Format feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 formatted_options<-paste0(1:length(feed_options),". ",feed_options)

 # Prompt user with options
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 cat(formatted_options,sep="\n")
 feed_choice<-as.integer(readline("Feed type: "))

 # Print selected option
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 selected_feed<-feed_options[feed_choice]
 print(subset(chicks,feed==selected_feed))
 
 
# Demonstrates interactive program to view data by feed type
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
# Read and clean data
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Determine feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)

 # Format feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 formatted_options<-paste0(1:length(feed_options),". ",feed_options)

 # Prompt user with options
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 cat(formatted_options,sep="\n")
 feed_choice<-as.integer(readline("Feed type: ")) # responder con 1,2,3,4,5 o 6.

 # Invalid choice?
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 if (feed_choice<1||feed_choice>length(feed_options)){
   cat("Invalid choice.")
   }

 selected_feed<-feed_options[feed_choice]
 print(subset(chicks,feed==selected_feed))
 
 
 
 
# Demonstrates interactive program to view data by feed type
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
# Read and clean data
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Determine feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)

 # Format feed options
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 formatted_options<-paste0(1:length(feed_options),". ",feed_options)

 # Prompt user with options
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 cat(formatted_options,sep="\n")
 feed_choice<-as.integer(readline("Feed type: "))

 # Invalid choice?
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 if (feed_choice<1||feed_choice>length(feed_options)){
   cat("Invalid choice.")
   }else{
     selected_feed<-feed_options[feed_choice]
     print(subset(chicks,feed==selected_feed))
   }
 
 
 
# Implements same functionality with `menu`
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 
 
# Read and clean data
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

chicks<-read.csv("chicks.csv")
chicks<-subset(chicks,!is.na(weight))

# Prompt user for input
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

feed_options<-unique(chicks$feed)
feed_choice<-menu(
  feed_options,
  title="Feed type:"
  )

 # Show subset
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

 selected_feed=feed_options[feed_choice]
 print(subset(chicks,feed==selected_feed))
 
 
 
# Reads 4 separate CSVs
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
Q1<-read.csv("Q1.csv")
Q2<-read.csv("Q2.csv")
Q3<-read.csv("Q3.csv")
Q4<-read.csv("Q4.csv")



# Combines data frames with `rbind`
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

Q1<-read.csv("Q1.csv")
Q2<-read.csv("Q2.csv")
Q3<-read.csv("Q3.csv")
Q4<-read.csv("Q4.csv")



sales<-rbind(Q1,Q2,Q3,Q4)



# Adds quarter column to data frames
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA



Q1<-read.csv("Q1.csv")
Q1$quarter<-"Q1"

Q2<-read.csv("Q2.csv")
Q2$quarter<-"Q2"

Q3<-read.csv("Q3.csv")
 Q3$quarter<-"Q3"

 Q4<-read.csv("Q4.csv")
 Q4$quarter<-"Q4"

 sales<-rbind(Q1,Q2,Q3,Q4)
 
 
 
# Demonstrates flagging sales as high value
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
Q1<-read.csv("Q1.csv")
Q1$quarter<-"Q1"

Q2<-read.csv("Q2.csv")
Q2$quarter<-"Q2"

Q3<-read.csv("Q3.csv")
 Q3$quarter<-"Q3"

 Q4<-read.csv("Q4.csv")
 Q4$quarter<-"Q4"

 sales<-rbind(Q1,Q2,Q3,Q4)

 sales$value<-ifelse(sales$sale_amount>100,"High Value","Regular")


# Applying Functions ------------------------------------------------------

# Demonstrates counting votes for 3 different candidates
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
mario<-as.integer(readline("Mario: "))
peach<-as.integer(readline("Peach: "))
bowser<-as.integer(readline("Bowser: "))

total<-sum(mario,peach,bowser)
cat("Total votes:",total)


# Demonstrates defining a function
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA



get_votes<-function(){
  votes<-as.integer(readline("Enter votes: "))
  return(votes)
  }

mario<-get_votes()
peach<-get_votes()
bowser<-get_votes()

total<-sum(mario,peach,bowser)
cat("Total votes:",total)


# Demonstrates R returning the last evaluated expression
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


get_votes<-function(){
  votes<-as.integer(readline("Enter votes: "))
  }

mario<-get_votes()
peach<-get_votes()
bowser<-get_votes()

total<-sum(mario,peach,bowser)
cat("Total votes:",total)



# Demonstrates defining a parameter
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


get_votes<-function(prompt){
  votes<-as.integer(readline(prompt))
  }

mario<-get_votes("Mario: ")
peach<-get_votes("Peach: ")
bowser<-get_votes("Bowser: ")

total<-sum(mario,peach,bowser)
cat("Total votes:",total)



# Demonstrates defining a parameter with a default value
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


get_votes<-function(prompt="Enter votes: "){
  votes<-as.integer(readline(prompt))
  }

mario<-get_votes()
peach<-get_votes()
bowser<-get_votes()

total<-sum(mario,peach,bowser)
cat("Total votes:",total)



# Demonstrates overriding the default value of a parameter
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


get_votes<-function(prompt="Enter votes: "){
votes<-as.integer(readline(prompt))
}

mario<-get_votes("Mario: ")
peach<-get_votes("Peach: ")
bowser<-get_votes("Bowser: ")

total<-sum(mario,peach,bowser)
cat("Total votes:",total)



# Demonstrates exact argument matching
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

get_votes<-function(prompt="Enter votes: "){
votes<-as.integer(readline(prompt))
}


mario<-get_votes(prompt="Mario: ")
peach<-get_votes(prompt="Peach: ")
bowser<-get_votes(prompt="Bowser: ")

total<-sum(mario,peach,bowser)
cat("Total votes:",total)



# Demonstrates anticipating invalid input
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

get_votes<-function(prompt="Enter votes: "){
  votes<-as.integer(readline(prompt))
  if (is.na(votes)){
    return(0)}
  else{
    return(votes)
    }
}

mario<-get_votes("Mario: ")
peach<-get_votes("Peach: ")
bowser<-get_votes("Bowser: ")

total<-sum(mario,peach,bowser)
cat("Total votes:",total)

#Demonstrates ifelse as last evaluated expression
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


get_votes<-function(prompt="Enter votes: "){
 votes<-as.integer(readline(prompt))
 ifelse(is.na(votes),0,votes)
 }
mario<-get_votes("Mario: ")
peach<-get_votes("Peach: ")
 bowser<-get_votes("Bowser: ")

 total<-sum(mario,peach,bowser)
 cat("Total votes:",total)
 
 
# Demonstrates suppressWarnings
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 
get_votes<-function(prompt="Enter votes: "){
 votes<-suppressWarnings(as.integer(readline(prompt)))
 ifelse(is.na(votes),0,votes)
}


mario<-get_votes("Mario: ")
peach<-get_votes("Peach: ")
 bowser<-get_votes("Bowser: ")

 total<-sum(mario,peach,bowser)
 cat("Total votes:",total)
 
 
# Demonstrates a duck quacking 3 times
 # NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
 
 
cat("quack!\n")
cat("quack!\n")
cat("quack!\n")



# Demonstrates duck quacking in an infinite loop
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA


repeat{
  cat("quack!\n")
}


# Demonstrates quacking 3 times with repeat
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA
i<-3
repeat{
  cat("quack!\n")
  i<-i-1
  if (i==0){
    break
    }else{
      next
    }
}




# Demonstrates removing extraneous next keyword
# NOTAS GITHUB BUSTOSMIGUEL

i<-3
repeat{
  cat("quack!\n")
  i<-i-1
  if (i==0){
    break
  }
  
}


# Demonstrates a while loop, counting down
# NOTAS GITHUB BUSTOSMIGUEL

i<-3
while (i!=0){
  cat("quack!\n")
  i<-i-1
}


# Demonstrates a while loop, counting up
# NOTAS GITHUB BUSTOSMIGUEL

i<-1
while (i<=3){
  cat("quack!\n")
  i<-i+1
}




# Demonstrates a for loop
# NOTAS GITHUB BUSTOSMIGUEL

for (i in c(1,2,3)){
  cat("quack!\n")
  }



# Demonstrates a for loop with syntactic sugar
# NOTAS GITHUB BUSTOSMIGUEL

for (i in 1:3){
  cat("quack!\n")
  }


# Demonstrates reprompting the user for valid input
# NOTAS GITHUB BUSTOSMIGUEL

get_votes<-function(prompt="Enter votes: "){
  repeat{
    votes<-suppressWarnings(as.integer(readline(prompt)))
    if (!is.na(votes)){
      break
    }
  }
  return(votes)
}


 mario<-get_votes("Mario: ")
 peach<-get_votes("Peach: ")
 bowser<-get_votes("Bowser: ")

 total<-sum(mario,peach,bowser)
 cat("Total votes:",total)
 
 
 
 
# Demonstrates tightening return
# NOTAS GITHUB BUSTOSMIGUEL
 
 
get_votes<-function(prompt="Enter votes: "){
  repeat{
    votes<-suppressWarnings(as.integer(readline(prompt)))
    if (!is.na(votes)){
      return(votes)
    }
  }
}

 mario<-get_votes("Mario: ")
 peach<-get_votes("Peach: ")
 bowser<-get_votes("Bowser: ")

 total<-sum(mario,peach,bowser)
 cat("Total votes:",total)
 
 
 
 
 
# Demonstrates prompting for input in a loop
# NOTAS GITHUB BUSTOSMIGUEL
 
get_votes<-function(prompt="Enter votes: "){
  repeat{
    votes<-suppressWarnings(as.integer(readline(prompt)))
    if (!is.na(votes)){
      return(votes)
    }
  }
}


for (name in c("Mario","Peach","Bowser")){
  votes<-get_votes(paste0(name,": "))
}



# Demonstrates prompting for input, tallying votes in a loop
# NOTAS GITHUB BUSTOSMIGUEL

get_votes<-function(prompt="Enter votes: "){
  repeat{
    votes<-suppressWarnings(as.integer(readline(prompt)))
    if (!is.na(votes)){
      return(votes)
    }
  }
}

total<-0

for (name in c("Mario","Peach","Bowser")){
  votes<-get_votes(paste0(name,": "))
  total<-total+votes
}

cat("Total votes:",total)




# Demonstrates summing votes for each candidate procedurally
# NOTAS GITHUB BUSTOSMIGUEL

votes<-read.csv("votes.csv")

total_votes<-c()
for (candidate in rownames(votes)){
  total_votes[candidate]<-sum(votes[candidate,])
}
total_votes



# Demonstrates summing votes for each voting method procedurally
# NOTAS GITHUB BUSTOSMIGUEL

votes<-read.csv("votes.csv")

total_votes<-c()
for (method in colnames(votes)){
  total_votes[method]<-sum(votes[,method])
}
total_votes


# Demonstrates summing votes for each candidate with apply
# NOTAS GITHUB BUSTOSMIGUEL

votes<-read.csv("votes.csv")
total_votes<-apply(votes,MARGIN=1,FUN=sum)
total_votes

# Demonstrates summing votes for each voting method with apply
# NOTAS GITHUB BUSTOSMIGUEL

votes<-read.csv("votes.csv")
total_votes<-apply(votes,MARGIN=2,FUN=sum)
total_votes



#Tidying Data ------------------------------------------------------------

# View storms tibble
# NOTAS GITHUB BUSTOSMIGUEL REGRESSION DATA

storms



# Remove selected columns

dplyr::select(
  storms,
  !c(lat,long,pressure,tropicalstorm_force_diameter,hurricane_force_diameter)
)



# Introduce ends_with

select(
  storms,
  !c(lat,long,pressure,ends_with("diameter"))
)


# Find only rows about hurricanes

filter(
4 select(
  5 storms,
  6 !c(lat,long,pressure,ends_with("diameter"))
  7 ),
8 status=="hurricane"
9 )
# Introduce pipe operator

storms|>
4 select(!c(lat,long,pressure,ends_with("diameter")))|>
5 filter(status=="hurricane")
# Find only rows about hurricanes, and arrange highest wind speed to least

storms|>
4 select(!c(lat,long,pressure,ends_with("force_diameter")))|>
5 filter(status=="hurricane")|>
6 arrange(desc(wind))
# If two hurricanes have same wind speed, sort alphabetically by name

storms|>
4 select(!c(lat,long,pressure,ends_with("force_diameter")))|>
5 filter(status=="hurricane")|>
6 arrange(desc(wind),name)
# Keep only first observation about each hurricane

storms|>
4 select(!c(lat,long,pressure,ends_with("force_diameter")))|>
5 filter(status=="hurricane")|>
6 arrange(desc(wind),name)|>
7 distinct(name,year,.keep_all=TRUE)
# Write subset of columns to a CSV

hurricanes<-storms|>
4 select(!c(lat,long,pressure,ends_with("force_diameter")))|>
5 filter(status=="hurricane")|>
6 arrange(desc(wind),name)|>
7 distinct(name,year,.keep_all=TRUE)

hurricanes|>
10 select(c(year,name,wind))|>
11 write.csv("hurricanes.csv",row.names=FALSE)
# Find most powerful hurricane for each year

hurricanes<-read.csv("hurricanes.csv")

hurricanes|>
6 group_by(year)|>
7 arrange(desc(wind))|>
8 slice_head()
# Introduce slice_max

hurricanes<-read.csv("hurricanes.csv")

hurricanes|>
6 group_by(year)|>
7 slice_max(order_by=wind)
# Show ungroup

hurricanes<-read.csv("hurricanes.csv")

hurricanes|>
6 group_by(year)|>
7 slice_max(order_by=wind)|>
8 ungroup()
# Find number of hurricanes per year

hurricanes<-read.csv("hurricanes.csv")

hurricanes|>
6 group_by(year)|>
7 summarize(hurricanes=n())
# Read CSV

students<-read.csv("students.csv")
View(students)
# Demonstrates pivot_wider

students<-read.csv("students.csv")

students<-pivot_wider(
6 students,
7 id_cols=student,
8 names_from=attribute,
9 values_from=value
10 )
# Demonstrates calculating average GPA by major

students<-read.csv("students.csv")

students<-pivot_wider(
6 students,
7 id_cols=student,
8 names_from=attribute,
9 values_from=value
10 )

 students$GPA<-as.numeric(students$GPA)

 students|>
15 group_by(major)|>
16 summarize(GPA=mean(GPA))
# Tally votes for favorite shows

shows<-read.csv("shows.csv")

shows|>
6 group_by(show)|>
7 summarize(votes=n())|>
8 ungroup()|>
9 arrange(desc(votes))
# Clean up leading and trailing whitespace

shows<-read.csv("shows.csv")

shows$show<-str_trim(shows$show)

shows|>
8 group_by(show)|>
9 summarize(votes=n())|>
10 ungroup()|>
11 arrange(desc(votes))
# Clean up inner whitespace

shows<-read.csv("shows.csv")

shows$show<-shows$show|>
6 str_trim()|>
7 str_squish()

shows|>
10 group_by(show)|>
11 summarize(votes=n())|>
12 ungroup()|>
13 arrange(desc(votes))
# Clean up capitalization

shows<-read.csv("shows.csv")

shows$show<-shows$show|>
6 str_trim()|>
7 str_squish()|>
8 str_to_title()

 shows|>
11 group_by(show)|>
12 summarize(votes=n())|>
13 ungroup()|>
14 arrange(desc(votes))
# Clean up spelling

shows<-read.csv("shows.csv")

shows$show<-shows$show|>
6 str_trim()|>
7 str_squish()|>
8 str_to_title()

 shows$show[str_detect(shows$show,"Avatar")]<-"Avatar: The Last Airbender"

 shows|>
13 group_by(show)|>
14 summarize(votes=n())|>
15 ungroup()|>
16 arrange(desc(votes))



 
 # Visualizing Data --------------------------------------------------------

# Create a blank visualization

votes<-read.csv("votes.csv")

ggplot()
# Supply data

votes<-read.csv("votes.csv")

ggplot(votes)
# Add first geometry

votes<-read.csv("votes.csv")

ggplot(votes)+
6 geom_col()
# Add x and y aesthetics

votes<-read.csv("votes.csv")

ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col()
# Adjust y scale

votes<-read.csv("votes.csv")

ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col()+
7 scale_y_continuous(limits=c(0,250))
# Add labels

votes<-read.csv("votes.csv")

ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col()+
7 scale_y_continuous(limits=c(0,250))+
8 labs(
  9 x="Candidate",
  10 y="Votes",
  11 title="Election Results"
  12 )
# Add fill aesthetic mapping for geom_col

votes<-read.csv("votes.csv")

ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col(aes(fill=candidate))+
7 scale_y_continuous(limits=c(0,250))+
8 labs(
  9 x="Candidate",
  10 y="Votes",
  11 title="Election Results"
  12 )
# Use viridis scale to design for color blindness

votes<-read.csv("votes.csv")

ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col(aes(fill=candidate))+
7 scale_fill_viridis_d("Candidate")+
8 scale_y_continuous(limits=c(0,250))+
9 labs(
  10 x="Candidate",
  11 y="Votes",
  12 title="Election Results"
  13 )
# Adjust ggplot theme

votes<-read.csv("votes.csv")

ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col(aes(fill=candidate))+
7 scale_fill_viridis_d("Candidate")+
8 scale_y_continuous(limits=c(0,250))+
9 labs(
  10 x="Candidate",
  11 y="Votes",
  12 title="Election Results"
  13 )+
14 theme_classic()
# Save file

votes<-read.csv("votes.csv")

p<-ggplot(votes,aes(x=candidate,y=votes))+
6 geom_col(aes(fill=candidate))+
7 scale_fill_viridis_d("Candidate")+
8 scale_y_continuous(limits=c(0,250))+
9 labs(
  10 x="Candidate",
  11 y="Votes",
  12 title="Election Results"
  13 )+
14 theme_classic()

 ggsave(
17 "votes.png",
18 plot=p,
19 width=1200,
20 height=900,
21 units="px"
22 )
# Introduce geom_point

load("candyRRRRRRRData")

ggplot(
6 candy,
7 aes(x=price_percentile,y=sugar_percentile)
8 )+
9 geom_point()
# Add labels and theme

load("candyRRRRRRRData")

ggplot(
6 candy,
7 aes(x=price_percentile,y=sugar_percentile)
8 )+
9 geom_point()+
10 labs(
  11 x="Price",
  12 y="Sugar",
  13 title="Price and Sugar"
  14 )+
15 theme_classic()
# Introduce geom_jitter

ggplot(
4 candy,
5 aes(x=price_percentile,y=sugar_percentile)
6 )+
7 geom_jitter()+
8 labs(
  9 x="Price",
  10 y="Sugar",
  11 title="Price and Sugar"
  12 )+
13 theme_classic()
# Introduce size and color aesthetic

ggplot(
4 candy,
5 aes(x=price_percentile,y=sugar_percentile)
6 )+
7 geom_jitter(
  8 color="darkorchid",
  9 size=2
  10 )+
11 labs(
  12 x="Price",
  13 y="Sugar",
  14 title="Price and Sugar"
  15 )+
16 theme_classic()
# Introduce point shape and fill color

ggplot(
4 candy,
5 aes(x=price_percentile,y=sugar_percentile)
6 )+
7 geom_jitter(
  8 color="darkorchid",
  9 fill="orchid",
  10 shape=21,
  11 size=2
  12 )+
13 labs(
  14 x="Price",
  15 y="Sugar",
  16 title="Price and Sugar"
  17 )+
18 theme_classic()
# Visualize with geom_point

load("anitaRRRRRRRData")

ggplot(anita,aes(x=timestamp,y=wind))+
6 geom_point()
# Introduce geom_line

load("anitaRRRRRRRData")

ggplot(anita,aes(x=timestamp,y=wind))+
6 geom_line()
# Combine geom_line and geom_point

load("anitaRRRRRRRData")

ggplot(anita,aes(x=timestamp,y=wind))+
6 geom_line()+
7 geom_point(color="deepskyblue4")
# Experiment with geom_line and geom_point aesthetics

load("anitaRRRRRRRData")

ggplot(anita,aes(x=timestamp,y=wind))+
6 geom_line(
  7 linetype=1,
  8 linewidth=0.5
  9 )+
10 geom_point(
  11 color="deepskyblue4",
  12 size=2
  13 )
# Add labels and adjust theme

load("anitaRRRRRRRData")

ggplot(anita,aes(x=timestamp,y=wind))+
6 geom_line(
  7 linetype=1,
  8 linewidth=0.5
  9 )+
10 geom_point(
  11 color="deepskyblue4",
  12 size=2
  13 )+
14 labs(
  15 y="Wind Speed (Knots)",
  16 x="Date",
  17 title="Hurricane Anita"
  18 )+
19 theme_classic()
# Add horizontal line to demarcate hurricane status

load("anitaRRRRRRRData")

ggplot(anita,aes(x=timestamp,y=wind))+
6 geom_line(
  7 linetype=1,
  8 linewidth=0.5
  9 )+
10 geom_point(
  11 color="deepskyblue4",
  12 size=2
  13 )+
14 geom_hline(
  15 linetype=3,
  16 yintercept=64
  17 )+
18 labs(
  19 y="Wind Speed (Knots)",
  20 x="Date",
  21 title="Hurricane Anita"
  22 )+
23 theme_classic()





# Testing Programs --------------------------------------------------------

# Define function to calculate average value in a vector

average<-function(x){
4 sum(x)/length(x)
5 }
# Handle non-numeric input

average<-function(x){
4 if (!is.numeric(x)){
  5 return(NA)
  6 }
7 sum(x)/length(x)
8 }
# Message about returning NA

average<-function(x){
4 if (!is.numeric(x)){
  5 message("`x` must be a numeric vector. Returning NA instead.")
  6 return(NA)
  7 }
8 sum(x)/length(x)
9 }
# Warn about returning NA

average<-function(x){
4 if (!is.numeric(x)){
  5 warning("`x` must be a numeric vector. Returning NA instead.")
  6 return(NA)
  7 }
8 sum(x)/length(x)
9 }
# Stop instead of warn

average<-function(x){
4 if (!is.numeric(x)){
  5 stop("`x` must be a numeric vector.")
  6 }
7 sum(x)/length(x)
8 }
# Handle NA values

average<-function(x){
4 if (!is.numeric(x)){
  5 stop("`x` must be a numeric vector.")
  6 }
7 if (any(is.na(x))){
  8 warning("`x` contains one or more NA values.")
  9 return(NA)
  10 }
11 sum(x)/length(x)
12 }
# Write test function

)

test_average<-function(){
6 if (average(c(1,2,3))==2){
  7 cat("`average` passed test :)\n")
  8 }else{
    9 cat("`average` failed test :(\n")
    10 }
11 }

 test_average()
# Add test cases

)

test_average<-function(){
6 if (average(c(1,2,3))==2){
  7 cat("`average` passed test :)\n")
  8 }else{
    9 cat("`average` failed test :(\n")
    10 }
11
12 if (average(c(-1,-2,-3))==-2){
  13 cat("`average` passed test :)\n")
  14 }else{
    15 cat("`average` failed test :(\n")
    16 }
17
18 if (average(c(-1,0,1))==0){
  19 cat("`average` passed test :)\n")
  20 }else{
    21 cat("`average` failed test :(\n")
    22 }
23 }

 test_average()
# Introduce test_that and add representative test cases to catch corner cases

)

test_that("`average` calculates mean",{
6 expect_equal(average(c(1,2,3)),2)
7 expect_equal(average(c(-1,-2,-3)),-2)
8 expect_equal(average(c(-1,0,1)),0)
9 expect_equal(average(c(-2,-1,1,2)),0)
10 })
# Test warning about NA values

)

test_that("`average` calculates mean",{
6 expect_equal(average(c(1,2,3)),2)
7 expect_equal(average(c(-1,-2,-3)),-2)
8 expect_equal(average(c(-1,0,1)),0)
9 expect_equal(average(c(-2,-1,1,2)),0)
10 })

 test_that("`average` warns about NAs in input",{
13 expect_warning(average(c(1,NA,3)))
14 expect_warning(average(c(NA,NA,NA)))
15 })
# Fix ordering of error handling

average<-function(x){
4 if (any(is.na(x))){
  5 warning("`x` contains one or more NA values.")
  6 return(NA)
  7 }
8 if (!is.numeric(x)){
  9 stop("`x` must be a numeric vector.")
  10 }
11 sum(x)/length(x)
12 }
# Test NA return values

)

test_that("`average` calculates mean",{
6 expect_equal(average(c(1,2,3)),2)
7 expect_equal(average(c(-1,-2,-3)),-2)
8 expect_equal(average(c(-1,0,1)),0)
9 expect_equal(average(c(-2,-1,1,2)),0)
10 })

 test_that("`average` returns NA with NAs in input",{
13 expect_equal(suppressWarnings(average(c(1,NA,3))),NA)
14 expect_equal(suppressWarnings(average(c(NA,NA,NA))),NA)
15 })

 test_that("`average` warns about NAs in input",{
18 expect_warning(average(c(1,NA,3)))
19 expect_warning(average(c(NA,NA,NA)))
20 })
# Test stop if argument is non-numeric

)

test_that("`average` calculates mean",{
6 expect_equal(average(c(1,2,3)),2)
7 expect_equal(average(c(-1,-2,-3)),-2)
8 expect_equal(average(c(-1,0,1)),0)
9 expect_equal(average(c(-2,-1,1,2)),0)
10 })

 test_that("`average` returns NA with NAs in input",{
13 expect_equal(suppressWarnings(average(c(1,NA,3))),NA)
14 expect_equal(suppressWarnings(average(c(NA,NA,NA))),NA)
15 })

 test_that("`average` warns about NAs in input",{
18 expect_warning(average(c(1,NA,3)))
19 expect_warning(average(c(NA,NA,NA)))
20 })

 test_that("`average` stops if `x` is non-numeric",{
23 expect_error(average(c("quack!")))
24 expect_error(average(c("1","2","3")))
25 })
# Demonstrates floating-point imprecision

print(0.3)
print(0.3,digits=17)
# Test doubles

)

test_that("`average` calculates mean",{
6 expect_equal(average(c(1,2,3)),2)
7 expect_equal(average(c(-1,-2,-3)),-2)
8 expect_equal(average(c(-1,0,1)),0)
9 expect_equal(average(c(-2,-1,1,2)),0)
10 expect_equal(average(c(0.1,0.5)),0.3)
11 })

 test_that("`average` returns NA with NAs in input",{
14 expect_equal(suppressWarnings(average(c(1,NA,3))),NA)
15 expect_equal(suppressWarnings(average(c(NA,NA,NA))),NA)
16 })

 test_that("`average` warns about NAs in input",{
19 expect_warning(average(c(1,NA,3)))
20 expect_warning(average(c(NA,NA,NA)))
21 })

 test_that("`average` stops if `x` is non-numeric",{
24 expect_error(average(c("quack!")))
25 expect_error(average(c("1","2","3")))
26 })
# Test greet

)

test_that("`greet` says hello to a user",{
6 expect_equal(greet("Carter"),"hello, Carter")
7 })
# Greets a user

greet<-function(to){
4 return(paste("hello,",to))
5 }
# Describe greet

)

describe("greet()",{
6 it("can say hello to a user",{
  7 name<-"Carter"
  8 expect_equal(greet(name),"hello, Carter")
  9 })
10 })
# Describe greet

)

describe("greet()",{
6 it("can say hello to a user",{
  7 name<-"Carter"
  8 expect_equal(greet(name),"hello, Carter")
  9 })
10 it("can say hello to the world",{
  11 expect_equal(greet(),"hello, world")
  12 })
13 })
# Provides default argument value

greet<-function(to="world"){
4 return(paste("hello,",to))
5 }





# Packaging Programs ------------------------------------------------------

# Demonstrates initializing a package

# Load devtools, tidyverse for package creation
library(devtools)
library(tidyverse)

# Create a new folder for package
dir.create("ducksay")

 # Set working directory to package directory
 setwd("ducksay")

 # Create a blank DESCRIPTION file
 file.create("DESCRIPTION")

 # Create a LICENSE file to fill in license details
 file.create("LICENSE")
# Demonstrates required components of a DESCRIPTION file

Package: ducksay
Title: Duck Say
Description: Say hello with a duck.
Version: 1.0
Authors@R: person("Carter", "Zenke", email = "carter@cs50.harvard.edu", role = c("aut", "cre", "cph"))
License: MIT + file LICENSE
cksay/DESCRIPTION1
# Demonstrates adding on to a license template

YEAR: ...
COPYRIGHT HOLDER: ducksay authors
cksay/LICENSE
# Demonstrates creating tests

# Initialize test folder structure
use_testthat()

# Create testing file for `ducksay`
use_test("ducksay")
# Demonstrates suggesting a dependency, for testing's sake

Package: ducksay
Title: Duck Say
Description: Say hello with a duck.
Version: 1.0
Authors@R: person("Carter", "Zenke", email = "carter@cs50.harvard.edu", role = c("aut", "cre", "cph"))
License: MIT + file LICENSE
Suggests:
10    testthat (>= 3.0.0)
 Config/testthat/edition: 3
cksay/DESCRIPTION2
# Demonstrates describing behavior of `ducksay`

describe("ducksay()",{
4 it("can print to the console with `cat`",{
  5 expect_output(cat(ducksay()))
  6 })
7 it("can say hello to the world",{
  8 expect_match(ducksay(),"hello, world")
  9 })
10 })
# Demonstrates creating a function

# Create `ducksay` file, in which to write function
use_r("ducksay")
# Demonstrates defining a function for a package

ducksay<-function(){
4 paste(
  5 "hello, world",
  6 ">(. )__",
  7 " (____/",
  8 sep="\n"
  9 )
10 }
# Demonstrates exporting and loading a package function

# Create a NAMESPACE file, in which to export ducksay function
file.create("NAMESPACE")

# Load function definitions for testing
load_all()
# Demonstrates declaring `ducksay` accessible to package end users

export(ducksay)
cksay/NAMESPACE
# Demonstrates running tests

test()
# Demonstrates checking for duck in output

describe("ducksay()",{
4 it("can print to the console with `cat`",{
  5 expect_output(cat(ducksay()))
  6 })
7 it("can say hello to the world",{
  8 expect_match(ducksay(),"hello, world")
  9 })
10 it("can say hello with a duck",{
  11 duck<-paste(
    12 ">(. )__",
    13 " (____/",
    14 sep="\n"
    15 )
  16 expect_match(ducksay(),duck,fixed=TRUE)
  17 })
18 })
# Demonstrates running tests

test()
# Demonstrates documenting a function

# Create a directory for documentation
dir.create("man")

# Create a file in which to write documentation for ducksay
file.create("man/ducksayRRRRRRRd")
# Demonstrates required markup for R documentation files

\name{ducksay}
\alias{ducksay}
\title{Duck Say}
\description{A duck that says hello.}
\usage{
8 ducksay()
9 }
 \value{
11 A string representation of a duck saying hello to the world.
12 }
 \examples{
14 cat(ducksay())
15 }
cksay/man/ducksay1RRRRRRRd
# Demonstrates rendering documentation

?ducksay
# Demonstrates "building" a package—converting it from source code to a bundled, shareable file

build()
# Demonstrates ensuring duck repeats given phrase

describe("ducksay()",{
4 it("can print to the console with `cat`",{
  5 expect_output(cat(ducksay()))
  6 })
7 it("can say hello to the world",{
  8 expect_match(ducksay(),"hello, world")
  9 })
10 it("can say hello with a duck",{
  11 duck<-paste(
    12 ">(. )__",
    13 " (____/",
    14 sep="\n"
    15 )
  16 expect_match(ducksay(),duck,fixed=TRUE)
  17 })
18 it("can say any given phrase",{
  19 expect_match(ducksay("quack!"),"quack!")
  20 })
21 })
# Demonstrates taking an argument to print

ducksay<-function(phrase="hello, world"){
4 paste(
  5 phrase,
  6 ">(. )__",
  7 " (____/",
  8 sep="\n"
  9 )
10 }
# Demonstrates updated markup, including specifying arguments

\name{ducksay}
\alias{ducksay}
\title{Duck Say}
\description{A duck that says hello.}
\usage{
8 ducksay(phrase = "hello, world")
9 }
 \arguments{
11 \item{phrase}{The phrase for the duck to say.}
12 }
 \value{
14 A string representation of a duck saying the given phrase.
15 }
 \examples{
17 cat(ducksay())
18 cat(ducksay("quack!"))
19 }
cksay/man/ducksay2RRRRRRRd
# Demonstrates "building" a package—converting it from source code to a bundled, shareable file

build()
# Demonstrates installing a custom package

# Installs package from source, if available
install("ducksay")

# Installs package from bundled file, if available
install.packages("ducksay_1.0.tar.gz")
# Demonstrates using custom package

library(ducksay)

name<-readline("What's your name? ")
greeting<-ducksay(paste("hello,",name))
cat(greeting)



