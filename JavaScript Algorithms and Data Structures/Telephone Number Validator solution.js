function telephoneCheck(str) {
  console.log(str, (/^[\(1]?[ \(]*?\d{3}[\) -]*?\d{3}[ -]?\d{4}$/).test(str));
  if ((/^[\(1]?[ \(]*?\d{3}[\) -]*?\d{3}[ -]?\d{4}$/).test(str)) {
    if ( (/\(/).test(str) || (/\)/).test(str) )  {
      return (/\(\d{3}\)/).test(str);
    }
  }
  return (/^[\(1]?[ \(]*?\d{3}[\) -]*?\d{3}[ -]?\d{4}$/).test(str);
}

telephoneCheck("1 (555) 555-5555");