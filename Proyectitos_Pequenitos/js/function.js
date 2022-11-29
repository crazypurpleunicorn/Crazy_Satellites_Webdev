/*Description of returnArrayTimeToUnlock: 
Dada una inversión 'x' que cuesta un determinado valor comprar: unlockPrice
Y dado el salario mensual actual que tenemos: basicIncome
...Nos vamos a imaginar lo siguiente. Estamos cansados de no ser ricos y como
personas sabias que somos, sabemos que con un salario no llegamos a ningún sitio.
Las curvas convencionales nos las pasamos por el forro.
A nosotros nos gustan las rectas que se tuercen.
Por ello decidimos que todo el dinero que ganemos lo vamos a ahorrar
para invertirlo en una máquina mágica que cuesta unlockPrice $. Esta máquina 
incrementará nuestro salario mensual en una cantidad determinda,monthlyIncrement(Por ejemplo, si compramos
un párquing mágico(unlockPrice=14000$ y que siempre está alquilado))
tendría un monthlyIncrement de 100$. Si tuvieras dos tu monthlyIncrement sería de 200$ sobre tu salari base.

Queremos saber, cuánto tiempo necesitamos para poder comprar otro párquing mágico, teniendo en cuenta
que todo lo que ganamos(baseIncome+incrementoMensual) va destinado a comprar el siguiente.
Queremos estudiar cómo va decrementandose el tiempo necesario en meses que necesito para comprar un párquing,
si mantenemos este religioso ahorro.

Así pues las funciones  "returnArrayTimeToUnlock"
devuelven un array con los tiempos necesarios para comprar el siguiente párquing
de ahí el nombre timeToUnlock.

Este array, lo hacemos crecer hasta que se cumpla una condición, por ejemplo,
hasta que cobre 1500$ sin hacer nada de nada, mágicamente a través de nuestras inversiones.

Otra opción es hacerlo crecer hasta que el tiempo para adquirir el párquing sea menor de 
X meses.¿Cuánto tardaría yo en poder comprar un párquing cada dos meses?

Así pues  returnArrayTimeToUnlockTillPassiveIncomeGreaterThan(), se corresponde a la primera opción.
y          returnArrayTimeToUnlockTillTimeToUnlockIsEqualTo(), se corresponde a la segunda opción


*/

//Duda: en js para que sirve asignar una función a una variable
//es una cosa bastante, especial, en qué casos se puede usar????

function returnArrayTimeToUnlockTillTimeToUnlockIsEqualTo(
  unlockPrice,
  baseIncome,
  monthlyIncrement,
  desiredTimeToUnlock
) {
  //desiredTimeToUnlock is in months
  //inicializaciones
  var timeToUnlock = unlockPrice / baseIncome;
  var arrayOfTimesToUnlock = [];

  //Calculate timeToUnlocks...untill. Basic income will become basic salary+monthly increment.
  while (timeToUnlock >= desiredTimeToUnlock) {
    arrayOfTimesToUnlock.push(timeToUnlock);
    baseIncome = baseIncome + monthlyIncrement;
    timeToUnlock = unlockPrice / baseIncome;
  }
  return arrayOfTimesToUnlock;
}

function returnArrayTimeToUnlockTillPassiveIncomeGreaterThan(
  unlockPrice,
  baseIncome,
  monthlyIncrement,
  desiredPassiveIncome
) {
  //inicializaciones
  var initialBasicIncome = baseIncome;
  var timeToUnlock = unlockPrice / baseIncome;
  var arrayOfTimesToUnlock = [];

  var passiveIncome = baseIncome - initialBasicIncome;

  //CalculateTimeToUnlocks...untill. Base income will become basic salary+monthly increment
  while (passiveIncome < desiredPassiveIncome) {
    arrayOfTimesToUnlock.push(timeToUnlock);
    baseIncome = baseIncome + monthlyIncrement;
    timeToUnlock = unlockPrice / baseIncome;
    passiveIncome = baseIncome - initialBasicIncome;
  }
  return arrayOfTimesToUnlock;
}

//Format function, this function formats the array data so it can be interpreted by the JSCharting library..
// it's an array of x and y arrays :[[x1,y1],[x2,y2],[x3,y3]...]

function formatVector(array) {
  var formattedArray = [];
  for (let i = 0; i < array.length; i++) {
    var x = i;
    var y = array[i];
    var xyArray = [x, y];
    formattedArray.push(xyArray);
  }
  return formattedArray;
}
