data = [
	{"openingHours":"Mon 0020;Tue 5568"},
	{"openingHours":"Wed 0020;Tue 5568"},
	{"openingHours":"Fri 0020;Sun 5568"}
]
fomatted_hour_data=[]
data.forEach(element => {
	temp_array = [];
	temp_oh_data = element["openingHours"].split(';')
	temp_oh_data.forEach(ele=>{
		data = {
			"dayofweek":ele.slice(0,4),
			"time":ele.slice(4)
		}
		temp_array.push(data)
	})
	fomatted_hour_data.push(temp_array)
	//console.log(temp_oh_data);
});
console.log(fomatted_hour_data);