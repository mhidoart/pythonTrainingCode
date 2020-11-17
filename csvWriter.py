import csv
with open("C:\\Users\\mehdi\\OneDrive\\Bureau\\python\\st.csv","w",newline='') as f:
    write = csv.writer(f,delimiter=",")
    # write.writerows([["one","two","threee"],["wahed","joj","tlata"]])
    # write.writerow(["one","two","threee"])
    # write.writerow(["wahed","joj","tlata"])
    write.writerows([["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]])
print("done")
    
