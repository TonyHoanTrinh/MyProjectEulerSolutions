largestPalindrome = 0
for (var x = 100; x < 1000; x++) {
  for (var y = 100; y < 1000; y++) {
    string = toString(x * y);
    if(string == string.reverse()){
      if ((x * y) > largestPalindrome) {
        largestPalindrome = x * y;
      }
    }
  }
}

console.log(largestPalindrome)
