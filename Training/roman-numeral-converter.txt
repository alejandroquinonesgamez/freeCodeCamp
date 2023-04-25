function units (number, one, five, ten) {
  let converted = '';
  if(number==0) {
    return converted;
  }
  if(number%5 == 4) {
    converted += one;  
    if(number == 9) {
      converted += ten;
    } else {
      converted += five;
    }
    return converted;
  }
  if(number >= 5) {
    converted += five;
  }
  if(number%5 > 0) {
    converted += one;  
    if(number%5 > 1) {
      converted += one; 
      if(number%5 > 2) {
        converted += one; 
      }
    }
  }
  return converted;
}


function convertToRoman(num) {
  let roman = '';
  if(num > 3999 || num < 1) {
    return false;
  }
  roman += units(parseInt(num/1000),      'M', '', '');
  roman += units(parseInt(num%1000/100),  'C', 'D', 'M');
  roman += units(parseInt(num%100/10),    'X', 'L', 'C');
  roman += units(parseInt(num%10),        'I', 'V', 'X');
  console.log(roman);
  return roman;
}


convertToRoman(36);