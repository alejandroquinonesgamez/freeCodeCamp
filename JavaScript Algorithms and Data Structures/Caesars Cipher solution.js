function rot13(str) {
  var abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  // control 01234567890123456789012345
  abc = abc.split('');
  let coded = str;
  coded = coded.split('');
  let decoded = '';
  for (let i=0; i<coded.length; i++) {
    if(coded[i].match(/[^\w]/)) {
      decoded += coded[i];
    } else {
      let index = (abc.indexOf(coded[i])-13)
      if (index < 0) {
        index += 26;
      }
      decoded += abc[index];
    }
  }
  console.log(decoded);
  return decoded;
}

rot13("SERR PBQR PNZC");