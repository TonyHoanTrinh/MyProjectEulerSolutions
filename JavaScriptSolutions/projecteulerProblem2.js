var sum = 0;

var previousTerm = 1;
var currentTerm = 2;

while(currentTerm < 4000000)
{
	let temp = previousTerm;
	previousTerm = currentTerm;
	if(currentTerm % 2 == 0)
	{
		sum += currentTerm;
	}
       	currentTerm = currentTerm + temp;  
}
console.log(sum)
