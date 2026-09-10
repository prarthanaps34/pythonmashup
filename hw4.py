web_development=['anu','anju','sulu'];
data_science=['karunya','prarthana','amritha'];
uiux=['asha','varsha','varshini'];

all_participants=[web_development,data_science,uiux];
print(all_participants);

web_development.append('arya');
print(web_development);

data_science.insert(1,'binza')
print(data_science);

uiux.pop()
print(uiux);

new_datascience=data_science.copy()
print(new_datascience)

data_science.clear()
print(data_science);

print(web_development[:2]);

length=[len(x) for x in new_datascience]
print(length);

print('asha' in uiux or new_datascience or web_development);

first_participants=(web_development[:1],new_datascience[:1],uiux[:1]);
print(first_participants);
 






