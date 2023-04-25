function checkCashRegister(price, cash, cid) {
  let change = [];
  let value = [["PENNY", 0.01], ["NICKEL", 0.05], ["DIME", 0.1], ["QUARTER", 0.25], ["ONE", 1], ["FIVE", 5], ["TEN", 10], ["TWENTY", 20], ["ONE HUNDRED", 100]];
  let qty = [["PENNY", 0], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]
  for (let i=cid.length-1; i>=0; i--) {
    qty[i][1] = Math.round(cid[i][1] / value[i][1]);
  }
  let notRetorned = cash-price;
  for (let i=cid.length-1; i>=0 && notRetorned!=0; i--) {
    if (value[i][1] <= notRetorned) {
      change.unshift(cid[i]);
      if (change[0][1] <= notRetorned) {
        notRetorned -= cid[i][1];
      } 
      else {
        notRetorned = Math.round(notRetorned*100)/100;
        while (change[0][1] > notRetorned) {
          change[0][1] -= value[i][1];
        }
        notRetorned -= Math.round(change[0][1]*100)/100;
      } 
    }
  }
  let funds = '';
  if (notRetorned == 0) {
    let checkClose = true;
    for (let i = 0; i<cid.length; i++) {
      console.log('checkeando cerrada')
      console.log(change[i], cid[i], (/*change[i] != cid[i] || */(change[i] == undefined && cid[i][1] != 0)))
      if ( change[i] == cid[i] || (change[i] == undefined && cid[i][1] == 0) ) {
        console.log('match')
        checkClose = true;
      }
      else {
        checkClose = false;
        i = cid.length;
      }
    }
    funds = (checkClose) ? 'CLOSED' : 'OPEN';
    console.log(funds)
    if (funds == 'CLOSED') {
      change = cid.reverse();
    }
  } else {
    funds = 'INSUFFICIENT_FUNDS';
    change = [];
  }
  change = change.reverse();
  for (let i=0; i<change.length; i++) {
    change[i][1] = Math.round(change[i][1]*100)/100;
  }
  let result = {status: funds, change: change}
  console.log(result);
  return result;
}

checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])