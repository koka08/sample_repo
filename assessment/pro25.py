st=str(raw_input("Enter email: "))
stg=st.split('@')
c=stg[1].split('.')
print("Company name = "+str(c[0]))