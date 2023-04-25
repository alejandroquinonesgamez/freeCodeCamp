function palindrome(str) {
  let clean = str.toLowerCase().replace(/[_,-\/\\\-\.\: \(\)]/gi, '');
  let reverse = clean.split('').reverse().join('');
  console.log(clean, reverse)
  return (clean == reverse)
  return true;
}

palindrome("_eye");